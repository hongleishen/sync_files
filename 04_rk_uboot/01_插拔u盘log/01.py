=> usb start
starting USB...
Bus dwc3@fcc00000: usb maximum-speed not found		// 下方usb口
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10
Bus dwc3@fd000000: usb maximum-speed not found
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10
Bus usb@fd800000: USB EHCI 1.00		// 4G模块
Bus usb@fd840000: USB OHCI 1.0
Bus usb@fd880000: USB EHCI 1.00		// 左上USB口
Bus usb@fd8c0000: USB OHCI 1.0
scanning bus dwc3@fcc00000 for devices... 1 USB Device(s) found
scanning bus dwc3@fd000000 for devices... 1 USB Device(s) found
scanning bus usb@fd800000 for devices... WARN: interface 1 has 12 endpoint descriptor, different from the interface descriptor's value: 2
2 USB Device(s) found
scanning bus usb@fd840000 for devices... 1 USB Device(s) found
scanning bus usb@fd880000 for devices... 1 USB Device(s) found
scanning bus usb@fd8c0000 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found
	   


=> usb tree
USB device tree:
  1  Hub (5 Gb/s, 0mA)
  |  U-Boot XHCI Host Controller
  |
  +-2  Mass Storage (5 Gb/s, 100mA)
       SanDisk Extreme AA010218130720293650

  1  Hub (5 Gb/s, 0mA)
     U-Boot XHCI Host Controller

  1  Hub (480 Mb/s, 0mA)
  |  u-boot EHCI Host Controller
  |
  +-2   (480 Mb/s, 500mA)
       Realtek 802.11n WLAN Adapter 00e04c000001

  1  Hub (12 Mb/s, 0mA)
      U-Boot Root Hub

  1  Hub (480 Mb/s, 0mA)
     u-boot EHCI Host Controller

  1  Hub (12 Mb/s, 0mA)
      U-Boot Root Hub	   


=> usb info
1: Hub,  USB Revision 3.0
 - U-Boot XHCI Host Controller
 - Class: Hub
 - PacketSize: 512  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 1.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 8 Interval 255ms

2: Mass Storage,  USB Revision 3.0
 - SanDisk Extreme AA010218130720293650
 - Class: (from Interface) Mass Storage
 - PacketSize: 512  Configurations: 1
 - Vendor: 0x0781  Product 0x5580 Version 0.16
   Configuration: 1
   - Interfaces: 1 Bus Powered 100mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 2
     - Class Mass Storage, Transp. SCSI, Bulk only
     - Endpoint 1 In Bulk MaxPacket 1024
     - Endpoint 2 Out Bulk MaxPacket 1024

1: Hub,  USB Revision 3.0
 - U-Boot XHCI Host Controller
 - Class: Hub
 - PacketSize: 512  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 1.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 8 Interval 255ms

1: Hub,  USB Revision 2.0
 - u-boot EHCI Host Controller
 - Class: Hub
 - PacketSize: 64  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 1.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 8 Interval 255ms

2: ,  USB Revision 2.0
 - Realtek 802.11n WLAN Adapter 00e04c000001
 - Class:
 - PacketSize: 64  Configurations: 1
 - Vendor: 0x0bda  Product 0xd723 Version 2.0
   Configuration: 1
   - Interfaces: 3 Self Powered Remote Wakeup 500mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 3
     - Class
     - String: "Bluetooth Radio"
     - Endpoint 1 In Interrupt MaxPacket 16 Interval 4ms
     - Endpoint 2 Out Bulk MaxPacket 512
     - Endpoint 2 In Bulk MaxPacket 512
     Interface: 1
     - Alternate Setting 0, Endpoints: 12
     - Class
     - String: "Bluetooth Radio"
     - Endpoint 3 Out Isochronous MaxPacket 0
     - Endpoint 3 In Isochronous MaxPacket 0
     - Endpoint 3 Out Isochronous MaxPacket 9
     - Endpoint 3 In Isochronous MaxPacket 9
     - Endpoint 3 Out Isochronous MaxPacket 17
     - Endpoint 3 In Isochronous MaxPacket 17
     - Endpoint 3 Out Isochronous MaxPacket 25
     - Endpoint 3 In Isochronous MaxPacket 25
     - Endpoint 3 Out Isochronous MaxPacket 33
     - Endpoint 3 In Isochronous MaxPacket 33
     - Endpoint 3 Out Isochronous MaxPacket 49
     - Endpoint 3 In Isochronous MaxPacket 49
     Interface: 2
     - Alternate Setting 0, Endpoints: 6
     - Class Vendor specific
     - String: "802.11n WLAN Adapter"
     - Endpoint 4 In Bulk MaxPacket 512
     - Endpoint 5 Out Bulk MaxPacket 512
     - Endpoint 6 Out Bulk MaxPacket 512
     - Endpoint 7 In Interrupt MaxPacket 64 Interval 3ms
     - Endpoint 8 Out Bulk MaxPacket 512
     - Endpoint 9 Out Bulk MaxPacket 512

