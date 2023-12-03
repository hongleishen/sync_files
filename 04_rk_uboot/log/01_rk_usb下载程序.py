


fastboot:
	while (1) {
		if (g_dnl_detach())
			break;
		if (ctrlc())
			break;
		usb_gadget_handle_interrupts(controller_index);
	}



[dbg: drivers/usb/gadget/g_dnl.c, g_dnl_detach, 194 ] [182]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add





[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add


[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_thread_interrupt, 2585 ] [2518]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_buf, 2536 ] [2470]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_transfer_complete, 1861 ] [1813]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_cleanup_done_reqs, 1816 ] [1769]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_cleanup_done_trbs, 1740 ] [1694]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_giveback, 232 ] [227]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_unmap_request, 67 ] [65]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_giveback_request, 88 ] [85]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, bulk_out_complete, 519 ] [509]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, wakeup_thread, 460 ] [454]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, finish_reply, 1537 ] [1504]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, send_status, 1634 ] [1600]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, __fsg_is_set, 392 ] [391]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, start_transfer, 600 ] [588]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_ep_queue, 1104 ] [1075]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_ep_queue, 997 ] [969]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_map_request, 53 ] [52]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_one_trb, 727 ] [704]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_trb_dma_offset, 335 ] [327]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_send_gadget_ep_cmd, 303 ] [296]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_thread_interrupt, 2585 ] [2518]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_buf, 2536 ] [2470]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_transfer_complete, 1861 ] [1813]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_cleanup_done_reqs, 1816 ] [1769]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_cleanup_done_trbs, 1740 ] [1694]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_giveback, 232 ] [227]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_unmap_request, 67 ] [65]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_giveback_request, 88 ] [85]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, bulk_in_complete, 501 ] [492]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, wakeup_thread, 460 ] [454]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, fsg_main_thread, 2454 ] [2409]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, get_next_command, 2163 ] [2125]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, set_bulk_out_req_length, 422 ] [418]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, __fsg_is_set, 392 ] [391]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, start_transfer, 600 ] [588]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_ep_queue, 1104 ] [1075]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_ep_queue, 997 ] [969]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_map_request, 53 ] [52]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_one_trb, 727 ] [704]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_trb_dma_offset, 335 ] [327]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_send_gadget_ep_cmd, 303 ] [296]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, sleep_thread, 664 ] [650]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, sleep_thread, 664 ] [650]  shl_add


[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_thread_interrupt, 2585 ] [2518]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_buf, 2536 ] [2470]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_transfer_complete, 1861 ] [1813]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_cleanup_done_reqs, 1816 ] [1769]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_cleanup_done_trbs, 1740 ] [1694]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_giveback, 232 ] [227]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_unmap_request, 67 ] [65]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_giveback_request, 88 ] [85]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, bulk_out_complete, 519 ] [509]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, wakeup_thread, 460 ] [454]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, __fsg_is_set, 392 ] [391]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, received_cbw, 2098 ] [2061]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, do_scsi_command, 1813 ] [1777]  shl_add
[dbg: drivers/usb/gadget/f_rockusb.c, rkusb_cmd_process, 776 ] [758]  shl_add
[dbg: drivers/usb/gadget/f_rockusb.c, dump_cbw, 106 ] [104]  shl_add
[dbg: drivers/usb/gadget/f_rockusb.c, rkusb_check_lun, 124 ] [121]  shl_add
[dbg: drivers/usb/gadget/f_rockusb.c, rkusb_do_reset, 169 ] [164]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, finish_reply, 1537 ] [1504]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, send_status, 1634 ] [1600]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, __fsg_is_set, 392 ] [391]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, start_transfer, 600 ] [588]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_ep_queue, 1104 ] [1075]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_ep_queue, 997 ] [969]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_map_request, 53 ] [52]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_trbs, 824 ] [800]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_prepare_one_trb, 727 ] [704]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_trb_dma_offset, 335 ] [327]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_send_gadget_ep_cmd, 303 ] [296]  shl_add
[dbg: drivers/usb/gadget/f_mass_storage.c, exception_in_progress, 414 ] [411]  shl_add

