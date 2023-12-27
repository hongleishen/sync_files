/**
 * Caller should take care of locking. This function will
 * return 0 on success or -EINVAL if wrong Test Selector
 * is passed
 */

static void dwc3_process_event_entry(struct dwc3 *dwc,
		const union dwc3_event *event)
{
	f_start_hook(9);
	/* Endpoint IRQ, handle it and return early */
	if (event->type.is_devspec == 0) {
		/* depevt */
		{f_end_hook();  return dwc3_endpoint_interrupt(dwc, &event->depevt);}
	}

	switch (event->type.type) {
	case DWC3_EVENT_TYPE_DEV:
		dwc3_gadget_interrupt(dwc, &event->devt);
		break;
	/* REVISIT what to do with Carkit and I2C events ? */
	default:
		dev_err(dwc->dev, "UNKNOWN IRQ type %d\n", event->raw);
	}
	f_end_hook();
}


void a(void)
{
	f_start_hook(28);
	int a = 10;
	{f_end_hook();
	return dwc3_send_gadget_ep_cmd(dwc, dep->number,
			DWC3_DEPCMD_SETEPCONFIG, &params);}
}


void b(void)
{
	f_start_hook(36);
	int a = 10;
	{f_end_hook();  return 10}
}

void b(void)
{
	f_start_hook(42);
	int a = 10;
	do {
		printf("a = %d\n", a);
	} while (a--);
	f_end_hook();
}
