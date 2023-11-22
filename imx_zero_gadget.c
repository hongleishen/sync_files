
// 汇集有各类描述符、有一个usb_funciton链表(实现数据传输)
struct usb_composite_dev {
    struct usb_gadget       *gadget;
    struct usb_request      *req;
    struct usb_request      *os_desc_req;
    struct usb_configuration    *config;
    /* OS String is a custom (yet popular) extension to the USB standard. */
    u8              qw_sign[OS_STRING_QW_SIGN_LEN];
    u8              b_vendor_code;
    struct usb_configuration    *os_desc_config;
    unsigned int            use_os_string:1;
    /* private: */
    /* internals */
    unsigned int            suspended:1;
    struct usb_device_descriptor    desc;
    struct list_head                configs;
    struct list_head        gstrings;
    struct usb_composite_driver *driver;
    u8              next_string_id;
    char                *def_manufacturer;
    /* the gadget driver won't enable the data pullup
     * while the deactivation count is nonzero.
     */
    unsigned            deactivations;
    /* the composite driver won't complete the control transfer's
     * data/status stages till delayed_status is zero.
     */
    int             delayed_status;
    /* protects deactivations and delayed_status counts*/
    spinlock_t          lock;
    /* public: */
    unsigned int            setup_pending:1;
    unsigned int            os_desc_pending:1;
};

// UDC的本意是"usb device controller"，usb_udc结构体里面有usb_gadget(表示UDC本身)、usb_gadget_driver()
struct usb_udc {
    struct usb_gadget_driver    *driver;
    struct usb_gadget       *gadget;
    struct device           dev;
    struct list_head        list;
    bool                vbus;
};



/*
    drivers/usb/gadget/legacy/zero.c
    Lagacy层次
*/
module_usb_composite_driver(zero_driver);

// -------------原型------------
#define module_usb_composite_driver(__usb_composite_driver) \
    module_driver(__usb_composite_driver, usb_composite_probe, \
               usb_composite_unregister)