[dbg: drivers/usb/dwc3/core.c, dwc3_uboot_handle_interrupt, 888 ] [865]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_uboot_handle_interrupt, 2763 ] [2691]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_interrupt, 2628 ] [2559]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_check_event_buf, 2603 ] [2535]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_thread_interrupt, 2585 ] [2518]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_buf, 2536 ] [2470]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_gadget_kick_transfer, 891 ] [866]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_process_event_entry, 2517 ] [2452]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_interrupt, 1912 ] [1863]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_endpoint_transfer_complete, 1861 ] [1813]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_cleanup_done_reqs, 1816 ] [1769]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, __dwc3_cleanup_done_trbs, 1740 ] [1694]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_gadget_giveback, 232 ] [227]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_unmap_request, 67 ] [65]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_giveback_request, 88 ] [85]  shl_add
[dbg: drivers/usb/gadget/f_rockusb.c, __do_reset, 154 ] [150]  shl_add
DDR Version V1.13 20220218
In
ddrconfig:15
DDR4, 324MHz
BW=32 Col=10 Bk=4 BG=2 CS0 Row=16 CS=1 Die BW=16 Size=2048MB
tdqss: cs0 dqs0: 24ps, dqs1: -24ps, dqs2: -96ps, dqs3: -120ps,

change to: 324MHz
clk skew:0x89
PHY drv:clk:37,ca:37,DQ:37,odt:0
vrefinner:50%, vrefout:50%
dram drv:34,odt:0

change to: 528MHz
clk skew:0x89
PHY drv:clk:37,ca:37,DQ:37,odt:139
vrefinner:50%, vrefout:61%
dram drv:34,odt:120

change to: 780MHz
clk skew:0x89
PHY drv:clk:37,ca:37,DQ:37,odt:139
vrefinner:50%, vrefout:61%
dram drv:34,odt:120

change to: 1560MHz(final freq)
clk skew:0x89
PHY drv:clk:37,ca:37,DQ:37,odt:139
vrefinner:50%, vrefout:61%
dram drv:34,odt:120
cs 0:
the read training result:
DQS0:0x2f, DQS1:0x2e, DQS2:0x27, DQS3:0x2c,
min  :0x10  0xf  0xf  0x8  0x4  0x2  0x8  0x1 , 0xc  0xd  0x1  0x8  0x9  0xd  0xd  0xb ,
       0x3  0x4  0x5  0x7  0x4  0x2  0x3  0x3 , 0x8  0x3  0x3  0x1  0x8  0x8  0xa  0x5 ,
mid  :0x28 0x26 0x26 0x21 0x1b 0x1b 0x20 0x1b ,0x25 0x26 0x19 0x21 0x23 0x27 0x25 0x24 ,
      0x1c 0x1e 0x20 0x21 0x1d 0x1c 0x1c 0x1c ,0x21 0x1d 0x1d 0x19 0x1f 0x21 0x22 0x1f ,
max  :0x41 0x3e 0x3e 0x3b 0x33 0x35 0x39 0x35 ,0x3f 0x3f 0x32 0x3a 0x3d 0x41 0x3d 0x3e ,
      0x36 0x38 0x3b 0x3c 0x37 0x36 0x36 0x36 ,0x3b 0x38 0x37 0x32 0x37 0x3b 0x3b 0x3a ,
range:0x31 0x2f 0x2f 0x33 0x2f 0x33 0x31 0x34 ,0x33 0x32 0x31 0x32 0x34 0x34 0x30 0x33 ,
      0x33 0x34 0x36 0x35 0x33 0x34 0x33 0x33 ,0x33 0x35 0x34 0x31 0x2f 0x33 0x31 0x35 ,
the write training result:
DQS0:0x8d, DQS1:0x85, DQS2:0x76, DQS3:0x72,
min  :0x79 0x79 0x7c 0x7a 0x6c 0x6d 0x6f 0x6f 0x73 ,0x70 0x6f 0x6a 0x70 0x6c 0x6f 0x6f 0x6e 0x6a ,
      0x63 0x67 0x68 0x67 0x5e 0x5f 0x5d 0x5e 0x5e ,0x5d 0x5b 0x5e 0x5a 0x5c 0x5a 0x59 0x5a 0x5d ,
mid  :0x94 0x92 0x94 0x92 0x83 0x85 0x88 0x86 0x8d ,0x89 0x8a 0x80 0x89 0x86 0x88 0x89 0x89 0x80 ,
      0x7c 0x81 0x80 0x7f 0x78 0x78 0x77 0x79 0x77 ,0x77 0x72 0x76 0x72 0x74 0x75 0x73 0x74 0x76 ,
