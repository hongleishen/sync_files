[BEGIN] 2023/10/29 星期日 21:37:21

=> usb start
starting USB...


// Bus dwc3@fcc00000: 是下方USB口
Bus dwc3@fcc00000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_get_by_indexed_prop(dev=000000007bd39d20, index=0, clk=000000007bdb5b80)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdb5b80)
clk_request(dev=000000007bd3ad70, clk=000000007bdb5b80)
clk_get_by_indexed_prop(dev=000000007bd39d20, index=1, clk=000000007bdb5b90)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdb5b90)
clk_request(dev=000000007bd3ad70, clk=000000007bdb5b90)
clk_get_by_indexed_prop(dev=000000007bd39d20, index=2, clk=000000007bdb5ba0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdb5ba0)
clk_request(dev=000000007bd3ad70, clk=000000007bdb5ba0)
clk_get_by_indexed_prop(dev=000000007bd39d20, index=3, clk=000000007bdb5bb0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdb5bb0)
clk_request(dev=000000007bd3ad70, clk=000000007bdb5bb0)
clk_enable(clk=000000007bdb5b80)
clk_enable(clk=000000007bdb5b90)
clk_enable(clk=000000007bdb5ba0)
clk_enable(clk=000000007bdb5bb0)
of_read_u32: #reset-cells: 0x1 (1)
reset_get_by_index(dev=000000007bd39dd0, index=0, reset_ctl=000000007bdb5c00)
of_read_u32: #reset-cells: 0x1 (1)
rockchip_reset_probe(base=00000000fdd20400) (sf_reset_offset=400, sf_reset_num=30)
reset_of_xlate_default(reset_ctl=000000007bdb5c00)
rockchip_reset_request(reset_ctl=000000007bdb5c00) (dev=000000007bd3aef0, id=148) (sf_reset_num=30)
reset_deassert(reset_ctl=000000007bdb5c00)
rockchip_reset_deassert(reset_ctl=000000007bdb5c00) (dev=000000007bd3aef0, id=148) (reg_addr=00000000fdd20424)
ofnode_read_string: dr_mode: otg
ofnode_read_string: maximum-speed: <not found>
usb maximum-speed not found
ofnode_read_string: dr_mode: otg
ofnode_read_bool: snps,has-lpm-erratum: false
ofnode_read_bool: snps,is-utmi-l1-suspend: false
ofnode_read_bool: snps,disable_scramble_quirk: false
ofnode_read_bool: snps,u2exit_lfps_quirk: false
ofnode_read_bool: snps,u2ss_inp3_quirk: false
ofnode_read_bool: snps,req_p1p2p3_quirk: false
ofnode_read_bool: snps,del_p1p2p3_quirk: false
ofnode_read_bool: snps,del_phy_power_chg_quirk: false
ofnode_read_bool: snps,lfps_filter_quirk: false
ofnode_read_bool: snps,rx_detect_poll_quirk: false
ofnode_read_bool: snps,dis_u3_susphy_quirk: false
ofnode_read_bool: snps,dis_u2_susphy_quirk: false
ofnode_read_bool: snps,dis_enblslpm_quirk: true
ofnode_read_bool: snps,dis-u2-freeclk-exists-quirk: true
ofnode_read_bool: snps,tx_de_emphasis_quirk: false
reset_assert(reset_ctl=000000007bdb5c00)
rockchip_reset_assert(reset_ctl=000000007bdb5c00) (dev=000000007bd3aef0, id=148) (reg_addr=00000000fdd20424)
of_read_u32: #phy-cells: 0x0 (0)
of_read_u32: #phy-cells: 0x1 (1)
generic_phy_get_by_index(dev=000000007bd39dd0, index=0, phy=000000007bdb5c40)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_bool: rockchip,grf: false
ofnode_read_bool: rockchip,usbgrf: true
ofnode_read_u32: rockchip,usbgrf: of_read_u32: rockchip,usbgrf: 0x125 (293)
** translation for device /syscon@fdca0000 **
bus is default (na=2, ns=2) on /
reached root node
** translation for device /usb2-phy@fe8a0000 **
bus is default (na=2, ns=2) on /
reached root node
reset_get_by_name(dev=000000007bdaa5c0, name=phy, reset_ctl=000000007bdb5cb8)
fdt_stringlist_search() failed: -22
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: (not found)
ofnode_read_u32: vbus-supply: of_read_u32: vbus-supply: 0x127 (295)
generic_phy_get_by_index(dev=000000007bd39dd0, index=1, phy=000000007bdb5c60)
of_read_u32: #phy-cells: 0x0 (0)
of_read_u32: #phy-cells: 0x1 (1)
ofnode_read_u32: rockchip,pipe-grf: of_read_u32: rockchip,pipe-grf: 0x11c (284)
** translation for device /syscon@fdc50000 **
bus is default (na=2, ns=2) on /
reached root node
ofnode_read_u32: rockchip,pipe-phy-grf: of_read_u32: rockchip,pipe-phy-grf: 0x11d (285)
** translation for device /syscon@fdc70000 **
bus is default (na=2, ns=2) on /
reached root node
clk_get_by_indexed_prop(dev=000000007bdaa300, index=0, clk=000000007bdb5d20)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdb5d20)
clk_request(dev=000000007bd3abf0, clk=000000007bdb5d20)
reset_get_by_name(dev=000000007bdaa300, name=combphy, reset_ctl=000000007bdb5d10)
comparing combphy with combphy-apb
comparing combphy with combphy
reset_get_by_index(dev=000000007bdaa300, index=1, reset_ctl=000000007bdb5d10)
of_read_u32: #reset-cells: 0x1 (1)
of_read_u32: #reset-cells: 0x1 (1)
reset_of_xlate_default(reset_ctl=000000007bdb5d10)
rockchip_reset_request(reset_ctl=000000007bdb5d10) (dev=000000007bd3aef0, id=453) (sf_reset_num=30)
ofnode_read_u32_array: rockchip,pcie1ln-sel-bits: of_read_u32_array: rockchip,pcie1ln-sel-bits: ofnode_read_bool: rockchip,enable-ssc: false
clk_enable(clk=000000007bdb5d20)
ofnode_read_bool: rockchip,enable-ssc: false
reset_deassert(reset_ctl=000000007bdb5d10)
rockchip_reset_deassert(reset_ctl=000000007bdb5d10) (dev=000000007bd3aef0, id=453) (reg_addr=00000000fdd20470)
fixed_regulator_set_enable: dev='vcc5v0-otg-regulator', enable=1, delay=0, has_gpio=1
fixed_regulator_set_enable: done
reset_deassert(reset_ctl=000000007bdb5c00)
rockchip_reset_deassert(reset_ctl=000000007bdb5c00) (dev=000000007bd3aef0, id=148) (reg_addr=00000000fdd20424)
xhci_register: dev='dwc3@fcc00000', ctrl=000000007bdcf340, hccr=00000000fcc00000, hcor=00000000fcc00020
// Halt the HC: 00000000fcc00020
// Reset the HC
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10


