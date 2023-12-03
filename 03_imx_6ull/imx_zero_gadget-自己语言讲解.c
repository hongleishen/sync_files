// 1. gadget/legacy/zero.c 

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

    // 最终展开
static int __init zero_driver_init(void) \
{ 
    return usb_composite_probe(&(zero_driver) ); 
} 
module_init(zero_driver_init); \


// 2. gadget/composite.c 
usb_composite_probe(struct usb_composite_driver *driver)
{
	struct usb_gadget_driver *gadget_driver;
	driver->gadget_driver = composite_driver_template;
	gadget_driver = &driver->gadget_driver;

	gadget_driver->function =  (char *) driver->name;
	gadget_driver->driver.name = driver->name;
	gadget_driver->max_speed = driver->max_speed;

	return usb_gadget_probe_driver(gadget_driver);
}

// 3. gadget/udc/core.c
usb_gadget_probe_driver(struct usb_gadget_driver *driver)
    udc_bind_to_driver(udc, driver);
        driver->bind(udc->gadget, driver);    // composite_bind

// 2-- gadget/composite.c
composite_bind(struct usb_gadget *gadget, struct usb_gadget_driver *gdriver)
	struct usb_composite_dev	*cdev;
	struct usb_composite_driver	*composite = to_cdriver(gdriver);
        composite->bind(cdev);              // zero_bind


// 1--  gadget/legacy/zero.c
zero_bind(struct usb_composite_dev *cdev)
