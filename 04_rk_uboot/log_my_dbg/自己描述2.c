// ^^^^^^^^^^^^     dwc3_uboot_init()     ^^^^^^^^^^^^^^core.c udc-core.c^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dwc3_uboot_init()                                                               // core.c
    struct dwc3		*dwc； // 初始化dwc成员

    dwc3_core_init()
        dwc3_core_soft_reset
        dwc3_phy_setup
    
    dwc3_core_init_mode()
        dwc3_set_mode(dwc, DWC3_GCTL_PRTCAP_DEVICE);
        dwc3_gadget_init(dwc);                                                  // gadget.c
            // gadget初始化
            dwc->gadget.ops			= &dwc3_gadget_ops;
            dwc->gadget.max_speed		= USB_SPEED_SUPER;
            dwc->gadget.speed		= USB_SPEED_UNKNOWN;
            dwc->gadget.name		= "dwc3-gadget";
            dwc3_gadget_init_endpoints(dwc);                                  

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




// ^^^^^^^^^^^^^^^^^^^^^^^  g_dnl_register()  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

// g_dnl.c      struct usb_composite_driver  g_dnl_driver    =  {.bind = g_dnl_bind}         在composite.c 中用
// composite.c  struct usb_gadget_driver     composite_driver = {.bind = composite_bind)     在 udc-core.c 中用
g_dnl_register("usb_dnl_fastboot");
    // g_dnl.c
    usb_composite_register(&g_dnl_driver);      // struct usb_composite_driver g_dnl_driver
        // composite.c
        composite = driver;
        
        // udc-core.c
        usb_gadget_register_driver(&composite_driver);             //  usb_gadget_driver composite_driver = {.bind = composite_bind)
        !
        usb_gadget_probe_driver(driver);                            //  usb_gadget_driver 参数正式使用
            找到UDC
        !
        udc_bind_to_driver(udc, driver);