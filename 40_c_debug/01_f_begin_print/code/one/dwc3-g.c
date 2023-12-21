
static int dwc3_glue_probe(struct udevice *dev)
{
	struct dwc3_glue_ops *ops = (struct dwc3_glue_ops *)dev_get_driver_data(dev);
	struct dwc3_glue_data *glue = dev_get_platdata(dev);
	struct udevice *child = NULL;
	int index = 0;
	int ret;

	glue->regs = dev_read_addr(dev);

	ret = dwc3_glue_clk_init(dev, glue);
	if (ret)
		return ret;

	ret = dwc3_glue_reset_init(dev, glue);
	if (ret)
		return ret;

	ret = device_find_first_child(dev, &child);
	if (ret)
		return ret;

	if (glue->resets.count < 1) {
		ret = dwc3_glue_reset_init(child, glue);
		if (ret)
			return ret;
	}

	while (child) {
		enum usb_dr_mode dr_mode;

		dr_mode = usb_get_dr_mode(child->node);
		device_find_next_child(&child);
		if (ops && ops->select_dr_mode)
			ops->select_dr_mode(dev, index, dr_mode);
		index++;
	}

	return 0;
}

static int dwc3_glue_remove(struct udevice *dev)
{
	struct dwc3_glue_data *glue = dev_get_platdata(dev);

	reset_release_bulk(&glue->resets);

	clk_release_bulk(&glue->clks);

	return 0;
}

static const struct udevice_id dwc3_glue_ids[] = {
	{ .compatible = "xlnx,zynqmp-dwc3" },
	{ .compatible = "ti,keystone-dwc3"},
	{ .compatible = "ti,dwc3", .data = (ulong)&ti_ops },
	{ .compatible = "ti,am437x-dwc3", .data = (ulong)&ti_ops },
	{ .compatible = "rockchip,rk3328-dwc3" },
	{ .compatible = "rockchip,rk3399-dwc3" },
	{ }
};

U_BOOT_DRIVER(dwc3_generic_wrapper) = {
	.name	= "dwc3-generic-wrapper",
	.id	= UCLASS_NOP,
	.of_match = dwc3_glue_ids,
	.bind = dwc3_glue_bind,
	.probe = dwc3_glue_probe,
	.remove = dwc3_glue_remove,
	.platdata_auto_alloc_size = sizeof(struct dwc3_glue_data),

};