# 这个用不到
Bus dwc3@fd000000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_get_by_indexed_prop(dev=000000007bd39ea0, index=0, clk=000000007bdd1f80)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd1f80)
clk_request(dev=000000007bd3ad70, clk=000000007bdd1f80)
clk_get_by_indexed_prop(dev=000000007bd39ea0, index=1, clk=000000007bdd1f90)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd1f90)
clk_request(dev=000000007bd3ad70, clk=000000007bdd1f90)
clk_get_by_indexed_prop(dev=000000007bd39ea0, index=2, clk=000000007bdd1fa0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd1fa0)
clk_request(dev=000000007bd3ad70, clk=000000007bdd1fa0)
clk_get_by_indexed_prop(dev=000000007bd39ea0, index=3, clk=000000007bdd1fb0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd1fb0)
clk_request(dev=000000007bd3ad70, clk=000000007bdd1fb0)
clk_enable(clk=000000007bdd1f80)
clk_enable(clk=000000007bdd1f90)
clk_enable(clk=000000007bdd1fa0)
clk_enable(clk=000000007bdd1fb0)
of_read_u32: #reset-cells: 0x1 (1)
reset_get_by_index(dev=000000007bd39f50, index=0, reset_ctl=000000007bdd3040)
of_read_u32: #reset-cells: 0x1 (1)
reset_of_xlate_default(reset_ctl=000000007bdd3040)
rockchip_reset_request(reset_ctl=000000007bdd3040) (dev=000000007bd3aef0, id=149) (sf_reset_num=30)
reset_deassert(reset_ctl=000000007bdd3040)
rockchip_reset_deassert(reset_ctl=000000007bdd3040) (dev=000000007bd3aef0, id=149) (reg_addr=00000000fdd20424)
ofnode_read_string: dr_mode: host
ofnode_read_string: maximum-speed: <not found>
usb maximum-speed not found
ofnode_read_string: dr_mode: host
ofnode_read_bool: snps,has-lpm-erratum: false
ofnode_read_bool: snps,is-utmi-l1-suspend: false
ofnode_read_bool: snps,disable_scramble_quirk: false
ofnode_read_bool: snps,u2exit_lfps_quirk: false
ofnode_read_bool: snps,u2ss_inp3_quirk: false
ofnode_read_bool: snps,req_p1p2p3_quirk: false
ofnode_read_bool: snps,del_p1p2p3_quirk: false
ofnode_read_bool: snps,del_phy_power_chg_quirk: false
ofnode_read_bool: snps,lfps_filter_quirk: false
ofnode_read_bool: snps,rx_detect_poll_quirk: false
ofnode_read_bool: snps,dis_u3_susphy_quirk: false
ofnode_read_bool: snps,dis_u2_susphy_quirk: false
ofnode_read_bool: snps,dis_enblslpm_quirk: true
ofnode_read_bool: snps,dis-u2-freeclk-exists-quirk: true
ofnode_read_bool: snps,tx_de_emphasis_quirk: false
reset_assert(reset_ctl=000000007bdd3040)
rockchip_reset_assert(reset_ctl=000000007bdd3040) (dev=000000007bd3aef0, id=149) (reg_addr=00000000fdd20424)
of_read_u32: #phy-cells: 0x0 (0)
of_read_u32: #phy-cells: 0x1 (1)
generic_phy_get_by_index(dev=000000007bd39f50, index=0, phy=000000007bdd3080)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: 0x126 (294)
generic_phy_get_by_index(dev=000000007bd39f50, index=1, phy=000000007bdd30a0)
of_read_u32: #phy-cells: 0x0 (0)
of_read_u32: #phy-cells: 0x1 (1)
ofnode_read_u32: rockchip,pipe-grf: of_read_u32: rockchip,pipe-grf: 0x11c (284)
ofnode_read_u32: rockchip,pipe-phy-grf: of_read_u32: rockchip,pipe-phy-grf: 0x11e (286)
** translation for device /syscon@fdc80000 **
bus is default (na=2, ns=2) on /
reached root node
clk_get_by_indexed_prop(dev=000000007bdaa3b0, index=0, clk=000000007bdd3110)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd3110)
clk_request(dev=000000007bd3abf0, clk=000000007bdd3110)
reset_get_by_name(dev=000000007bdaa3b0, name=combphy, reset_ctl=000000007bdd3100)
comparing combphy with combphy-apb
comparing combphy with combphy
reset_get_by_index(dev=000000007bdaa3b0, index=1, reset_ctl=000000007bdd3100)
of_read_u32: #reset-cells: 0x1 (1)
of_read_u32: #reset-cells: 0x1 (1)
reset_of_xlate_default(reset_ctl=000000007bdd3100)
rockchip_reset_request(reset_ctl=000000007bdd3100) (dev=000000007bd3aef0, id=455) (sf_reset_num=30)
ofnode_read_u32_array: rockchip,pcie1ln-sel-bits: of_read_u32_array: rockchip,pcie1ln-sel-bits: ofnode_read_bool: rockchip,enable-ssc: false
clk_enable(clk=000000007bdd3110)
ofnode_read_bool: rockchip,enable-ssc: false
reset_deassert(reset_ctl=000000007bdd3100)
rockchip_reset_deassert(reset_ctl=000000007bdd3100) (dev=000000007bd3aef0, id=455) (reg_addr=00000000fdd20470)
fixed_regulator_set_enable: dev='vcc5v0-host-regulator', enable=1, delay=0, has_gpio=1
fixed_regulator_set_enable: done
reset_deassert(reset_ctl=000000007bdd3040)
rockchip_reset_deassert(reset_ctl=000000007bdd3040) (dev=000000007bd3aef0, id=149) (reg_addr=00000000fdd20424)
xhci_register: dev='dwc3@fd000000', ctrl=000000007bdd1280, hccr=00000000fd000000, hcor=00000000fd000020
// Halt the HC: 00000000fd000020
// Reset the HC
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10


