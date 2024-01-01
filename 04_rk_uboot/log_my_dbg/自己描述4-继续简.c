// ^^^^^^^^^^^^     dwc3_uboot_init()     ^^^^^^^^^^^^^^core.c udc-core.c^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dwc3_uboot_init()                                                               // core.c
    dwc3 成员初始化
    dwc3_core_init()
    dwc3_core_init_mode()
        dwc3_set_mode()           // 设置device
        dwc3_gadget_init()
            // gadget初始化
            dwc3_gadget_init_endpoints
            usb_add_gadget_udc
                // udc初始化
    

// ^^^^^^^^^^^^^^^^^^^^^^^  g_dnl_register()  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

// g_dnl.c      struct usb_composite_driver  g_dnl_driver    =  {.bind = g_dnl_bind, .name = "usb_dnl_fastboot"}         
//      在composite.c 中用        composite = g_dnl_driver   找到udc， 调用 usb_gadget_driver.bind

// composite.c  struct usb_gadget_driver     composite_driver = {.bind = composite_bind)                                 
// 在 udc-core.c 中用
g_dnl_register("usb_dnl_fastboot");
    // g_dnl.c            usb_composite_driver   
    g_dnl_driver.name = name;
    usb_composite_register(&g_dnl_driver);
        // composite.c
        composite = driver;

        // udc-core.c              usb_gadget_driver
        usb_gadget_register_driver(&composite_driver);             //  usb_gadget_driver composite_driver = {.bind = composite_bind)
        !   //   找到UDC        usb_gadget_driver
        udc_bind_to_driver(udc, driver);
            udc->driver = driver;
            usb_gadget_udc_set_speed(udc, driver->speed);
            driver->bind(udc->gadget);
                // composite.c
                composite_bind(struct usb_gadget *gadget)
                    cdev 初始化
                    composite->bind(cdev);     
                    // 就是 g_dnl_driver.bind()
                    ---->
                        g_dnl_bind();  //  下面解释 g_dnl_bind(cdev)  ^^^^^^g_dnl_bind 汉语简述^^^^^^^^^^^^^^^^^^^^^              
                                device_desc                 // 设备描述符 参数设置
                                usb_configuration *config;  // 配置描述符 初始化化
                                list_add_tail(&config->list, &cdev->configs);
                                config->bind(config);       // g_dnl_do_config()
                                    g_dnl_do_config
                                        fastboot_add()      // 
                                            // function 初始化
                                            usb_add_function()
                                                list_add_tail(&function->list, &config->functions);
                                                function->bind(config, function);       // fastboot_bind !!!!!!!!!!!!!!!!
                                                    interface_desc.bInterfaceNumber = id;                   // 接口描述符 初始化
                                                    interface_desc.iInterface = id;
                                                    f_fb->in_ep = usb_ep_autoconfig(gadget, &fs_ep_in);

                                                    f->descriptors = fb_fs_function;        // 全局， 接口，端点描述符
                                                    f->hs_descriptors = fb_hs_function;     // 全局， 接口，端点描述符

                                usb_gadget_connect(udc->gadget);
                                    dwc3_writel(dwc->regs, DWC3_DCTL, DWC3_DCTL_RUN_STOP);


            usb_gadget_udc_start(udc);
                udc->gadget->ops->udc_start(udc->gadget, udc->driver);
                !
                // gadget.c
                dwc3_gadget_start(struct usb_gadget *g, struct usb_gadget_driver *driver)
                    dwc3_writel(dwc->regs, DWC3_DCFG, DWC3_DSTS_HIGHSPEED);

                    dep = dwc->eps[0]; dep = dwc->eps[1];
                    __dwc3_gadget_ep_enable(dep, &dwc3_gadget_ep0_desc, NULL, false, false);
                    dwc3_ep0_out_start(dwc);
                        dwc3_ep0_start_trans(dwc, 0, dwc->ctrl_req_addr, 8,  DWC3_TRBCTL_CONTROL_SETUP, 0);
                            dwc3_send_gadget_ep_cmd(dwc, dep->number, DWC3_DEPCMD_STARTTRANSFER, &params);
                    dwc3_gadget_enable_irq(dwc)


            usb_gadget_connect(udc->gadget);
                gadget->ops->pullup(gadget, 1);
                // gadget.c
                    dwc3_writel(dwc->regs, DWC3_DCTL, DWC3_DCTL_RUN_STOP);