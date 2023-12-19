
// dwc3_core_init
usb_write_d(0xf420c704, 0x40000000); //dwc3_writel(dwc->regs, DWC3_DCTL, DWC3_DCTL_CSFTRST);
    // dwc3_core_soft_reset
usb_write_d(0xf420c110, 0x30c12804);    // set DWC3_GCTL  put Core in Reset 
usb_write_d(0xf420c2c0, 0x810c0002);        // set DWC3_GUSB3PIPECTL
usb_write_d(0xf420c200, 0xc0102400);        // set DWC3_GUSB2PHYCFG

usb_write_d(0xf420c2c0, 0x010c0002);        // clr DWC3_GUSB3PIPECTL
usb_write_d(0xf420c200, 0x40102400);        // clr DWC3_GUSB2PHYCFG
usb_write_d(0xf420c110, 0x30c12004);    // clrDWC3_GCTL_CORESOFTRESET


usb_write_d(0xf420c11c, 0x0404018a);    // DWC3_GUCTL1 DWC3_GUCTL1_DEV_FORCE_20_CLK_FOR_30_CLK
usb_write_d(0xf420c110, 0x30c12004);    // hwparams1  DWC3_GCTL
usb_write_d(0xf420c2c0, 0x010c0002);    // dwc3_phy_setup  DWC3_GUSB3PIPECTL
usb_write_d(0xf420c200, 0x40102400);        // dwc3_hsphy_mode_setup  DWC3_GUSB2PHYCFG
usb_write_d(0xf420c200, 0x40101408);        // DWC3_GUSB2PHYCFG


// dwc3_event_buffers_setup
usb_write_d(0xf420c400, 0x7bd97880);    // DWC3_GEVNTADRLO
usb_write_d(0xf420c404, 0x00000000);    // DWC3_GEVNTADRHI
usb_write_d(0xf420c408, 0x00000100);    // DWC3_GEVNTSIZ
usb_write_d(0xf420c40c, 0x00000000);    // DWC3_GEVNTCOUNT

// dwc3_core_init_mode
usb_write_d(0xf420c110, 0x30c12004);    // dwc3_set_mode dwc3_core_init_mode

// gadget.c
usb_write_d(0xf420c704, 0x80000000);    // g_dnl_register DWC3_DCTL  run
usb_write_d(0xf420c700, 0x00080800);    // DWC3_DCFG speed
usb_write_d(0xf420c808, 0x00000000);    // DWC3_DEPCMDPAR0
usb_write_d(0xf420c804, 0x00000000);
usb_write_d(0xf420c800, 0x00000000);
usb_write_d(0xf420c80c, 0x00000409);
usb_write_d(0xf420c808, 0x00001000);
usb_write_d(0xf420c804, 0x00000500);
usb_write_d(0xf420c800, 0x00000000);
usb_write_d(0xf420c80c, 0x00000401);
usb_write_d(0xf420c808, 0x00000001);
usb_write_d(0xf420c804, 0x00000000);
usb_write_d(0xf420c800, 0x00000000);
usb_write_d(0xf420c80c, 0x00000402);
usb_write_d(0xf420c720, 0x00000001);
usb_write_d(0xf420c818, 0x00001000);
usb_write_d(0xf420c814, 0x02000500);
usb_write_d(0xf420c810, 0x00000000);
usb_write_d(0xf420c81c, 0x00000401);
usb_write_d(0xf420c818, 0x00000001);
usb_write_d(0xf420c814, 0x00000000);
usb_write_d(0xf420c810, 0x00000000);
usb_write_d(0xf420c81c, 0x00000402);
usb_write_d(0xf420c720, 0x00000003);
usb_write_d(0xf420c808, 0x00000000);
usb_write_d(0xf420c804, 0x7bd97a00);
usb_write_d(0xf420c800, 0x00000000);
usb_write_d(0xf420c80c, 0x00000406);
usb_write_d(0xf420c708, 0x00001e1f);
usb_write_d(0xf420c704, 0x80000000);