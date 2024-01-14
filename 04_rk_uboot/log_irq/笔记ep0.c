// 第 1 次  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[dbg: board/rockchip/evb_rk3568/evb_rk3568.c, usb_gadget_handle_interrupts, 25] ==== a. ====================================
... 
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_interrupt, 1122 ] [1092]  shl_add
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_state_string, 36 ] [35]  shl_add
Transfer Complete while ep0out in state 'Setup Phase'
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_xfer_complete, 928 ] [905]  shl_add
Setup Phase
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_inspect_setup, 758 ] [738]  shl_add
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_std_request, 714 ] [695]  shl_add
Forwarding to gadget driver
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_delegate_req, 542 ] [528]  shl_add
[dbg: drivers/usb/gadget/composite.c, composite_setup, 816 ] [795]  shl_add
[dbg: drivers/usb/gadget/composite.c, count_configs, 282 ] [274]  shl_add

[dbg: drivers/usb/dwc3/ep0.c, dwc3_gadget_ep0_queue, 219 ] [215]  shl_add       // ep0_queue ^^^^^^^^^^^^^^
0
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_state_string, 36 ] [35]  shl_add
queueing request 000000007bdc3a40 to ep0out length 18 state 'Setup Phase'
[dbg: drivers/usb/dwc3/ep0.c, __dwc3_gadget_ep0_queue, 115 ] [112]  shl_add
[dbg: drivers/usb/dwc3/ep0.c, __dwc3_ep0_do_control_data, 958 ] [934]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_map_request, 53 ] [52]  shl_add
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_start_trans, 54 ] [52]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_send_gadget_ep_cmd, 303 ] [296]  shl_add
[dwc3_writel drivers/usb/dwc3/gadget.c 307] 0x00000000fcc0c818 = 0x00000000
[dwc3_writel drivers/usb/dwc3/gadget.c 308] 0x00000000fcc0c814 = 0x7bdc0480
[dwc3_writel drivers/usb/dwc3/gadget.c 309] 0x00000000fcc0c810 = 0x00000000
[dwc3_writel drivers/usb/dwc3/gadget.c 311] 0x00000000fcc0c81c = 0x00000406
Command Complete --> 0

[dwc3_writel drivers/usb/dwc3/gadget.c 2568] 0x00000000fcc0c40c = 0x00000004

// log end =============================================================================================



d.2 dwc3_thread_interrupt                   // for (i = 0; i < dwc->num_event_buffers; i++)
    d.2.1 dwc3_process_event_buf(dwc, i);   //  根据 evt->count 次数，修改event地址， 进入 event_entry; 最后修改标志位; 开中断
        1. dwc3_process_event_entry(dwc, dwc3_event *event)         // dep_evt or  设备事件
            2.1 dwc3_endpoint_interrupt(dwc, dwc3_event_depevt *event)
            	if (epnum == 0 || epnum == 1) {
                    dwc3_ep0_interrupt(dwc, event);
                    return;
                }

dwc3_ep0_interrupt(struct dwc3 *dwc, struct dwc3_event_depevt *event) // ep0.c



// ^^^^^^^^^^^^^ dwc3_ep0_interrupt   ep0.c  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
struct usb_ctrlrequest {
	__u8 bRequestType;
	__u8 bRequest;
	__le16 wValue;
	__le16 wIndex;
	__le16 wLength;
} __attribute__ ((packed));

typedef u32 dma_addr_t;



struct dwc3 {
	struct usb_ctrlrequest	*ctrl_req;
	struct dwc3_trb		*ep0_trb;
	void			*ep0_bounce;
	void			*scratchbuf;
	u8			*setup_buf;
	dma_addr_t		ctrl_req_addr;
	dma_addr_t		ep0_trb_addr;

}