# usb2.0口 用不到
Bus usb@fd800000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop(dev=000000007bd3a020, index=0, clk=000000007bdd4780)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4780)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4780)
clk_enable(clk=000000007bdd4780)
clk_get_by_indexed_prop(dev=000000007bd3a020, index=1, clk=000000007bdd4790)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4790)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4790)
clk_enable(clk=000000007bdd4790)
clk_get_by_indexed_prop(dev=000000007bd3a020, index=2, clk=000000007bdd47a0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd47a0)
clk_request(dev=000000007bd3ad70, clk=000000007bdd47a0)
clk_enable(clk=000000007bdd47a0)
clk_get_by_indexed_prop(dev=000000007bd3a020, index=3, clk=000000007bdd47b0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop: uclass_get_device_by_of_offset failed: err=-19
ofnode_read_u32: vbus-supply: of_read_u32: vbus-supply: (not found)
generic_phy_get_by_index(dev=000000007bd3a020, index=0, phy=000000007bdd46d0)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_bool: rockchip,grf: false
ofnode_read_bool: rockchip,usbgrf: true
ofnode_read_u32: rockchip,usbgrf: of_read_u32: rockchip,usbgrf: 0x128 (296)
** translation for device /syscon@fdca8000 **
bus is default (na=2, ns=2) on /
reached root node
** translation for device /usb2-phy@fe8b0000 **
bus is default (na=2, ns=2) on /
reached root node
reset_get_by_name(dev=000000007bdaa7d0, name=phy, reset_ctl=000000007bdd3158)
fdt_stringlist_search() failed: -22
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: 0x126 (294)
ehci_register: dev='usb@fd800000', ctrl=000000007bdd4540, hccr=00000000fd800000, hcor=00000000fd800010, init=0
Register 1111 NbrPorts 1
USB EHCI 1.00

Bus usb@fd840000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop(dev=000000007bd3a0d0, index=0, clk=000000007bdd4840)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4840)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4840)
clk_enable(clk=000000007bdd4840)
clk_get_by_indexed_prop(dev=000000007bd3a0d0, index=1, clk=000000007bdd4850)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4850)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4850)
clk_enable(clk=000000007bdd4850)
clk_get_by_indexed_prop(dev=000000007bd3a0d0, index=2, clk=000000007bdd4860)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4860)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4860)
clk_enable(clk=000000007bdd4860)
clk_get_by_indexed_prop(dev=000000007bd3a0d0, index=3, clk=000000007bdd4870)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop: uclass_get_device_by_of_offset failed: err=-19
generic_phy_get_by_index(dev=000000007bd3a0d0, index=0, phy=000000007bde2690)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: 0x126 (294)
USB OHCI 1.0

