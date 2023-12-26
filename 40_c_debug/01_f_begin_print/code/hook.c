static int dwc3_core_soft_reset(struct dwc3 *dwc)
{
	f_start_hook(2);
	u32	reg;
	reg = dwc3_readl(dwc->regs, DWC3_GCTL);
		{f_end_hook();  return abc;}
	reg &= ~DWC3_GCTL_CORESOFTRESET;
	dwc3_writel(dwc->regs, DWC3_GCTL, reg);
	f_end_hook();
}
