// ^^^^^^^^^^^^     dwc3_uboot_init()     ^^^^^^^^^^^^^^core.c udc-core.c^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
dwc3_uboot_init()                                                               // core.c
    dwc3 成员初始化
    dwc3_core_init()
    dwc3_core_init_mode()
        dwc3_set_mode()           // 设置device
        dwc3_gadget_init()
            // gadget初始化
            dwc3_gadget_init_endpoints
                dwc3_gadget_init_hw_endpoints(dwc, dwc->num_out_eps, 0);
                dwc3_gadget_init_hw_endpoints(dwc, dwc->num_in_eps, 1);
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
            usb_gadget_udc_set_speed(udc, driver->speed);   // 空函数

            driver->bind(udc->gadget);
                // composite.c
                composite_bind(struct usb_gadget *gadget)
                    cdev 初始化
                    composite->bind(cdev);     
                    // 就是 g_dnl_driver.bind()
                    ---->
                        g_dnl_bind();  //  下面解释 g_dnl_bind(cdev)  ||||||||||||||||||||||||||| 下面解释 ||||||||||||||||||||||||||||||||||||||||                   
                    debug("usb_dnl_fastboot: ready")

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
    device_desc->idVendor  = __constant_cpu_to_le16(0x18d1);    // g_dnl_bind_fixup
    device_desc->idProduct = __constant_cpu_to_le16(0xd00d);

	g_dnl_string_defs[2].id = id;       // 2      .s = g_dnl_serial,  fastboot_bind() -> g_dnl_set_serialnumber() -> g_dnl_set_serialnumber(env_get("serial#"))  
	device_desc.iSerialNumber = id;

    g_dnl_config_register(cdev);                                // 注册 配置  config
        config 初始化
        // composite.c
        usb_add_config(cdev, config);       // config 加入到cdev->configs 链表
            config->cdev = cdev;    
            // usb_add_config: adding config #1 'usb_dnload'/000000007bd9e0c0
            list_add_tail(&config->list, &cdev->configs);
            config->bind(config);       // !!!!!!
            !
            g_dnl_do_config(struct usb_configuration *c)  // callback->fptr(c);      // "usb_dnl_fastboot"  根据名字找到函数 fastboot_add
                !
            // f_fastboot.c     配置 添加  function
            fastboot_add(struct usb_configuration *c)
                struct f_fastboot *f_fb = fastboot_func;        // fastboot_func 是全局变量
                // f_fb->usb_function 初始化
                usb_add_function(c, &f_fb->usb_function);
                !
                // composite.c
                usb_add_function(struct usb_configuration *config, struct usb_function *function)
                    function->config = config;
                    list_add_tail(&function->list, &config->functions);
                    function->bind(config, function);       // fastboot_bind !!!!!!!!!!!!!!!!
                    !
                    fastboot_bind(struct usb_configuration *c, struct usb_function *f)
                        interface_desc.bInterfaceNumber = id;       // id = config->next_interface_id;  config->interface[id] = function;    
                        fastboot_string_defs[0].id = id;            // fastboot_string_defs[0].s =   "Android Fastboot";    id = cdev->next_string_id;      // 第一个应该是1
                        interface_desc.iInterface = id;

                        f_fb->in_ep = usb_ep_autoconfig(gadget, &fs_ep_in);
                        f_fb->out_ep->driver_data = c->cdev;
                        
                        f->descriptors = fb_fs_function;        // 全局， 接口，端点描述符
                        f->hs_descriptors = fb_hs_function;     // 全局， 接口，端点描述符
                        

                        g_dnl_set_serialnumber(env_get("serial#");)
                            g_dnl_serial[] = env_get("serial#");



            // cfg 1/000000007bd9e0c0 speeds: super high full
            // usb_add_config: interface 0 = f_fastboot/000000007bd9e200

    device_desc.bcdDevice = g_dnl_get_bcd_device_number() ; // usb_gadget_controller_number
    // g_dnl_bind: calling usb_gadget_connect for controller 'dwc3-gadget'
    

    usb_gadget_connect(udc->gadget);
        gadget->ops->pullup(gadget, 1);
        // gadget.c
            dwc3_writel(dwc->regs, DWC3_DCTL, DWC3_DCTL_RUN_STOP);


// ^^^^^^g_dnl_bind 汉语简述^^^^^^^^^^^^^^^^^^^^^
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