Bus usb@fd880000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop(dev=000000007bd3a180, index=0, clk=000000007bdd4c80)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4c80)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4c80)
clk_enable(clk=000000007bdd4c80)
clk_get_by_indexed_prop(dev=000000007bd3a180, index=1, clk=000000007bdd4c90)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4c90)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4c90)
clk_enable(clk=000000007bdd4c90)
clk_get_by_indexed_prop(dev=000000007bd3a180, index=2, clk=000000007bdd4ca0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4ca0)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4ca0)
clk_enable(clk=000000007bdd4ca0)
clk_get_by_indexed_prop(dev=000000007bd3a180, index=3, clk=000000007bdd4cb0)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop: uclass_get_device_by_of_offset failed: err=-19
ofnode_read_u32: vbus-supply: of_read_u32: vbus-supply: (not found)
generic_phy_get_by_index(dev=000000007bd3a180, index=0, phy=000000007bdd4bd0)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: 0x126 (294)
fixed_regulator_set_enable: dev='vcc5v0-host-regulator', enable=1, delay=0, has_gpio=1
fixed_regulator_set_enable: done
ehci_register: dev='usb@fd880000', ctrl=000000007bdd4a40, hccr=00000000fd880000, hcor=00000000fd880010, init=0
Register 1111 NbrPorts 1
USB EHCI 1.00

Bus usb@fd8c0000: of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop(dev=000000007bd3a230, index=0, clk=000000007bdd4d00)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4d00)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4d00)
clk_enable(clk=000000007bdd4d00)
clk_get_by_indexed_prop(dev=000000007bd3a230, index=1, clk=000000007bdd4d10)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4d10)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4d10)
clk_enable(clk=000000007bdd4d10)
clk_get_by_indexed_prop(dev=000000007bd3a230, index=2, clk=000000007bdd4d20)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
clk_of_xlate_default(clk=000000007bdd4d20)
clk_request(dev=000000007bd3ad70, clk=000000007bdd4d20)
clk_enable(clk=000000007bdd4d20)
clk_get_by_indexed_prop(dev=000000007bd3a230, index=3, clk=000000007bdd4d30)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x1 (1)
of_read_u32: #clock-cells: 0x0 (0)
clk_get_by_indexed_prop: uclass_get_device_by_of_offset failed: err=-19
generic_phy_get_by_index(dev=000000007bd3a230, index=0, phy=000000007bdee690)
of_read_u32: #phy-cells: 0x0 (0)
ofnode_read_u32: phy-supply: of_read_u32: phy-supply: 0x126 (294)
fixed_regulator_set_enable: dev='vcc5v0-host-regulator', enable=1, delay=0, has_gpio=1
fixed_regulator_set_enable: done
USB OHCI 1.0


# shl scanning  这个是实验用到的usb3.0
scanning bus dwc3@fcc00000 for devices... 
Calling usb_setup_device(), portnr=0
xhci_alloc_device: dev='dwc3@fcc00000', udev=000000007b9f8580
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_REQ_SET_ADDRESS
scrlen = 0
 req->length = 0
Len is 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_DEVICE request
scrlen = 18
 req->length = 18
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_CONFIG config
scrlen = 25
 req->length = 9
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x1F
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_CONFIG config
scrlen = 25
 req->length = 31
get_conf_no 0 Result 25, wLength 31
if 0, ep 0
##EP epmaxpacketin[1] = 8
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
scrlen = 0
 req->length = 0
Len is 0
new device strings: Mfr=1, Product=2, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_STRING config
scrlen = 4
 req->length = 255
USB device number 1 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_STRING config
scrlen = 14
 req->length = 255
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f8580, udev->dev='dwc3@fcc00000', portnr=0
USB_DT_STRING config
scrlen = 42
 req->length = 255
Manufacturer U-Boot
Product      XHCI Host Controller
SerialNumber 
read_descriptor for 'dwc3@fcc00000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdd4f10
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2A00 index 0x0 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
USB_DT_HUB config
scrlen = 8
 req->length = 4
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2A00 index 0x0 length 0xC
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
USB_DT_HUB config
scrlen = 8
 req->length = 12
2 ports detected
ganged power switching
standalone hub
individual port over-current protection
TT requires at most 8 FS bit times (666 ns)
power on to power good time: 20ms
hub controller current requirement: 0mA
port 1 is removable
port 2 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 2
 req->length = 4
get_hub_status returned status 1, change 802
local power source is lost (inactive)
no over-current condition exists
xhci_update_hub_device: dev='dwc3@fcc00000', udev=000000007bdd6040
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
port 1 returns 0
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x2 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
port 2 returns 0
pgood_delay=20ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
SPEED = FULLSPEED
scrlen = 4
 req->length = 4
Port 1 Status 101 Change 1
devnum=1 port=1: USB dev found
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
SPEED = FULLSPEED
scrlen = 4
 req->length = 4
portstatus 101, change 1, 12 Mb/s
usb_control_msg: request: 0x1, requesttype: 0x23, value 0x10 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
clear port connect change, actual port 1 status  = 0x6e1
scrlen = 0
 req->length = 0
Len is 0
usb_hub_port_reset: resetting 'usb_hub' port 1...
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x4 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
SPEED = FULLSPEED
scrlen = 4
 req->length = 4
portstatus 111, change 0, 12 Mb/s
STAT_C_CONNECTION = 0 STAT_CONNECTION = 1  USB_PORT_STAT_ENABLE 0
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x4 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
SPEED = HIGHSPEED
scrlen = 4
 req->length = 4