#define module_driver(__driver, __register, __unregister, ...) \
static int __init __driver##_init(void) \
{ \
    return __register(&(__driver) , ##__VA_ARGS__); \
} \
module_init(__driver##_init); \
static void __exit __driver##_exit(void) \
{ \
    __unregister(&(__driver) , ##__VA_ARGS__); \
} \
module_exit(__driver##_exit);
// ===================================================
// 中间展开
#define module_usb_composite_driver(zero_driver) \
    module_driver(zero_driver, usb_composite_probe, \
               usb_composite_unregister)
#define module_driver(zero_driver, usb_composite_probe, usb_composite_unregister, ...) \

// 最终展开
static int __init zero_driver_init(void) \
{ 
    return usb_composite_probe(&(zero_driver) ); 
} 
module_init(zero_driver_init); \




//^^^^^^^^^^^^ driver/usb/gadget/ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
//                              legacy/zero.c
static struct usb_composite_driver zero_driver = {
    .name       = "zero",
    .dev        = &device_desc,
    .strings    = dev_strings,
    .max_speed  = USB_SPEED_SUPER,
    .bind       = zero_bind,
    .unbind     = zero_unbind,
    .suspend    = zero_suspend,
    .resume     = zero_resume,
};

module_usb_composite_driver(zero_driver);



/* ****************** composite.c  **************************************
    drivers/usb/gadget/composite.c
    正式分析
    重要调用函数
    composite_bind
    zero_bind
    sourcesink_bind
    loopback_bind
*/
static const struct usb_gadget_driver composite_driver_template = {
    .bind       = composite_bind,
    .unbind     = composite_unbind,
    .setup      = composite_setup,
    .reset      = composite_disconnect,
    .disconnect = composite_disconnect,
    .suspend    = composite_suspend,
    .resume     = composite_resume,
    .driver = {
        .owner      = THIS_MODULE,
    },
};


usb_composite_probe(struct usb_composite_driver *driver)  // 找到UDC驱动程序， 触发后面的调用
    struct usb_gadget_driver *gadget_driver;
    driver->gadget_driver = composite_driver_template;  // gadget_driver拷贝一个模型
    gadget_driver = &driver->gadget_driver;
    gadget_driver->function =  (char *) driver->name;
    gadget_driver->driver.name = driver->name;
    gadget_driver->max_speed = driver->max_speed;
    return usb_gadget_probe_driver(gadget_driver);

/* udc/core.c */
struct usb_udc {
    struct usb_gadget_driver    *driver;
    struct usb_gadget       *gadget;        // 硬件UDC驱动
    struct device           dev;
    struct list_head        list;
    bool                vbus;
};

// udc/core.c
int usb_gadget_probe_driver(struct usb_gadget_driver *driver)
    struct usb_udc      *udc = NULL;
    int         ret = -ENODEV;
    if (driver->udc_name) { // 没有udc_name
        list_for_each_entry(udc, &udc_list, list) {
            ret = strcmp(driver->udc_name, dev_name(&udc->dev));   
            if (!ret)
                break;
        }
    } else {        // 用这里
        list_for_each_entry(udc, &udc_list, list) {     
            /* For now we take the first one */
            if (!udc->driver)
                goto found;
        }
    }
    udc_bind_to_driver(udc, driver);

// udc/core.c
udc_bind_to_driver(struct usb_udc *udc, struct usb_gadget_driver *driver)
    udc->driver = driver;
    udc->dev.driver = &driver->driver;
    udc->gadget->dev.driver = &driver->driver;
    driver->bind(udc->gadget, driver);
        // cpmposite.c
        composite_bind(struct usb_gadget *gadget, struct usb_gadget_driver *gdriver)
                struct usb_composite_dev    *cdev;
                struct usb_composite_driver *composite = to_cdriver(gdriver);
                int             status = -ENOMEM;
                cdev = kzalloc(sizeof *cdev, GFP_KERNEL);

                spin_lock_init(&cdev->lock);
                cdev->gadget = gadget;              // 硬件驱动
                set_gadget_data(gadget, cdev);
                INIT_LIST_HEAD(&cdev->configs);
                INIT_LIST_HEAD(&cdev->gstrings);
                composite_dev_prepare(composite, cdev);

                /* composite gadget needs to assign strings for whole device (like
                * serial number), register function drivers, potentially update
                * power state and consumption, etc
                */
                composite->bind(cdev);          //  legacy/zero.c/zero_bind

                /*
                    static struct usb_device_descriptor device_desc = {
                    .bLength =      sizeof device_desc,
                    .bDescriptorType =  USB_DT_DEVICE,
                    //.bcdUSB = DYNAMIC 
                    .bDeviceClass =     USB_CLASS_VENDOR_SPEC,
                    .idVendor =     cpu_to_le16(DRIVER_VENDOR_NUM),
                    .idProduct =        cpu_to_le16(DRIVER_PRODUCT_NUM),
                    .bNumConfigurations =   2,

                    static struct usb_composite_driver zero_driver = {
                        .name       = "zero",
                        .dev        = &device_desc,
                */
                update_unchanged_dev_desc(&cdev->desc, composite->dev);     // 设置设备描述符

    usb_gadget_udc_start(udc);
    usb_udc_connect_control(udc);


/*
这段代码是一个函数实现，看起来是一个 USB 复合设备的绑定函数。它主要负责配置和初始化 USB 复合设备的不同功能（Function），并设置相关的参数和选项。这段代码可能是针对 Linux 内核中的 USB Gadget 驱动进行操作的。
具体来说，函数的作用可以总结如下：
分配字符串描述符的编号，用于 USB 设备的标识。
配置 USB 设备描述符的制造商、产品和序列号。
初始化定时器，以便在需要的时候执行自动恢复操作。
获取 SourceSink 和 Loopback 两个 USB Function 实例，然后根据配置设置其选项。
配置 SourceSink 和 Loopback 两个 USB Function 的 iConfiguration 字段。
根据需要，启用远程唤醒功能。
如果设备支持 OTG（On-The-Go）功能，配置相应的 OTG 描述符。
注册配置和功能，并设置自动配置的 Endpoint。
最后，输出设备信息。
总之，这段代码是用来初始化和配置 USB 复合设备的不同功能，并且涉及了许多与 USB 设备描述符、功能选项和配置相关的操作。它是在 USB Gadget 驱动中完成 USB 复合设备的初始化工作的一部分。
*/

// legacy/zero.c    
static int zero_bind(struct usb_composite_dev *cdev)
{
    struct f_ss_opts    *ss_opts;
    struct f_lb_opts    *lb_opts;
    int         status;

    // 分配字符串描述符的编号，用于 USB 设备的标识。
    device_desc.iManufacturer = strings_dev[USB_GADGET_MANUFACTURER_IDX].id;
    device_desc.iProduct = strings_dev[USB_GADGET_PRODUCT_IDX].id;
    device_desc.iSerialNumber = strings_dev[USB_GADGET_SERIAL_IDX].id;

    // 获取功能 SourceSink
    func_inst_ss = usb_get_function_instance("SourceSink");
    if (IS_ERR(func_inst_ss))
        return PTR_ERR(func_inst_ss);
    ss_opts =  container_of(func_inst_ss, struct f_ss_opts, func_inst);
    ss_opts->pattern = gzero_options.pattern;
    ss_opts->isoc_interval = gzero_options.isoc_interval;
    ss_opts->isoc_maxpacket = gzero_options.isoc_maxpacket;
    ss_opts->isoc_mult = gzero_options.isoc_mult;
    ss_opts->isoc_maxburst = gzero_options.isoc_maxburst;
    ss_opts->bulk_buflen = gzero_options.bulk_buflen;
    ss_opts->bulk_qlen = gzero_options.ss_bulk_qlen;
    ss_opts->iso_qlen = gzero_options.ss_iso_qlen;
    func_ss = usb_get_function(func_inst_ss);

    func_inst_lb = usb_get_function_instance("Loopback");
    lb_opts = container_of(func_inst_lb, struct f_lb_opts, func_inst);
    lb_opts->bulk_buflen = gzero_options.bulk_buflen;
    lb_opts->qlen = gzero_options.qlen;
    func_lb = usb_get_function(func_inst_lb);

    sourcesink_driver.iConfiguration = strings_dev[USB_GZERO_SS_DESC].id;
    loopback_driver.iConfiguration = strings_dev[USB_GZERO_LB_DESC].id;
    /* support autoresume for remote wakeup testing */
    sourcesink_driver.bmAttributes &= ~USB_CONFIG_ATT_WAKEUP;
    loopback_driver.bmAttributes &= ~USB_CONFIG_ATT_WAKEUP;
    sourcesink_driver.descriptors = NULL;
    loopback_driver.descriptors = NULL;
    if (autoresume) {
        sourcesink_driver.bmAttributes |= USB_CONFIG_ATT_WAKEUP;
        loopback_driver.bmAttributes |= USB_CONFIG_ATT_WAKEUP;
        autoresume_step_ms = autoresume * 1000;
    }
    /* support OTG systems */
    if (gadget_is_otg(cdev->gadget)) {
        if (!otg_desc[0]) {
            struct usb_descriptor_header *usb_desc;
            usb_desc = usb_otg_descriptor_alloc(cdev->gadget);
            usb_otg_descriptor_init(cdev->gadget, usb_desc);
            otg_desc[0] = usb_desc;
            otg_desc[1] = NULL;
        }
        sourcesink_driver.descriptors = otg_desc;
        sourcesink_driver.bmAttributes |= USB_CONFIG_ATT_WAKEUP;
        loopback_driver.descriptors = otg_desc;
        loopback_driver.bmAttributes |= USB_CONFIG_ATT_WAKEUP;
    }
    /* Register primary, then secondary configuration.  Note that
     * SH3 only allows one config...
     */
    // 配置描述符
    if (loopdefault) {
        usb_add_config_only(cdev, &loopback_driver);
        usb_add_config_only(cdev, &sourcesink_driver);
    } else {
        usb_add_config_only(cdev, &sourcesink_driver);
        usb_add_config_only(cdev, &loopback_driver);
    }
    // 功能添加到配置里
    status = usb_add_function(&sourcesink_driver, func_ss);
    usb_ep_autoconfig_reset(cdev->gadget);
    usb_add_function(&loopback_driver, func_lb);

    usb_ep_autoconfig_reset(cdev->gadget);
    usb_composite_overwrite_options(cdev, &coverwrite);
}

// composite.c
 usb_add_function(struct usb_configuration *config, struct usb_function *function)
    list_add_tail(&function->list, &config->functions);
    function->bind(config, function);
    //-->

// f_sourcesink.c
sourcesink_bind(struct usb_configuration *c, struct usb_function *f)
    source_sink_intf_alt0.bInterfaceNumber = id;
    source_sink_intf_alt1.bInterfaceNumber = id;
    usb_assign_descriptors(f, fs_source_sink_descs, hs_source_sink_descs, ss_source_sink_descs, NULL);
        f->fs_descriptors = usb_copy_descriptors(fs);
        f->hs_descriptors = usb_copy_descriptors(hs);




// 描述：^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
static struct usb_composite_driver zero_driver = {
    .name       = "zero",
    .dev        = &device_desc,
    .strings    = dev_strings,
    .max_speed  = USB_SPEED_SUPER,
    .bind       = zero_bind,

    .gadget_driver = composite_driver_template;
};

zero.c 文件         首先定义 usb_composite_driver zero_driver， 然后调用宏module_usb_composite_driver，最终  --->


composite.c 文件    usb_composite_probe 函数中，填充gadget_driver = composite_driver_template;  调用 usb_gadget_probe_driver(gadget_driver);


udc/core.c 文件     udc_bind_to_driver(udc, driver);  usd->driver = usb_gadget_driver, usc_start, 
                    最重要调用 driver->bind()  也就是 usb_gadget_driver->bind()   -->   也就是 composite_bind()

composite.c 文件   composite_bind()分配usb_composite_dev cdev， 调用 usb_composite_driver->bind()也就是 zero_bind()


zero.c 文件         初始化 function, config, ...