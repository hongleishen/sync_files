static int dwc3_core_soft_reset(struct dwc3 *dwc)
{
	u32	reg;
	reg = dwc3_readl(dwc->regs, DWC3_GCTL);
	reg &= ~DWC3_GCTL_CORESOFTRESET;
	dwc3_writel(dwc->regs, DWC3_GCTL, reg);
	return 0;
}