max  :0xb0 0xac 0xac 0xaa 0x9b 0x9d 0xa1 0x9e 0xa8 ,0xa3 0xa6 0x96 0xa2 0xa1 0xa2 0xa4 0xa4 0x97 ,
      0x96 0x9b 0x98 0x98 0x93 0x91 0x91 0x94 0x91 ,0x91 0x8a 0x8f 0x8a 0x8d 0x91 0x8e 0x8e 0x8f ,
range:0x37 0x33 0x30 0x30 0x2f 0x30 0x32 0x2f 0x35 ,0x33 0x37 0x2c 0x32 0x35 0x33 0x35 0x36 0x2d ,
      0x33 0x34 0x30 0x31 0x35 0x32 0x34 0x36 0x33 ,0x34 0x2f 0x31 0x30 0x31 0x37 0x35 0x34 0x32 ,
out
U-Boot SPL board init
U-Boot SPL 2017.09-gaaca6ffec1-211203 #zzz (Dec 03 2021 - 18:42:16)
unknown raw ID phN
unrecognized JEDEC id bytes: 00, 00, 00
Trying to boot from MMC2
MMC error: The cmd index is 1, ret is -110
Card did not respond to voltage select!
mmc_init: -95, time 16
spl: mmc init failed with error: -95
Trying to boot from MMC1
SPL: A/B-slot: _a, successful: 0, tries-remain: 7
Trying fit image at 0x4000 sector
## Verified-boot: 0
## Checking atf-1 0x00040000 ... sha256(fe4f274c06...) + OK
## Checking uboot 0x00a00000 ... sha256(a15bab0516...) + OK
## Checking fdt 0x00b5ab20 ... sha256(fcfda359c0...) + OK
## Checking atf-2 0x00068000 ... sha256(8d44036095...) + OK
## Checking atf-3 0xfdcd0000 ... sha256(e410275b51...) + OK
## Checking atf-4 0xfdcc9000 ... sha256(990c53fc01...) + OK
## Checking atf-5 0x00066000 ... sha256(315a4195a9...) + OK
## Checking optee 0x08400000 ... sha256(66bbd17352...) + OK
Jumping to U-Boot(0x00a00000) via ARM Trusted Firmware(0x00040000)
Total: 307.668 ms

INFO:    Preloader serial: 2
NOTICE:  BL31: v2.3():v2.3-181-gc9a647cae:cl
NOTICE:  BL31: Built : 10:55:41, Oct 18 2021
INFO:    GICv3 without legacy support detected.
INFO:    ARM GICv3 driver initialized in EL3
INFO:    pmu v1 is valid
INFO:    dfs DDR fsp_param[0].freq_mhz= 1560MHz
INFO:    dfs DDR fsp_param[1].freq_mhz= 324MHz
INFO:    dfs DDR fsp_param[2].freq_mhz= 528MHz
INFO:    dfs DDR fsp_param[3].freq_mhz= 780MHz
INFO:    Using opteed sec cpu_context!
INFO:    boot cpu mask: 0
INFO:    BL31: Initializing runtime services
INFO:    BL31: Initializing BL32
I/TC:
I/TC: OP-TEE version: 3.13.0-641-g4167319d3 #hisping.lin (gcc version 10.2.1 20201103 (GNU Toolchain for the A-profile Architecture 10.2-2020.11 (arm-10.16))) #8 Wed Mar 16 15:14:56 CST 2022 aarch64
I/TC: Primary CPU initializing
I/TC: Primary CPU switching to normal world boot
INFO:    BL31: Preparing for EL3 exit to normal world
INFO:    Entry point address = 0xa00000
INFO:    SPSR = 0x3c9
[dbg: drivers/usb/dwc3/dwc3-generic.c, dwc3_glue_bind, 312 ] [302]  shl_add
[dbg: drivers/usb/common/common.c, usb_get_dr_mode, 27 ] [26]  shl_add
[dbg: drivers/usb/dwc3/dwc3-generic.c, dwc3_glue_bind, 312 ] [302]  shl_add
[dbg: drivers/usb/common/common.c, usb_get_dr_mode, 27 ] [26]  shl_add


U-Boot 2017.09-gab70221-dirty #topeet (Nov 04 2023 - 22:01:29 +0800)