dwc->ctrl_req = dma_alloc_coherent(sizeof(*dwc->ctrl_req), (unsigned long *)&dwc->ctrl_req_addr);
static inline void *dma_alloc_coherent(size_t len, unsigned long *handle)
{
	*handle = (unsigned long)memalign(ARCH_DMA_MINALIGN, len);   // ctrl_req_addr值是分配的地址
	return (void *)*handle;
}




dwc3_ep0_interrupt(struct dwc3 *dwc,  struct dwc3_event_depevt *event)
	switch (event->endpoint_event) 
	case DWC3_DEPEVT_XFERCOMPLETE:
    !

dwc3_ep0_xfer_complete(struct dwc3 *dwc, struct dwc3_event_depevt *event)
	struct dwc3_ep		*dep = dwc->eps[event->endpoint_number];

	dep->flags &= ~DWC3_EP_BUSY;
	dep->resource_index = 0;
	dwc->setup_packet_pending = false;

	switch (dwc->ep0state)
	case EP0_SETUP_PHASE:
		dev_vdbg(dwc->dev, "Setup Phase");
		dwc3_ep0_inspect_setup(dwc, event);
        !
		break;

	case EP0_DATA_PHASE:
		dev_vdbg(dwc->dev, "Data Phase");
		dwc3_ep0_complete_data(dwc, event);
		break;

	case EP0_STATUS_PHASE:
		dev_vdbg(dwc->dev, "Status Phase");
		dwc3_ep0_complete_status(dwc, event);
		break;


dwc3_ep0_inspect_setup(dwc, event)
    struct usb_ctrlrequest *ctrl = dwc->ctrl_req;   // shl? ctrl 什么时候拿到数据？

    dwc->three_stage_setup = true;
    dwc->ep0_expect_in = !!(ctrl->bRequestType & USB_DIR_IN);
    dwc->ep0_next_event = DWC3_EP0_NRDY_DATA;

	if ((ctrl->bRequestType & USB_TYPE_MASK) == USB_TYPE_STANDARD)
		dwc3_ep0_std_request(dwc, ctrl);
        switch (ctrl->bRequest)
        default:                            // log 第一走此处
            dwc3_ep0_delegate_req(dwc, ctrl);
                dwc->gadget_driver->setup(&dwc->gadget, ctrl);
                    composite_setup(struct usb_gadget *gadget, const struct usb_ctrlrequest *ctrl)
                    !