portstatus 503, change 10, 480 Mb/s
STAT_C_CONNECTION = 0 STAT_CONNECTION = 1  USB_PORT_STAT_ENABLE 1
usb_control_msg: request: 0x1, requesttype: 0x23, value 0x14 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
clear port reset change, actual port 1 status  = 0xe03
scrlen = 0
 req->length = 0
Len is 0
Calling usb_setup_device(), portnr=1
xhci_alloc_device: dev='dwc3@fcc00000', udev=000000007b9f7640
EP STATE RUNNING.
set address 2
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x2 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
Setting up addressable devices 000000007bdd0140
route string 0
port_num = 1
SPEED = 3
Setting Packet size = 64bytes
EP STATE RUNNING.
Successful Address Device command
xHC internal address is: 1
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=256 (0x100), index=0
EP STATE RUNNING.
start_trb 000000007bdeef80, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 256,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 18
length_field = 18, length = 18,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=512 (0x200), index=0
EP STATE RUNNING.
start_trb 000000007bdeefb0, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 512,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 9
length_field = 9, length = 9,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x20
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=512 (0x200), index=0
EP STATE RUNNING.
start_trb 000000007bdeefe0, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 512,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 32
length_field = 32, length = 32,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
get_conf_no 0 Result 32, wLength 32
if 0, ep 0
if 0, ep 1
##EP epmaxpacketout[1] = 512
##EP epmaxpacketin[2] = 512
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
EP STATE RUNNING.
Successful Configure Endpoint command
req=9 (0x9), type=0 (0x0), value=1 (0x1), index=0
EP STATE RUNNING.
start_trb 000000007bdef010, start_cycle 1
req->requesttype = 0, req->request = 9,le16_to_cpu(req->value) = 1,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 0
length_field = 0, length = 0,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
new device strings: Mfr=1, Product=2, SerialNumber=3
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=768 (0x300), index=0
EP STATE RUNNING.
start_trb 000000007bdef030, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 768,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 255
length_field = 255, length = 255,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
USB device number 2 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=769 (0x301), index=1033
EP STATE RUNNING.
start_trb 000000007bdef060, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 769,le16_to_cpu(req->index) = 1033,le16_to_cpu(req->length) = 255
length_field = 255, length = 255,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=770 (0x302), index=1033
EP STATE RUNNING.
start_trb 000000007bdef090, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 770,le16_to_cpu(req->index) = 1033,le16_to_cpu(req->length) = 255
length_field = 255, length = 255,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x303 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
req=6 (0x6), type=128 (0x80), value=771 (0x303), index=1033
EP STATE RUNNING.
start_trb 000000007bdef0c0, start_cycle 1
req->requesttype = 128, req->request = 6,le16_to_cpu(req->value) = 771,le16_to_cpu(req->index) = 1033,le16_to_cpu(req->length) = 255
length_field = 255, length = 255,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
Manufacturer USB
Product      Disk 2.0
SerialNumber 9207152395650425647
read_descriptor for 'usb_hub': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
usb_find_and_bind_driver: Match found: usb_mass_storage
usb_scan_device: Probing 'usb_mass_storage', plat=000000007bdd4c30


Probing for storage


USB Mass Storage device detected
Transport: Bulk/Bulk/Bulk
Endpoints In 2 Out 1 Int 0
usb_control_msg: request: 0xFE, requesttype: 0xA1, value 0x0 index 0x0 length 0x1
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdefc10, udev->dev='usb_mass_storage', portnr=1
req=254 (0xfe), type=161 (0xa1), value=0 (0x0), index=0
EP STATE RUNNING.
start_trb 000000007bdef0f0, start_cycle 1
req->requesttype = 161, req->request = 254,le16_to_cpu(req->value) = 0,le16_to_cpu(req->index) = 0,le16_to_cpu(req->length) = 1
length_field = 1, length = 1,xhci_td_remainder(length) = 0 , TRB_INTR_TARGET(0) = 0
Get Max LUN -> len = 1, result = 0
 address 2
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9f72c0, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7400, length=36
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7240, length=13
EP STATE RUNNING.
inquiry returns 0
ISO Vers 4, Response Data 2
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9f72c0, length=31
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7240, length=13
EP STATE RUNNING.
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9f72c0, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7380, length=8
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7240, length=13
EP STATE RUNNING.
Read Capacity returns: 0xff3f1f00, 0x00020000
Capacity = 0x001f4000, blocksz = 0x00000200
 address 2
rkram_part_init: No ATAGS ramdisk partition
part_init: try 'RKRAM_PART': ret=-61

usb_read: udev 0

usb_read: dev 0 startblk 0, blccnt 1 buffer 7b9f71c0
read10: start 0 blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9f7080, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f71c0, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9f7000, length=13
EP STATE RUNNING.
usb_read: end startblk 1, blccnt 1 buffer 7b9f73c0

usb_read: udev 0

usb_read: dev 0 startblk 0, blccnt 1 buffer 7b9b7100
read10: start 0 blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9b7000, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b7100, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b6f80, length=13
EP STATE RUNNING.
usb_read: end startblk 1, blccnt 1 buffer 7b9b7300

usb_read: udev 0

usb_read: dev 0 startblk 1, blccnt 1 buffer 7bdd6d40
read10: start 1 blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9b7000, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007bdd6d40, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b6f80, length=13
EP STATE RUNNING.
usb_read: end startblk 2, blccnt 1 buffer 7bdd6f40

