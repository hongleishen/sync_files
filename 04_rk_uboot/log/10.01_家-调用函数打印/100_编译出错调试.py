 pack u-boot.itb okay! Input: /home/topeet/Android/rk356x_linux/rkbin/RKTRUST/RK3568TRUST.ini
 ...
 
  Hash value:   66bbd173528d12e9739c336926e33ee1ac1f4c7078fcac5712eeb8747d02163e
 Image 7 (fdt)
  Description:  U-Boot dtb
  Created:      Sun Nov  5 18:27:46 2023
  Type:         Flat Device Tree
  Compression:  uncompressed
  Data Size:    14285 Bytes = 13.95 KiB = 0.01 MiB
  Architecture: AArch64
  Hash algo:    sha256
  Hash value:   fcfda359c09a8b315de67f0f6a4db29122f97fadfa185d0d4a9aee69488cc76d
 Default Configuration: 'conf'
 Configuration 0 (conf)
  Description:  rk3568-evb
  Kernel:       unavailable
  Firmware:     atf-1
  FDT:          fdt
  Loadables:    uboot
                atf-2
                atf-3
                atf-4
                atf-5
                optee
********boot_merger ver 1.2********
Info:Pack loader ok.
pack loader okay! Input: /home/topeet/Android/rk356x_linux/rkbin/RKBOOT/RK3568MINIALL.ini
/home/topeet/Android/rk356x_linux/u-boot


ERROR: pack uboot.img failed! fit/uboot.itb actual: 2099200 bytes, max limit: 2097152 bytes







ERROR: Running build_uboot failed!
ERROR: exit code 1 from line 515:
    ./make.sh $RK_UBOOT_DEFCONFIG $UBOOT_COMPILE_COMMANDS




    scripts/fit-resign.sh:98:			echo "ERROR: pack ${IMG_UBOOT} failed! ${ITB} actual: ${ITB_BS} bytes, max limit: ${ITB_MAX_BS} bytes"



fit_resign
    error



scripts/fit-core.sh:544:		echo "ERROR: pack ${IMG_UBOOT} failed! ${ITB} actual: ${ITB_BS} bytes, max limit: ${ITB_MAX_BS} bytes"



fit.sh
    source ./scripts/fit-core.sh
        function fit_gen_uboot_img()
            error