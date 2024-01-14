// ^^^^^^^^^^^^     dwc3_uboot_init()     ^^^^^^^^^^^^^^core.c udc-core.c^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dwc3_uboot_init()                                                               // core.c
    struct dwc3		*dwc； // 初始化dwc成员

    dwc3_alloc_event_buffers(dwc, DWC3_EVENT_BUFFERS_SIZE);
        num = DWC3_NUM_INT(dwc->hwparams.hwparams1);        // num =1  
        for (i = 0; i < num; i++)
            evt =  dwc3_alloc_one_event_buffer(dwc, length);
                    evt->dwc	= dwc;
                    evt->length	= length;
                    evt->buf  = dma_alloc_coherent(length, (unsigned long *)&evt->dma);
                                dma_alloc_coherent(size_t len, unsigned long *handle)
                                        *handle = (unsigned long)memalign(ARCH_DMA_MINALIGN, len);
                                        return (void *)*handle;
            dwc->ev_buffs[i] = evt;     // 只有一个

    dwc3_core_init()
        dwc3_core_soft_reset
        dwc3_phy_setup


    dwc3_event_buffers_setup(dwc);
        for (n = 0; n < dwc->num_event_buffers; n++) {
            dwc3_writel(dwc->regs, DWC3_GEVNTADRLO(n), lower_32_bits(evt->dma));
            dwc3_writel(dwc->regs, DWC3_GEVNTADRHI(n), upper_32_bits(evt->dma));
            dwc3_writel(dwc->regs, DWC3_GEVNTSIZ(n), DWC3_GEVNTSIZ_SIZE(evt->length));
            dwc3_writel(dwc->regs, DWC3_GEVNTCOUNT(n), 0);

    dwc3_core_init_mode()
        dwc3_set_mode(dwc, DWC3_GCTL_PRTCAP_DEVICE);
        dwc3_gadget_init(dwc);                                                  // gadget.c
            // gadget初始化
            dwc->gadget.ops			= &dwc3_gadget_ops;
            dwc->gadget.max_speed		= USB_SPEED_SUPER;
            dwc->gadget.speed		= USB_SPEED_UNKNOWN;
            dwc->gadget.name		= "dwc3-gadget";
            dwc3_gadget_init_endpoints(dwc);    
                dwc3_gadget_init_hw_endpoints(dwc, dwc->num_out_eps, 0);            // out 0
                    struct dwc3_ep			*dep;
                    for (i = 0; i < num; i++)
                        epnum = (i << 1) | (!!direction);
                        dep = kzalloc()
                        dep->number = epnum;
                        dwc->eps[epnum] = dep;
                        dep->endpoint.ops = &dwc3_gadget_ep0_ops;
                        dwc->gadget.ep0 = &dep->endpoint;
                        list_add_tail(&dep->endpoint.ep_list, &dwc->gadget.ep_list);

                dwc3_gadget_init_hw_endpoints(dwc, dwc->num_in_eps, 1);            // in 1                  

            usb_add_gadget_udc((struct device *)dwc->dev, &dwc->gadget);        // udc-core.c
            !
            usb_add_gadget_udc_release(parent, gadget, NULL);
                udc = kzalloc(sizeof(*udc), GFP_KERNEL);        // 分配udc
                dev_set_name(&gadget->dev, "gadget");
                gadget->dev.parent = parent;

                udc->dev.release = usb_udc_release;
                udc->dev.class = udc_class;
                udc->dev.parent = parent;

                udc->gadget = gadget;

                mutex_lock(&udc_lock);
                list_add_tail(&udc->list, &udc_list);
                usb_gadget_set_state(gadget, USB_STATE_NOTATTACHED);






// ^^^^^^^^^^^^^^^^^^^^^^^  g_dnl_register()  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

// g_dnl.c      struct usb_composite_driver  g_dnl_driver    =  {.bind = g_dnl_bind, .name = "usb_dnl_fastboot"}         
//      在composite.c 中用        composite = g_dnl_driver

// composite.c  struct usb_gadget_driver     composite_driver = {.bind = composite_bind)                                 在 udc-core.c 中用
// 
g_dnl_register("usb_dnl_fastboot");
    // g_dnl.c            usb_composite_driver   
    g_dnl_driver.name = name;
    usb_composite_register(&g_dnl_driver);
        // composite.c
        composite = driver;

        // udc-core.c              usb_gadget_driver
        usb_gadget_register_driver(&composite_driver);             //  usb_gadget_driver composite_driver = {.bind = composite_bind)
        !   //                 usb_gadget_driver
        usb_gadget_probe_driver(driver);                            //  usb_gadget_driver 参数正式使用
            找到UDC
        !   //                  usb_gadget_driver
        udc_bind_to_driver(udc, driver);
            udc->driver = driver;
            driver->bind(udc->gadget);
                // composite.c
                composite_bind(struct usb_gadget *gadget)
                    cdev = calloc(sizeof *cdev, 1);         // 分配cdev
                    gadget->dev.driver_data = cdev;
                    cdev->gadget = gadget;


                    cdev->req = dwc3_gadget_ep_alloc_request(gadget->ep0, GFP_KERNEL);
                        *dwc3_gadget_ep_alloc_request(struct usb_ep *ep, gfp_t gfp_flags)
                        struct dwc3_request		*req;
                        struct dwc3_ep			*dep = to_dwc3_ep(ep);
                        req = kzalloc(sizeof(*req), gfp_flags);     // 分配req
                        req->epnum	= dep->number;
                        req->dep	= dep;
                        return &req->request;
                    
                    cdev->req->complete = composite_setup_complete;
                    cdev->driver = composite;               // g_dnl_driver
                    usb_gadget_set_selfpowered(gadget);     // 仅仅设置变了标志
                    usb_ep_autoconfig_reset(cdev->gadget);  // ep->driver_data = NULL;
                    // usb_composite_driver *composite;
                    composite->bind(cdev);     
                    // 就是 g_dnl_driver.bind()
                    ---->
                        g_dnl_bind();  //  下面解释 g_dnl_bind(cdev)  ||||||||||||||||||||||||||| 下面解释 ||||||||||||||||||||||||||||||||||||||||
                    memcpy(&cdev->desc, composite->dev)


            usb_gadget_udc_start(udc);
                udc->gadget->ops->udc_start(udc->gadget, udc->driver);
                !
                // gadget.c
                dwc3_gadget_start(struct usb_gadget *g, struct usb_gadget_driver *driver)
                    dwc->gadget_driver	= driver;
                    switch (dwc->maximum_speed) 
                        case USB_SPEED_HIGH:
                                    reg |= DWC3_DSTS_HIGHSPEED;

                    dep = dwc->eps[0];
                    __dwc3_gadget_ep_enable(dep, &dwc3_gadget_ep0_desc, NULL, false, false);
                        dwc3_gadget_start_config(dwc, dep);
                        dwc3_gadget_set_ep_config(dwc, dep, desc, comp_desc, ignore, restore);
                        dwc3_gadget_set_xfer_resource(dwc, dep);
                        DWC3_DALEPENA_EP(dep->number);
                        dwc3_writel(dwc->regs, DWC3_DALEPENA, reg);         // 0xc720
                        trb_link->bpl = lower_32_bits(dwc3_trb_dma_offset(dep, trb_st_hw));
                        trb_link->bph = upper_32_bits(dwc3_trb_dma_offset(dep, trb_st_hw));
                        trb_link->ctrl |= DWC3_TRBCTL_LINK_TRB;
                        trb_link->ctrl |= DWC3_TRB_CTRL_HWO;

                    dep = dwc->eps[1];
                    __dwc3_gadget_ep_enable(dep, &dwc3_gadget_ep0_desc, NULL, false, false);
                    /* begin to receive SETUP packets */
                    dwc->ep0state = EP0_SETUP_PHASE;
                    dwc3_ep0_out_start(dwc);
                        // 后面再细化
                        dwc3_ep0_start_trans(dwc, 0, dwc->ctrl_req_addr, 8,  DWC3_TRBCTL_CONTROL_SETUP, 0);
                            dwc3_send_gadget_ep_cmd(dwc, dep->number, DWC3_DEPCMD_STARTTRANSFER, &params);

                    dwc3_gadget_enable_irq(dwc)
                    	reg = (DWC3_DEVTEN_VNDRDEVTSTRCVEDEN |   // vndrdevtstrcvenden
                        DWC3_DEVTEN_EVNTOVERFLOWEN |     // evntoverflowen
                        DWC3_DEVTEN_CMDCMPLTEN |        // cmd cmplt en
                        DWC3_DEVTEN_ERRTICERREN |       // errticerren
                        DWC3_DEVTEN_WKUPEVTEN |         // wkup ev ten
                        DWC3_DEVTEN_ULSTCNGEN |         // ulstcngen
                        DWC3_DEVTEN_CONNECTDONEEN |     // connectdoneen
                        DWC3_DEVTEN_USBRSTEN |          // usbrsten
                        DWC3_DEVTEN_DISCONNEVTEN);      // dis connnevten

                        DWC3_DEVTEN_VNDRDEVTSTRCVEDEN: 启用供应商特定事件接收。
                        DWC3_DEVTEN_EVNTOVERFLOWEN: 启用事件溢出事件。当事件缓冲区溢出时触发。
                        DWC3_DEVTEN_CMDCMPLTEN: 启用命令完成事件。当命令处理完成时触发。
                        DWC3_DEVTEN_ERRTICERREN: 启用错误提示事件。当检测到错误时触发。
                        DWC3_DEVTEN_WKUPEVTEN: 启用唤醒事件。当设备从休眠状态唤醒时触发。
                        DWC3_DEVTEN_ULSTCNGEN: 启用 USB 链接状态改变事件。当 USB 链接状态发生变化时触发。
                        DWC3_DEVTEN_CONNECTDONEEN: 启用连接完成事件。当 USB 设备完成连接过程时触发。
                        DWC3_DEVTEN_USBRSTEN: 启用 USB 重置事件。当 USB 总线重置时触发。
                        DWC3_DEVTEN_DISCONNEVTEN: 启用断开连接事件。当 USB 设备从总线断开时触发。
                        dwc3_writel(dwc->regs, DWC3_DEVTEN, reg);



            usb_gadget_connect(udc->gadget);
                gadget->ops->pullup(gadget, 1);
                // gadget.c
                dwc3_gadget_pullup(struct usb_gadget *g, int is_on)
                    dwc3_gadget_run_stop(dwc, is_on, false);
                        if (is_on) {
                            reg |= DWC3_DCTL_RUN_STOP;                  // shl 重要 run
                        dwc3_writel(dwc->regs, DWC3_DCTL, reg);



/*
usb_gadget_driver.bind = composite_bind
          driver->bind(udc->gadget);


composite = driver;  g_dnl_driver  usb_composite_driver
  composite->bind(cdev);
g_dnl_driver.bind()
g_dnl_bind();
*/
// ^^^^^^^^^^^^^^^^^^^^^^^^ g_dnl_register -> udc_bind_to_driver ->  composite_driver.bind  ->  g_dnl_driver.bind()    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


// g_dnl.c
g_dnl_bind(cdev)
	g_dnl_string_defs[0].id = id;       // 0     .s = manufacturer ; "Rockchip"
	device_desc.iManufacturer = id;

	g_dnl_string_defs[1].id = id;       // 1    .s = product;     "USB download gadget";
	device_desc.iProduct = id;
    g_dnl_bind_fixup(&device_desc, cdev->driver->name);         // /* Fix to Google's VID and PID */  谷歌的VID PID
		/* Fix to Google's VID and PID */
		dev->idVendor  = __constant_cpu_to_le16(0x18d1);
		dev->idProduct = __constant_cpu_to_le16(0xd00d);

	g_dnl_string_defs[2].id = id;       // 2      .s = g_dnl_serial,  fastboot_bind() -> g_dnl_set_serialnumber() -> g_dnl_set_serialnumber(env_get("serial#"))  
	device_desc.iSerialNumber = id;

    g_dnl_config_register(cdev);                                // 注册 配置  config
        usb_configuration *config;
        config->label = "usb_dnload";
        config->bmAttributes = USB_CONFIG_ATT_ONE | USB_CONFIG_ATT_SELFPOWER;       // device 自供电
        config->bConfigurationValue = CONFIGURATION_NUMBER;     // 1     number
        config->iConfiguration = STRING_USBDOWN;                // 2   string usbdown
        config->bind = g_dnl_do_config;
        // composite.c
        usb_add_config(cdev, config);   
            config->cdev = cdev;    
            // usb_add_config: adding config #1 'usb_dnload'/000000007bd9e0c0
            list_add_tail(&config->list, &cdev->configs);

            config->bind(config);       // !!!!!!
            !
            // g_dnl.c
            g_dnl_do_config(struct usb_configuration *c)
                const char *s = c->cdev->driver->name;      // "usb_dnl_fastboot"
                for (; callback != g_dnl_bind_callback_end(); callback++)
                    if (!strcmp(s, callback->usb_function_name))
                        return callback->fptr(c);
                !
                // f_fastboot.c     配置 添加  function
                fastboot_add(struct usb_configuration *c)
                    struct f_fastboot *f_fb = fastboot_func;        // f_fb 全局变量  fastboot_func 没初始化
                    f_fb->usb_function.name = "f_fastboot";
                    f_fb->usb_function.bind = fastboot_bind;        // fastboot_bind
                    f_fb->usb_function.set_alt = fastboot_set_alt;
                    f_fb->usb_function.disable = fastboot_disable;
                    f_fb->usb_function.strings = fastboot_strings;
                    usb_add_function(c, &f_fb->usb_function);
                    !
                    // composite.c
                    usb_add_function(struct usb_configuration *config, struct usb_function *function)
                        function->config = config;
                        list_add_tail(&function->list, &config->functions);
                        function->bind(config, function);       // fastboot_bind !!!!!!!!!!!!!!!!
                        !
                        // f_fastboot.c
                        fastboot_bind(struct usb_configuration *c, struct usb_function *f)
                            id = usb_interface_id(c, f);
                                    id = config->next_interface_id;
                                    config->interface[id] = function;
                                    return id;

                            interface_desc.bInterfaceNumber = id;
                            
                            id = usb_string_id(c->cdev);
                                id = cdev->next_string_id;      // 第一个应该是1
                            fastboot_string_defs[0].id = id;    // fastboot_string_defs[0].s =   "Android Fastboot";
                            interface_desc.iInterface = id;
                            f_fb->in_ep = usb_ep_autoconfig(gadget, &fs_ep_in);
                            f_fb->in_ep->driver_data = c->cdev;

                                    #define USB_ENDPOINT_XFERTYPE_MASK	0x03	/* in bmAttributes */
                                    #define USB_ENDPOINT_XFER_CONTROL	0
                                    #define USB_ENDPOINT_XFER_ISOC		1
                                    #define USB_ENDPOINT_XFER_BULK		2
                                    #define USB_ENDPOINT_XFER_INT		3

                                    static struct usb_endpoint_descriptor fs_ep_in = {
                                        .bLength            = USB_DT_ENDPOINT_SIZE,
                                        .bDescriptorType    = USB_DT_ENDPOINT,
                                        .bEndpointAddress   = USB_DIR_IN,
                                        .bmAttributes       = USB_ENDPOINT_XFER_BULK,
                                        .wMaxPacketSize     = cpu_to_le16(64),
                                    };

                                    struct usb_ep *usb_ep_autoconfig(
                                                            struct usb_gadget		*gadget,
                                                            struct usb_endpoint_descriptor	*desc
                                                            )
                                        if (gadget_is_dwc3(gadget))
                                            if ((desc->bEndpointAddress & USB_DIR_IN) &&
                                                type == USB_ENDPOINT_XFER_BULK)
                                                name = "ep1in";
                                            else if ((desc->bEndpointAddress & USB_DIR_IN) == 0 &&
                                                type == USB_ENDPOINT_XFER_BULK)
                                                name = "ep2out";
                                            find_ep(gadget, name);

                            f_fb->out_ep = usb_ep_autoconfig(gadget, &fs_ep_out);
                            f_fb->out_ep->driver_data = c->cdev;
                            f->descriptors = fb_fs_function;        // f usb_function
                            if (gadget_is_dualspeed(gadget)) {
                                /* Assume endpoint addresses are the same for both speeds */
                                hs_ep_in.bEndpointAddress = fs_ep_in.bEndpointAddress;
                                hs_ep_out.bEndpointAddress = fs_ep_out.bEndpointAddress;
                                /* copy HS descriptors */
                                f->hs_descriptors = fb_hs_function;                         // 全局， 接口，端点描述符
                            }

                            g_dnl_serial[] = env_get("serial#");



            // cfg 1/000000007bd9e0c0 speeds: super high full
            // usb_add_config: interface 0 = f_fastboot/000000007bd9e200
    gcnum = g_dnl_get_bcd_device_number(cdev);
        gcnum = usb_gadget_controller_number(gadget);
            if (gadget_is_dwc3(gadget))
                return 0x23;
        gcnum += 0x200;

    device_desc.bcdDevice = gcnum
    // g_dnl_bind: calling usb_gadget_connect for controller 'dwc3-gadget'
    
    usb_gadget_connect(gadget);
        gadget->ops->pullup(gadget, 1);
            dwc3_gadget_pullup(struct usb_gadget *g, int is_on)
                struct dwc3		*dwc = gadget_to_dwc(g);
                dwc3_gadget_run_stop(dwc, is_on, false);

                    if (is_on) {

                        if (dwc->revision >= DWC3_REVISION_194A)
                            reg &= ~DWC3_DCTL_KEEP_CONNECT;
                        reg |= DWC3_DCTL_RUN_STOP;

                        if (dwc->has_hibernation)
                            reg |= DWC3_DCTL_KEEP_CONNECT;

                        dwc->pullups_connected = true;
                    dwc3_writel(dwc->regs, DWC3_DCTL, reg);




// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

/* All standard descriptors have these 2 fields at the beginning */
/*
struct usb_interface_descriptor {
    u8 bLength;
    u8 bDescriptorType;	// 0x04  接口描述符
    u8 bInterfaceNumber;    // 接口编号。这是用来区分设备上的不同接口的唯一编号。
    u8 bAlternateSetting;
    u8 bNumEndpoints;
    u8 bInterfaceClass;     // 接口的类代码。这个值用来标识接口的类别，如 HID（人机交互设备）或 Mass Storage（大容量存储）等。
    u8 bInterfaceSubClass;
    u8 bInterfaceProtocol;  // 接口所遵循的协议代码。这指定了接口使用的特定协议。
    u8 iInterface;}         // 字符串 index    "Android Fastboot";     
*/
static struct usb_interface_descriptor interface_desc = {
	.bLength		= USB_DT_INTERFACE_SIZE,
	.bDescriptorType	= USB_DT_INTERFACE,
	.bInterfaceNumber	= 0x00,
	.bAlternateSetting	= 0x00,
	.bNumEndpoints		= 0x02,
	.bInterfaceClass	= FASTBOOT_INTERFACE_CLASS,
	.bInterfaceSubClass	= FASTBOOT_INTERFACE_SUB_CLASS,
	.bInterfaceProtocol	= FASTBOOT_INTERFACE_PROTOCOL,
};

static struct usb_endpoint_descriptor hs_ep_in = {
	.bLength		= USB_DT_ENDPOINT_SIZE,
	.bDescriptorType	= USB_DT_ENDPOINT,
	.bEndpointAddress	= USB_DIR_IN,
	.bmAttributes		= USB_ENDPOINT_XFER_BULK,
	.wMaxPacketSize		= cpu_to_le16(512),
};

static struct usb_endpoint_descriptor hs_ep_out = {
	.bLength		= USB_DT_ENDPOINT_SIZE,
	.bDescriptorType	= USB_DT_ENDPOINT,
	.bEndpointAddress	= USB_DIR_OUT,
	.bmAttributes		= USB_ENDPOINT_XFER_BULK,
	.wMaxPacketSize		= cpu_to_le16(512),
};

struct usb_descriptor_header {
	__u8  bLength;
	__u8  bDescriptorType;
} __attribute__ ((packed));

static struct usb_descriptor_header *fb_hs_function[] = {
	(struct usb_descriptor_header *)&interface_desc,
	(struct usb_descriptor_header *)&hs_ep_in,
	(struct usb_descriptor_header *)&hs_ep_out,
	NULL,
};