usb_read: udev 0

usb_read: dev 0 startblk 0, blccnt 1 buffer 7b9b7100
read10: start 0 blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9b7000, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b7100, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b6f80, length=13
EP STATE RUNNING.
usb_read: end startblk 1, blccnt 1 buffer 7b9b7300

usb_read: udev 0

usb_read: dev 0 startblk 1f3fff, blccnt 1 buffer 7bdf05c0
read10: start 1f3fff blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9b7000, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007bdf05c0, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b6f80, length=13
EP STATE RUNNING.
usb_read: end startblk 1f4000, blccnt 1 buffer 7bdf07c0
GUID Partition Table Header signature is wrong: 0xFFFFFFFFFFFFFFFF != 0x5452415020494645
part_init: try 'EFI': ret=-1

usb_read: udev 0

usb_read: dev 0 startblk 0, blccnt 1 buffer 7b9b73c0
read10: start 0 blocks 1
COMMAND phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0008203, buffer=000000007b9b72c0, length=31
EP STATE RUNNING.
DATA phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b73c0, length=512
EP STATE RUNNING.
STATUS phase
xhci_submit_bulk_msg: dev='dwc3@fcc00000', udev=000000007bdefc10
dev=000000007bdefc10, pipe=c0010283, buffer=000000007b9b7240, length=13
EP STATE RUNNING.
usb_read: end startblk 1, blccnt 1 buffer 7b9b75c0
part_init: try 'DOS': ret=0
usb_stor_probe_device: Found device 000000007bdefc10
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fcc00000', udev=000000007bdd6040, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
devnum=1 port=2: timeout
2 USB Device(s) found
# usb3.0 口扫描U盘结束


# 下面的可以不用看了
scanning bus dwc3@fd000000 for devices... 
Calling usb_setup_device(), portnr=0
xhci_alloc_device: dev='dwc3@fd000000', udev=000000007b9f8580
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_REQ_SET_ADDRESS
scrlen = 0
 req->length = 0
Len is 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_DEVICE request
scrlen = 18
 req->length = 18
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_CONFIG config
scrlen = 25
 req->length = 9
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x1F
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_CONFIG config
scrlen = 25
 req->length = 31
get_conf_no 0 Result 25, wLength 31
if 0, ep 0
##EP epmaxpacketin[1] = 8
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
scrlen = 0
 req->length = 0
Len is 0
new device strings: Mfr=1, Product=2, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_STRING config
scrlen = 4
 req->length = 255
USB device number 1 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_STRING config
scrlen = 14
 req->length = 255
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x409 length 0xFF
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007b9f8580, udev->dev='dwc3@fd000000', portnr=0
USB_DT_STRING config
scrlen = 42
 req->length = 255
Manufacturer U-Boot
Product      XHCI Host Controller
SerialNumber 
read_descriptor for 'dwc3@fd000000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdd6df0
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2A00 index 0x0 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
USB_DT_HUB config
scrlen = 8
 req->length = 4
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2A00 index 0x0 length 0xC
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
USB_DT_HUB config
scrlen = 8
 req->length = 12
2 ports detected
ganged power switching
standalone hub
individual port over-current protection
TT requires at most 8 FS bit times (666 ns)
power on to power good time: 20ms
hub controller current requirement: 0mA
port 1 is removable
port 2 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 2
 req->length = 4
get_hub_status returned status 1, change 802
local power source is lost (inactive)
no over-current condition exists
xhci_update_hub_device: dev='dwc3@fd000000', udev=000000007bdf05c0
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
port 1 returns 0
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x2 length 0x0
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 0
 req->length = 0
Len is 0
port 2 returns 0
pgood_delay=20ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x2 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 2 Status 100 Change 0
devnum=1 port=2: timeout
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
xhci_submit_control_msg: dev='dwc3@fd000000', udev=000000007bdf05c0, udev->dev='usb_hub', portnr=0
scrlen = 4
 req->length = 4
Port 1 Status 100 Change 0
devnum=1 port=1: timeout
1 USB Device(s) found


