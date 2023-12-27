static irqreturn_t dwc3_check_event_buf(struct dwc3 *dwc, u32 buf)
{
	dwc3_writel(dwc->regs, DWC3_GEVNTSIZ(buf), reg);

	return IRQ_WAKE_THREAD;
}