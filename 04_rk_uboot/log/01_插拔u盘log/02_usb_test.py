=> usb
usb - USB sub-system

Usage:
usb start - start (scan) USB controller
usb reset - reset (rescan) USB controller
usb stop [f] - stop USB [f]=force stop
usb tree - show USB device tree
usb info [dev] - show available USB devices
usb test [dev] [port] [mode] - set USB 2.0 test mode
    (specify port 0 to indicate the device's upstream port)
    Available modes: J, K, S[E0_NAK], P[acket], F[orce_Enable]
usb storage - show details of USB storage devices
usb dev [dev] - show or set current USB storage device
usb part [dev] - print partition table of one or all USB storage    devices
usb read addr blk# cnt - read `cnt' blocks starting at block `blk#'
    to memory address `addr'
usb write addr blk# cnt - write `cnt' blocks starting at block `blk#'
    from memory address `addr'





# 测试

=> usb storage
  Device 0: Vendor: SanDisk  Rev: 0001 Prod: Extreme
            Type: Hard Disk
            Capacity: 15272.0 MB = 14.9 GB (31277232 x 512)

=> usb dev

IDE device 0: Vendor: SanDisk  Rev: 0001 Prod: Extreme
            Type: Hard Disk
            Capacity: 15272.0 MB = 14.9 GB (31277232 x 512)


=> usb dev 0

Device 0: Vendor: SanDisk  Rev: 0001 Prod: Extreme
            Type: Hard Disk
            Capacity: 15272.0 MB = 14.9 GB (31277232 x 512)
... is now current device


=> usb test 0 1 P
Setting Test_Packet mode on downstream facing port 1...
The request port(1024) exceeds maximum port number
Test mode successfully set. Use 'usb start' to return to normal operation.


=> usb test 0 1 J
Setting Test_J mode on downstream facing port 1...
The request port(256) exceeds maximum port number
Test mode successfully set. Use 'usb start' to return to normal operation.

=> usb test 0 1 K
Setting Test_K mode on downstream facing port 1...
The request port(512) exceeds maximum port number
Test mode successfully set. Use 'usb start' to return to normal operation.

=> usb test 0 1 S
Setting Test_SE0_NAK mode on downstream facing port 1...
The request port(768) exceeds maximum port number
Test mode successfully set. Use 'usb start' to return to normal operation.


=> usb test 0 1 f
Setting Test_Force_Enable mode on downstream facing port 1...
The request port(1280) exceeds maximum port number
Test mode successfully set. Use 'usb start' to return to normal operation.

/*
    => fatinfo
    usage: fatinfo <interface> [<dev[:part]>]
    fatinfo - print information about filesystem
*/
    => fatinfo usb 0
    Interface:  USB
    Device 0: Vendor: SanDisk  Rev: 0001 Prod: Extreme
                Type: Hard Disk
                Capacity: 15272.0 MB = 14.9 GB (31277232 x 512)
    Filesystem: FAT32 "NO NAME    "


/*
    => fatload
    fatload - load binary file from a dos filesystem

    Usage:
    fatload <interface> [<dev[:part]> [<addr> [<filename> [bytes [pos]]]]]
        - Load binary file 'filename' from 'dev' on 'interface'
        to address 'addr' from dos filesystem.
        'pos' gives the file position to start loading from.
        If 'pos' is omitted, 0 is used. 'pos' requires 'bytes'.
        'bytes' gives the size to load. If 'bytes' is 0 or omitted,
        the load stops on end of file.
        If either 'pos' or 'bytes' are not aligned to
        ARCH_DMA_MINALIGN then a misaligned buffer warning will
        be printed and performance will suffer for the load.
*/
=> fatload usb 0 0x30000000 IMG_20160225_170251.jpg
reading IMG_20160225_170251.jpg
3894492 bytes read in 207 ms (17.9 MiB/s)




/*
    fatls   - list files in a directory (default /)
    fatls <interface> [<dev[:part]>] [directory]
*/
=> fatls usb 0
            LOST.DIR/
            Music/
            Movies/
            Pictures/
            $RECYCLE.BIN/
            System Volume Information/
            Android/