scanning bus usb@fd800000 for devices... 
Calling usb_setup_device(), portnr=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x40
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=256, index=0
USB_DT_DEVICE request
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=5 (0x5), type=0 (0x0), value=1, index=0
USB_REQ_SET_ADDRESS
Len is 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=256, index=0
USB_DT_DEVICE request
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=512, index=0
USB_DT_CONFIG config
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x19
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=512, index=0
USB_DT_CONFIG config
get_conf_no 0 Result 25, wLength 25
if 0, ep 0
##EP epmaxpacketin[1] = 8
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=9 (0x9), type=0 (0x0), value=1, index=0
USB_REQ_SET_CONFIGURATION
Len is 0
new device strings: Mfr=1, Product=2, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=768, index=0
USB_DT_STRING config
USB device number 1 default language ID 0x1
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x1 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=769, index=1
USB_DT_STRING config
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x1 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f8580, udev->dev='usb@fd800000', portnr=0
req=6 (0x6), type=128 (0x80), value=770, index=1
USB_DT_STRING config
Manufacturer u-boot
Product      EHCI Host Controller
SerialNumber 
read_descriptor for 'usb@fd800000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdd6f40
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x4
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=6 (0x6), type=160 (0xa0), value=10496, index=0
USB_DT_HUB config
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x8
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=6 (0x6), type=160 (0xa0), value=10496, index=0
USB_DT_HUB config
1 ports detected
individual port power switching
standalone hub
global over-current protection
Single TT
TT requires at most 8 FS bit times (666 ns)
power on to power good time: 20ms
hub controller current requirement: 0mA
port 1 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=160 (0xa0), value=0, index=0
get_hub_status returned status 1, change 101
local power source is lost (inactive)
no over-current condition exists
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=3 (0x3), type=35 (0x23), value=8, index=1
Len is 0
port 1 returns 0
pgood_delay=20ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 501 Change 1
devnum=1 port=1: USB dev found
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
portstatus 501, change 1, 480 Mb/s
usb_control_msg: request: 0x1, requesttype: 0x23, value 0x10 index 0x1 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=1 (0x1), type=35 (0x23), value=16, index=1
Len is 0
usb_hub_port_reset: resetting 'usb_hub' port 1...
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x4 index 0x1 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=3 (0x3), type=35 (0x23), value=4, index=1
Len is 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
portstatus 503, change 10, 480 Mb/s
STAT_C_CONNECTION = 0 STAT_CONNECTION = 1  USB_PORT_STAT_ENABLE 1
usb_control_msg: request: 0x1, requesttype: 0x23, value 0x14 index 0x1 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007bdf0f80, udev->dev='usb_hub', portnr=0
req=1 (0x1), type=35 (0x23), value=20, index=1
Len is 0
Calling usb_setup_device(), portnr=1
set address 2
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x2 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=8c000000, buffer=0000000000000000, length=0, req=000000007b9f7500
req=5 (0x5), type=0 (0x0), value=2 (0x2), index=0
TOKEN=0x8d00
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f7300, length=18, req=000000007b9f7240
req=6 (0x6), type=128 (0x80), value=256 (0x100), index=0
TOKEN=0x8c00
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f74c0, length=9, req=000000007b9f7400
req=6 (0x6), type=128 (0x80), value=512 (0x200), index=0
TOKEN=0x8c00
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0xEC
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007bdf1940, length=236, req=000000007b9f7480
req=6 (0x6), type=128 (0x80), value=512 (0x200), index=0
TOKEN=0x8c00
get_conf_no 0 Result 236, wLength 236
unknown Description Type : b
if 0, ep 0
if 0, ep 1
if 0, ep 2
if 1, ep 0
if 1, ep 1
if 1, ep 2
if 1, ep 3
if 1, ep 4
if 1, ep 5
if 1, ep 6
if 1, ep 7
if 1, ep 8
if 1, ep 9
if 1, ep 10
if 1, ep 11
if 2, ep 0
if 2, ep 1
if 2, ep 2
if 2, ep 3
if 2, ep 4
if 2, ep 5
WARN: interface 1 has 12 endpoint descriptor, different from the interface descriptor's value: 2
##EP epmaxpacketin[1] = 16
##EP epmaxpacketout[2] = 512
##EP epmaxpacketin[2] = 512
##EP epmaxpacketout[3] = 9
##EP epmaxpacketin[3] = 9
##EP epmaxpacketout[3] = 17
##EP epmaxpacketin[3] = 17
##EP epmaxpacketout[3] = 25
##EP epmaxpacketin[3] = 25
##EP epmaxpacketout[3] = 33
##EP epmaxpacketin[3] = 33
##EP epmaxpacketout[3] = 49
##EP epmaxpacketin[3] = 49
##EP epmaxpacketin[4] = 512
##EP epmaxpacketout[5] = 512
##EP epmaxpacketout[6] = 512
##EP epmaxpacketin[7] = 64
##EP epmaxpacketout[8] = 512
##EP epmaxpacketout[9] = 512
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000203, buffer=0000000000000000, length=0, req=000000007b9f74c0
req=9 (0x9), type=0 (0x0), value=1 (0x1), index=0
TOKEN=0x8d00
new device strings: Mfr=1, Product=2, SerialNumber=3
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f7300, length=255, req=000000007b9f71c0
req=6 (0x6), type=128 (0x80), value=768 (0x300), index=0
TOKEN=0x8c00
USB device number 2 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f7300, length=255, req=000000007b9f71c0
req=6 (0x6), type=128 (0x80), value=769 (0x301), index=1033
TOKEN=0x8c00
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x409 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f7300, length=255, req=000000007b9f71c0
req=6 (0x6), type=128 (0x80), value=770 (0x302), index=1033
TOKEN=0x8c00
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x303 index 0x409 length 0xFF
ehci_submit_control_msg: dev='usb@fd800000', udev=000000007b9f7640, udev->dev='usb_hub', portnr=1
dev=000000007b9f7640, pipe=80000283, buffer=000000007b9f7300, length=255, req=000000007b9f71c0
req=6 (0x6), type=128 (0x80), value=771 (0x303), index=1033
TOKEN=0x8c00
Manufacturer Realtek
Product      802.11n WLAN Adapter
SerialNumber 00e04c000001
read_descriptor for 'usb_hub': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
usb_find_and_bind_driver: No match found: 0
usb_scan_device: Probing 'generic_bus_2_dev_2', plat=000000007bdd4fb0
2 USB Device(s) found