// composite.c
composite_setup(struct usb_gadget *gadget, const struct usb_ctrlrequest *ctrl)
	switch (ctrl->bRequest) {
	case USB_REQ_GET_DESCRIPTOR:
		switch (w_value >> 8) {
		case USB_DT_DEVICE:
            memcpy(req->buf, &cdev->desc);

    req->length = value;
    req->zero = value < w_length;
    value = usb_ep_queue(gadget->ep0, req, GFP_KERNEL);
    !
    if (value < 0) {
        debug("ep_queue --> %d\n", value);
        req->status = 0;
        composite_setup_complete(gadget->ep0, req);
    }

    ep->ops->queue(ep, req, gfp_flags);

        // ep0.c
        dwc3_gadget_ep0_queue(struct usb_ep *ep, struct usb_request *request, gfp_t gfp_flags)
             __dwc3_gadget_ep0_queue(dep, req);
                __dwc3_ep0_do_control_data(dep, req);
                    dwc3_ep0_start_trans(dwc, dep->number,
						   req->request.dma,
						   transfer_size,
						   DWC3_TRBCTL_CONTROL_DATA, 1);


#define DWC3_TRBCTL_NORMAL		DWC3_TRB_CTRL_TRBCTL(1)
#define DWC3_TRBCTL_CONTROL_SETUP	DWC3_TRB_CTRL_TRBCTL(2)
#define DWC3_TRBCTL_CONTROL_STATUS2	DWC3_TRB_CTRL_TRBCTL(3)
#define DWC3_TRBCTL_CONTROL_STATUS3	DWC3_TRB_CTRL_TRBCTL(4)
#define DWC3_TRBCTL_CONTROL_DATA	DWC3_TRB_CTRL_TRBCTL(5)
#define DWC3_TRBCTL_ISOCHRONOUS_FIRST	DWC3_TRB_CTRL_TRBCTL(6)
#define DWC3_TRBCTL_ISOCHRONOUS		DWC3_TRB_CTRL_TRBCTL(7)
#define DWC3_TRBCTL_LINK_TRB		DWC3_TRB_CTRL_TRBCTL(8)



static int dwc3_ep0_start_trans(struct dwc3 *dwc, u8 epnum, dma_addr_t buf_dma,
				u32 len, u32 type, unsigned chain)
{
	my_dbg(" [52]  shl_add\n");
	struct dwc3_gadget_ep_cmd_params params;
	struct dwc3_trb			*trb;
	struct dwc3_ep			*dep;

	int				ret;

	dep = dwc->eps[epnum];
	if (dep->flags & DWC3_EP_BUSY) {
		dev_vdbg(dwc->dev, "%s still busy", dep->name);
		return 0;
	}

	trb = &dwc->ep0_trb[dep->free_slot];

	if (chain)
		dep->free_slot++;

	trb->bpl = lower_32_bits(buf_dma);
	trb->bph = upper_32_bits(buf_dma);
	trb->size = len;
	trb->ctrl = type;

	trb->ctrl |= (DWC3_TRB_CTRL_HWO
			| DWC3_TRB_CTRL_ISP_IMI);

	if (chain)
		trb->ctrl |= DWC3_TRB_CTRL_CHN;
	else
		trb->ctrl |= (DWC3_TRB_CTRL_IOC
				| DWC3_TRB_CTRL_LST);

	dwc3_flush_cache((uintptr_t)buf_dma, len);
	dwc3_flush_cache((uintptr_t)trb, sizeof(*trb));

	if (chain)
		return 0;

	memset(&params, 0, sizeof(params));
	params.param0 = upper_32_bits(dwc->ep0_trb_addr);       // !!!
	params.param1 = lower_32_bits(dwc->ep0_trb_addr);       // !!!

	ret = dwc3_send_gadget_ep_cmd(dwc, dep->number,
			DWC3_DEPCMD_STARTTRANSFER, &params);
	if (ret < 0) {
		dev_dbg(dwc->dev, "%s STARTTRANSFER failed", dep->name);
		return ret;
	}

	dep->flags |= DWC3_EP_BUSY;
	dep->resource_index = dwc3_gadget_ep_get_transfer_index(dwc,
			dep->number);

	dwc->ep0_next_event = DWC3_EP0_COMPLETE;

	return 0;
}




[dbg: drivers/usb/dwc3/ep0.c, __dwc3_ep0_do_control_data, 958 ] [934]  shl_add
[dbg: drivers/usb/gadget/udc/udc-core.c, usb_gadget_map_request, 53 ] [52]  shl_add
[dbg: drivers/usb/dwc3/ep0.c, dwc3_ep0_start_trans, 54 ] [52]  shl_add
[dbg: drivers/usb/dwc3/gadget.c, dwc3_send_gadget_ep_cmd, 303 ] [296]  shl_add
[dwc3_writel drivers/usb/dwc3/gadget.c 307] 0x00000000fcc0c818 = 0x00000000
[dwc3_writel drivers/usb/dwc3/gadget.c 308] 0x00000000fcc0c814 = 0x7bdc0480
[dwc3_writel drivers/usb/dwc3/gadget.c 309] 0x00000000fcc0c810 = 0x00000000
[dwc3_writel drivers/usb/dwc3/gadget.c 311] 0x00000000fcc0c81c = 0x00000406
Command Complete --> 0

[dwc3_writel drivers/usb/dwc3/gadget.c 2568] 0x00000000fcc0c40c = 0x00000004