1: Hub,  USB Revision 1.10
 -  U-Boot Root Hub
 - Class: Hub
 - PacketSize: 8  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 0.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 2 Interval 255ms

1: Hub,  USB Revision 2.0
 - u-boot EHCI Host Controller
 - Class: Hub
 - PacketSize: 64  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 1.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 8 Interval 255ms

1: Hub,  USB Revision 1.10
 -  U-Boot Root Hub
 - Class: Hub
 - PacketSize: 8  Configurations: 1
 - Vendor: 0x0000  Product 0x0000 Version 0.0
   Configuration: 1
   - Interfaces: 1 Self Powered 0mA
     Interface: 0
     - Alternate Setting 0, Endpoints: 1
     - Class Hub
     - Endpoint 1 In Interrupt MaxPacket 2 Interval 255ms
	   
	   
	   
// 左上角插入2.0 U盘   3.0U盘
resetting USB...
Bus dwc3@fcc00000: usb maximum-speed not found
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10
Bus dwc3@fd000000: usb maximum-speed not found
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10
Bus usb@fd800000: USB EHCI 1.00
Bus usb@fd840000: USB OHCI 1.0
Bus usb@fd880000: USB EHCI 1.00  // 左上插入2.0 U盘
Bus usb@fd8c0000: USB OHCI 1.0
scanning bus dwc3@fcc00000 for devices... 1 USB Device(s) found
scanning bus dwc3@fd000000 for devices... 1 USB Device(s) found
scanning bus usb@fd800000 for devices... WARN: interface 1 has 12 endpoint descriptor, different from the interface descriptor's value: 2
2 USB Device(s) found
scanning bus usb@fd840000 for devices... 1 USB Device(s) found
//																						0x5EEB   3.0 U盘
scanning bus usb@fd880000 for devices... GUID Partition Table Header signature is wrong: 0xFFFFFFFFFFFFFFFF != 0x5452415020494645
2 USB Device(s) found
scanning bus usb@fd8c0000 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
	   

// 下方usb口
=> usb start
starting USB...

Bus dwc3@fcc00000: usb maximum-speed not found
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10

Bus dwc3@fd000000: usb maximum-speed not found
Register 2000140 NbrPorts 2
Starting the controller
USB XHCI 1.10

Bus usb@fd800000: USB EHCI 1.00
Bus usb@fd840000: USB OHCI 1.0
Bus usb@fd880000: USB EHCI 1.00
Bus usb@fd8c0000: USB OHCI 1.0

scanning bus dwc3@fcc00000 for devices... GUID Partition Table Header signature is wrong: 0x5EEB != 0x5452415020494645
2 USB Device(s) found
scanning bus dwc3@fd000000 for devices... 1 USB Device(s) found
scanning bus usb@fd800000 for devices... WARN: interface 1 has 12 endpoint descriptor, different from the interface descriptor's value: 2
2 USB Device(s) found
scanning bus usb@fd840000 for devices... 1 USB Device(s) found
scanning bus usb@fd880000 for devices... 1 USB Device(s) found
scanning bus usb@fd8c0000 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
	   


	   
// usb 2.0 U盘
=> usb dev

scanning bus dwc3@fcc00000 for devices... GUID Partition Table Header signature is wrong: 0xFFFFFFFFFFFFFFFF != 0x5452415020494645
2 USB Device(s) found
IDE device 0: Vendor: Generic Rev: 2.00 Prod: Flash-Disk
            Type: Removable Hard Disk
            Capacity: 1000.0 MB = 0.9 GB (2048000 x 512)
			
// usb 3.0U盘
scanning bus dwc3@fcc00000 for devices... GUID Partition Table Header signature is wrong: 0x5EEB != 0x5452415020494645
2 USB Device(s) found
IDE device 0: Vendor: SanDisk  Rev: 0001 Prod: Extreme
            Type: Hard Disk
            Capacity: 15272.0 MB = 14.9 GB (31277232 x 512)