scanning bus usb@fd840000 for devices... 
Calling usb_setup_device(), portnr=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x40
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x19
get_conf_no 0 Result 25, wLength 25
if 0, ep 0
##EP epmaxpacketin[1] = 2
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
new device strings: Mfr=0, Product=1, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
USB device number 1 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
Manufacturer 
Product      U-Boot Root Hub
SerialNumber 
read_descriptor for 'usb@fd840000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdf2400
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x4
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x9
1 ports detected
ganged power switching
standalone hub
no over-current protection
power on to power good time: 4ms
hub controller current requirement: 0mA
port 1 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
get_hub_status returned status 0, change 0
local power source is good
no over-current condition exists
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
port 1 returns 0
pgood_delay=4ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
devnum=1 port=1: timeout
1 USB Device(s) found

scanning bus usb@fd880000 for devices... 
Calling usb_setup_device(), portnr=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x40
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=256, index=0
USB_DT_DEVICE request
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=5 (0x5), type=0 (0x0), value=1, index=0
USB_REQ_SET_ADDRESS
Len is 0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=256, index=0
USB_DT_DEVICE request
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=512, index=0
USB_DT_CONFIG config
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x19
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=512, index=0
USB_DT_CONFIG config
get_conf_no 0 Result 25, wLength 25
if 0, ep 0
##EP epmaxpacketin[1] = 8
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=9 (0x9), type=0 (0x0), value=1, index=0
USB_REQ_SET_CONFIGURATION
Len is 0
new device strings: Mfr=1, Product=2, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=768, index=0
USB_DT_STRING config
USB device number 1 default language ID 0x1
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x1 length 0xFF
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=769, index=1
USB_DT_STRING config
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x302 index 0x1 length 0xFF
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007b9f8580, udev->dev='usb@fd880000', portnr=0
req=6 (0x6), type=128 (0x80), value=770, index=1
USB_DT_STRING config
Manufacturer u-boot
Product      EHCI Host Controller
SerialNumber 
read_descriptor for 'usb@fd880000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdf2f00
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=6 (0x6), type=160 (0xa0), value=10496, index=0
USB_DT_HUB config
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x8
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=6 (0x6), type=160 (0xa0), value=10496, index=0
USB_DT_HUB config
1 ports detected
individual port power switching
standalone hub
global over-current protection
Single TT
TT requires at most 8 FS bit times (666 ns)
power on to power good time: 20ms
hub controller current requirement: 0mA
port 1 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=160 (0xa0), value=0, index=0
get_hub_status returned status 1, change 101
local power source is lost (inactive)
no over-current condition exists
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=3 (0x3), type=35 (0x23), value=8, index=1
Len is 0
port 1 returns 0
pgood_delay=20ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
ehci_submit_control_msg: dev='usb@fd880000', udev=000000007bdf2fc0, udev->dev='usb_hub', portnr=0
req=0 (0x0), type=163 (0xa3), value=0, index=1
Port 1 Status 500 Change 0
devnum=1 port=1: timeout
1 USB Device(s) found

scanning bus usb@fd8c0000 for devices... 
Calling usb_setup_device(), portnr=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x40
set address 1
usb_control_msg: request: 0x5, requesttype: 0x0, value 0x1 index 0x0 length 0x0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x100 index 0x0 length 0x12
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x9
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x200 index 0x0 length 0x19
get_conf_no 0 Result 25, wLength 25
if 0, ep 0
##EP epmaxpacketin[1] = 2
set configuration 1
usb_control_msg: request: 0x9, requesttype: 0x0, value 0x1 index 0x0 length 0x0
new device strings: Mfr=0, Product=1, SerialNumber=0
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x300 index 0x0 length 0xFF
USB device number 1 default language ID 0x409
usb_control_msg: request: 0x6, requesttype: 0x80, value 0x301 index 0x409 length 0xFF
Manufacturer 
Product      U-Boot Root Hub
SerialNumber 
read_descriptor for 'usb@fd8c0000': ret=0
** usb_find_child returns -2
usb_find_and_bind_driver: Searching for driver
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
ofnode_read_bool: u-boot,dm-pre-reloc: false
ofnode_read_bool: u-boot,dm-spl: false
usb_find_and_bind_driver: Match found: usb_hub
usb_scan_device: Probing 'usb_hub', plat=000000007bdf3a00
usb_hub_post_probe
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x4
usb_control_msg: request: 0x6, requesttype: 0xA0, value 0x2900 index 0x0 length 0x9
1 ports detected
ganged power switching
standalone hub
no over-current protection
power on to power good time: 4ms
hub controller current requirement: 0mA
port 1 is removable
usb_control_msg: request: 0x0, requesttype: 0xA0, value 0x0 index 0x0 length 0x4
get_hub_status returned status 0, change 0
local power source is good
no over-current condition exists
enabling power on all ports
usb_control_msg: request: 0x3, requesttype: 0x23, value 0x8 index 0x1 length 0x0
port 1 returns 0
pgood_delay=4ms
devnum=1 poweron: query_delay=100 connect_timeout=1100
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
usb_control_msg: request: 0x0, requesttype: 0xA3, value 0x0 index 0x1 length 0x4
Port 1 Status 100 Change 0
devnum=1 port=1: timeout
1 USB Device(s) found
scan end
       scanning usb for storage devices... 1 Storage Device(s) found

[END] 2023/10/29 星期日 21:37:46
