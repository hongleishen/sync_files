do_fastboot 函数首先调用 usb_gadget_initialize() 
最终调用
dwc3_uboot_init()  
    struct dwc3		*dwc； // 初始化dwc成员

    dwc3_core_init()
        dwc3_core_soft_reset
        dwc3_phy_setup
    
    dwc3_core_init_mode()
        dwc3_set_mode(dwc, DWC3_GCTL_PRTCAP_DEVICE);
        dwc3_gadget_init(dwc);
            // gadget初始化
            dwc->gadget.ops			= &dwc3_gadget_ops;
            dwc->gadget.max_speed		= USB_SPEED_SUPER;
            dwc->gadget.speed		= USB_SPEED_UNKNOWN;
            dwc->gadget.name		= "dwc3-gadget";
            dwc3_gadget_init_endpoints(dwc);

            // udc-core.c
            usb_add_gadget_udc((struct device *)dwc->dev, &dwc->gadget);
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



接着do_fastboot 调用  g_dnl_register("usb_dnl_fastboot");
// gadget/g_dnl.c  ^^^^^^^^^ g_dnl_register ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
// fastboot.c
g_dnl_register("usb_dnl_fastboot");
    // g_dnl.c     
    usb_composite_register(&g_dnl_driver);
        // composite.c
        usb_composite_register(struct usb_composite_driver *driver)     // struct usb_composite_driver g_dnl_driver
            // static struct usb_composite_driver *composite;
            composite = driver;
            usb_gadget_register_driver(&composite_driver);             //  usb_gadget_driver composite_driver = {.bind = composite_bind)
                // udc/udc-core.c
                usb_gadget_register_driver(struct usb_gadget_driver *driver)
                    usb_gadget_probe_driver(driver);                            //  usb_gadget_driver 参数正式使用
                        udc_bind_to_driver(udc, driver);
                    
                        
                        udc_bind_to_driver(struct usb_udc *udc, struct usb_gadget_driver *driver)
                                usb_gadget_udc_set_speed(udc, driver->speed);

                                driver->bind(udc->gadget);
                                    // composite.c
                                    composite_bind()

                                        cdev = calloc(sizeof *cdev, 1);         // 分配cdev
                                        gadget->dev.driver_data = cdev;
                                        cdev->gadget = gadget;
                                        cdev->req = usb_ep_alloc_request(gadget->ep0, GFP_KERNEL);
                                        cdev->req->complete = composite_setup_complete;
                                        cdev->driver = composite;               // g_dnl_driver
                                        usb_gadget_set_selfpowered(gadget);     // 仅仅设置变了标志
                                        usb_ep_autoconfig_reset(cdev->gadget);
                                        composite->bind(cdev);     // 就是 g_dnl_driver.bind()
                                        ---->
                                            g_dnl_bind();  //  下面解释 g_dnl_bind(cdev)



                                usb_gadget_udc_start(udc);
                                    udc->gadget->ops->udc_start(udc->gadget, udc->driver);
                                        // gadget.c
                                        dwc3_gadget_start(struct usb_gadget *g, struct usb_gadget_driver *driver)
                                            dwc->gadget_driver	= driver;
                                            switch (dwc->maximum_speed) 
                                                dwc3_writel(dwc->regs, DWC3_DCFG, reg);

                                            dep = dwc->eps[0];
                                            __dwc3_gadget_ep_enable(dep, &dwc3_gadget_ep0_desc, NULL, false, false);
                                                dwc3_writel(dwc->regs, DWC3_DALEPENA, reg);         // 0xc720
                                            dep = dwc->eps[0];
                                            __dwc3_gadget_ep_enable(dep, &dwc3_gadget_ep0_desc, NULL, false, false);
                                            /* begin to receive SETUP packets */
                                            dwc->ep0state = EP0_SETUP_PHASE;
                                            dwc3_ep0_out_start(dwc);

                                            dwc3_gadget_enable_irq(dwc)

                                usb_gadget_connect(udc->gadget);
                                    gadget->ops->pullup(gadget, 1);
                                    // gadget.c
                                    dwc3_gadget_pullup(struct usb_gadget *g, int is_on)
                                        dwc3_gadget_run_stop(dwc, is_on, false);
                                            if (is_on) {
                                                reg |= DWC3_DCTL_RUN_STOP;                  // shl 重要 run
                                            dwc3_writel(dwc->regs, DWC3_DCTL, reg);




// g_dnl.c
g_dnl_bind(cdev)
	g_dnl_string_defs[0].id = id;       // 0
	device_desc.iManufacturer = id;

	g_dnl_string_defs[1].id = id;       // 1
	device_desc.iProduct = id;
    g_dnl_bind_fixup(&device_desc, cdev->driver->name);         // /* Fix to Google's VID and PID */  谷歌的VID PID

	g_dnl_string_defs[2].id = id;       // 2
	device_desc.iSerialNumber = id;

    g_dnl_config_register(cdev);                                // 注册 配置  config
        struct usb_configuration *config;
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
                g_dnl_do_config(struct usb_configuration *c)
                    const char *s = c->cdev->driver->name;      // "usb_dnl_fastboot"
                    for (; callback != g_dnl_bind_callback_end(); callback++)
                        if (!strcmp(s, callback->usb_function_name))
                            return callback->fptr(c);
                                    // f_fastboot.c
                                    fastboot_add(struct usb_configuration *c)
                                        struct f_fastboot *f_fb = fastboot_func;
                                        f_fb->usb_function.name = "f_fastboot";
                                        f_fb->usb_function.bind = fastboot_bind;
                                        f_fb->usb_function.set_alt = fastboot_set_alt;
                                        f_fb->usb_function.disable = fastboot_disable;
                                        f_fb->usb_function.strings = fastboot_strings;
                                        usb_add_function(c, &f_fb->usb_function);
                                        // composite.c
                                        usb_add_function(struct usb_configuration *config, struct usb_function *function)
                                            function->config = config;
                                            list_add_tail(&function->list, &config->functions);
                                            function->bind(config, function);       // fastboot_bind !!!!!!!!!!!!!!!!
    
                                            // f_fastboot.c    function->bind(config, function);
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
                                                f->descriptors = fb_fs_function;
                                                if (gadget_is_dualspeed(gadget)) {
                                                    /* Assume endpoint addresses are the same for both speeds */
                                                    hs_ep_in.bEndpointAddress = fs_ep_in.bEndpointAddress;
                                                    hs_ep_out.bEndpointAddress = fs_ep_out.bEndpointAddress;
                                                    /* copy HS descriptors */
                                                    f->hs_descriptors = fb_hs_function;
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