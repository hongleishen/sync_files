static irqreturn_t dwc3_check_event_buf(struct dwc3 *dwc, u32 buf)
{
	f_start_hook(2);
	dwc3_writel(dwc->regs, DWC3_GEVNTSIZ(buf), reg);

	{f_end_hook();  return IRQ_WAKE_THREAD;}
}
