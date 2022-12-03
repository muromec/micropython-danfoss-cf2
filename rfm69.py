_REG_FIFO									= const(0x00)
_REG_OPMODE									= const(0x01)
_REG_DATAMODUL								= const(0x02)
_REG_BITRATEMSB								= const(0x03)
_REG_BITRATELSB								= const(0x04)
_REG_FDEVMSB									= const(0x05)
_REG_FDEVLSB									= const(0x06)
_REG_FRFMSB									= const(0x07)
_REG_FRFMID									= const(0x08)
_REG_FRFLSB									= const(0x09)
_REG_OSC1									= const(0x0A)
_REG_AFCCTRL									= const(0x0B)
_REG_LOWBAT									= const(0x0C)
_REG_LISTEN1									= const(0x0D)
_REG_LISTEN2									= const(0x0E)
_REG_LISTEN3									= const(0x0F)
_REG_VERSION									= const(0x10)
_REG_PALEVEL									= const(0x11)
_REG_PARAMP									= const(0x12)
_REG_OCP										= const(0x13)
_REG_AGCREF									= const(0x14)
_REG_AGCTHRESH1								= const(0x15)
_REG_AGCTHRESH2								= const(0x16)
_REG_AGCTHRESH3								= const(0x17)
_REG_LNA										= const(0x18)
_REG_RXBW									= const(0x19)
_REG_AFCBW									= const(0x1A)
_REG_OOKPEAK									= const(0x1B)
_REG_OOKAVG									= const(0x1C)
_REG_OOKFIX									= const(0x1D)
_REG_AFCFEI									= const(0x1E)
_REG_AFCMSB									= const(0x1F)
_REG_AFCLSB									= const(0x20)
_REG_FEIMSB									= const(0x21)
_REG_FEILSB									= const(0x22)
_REG_RSSICONFIG								= const(0x23)
_REG_RSSIVALUE								= const(0x24)
_REG_DIOMAPPING1								= const(0x25)
_REG_DIOMAPPING2								= const(0x26)
_REG_IRQFLAGS1								= const(0x27)
_REG_IRQFLAGS2								= const(0x28)
_REG_RSSITHRESH								= const(0x29)
_REG_RXTIMEOUT1								= const(0x2A)
_REG_RXTIMEOUT2								= const(0x2B)
_REG_PREAMBLEMSB								= const(0x2C)
_REG_PREAMBLELSB								= const(0x2D)
_REG_SYNCCONFIG								= const(0x2E)
_REG_SYNCVALUE1								= const(0x2F)
_REG_SYNCVALUE2								= const(0x30)
_REG_SYNCVALUE3								= const(0x31)
_REG_SYNCVALUE4								= const(0x32)
_REG_SYNCVALUE5								= const(0x33)
_REG_SYNCVALUE6								= const(0x34)
_REG_SYNCVALUE7								= const(0x35)
_REG_SYNCVALUE8								= const(0x36)
_REG_PACKETCONFIG1							= const(0x37)
_REG_PAYLOADLENGTH							= const(0x38)
_REG_NODEADRS								= const(0x39)
_REG_BROADCASTADRS							= const(0x3A)
_REG_AUTOMODES								= const(0x3B)
_REG_FIFOTHRESH								= const(0x3C)
_REG_PACKETCONFIG2							= const(0x3D)
_REG_AESKEY1									= const(0x3E)
_REG_AESKEY2									= const(0x3F)
_REG_AESKEY3									= const(0x40)
_REG_AESKEY4									= const(0x41)
_REG_AESKEY5									= const(0x42)
_REG_AESKEY6									= const(0x43)
_REG_AESKEY7									= const(0x44)
_REG_AESKEY8									= const(0x45)
_REG_AESKEY9									= const(0x46)
_REG_AESKEY10								= const(0x47)
_REG_AESKEY11								= const(0x48)
_REG_AESKEY12								= const(0x49)
_REG_AESKEY13								= const(0x4A)
_REG_AESKEY14								= const(0x4B)
_REG_AESKEY15								= const(0x4C)
_REG_AESKEY16								= const(0x4D)
_REG_TEMP1									= const(0x4E)
_REG_TEMP2									= const(0x4F)
_REG_TESTPA1									= const(0x5A) # only present on _RFM69HW/SX1231H
_REG_TESTPA2									= const(0x5C) # only present on _RFM69HW/SX1231H
_REG_TESTDAGC								= const(0x6F)
	
#******************************************************
# _RF69/SX1231 bit control definition
#******************************************************
# _Reg Op Mode
_RF_OPMODE_SEQUENCER_OFF						= const(0x80)
_RF_OPMODE_SEQUENCER_ON						= const(0x00) # Default

_RF_OPMODE_LISTEN_ON							= const(0x40)
_RF_OPMODE_LISTEN_OFF						= const(0x00) # Default

_RF_OPMODE_LISTENABORT						= const(0x20)

_RF_OPMODE_SLEEP								= const(0x00)
_RF_OPMODE_STANDBY							= const(0x04) # Default
_RF_OPMODE_SYNTHESIZER						= const(0x08)
_RF_OPMODE_TRANSMITTER						= const(0x0C)
_RF_OPMODE_RECEIVER							= const(0x10)

# _Reg Data Modul
_RF_DATAMODUL_DATAMODE_PACKET				= const(0x00) # Default
_RF_DATAMODUL_DATAMODE_CONTINUOUS			= const(0x40)
_RF_DATAMODUL_DATAMODE_CONTINUOUSNOBSYNC		= const(0x60)

_RF_DATAMODUL_MODULATIONTYPE_FSK				= const(0x00) # Default
_RF_DATAMODUL_MODULATIONTYPE_OOK				= const(0x08)

_RF_DATAMODUL_MODULATIONSHAPING_00			= const(0x00) # Default
_RF_DATAMODUL_MODULATIONSHAPING_01			= const(0x01)
_RF_DATAMODUL_MODULATIONSHAPING_10			= const(0x02)
_RF_DATAMODUL_MODULATIONSHAPING_11			= const(0x03)

# _RegBitRate (bits/sec) example bitrates
_RF_BITRATEMSB_1200							= const(0x68)
_RF_BITRATELSB_1200							= const(0x2B)
_RF_BITRATEMSB_2400							= const(0x34)
_RF_BITRATELSB_2400							= const(0x15)
_RF_BITRATEMSB_4800							= const(0x1A) # Default
_RF_BITRATELSB_4800							= const(0x0B) # Default
_RF_BITRATEMSB_9600							= const(0x0D)
_RF_BITRATELSB_9600							= const(0x05)
_RF_BITRATEMSB_19200							= const(0x06)
_RF_BITRATELSB_19200							= const(0x83)
_RF_BITRATEMSB_38400							= const(0x03)
_RF_BITRATELSB_38400							= const(0x41)
_RF_BITRATEMSB_38323							= const(0x03)
_RF_BITRATELSB_38323							= const(0x43)
_RF_BITRATEMSB_34482							= const(0x03)
_RF_BITRATELSB_34482							= const(0xA0)
_RF_BITRATEMSB_76800							= const(0x01)
_RF_BITRATELSB_76800							= const(0xA1)
_RF_BITRATEMSB_153600						= const(0x00)
_RF_BITRATELSB_153600						= const(0xD0)
_RF_BITRATEMSB_57600							= const(0x02)
_RF_BITRATELSB_57600							= const(0x2C)
_RF_BITRATEMSB_115200						= const(0x01)
_RF_BITRATELSB_115200						= const(0x16)
_RF_BITRATEMSB_12500							= const(0x0A)
_RF_BITRATELSB_12500							= const(0x00)
_RF_BITRATEMSB_25000							= const(0x05)
_RF_BITRATELSB_25000							= const(0x00)
_RF_BITRATEMSB_50000							= const(0x02)
_RF_BITRATELSB_50000							= const(0x80)
_RF_BITRATEMSB_100000						= const(0x01)
_RF_BITRATELSB_100000						= const(0x40)
_RF_BITRATEMSB_150000						= const(0x00)
_RF_BITRATELSB_150000						= const(0xD5)
_RF_BITRATEMSB_200000						= const(0x00)
_RF_BITRATELSB_200000						= const(0xA0)
_RF_BITRATEMSB_250000						= const(0x00)
_RF_BITRATELSB_250000						= const(0x80)
_RF_BITRATEMSB_300000						= const(0x00)
_RF_BITRATELSB_300000						= const(0x6B)
_RF_BITRATEMSB_32768							= const(0x03)
_RF_BITRATELSB_32768							= const(0xD1)
# custom bitrates
_RF_BITRATEMSB_55555							= const(0x02)
_RF_BITRATELSB_55555							= const(0x40)
_RF_BITRATEMSB_200KBPS						= const(0x00)
_RF_BITRATELSB_200KBPS						= const(0xa0)

# _RegFdev - frequency deviation (Hz)
_RF_FDEVMSB_2000								= const(0x00)
_RF_FDEVLSB_2000								= const(0x21)
_RF_FDEVMSB_5000								= const(0x00) # Default
_RF_FDEVLSB_5000								= const(0x52) # Default
_RF_FDEVMSB_7500								= const(0x00)
_RF_FDEVLSB_7500								= const(0x7B)
_RF_FDEVMSB_10000							= const(0x00)
_RF_FDEVLSB_10000							= const(0xA4)
_RF_FDEVMSB_15000							= const(0x00)
_RF_FDEVLSB_15000							= const(0xF6)
_RF_FDEVMSB_20000							= const(0x01)
_RF_FDEVLSB_20000							= const(0x48)
_RF_FDEVMSB_25000							= const(0x01)
_RF_FDEVLSB_25000							= const(0x9A)
_RF_FDEVMSB_30000							= const(0x01)
_RF_FDEVLSB_30000							= const(0xEC)
_RF_FDEVMSB_35000							= const(0x02)
_RF_FDEVLSB_35000							= const(0x3D)
_RF_FDEVMSB_40000							= const(0x02)
_RF_FDEVLSB_40000							= const(0x8F)
_RF_FDEVMSB_45000							= const(0x02)
_RF_FDEVLSB_45000							= const(0xE1)
_RF_FDEVMSB_50000							= const(0x03)
_RF_FDEVLSB_50000							= const(0x33)
_RF_FDEVMSB_55000							= const(0x03)
_RF_FDEVLSB_55000							= const(0x85)
_RF_FDEVMSB_60000							= const(0x03)
_RF_FDEVLSB_60000							= const(0xD7)
_RF_FDEVMSB_65000							= const(0x04)
_RF_FDEVLSB_65000							= const(0x29)
_RF_FDEVMSB_70000							= const(0x04)
_RF_FDEVLSB_70000							= const(0x7B)
_RF_FDEVMSB_75000							= const(0x04)
_RF_FDEVLSB_75000							= const(0xCD)
_RF_FDEVMSB_80000							= const(0x05)
_RF_FDEVLSB_80000							= const(0x1F)
_RF_FDEVMSB_85000							= const(0x05)
_RF_FDEVLSB_85000							= const(0x71)
_RF_FDEVMSB_90000							= const(0x05)
_RF_FDEVLSB_90000							= const(0xC3)
_RF_FDEVMSB_95000							= const(0x06)
_RF_FDEVLSB_95000							= const(0x14)
_RF_FDEVMSB_100000							= const(0x06)
_RF_FDEVLSB_100000							= const(0x66)
_RF_FDEVMSB_110000							= const(0x07)
_RF_FDEVLSB_110000							= const(0x0A)
_RF_FDEVMSB_120000							= const(0x07)
_RF_FDEVLSB_120000							= const(0xAE)
_RF_FDEVMSB_130000							= const(0x08)
_RF_FDEVLSB_130000							= const(0x52)
_RF_FDEVMSB_140000							= const(0x08)
_RF_FDEVLSB_140000							= const(0xF6)
_RF_FDEVMSB_150000							= const(0x09)
_RF_FDEVLSB_150000							= const(0x9A)
_RF_FDEVMSB_160000							= const(0x0A)
_RF_FDEVLSB_160000							= const(0x3D)
_RF_FDEVMSB_170000							= const(0x0A)
_RF_FDEVLSB_170000							= const(0xE1)
_RF_FDEVMSB_180000							= const(0x0B)
_RF_FDEVLSB_180000							= const(0x85)
_RF_FDEVMSB_190000							= const(0x0C)
_RF_FDEVLSB_190000							= const(0x29)
_RF_FDEVMSB_200000							= const(0x0C)
_RF_FDEVLSB_200000							= const(0xCD)
_RF_FDEVMSB_210000							= const(0x0D)
_RF_FDEVLSB_210000							= const(0x71)
_RF_FDEVMSB_220000							= const(0x0E)
_RF_FDEVLSB_220000							= const(0x14)
_RF_FDEVMSB_230000							= const(0x0E)
_RF_FDEVLSB_230000							= const(0xB8)
_RF_FDEVMSB_240000							= const(0x0F)
_RF_FDEVLSB_240000							= const(0x5C)
_RF_FDEVMSB_250000							= const(0x10)
_RF_FDEVLSB_250000							= const(0x00)
_RF_FDEVMSB_260000							= const(0x10)
_RF_FDEVLSB_260000							= const(0xA4)
_RF_FDEVMSB_270000							= const(0x11)
_RF_FDEVLSB_270000							= const(0x48)
_RF_FDEVMSB_280000							= const(0x11)
_RF_FDEVLSB_280000							= const(0xEC)
_RF_FDEVMSB_290000							= const(0x12)
_RF_FDEVLSB_290000							= const(0x8F)
_RF_FDEVMSB_300000							= const(0x13)
_RF_FDEVLSB_300000							= const(0x33)

# _Reg Frf (MHz) - carrier frequency
# 315 Mhz band
_RF_FRFMSB_314								= const(0x4E)
_RF_FRFMID_314								= const(0x80)
_RF_FRFLSB_314								= const(0x00)
_RF_FRFMSB_315								= const(0x4E)
_RF_FRFMID_315								= const(0xC0)
_RF_FRFLSB_315								= const(0x00)
_RF_FRFMSB_316								= const(0x4F)
_RF_FRFMID_316								= const(0x00)
_RF_FRFLSB_316								= const(0x00)
# 433 mhz band
_RF_FRFMSB_433								= const(0x6C)
_RF_FRFMID_433								= const(0x40)
_RF_FRFLSB_433								= const(0x00)
_RF_FRFMSB_434								= const(0x6C)
_RF_FRFMID_434								= const(0x80)
_RF_FRFLSB_434								= const(0x00)
_RF_FRFMSB_435								= const(0x6C)
_RF_FRFMID_435								= const(0xC0)
_RF_FRFLSB_435								= const(0x00)
# 868 Mhz band
_RF_FRFMSB_863								= const(0xD7)
_RF_FRFMID_863								= const(0xC0)
_RF_FRFLSB_863								= const(0x00)
_RF_FRFMSB_864								= const(0xD8)
_RF_FRFMID_864								= const(0x00)
_RF_FRFLSB_864								= const(0x00)
_RF_FRFMSB_865								= const(0xD8)
_RF_FRFMID_865								= const(0x40)
_RF_FRFLSB_865								= const(0x00)
_RF_FRFMSB_866								= const(0xD8)
_RF_FRFMID_866								= const(0x80)
_RF_FRFLSB_866								= const(0x00)
_RF_FRFMSB_867								= const(0xD8)
_RF_FRFMID_867								= const(0xC0)
_RF_FRFLSB_867								= const(0x00)
_RF_FRFMSB_868								= const(0xD9)
_RF_FRFMID_868								= const(0x00)
_RF_FRFLSB_868								= const(0x00)
_RF_FRFMSB_869								= const(0xD9)
_RF_FRFMID_869								= const(0x40)
_RF_FRFLSB_869								= const(0x00)
_RF_FRFMSB_870								= const(0xD9)
_RF_FRFMID_870								= const(0x80)
_RF_FRFLSB_870								= const(0x00)
# 915 Mhz band
_RF_FRFMSB_902								= const(0xE1)
_RF_FRFMID_902								= const(0x80)
_RF_FRFLSB_902								= const(0x00)
_RF_FRFMSB_903								= const(0xE1)
_RF_FRFMID_903								= const(0xC0)
_RF_FRFLSB_903								= const(0x00)
_RF_FRFMSB_904								= const(0xE2)
_RF_FRFMID_904								= const(0x00)
_RF_FRFLSB_904								= const(0x00)
_RF_FRFMSB_905								= const(0xE2)
_RF_FRFMID_905								= const(0x40)
_RF_FRFLSB_905								= const(0x00)
_RF_FRFMSB_906								= const(0xE2)
_RF_FRFMID_906								= const(0x80)
_RF_FRFLSB_906								= const(0x00)
_RF_FRFMSB_907								= const(0xE2)
_RF_FRFMID_907								= const(0xC0)
_RF_FRFLSB_907								= const(0x00)
_RF_FRFMSB_908								= const(0xE3)
_RF_FRFMID_908								= const(0x00)
_RF_FRFLSB_908								= const(0x00)
_RF_FRFMSB_909								= const(0xE3)
_RF_FRFMID_909								= const(0x40)
_RF_FRFLSB_909								= const(0x00)
_RF_FRFMSB_910								= const(0xE3)
_RF_FRFMID_910								= const(0x80)
_RF_FRFLSB_910								= const(0x00)
_RF_FRFMSB_911								= const(0xE3)
_RF_FRFMID_911								= const(0xC0)
_RF_FRFLSB_911								= const(0x00)
_RF_FRFMSB_912								= const(0xE4)
_RF_FRFMID_912								= const(0x00)
_RF_FRFLSB_912								= const(0x00)
_RF_FRFMSB_913								= const(0xE4)
_RF_FRFMID_913								= const(0x40)
_RF_FRFLSB_913								= const(0x00)
_RF_FRFMSB_914								= const(0xE4)
_RF_FRFMID_914								= const(0x80)
_RF_FRFLSB_914								= const(0x00)
_RF_FRFMSB_915								= const(0xE4) # Default
_RF_FRFMID_915								= const(0xC0) # Default
_RF_FRFLSB_915								= const(0x00) # Default
_RF_FRFMSB_916								= const(0xE5)
_RF_FRFMID_916								= const(0x00)
_RF_FRFLSB_916								= const(0x00)
_RF_FRFMSB_917								= const(0xE5)
_RF_FRFMID_917								= const(0x40)
_RF_FRFLSB_917								= const(0x00)
_RF_FRFMSB_918								= const(0xE5)
_RF_FRFMID_918								= const(0x80)
_RF_FRFLSB_918								= const(0x00)
_RF_FRFMSB_919								= const(0xE5)
_RF_FRFMID_919								= const(0xC0)
_RF_FRFLSB_919								= const(0x00)
_RF_FRFMSB_920								= const(0xE6)
_RF_FRFMID_920								= const(0x00)
_RF_FRFLSB_920								= const(0x00)
_RF_FRFMSB_921								= const(0xE6)
_RF_FRFMID_921								= const(0x40)
_RF_FRFLSB_921								= const(0x00)
_RF_FRFMSB_922								= const(0xE6)
_RF_FRFMID_922								= const(0x80)
_RF_FRFLSB_922								= const(0x00)
_RF_FRFMSB_923								= const(0xE6)
_RF_FRFMID_923								= const(0xC0)
_RF_FRFLSB_923								= const(0x00)
_RF_FRFMSB_924								= const(0xE7)
_RF_FRFMID_924								= const(0x00)
_RF_FRFLSB_924								= const(0x00)
_RF_FRFMSB_925								= const(0xE7)
_RF_FRFMID_925								= const(0x40)
_RF_FRFLSB_925								= const(0x00)
_RF_FRFMSB_926								= const(0xE7)
_RF_FRFMID_926								= const(0x80)
_RF_FRFLSB_926								= const(0x00)
_RF_FRFMSB_927								= const(0xE7)
_RF_FRFMID_927								= const(0xC0)
_RF_FRFLSB_927								= const(0x00)
_RF_FRFMSB_928								= const(0xE8)
_RF_FRFMID_928								= const(0x00)
_RF_FRFLSB_928								= const(0x00)

# _Reg Osc 1
_RF_OSC1_RCCAL_START							= const(0x80)
_RF_OSC1_RCCAL_DONE							= const(0x40)

# _Reg Low Bat
_RF_LOWBAT_MONITOR							= const(0x10)
_RF_LOWBAT_ON								= const(0x08)
_RF_LOWBAT_OFF								= const(0x00) # Default

_RF_LOWBAT_TRIM_1695							= const(0x00)
_RF_LOWBAT_TRIM_1764							= const(0x01)
_RF_LOWBAT_TRIM_1835							= const(0x02) # Default
_RF_LOWBAT_TRIM_1905							= const(0x03)
_RF_LOWBAT_TRIM_1976							= const(0x04)
_RF_LOWBAT_TRIM_2045							= const(0x05)
_RF_LOWBAT_TRIM_2116							= const(0x06)
_RF_LOWBAT_TRIM_2185							= const(0x07)

# _Reg Listen 1
_RF_LISTEN1_RESOL_64							= const(0x50)
_RF_LISTEN1_RESOL_4100						= const(0xA0) # Default
_RF_LISTEN1_RESOL_262000						= const(0xF0)

_RF_LISTEN1_CRITERIA_RSSI					= const(0x00) # Default
_RF_LISTEN1_CRITERIA_RSSIANDSYNC				= const(0x08)

_RF_LISTEN1_END_00							= const(0x00)
_RF_LISTEN1_END_01							= const(0x02) # Default
_RF_LISTEN1_END_10							= const(0x04)

# _Reg Listen 2
_RF_LISTEN2_COEFIDLE_VALUE					= const(0xF5) # Default

# _Reg Listen 3
_RF_LISTEN3_COEFRX_VALUE						= const(0x20) # Default

# _Reg PaLevel
_RF_PALEVEL_PA0_ON							= const(0x80) # Default
_RF_PALEVEL_PA0_OFF							= const(0x00)
_RF_PALEVEL_PA1_ON							= const(0x40)
_RF_PALEVEL_PA1_OFF							= const(0x00) # Default
_RF_PALEVEL_PA2_ON							= const(0x20)
_RF_PALEVEL_PA2_OFF							= const(0x00) # Default

_RF_PALEVEL_OUTPUTPOWER_00000				= const(0x00)
_RF_PALEVEL_OUTPUTPOWER_00001				= const(0x01)
_RF_PALEVEL_OUTPUTPOWER_00010				= const(0x02)
_RF_PALEVEL_OUTPUTPOWER_00011				= const(0x03)
_RF_PALEVEL_OUTPUTPOWER_00100				= const(0x04)
_RF_PALEVEL_OUTPUTPOWER_00101				= const(0x05)
_RF_PALEVEL_OUTPUTPOWER_00110				= const(0x06)
_RF_PALEVEL_OUTPUTPOWER_00111				= const(0x07)
_RF_PALEVEL_OUTPUTPOWER_01000				= const(0x08)
_RF_PALEVEL_OUTPUTPOWER_01001				= const(0x09)
_RF_PALEVEL_OUTPUTPOWER_01010				= const(0x0A)
_RF_PALEVEL_OUTPUTPOWER_01011				= const(0x0B)
_RF_PALEVEL_OUTPUTPOWER_01100				= const(0x0C)
_RF_PALEVEL_OUTPUTPOWER_01101				= const(0x0D)
_RF_PALEVEL_OUTPUTPOWER_01110				= const(0x0E)
_RF_PALEVEL_OUTPUTPOWER_01111				= const(0x0F)
_RF_PALEVEL_OUTPUTPOWER_10000				= const(0x10)
_RF_PALEVEL_OUTPUTPOWER_10001				= const(0x11)
_RF_PALEVEL_OUTPUTPOWER_10010				= const(0x12)
_RF_PALEVEL_OUTPUTPOWER_10011				= const(0x13)
_RF_PALEVEL_OUTPUTPOWER_10100				= const(0x14)
_RF_PALEVEL_OUTPUTPOWER_10101				= const(0x15)
_RF_PALEVEL_OUTPUTPOWER_10110				= const(0x16)
_RF_PALEVEL_OUTPUTPOWER_10111				= const(0x17)
_RF_PALEVEL_OUTPUTPOWER_11000				= const(0x18)
_RF_PALEVEL_OUTPUTPOWER_11001				= const(0x19)
_RF_PALEVEL_OUTPUTPOWER_11010				= const(0x1A)
_RF_PALEVEL_OUTPUTPOWER_11011				= const(0x1B)
_RF_PALEVEL_OUTPUTPOWER_11100				= const(0x1C)
_RF_PALEVEL_OUTPUTPOWER_11101				= const(0x1D)
_RF_PALEVEL_OUTPUTPOWER_11110				= const(0x1E)
_RF_PALEVEL_OUTPUTPOWER_11111				= const(0x1F) # Default

# _Reg PaRamp
_RF_PARAMP_3400								= const(0x00)
_RF_PARAMP_2000								= const(0x01)
_RF_PARAMP_1000								= const(0x02)
_RF_PARAMP_500								= const(0x03)
_RF_PARAMP_250								= const(0x04)
_RF_PARAMP_125								= const(0x05)
_RF_PARAMP_100								= const(0x06)
_RF_PARAMP_62								= const(0x07)
_RF_PARAMP_50								= const(0x08)
_RF_PARAMP_40								= const(0x09) # Default
_RF_PARAMP_31								= const(0x0A)
_RF_PARAMP_25								= const(0x0B)
_RF_PARAMP_20								= const(0x0C)
_RF_PARAMP_15								= const(0x0D)
_RF_PARAMP_12								= const(0x0E)
_RF_PARAMP_10								= const(0x0F)

# _Reg Ocp
_RF_OCP_OFF									= const(0x0F)
_RF_OCP_ON									= const(0x1A) # Default

_RF_OCP_TRIM_45								= const(0x00)
_RF_OCP_TRIM_50								= const(0x01)
_RF_OCP_TRIM_55								= const(0x02)
_RF_OCP_TRIM_60								= const(0x03)
_RF_OCP_TRIM_65								= const(0x04)
_RF_OCP_TRIM_70								= const(0x05)
_RF_OCP_TRIM_75								= const(0x06)
_RF_OCP_TRIM_80								= const(0x07)
_RF_OCP_TRIM_85								= const(0x08)
_RF_OCP_TRIM_90								= const(0x09)
_RF_OCP_TRIM_95								= const(0x0A)
_RF_OCP_TRIM_100								= const(0x0B) # Default
_RF_OCP_TRIM_105								= const(0x0C)
_RF_OCP_TRIM_110								= const(0x0D)
_RF_OCP_TRIM_115								= const(0x0E)
_RF_OCP_TRIM_120								= const(0x0F)

# _Reg Agc _Ref
_RF_AGCREF_AUTO_ON							= const(0x40) # Default
_RF_AGCREF_AUTO_OFF							= const(0x00)

_RF_AGCREF_LEVEL_MINUS80						= const(0x00) # Default
_RF_AGCREF_LEVEL_MINUS81						= const(0x01)
_RF_AGCREF_LEVEL_MINUS82						= const(0x02)
_RF_AGCREF_LEVEL_MINUS83						= const(0x03)
_RF_AGCREF_LEVEL_MINUS84						= const(0x04)
_RF_AGCREF_LEVEL_MINUS85						= const(0x05)
_RF_AGCREF_LEVEL_MINUS86						= const(0x06)
_RF_AGCREF_LEVEL_MINUS87						= const(0x07)
_RF_AGCREF_LEVEL_MINUS88						= const(0x08)
_RF_AGCREF_LEVEL_MINUS89						= const(0x09)
_RF_AGCREF_LEVEL_MINUS90						= const(0x0A)
_RF_AGCREF_LEVEL_MINUS91						= const(0x0B)
_RF_AGCREF_LEVEL_MINUS92						= const(0x0C)
_RF_AGCREF_LEVEL_MINUS93						= const(0x0D)
_RF_AGCREF_LEVEL_MINUS94						= const(0x0E)
_RF_AGCREF_LEVEL_MINUS95						= const(0x0F)
_RF_AGCREF_LEVEL_MINUS96						= const(0x10)
_RF_AGCREF_LEVEL_MINUS97						= const(0x11)
_RF_AGCREF_LEVEL_MINUS98						= const(0x12)
_RF_AGCREF_LEVEL_MINUS99						= const(0x13)
_RF_AGCREF_LEVEL_MINUS100					= const(0x14)
_RF_AGCREF_LEVEL_MINUS101					= const(0x15)
_RF_AGCREF_LEVEL_MINUS102					= const(0x16)
_RF_AGCREF_LEVEL_MINUS103					= const(0x17)
_RF_AGCREF_LEVEL_MINUS104					= const(0x18)
_RF_AGCREF_LEVEL_MINUS105					= const(0x19)
_RF_AGCREF_LEVEL_MINUS106					= const(0x1A)
_RF_AGCREF_LEVEL_MINUS107					= const(0x1B)
_RF_AGCREF_LEVEL_MINUS108					= const(0x1C)
_RF_AGCREF_LEVEL_MINUS109					= const(0x1D)
_RF_AGCREF_LEVEL_MINUS110					= const(0x1E)
_RF_AGCREF_LEVEL_MINUS111					= const(0x1F)
_RF_AGCREF_LEVEL_MINUS112					= const(0x20)
_RF_AGCREF_LEVEL_MINUS113					= const(0x21)
_RF_AGCREF_LEVEL_MINUS114					= const(0x22)
_RF_AGCREF_LEVEL_MINUS115					= const(0x23)
_RF_AGCREF_LEVEL_MINUS116					= const(0x24)
_RF_AGCREF_LEVEL_MINUS117					= const(0x25)
_RF_AGCREF_LEVEL_MINUS118					= const(0x26)
_RF_AGCREF_LEVEL_MINUS119					= const(0x27)
_RF_AGCREF_LEVEL_MINUS120					= const(0x28)
_RF_AGCREF_LEVEL_MINUS121					= const(0x29)
_RF_AGCREF_LEVEL_MINUS122					= const(0x2A)
_RF_AGCREF_LEVEL_MINUS123					= const(0x2B)
_RF_AGCREF_LEVEL_MINUS124					= const(0x2C)
_RF_AGCREF_LEVEL_MINUS125					= const(0x2D)
_RF_AGCREF_LEVEL_MINUS126					= const(0x2E)
_RF_AGCREF_LEVEL_MINUS127					= const(0x2F)
_RF_AGCREF_LEVEL_MINUS128					= const(0x30)
_RF_AGCREF_LEVEL_MINUS129					= const(0x31)
_RF_AGCREF_LEVEL_MINUS130					= const(0x32)
_RF_AGCREF_LEVEL_MINUS131					= const(0x33)
_RF_AGCREF_LEVEL_MINUS132					= const(0x34)
_RF_AGCREF_LEVEL_MINUS133					= const(0x35)
_RF_AGCREF_LEVEL_MINUS134					= const(0x36)
_RF_AGCREF_LEVEL_MINUS135					= const(0x37)
_RF_AGCREF_LEVEL_MINUS136					= const(0x38)
_RF_AGCREF_LEVEL_MINUS137					= const(0x39)
_RF_AGCREF_LEVEL_MINUS138					= const(0x3A)
_RF_AGCREF_LEVEL_MINUS139					= const(0x3B)
_RF_AGCREF_LEVEL_MINUS140					= const(0x3C)
_RF_AGCREF_LEVEL_MINUS141					= const(0x3D)
_RF_AGCREF_LEVEL_MINUS142					= const(0x3E)
_RF_AGCREF_LEVEL_MINUS143					= const(0x3F)

# _Reg Agc Thresh 1
_RF_AGCTHRESH1_SNRMARGIN_000					= const(0x00)
_RF_AGCTHRESH1_SNRMARGIN_001					= const(0x20)
_RF_AGCTHRESH1_SNRMARGIN_010					= const(0x40)
_RF_AGCTHRESH1_SNRMARGIN_011					= const(0x60)
_RF_AGCTHRESH1_SNRMARGIN_100					= const(0x80)
_RF_AGCTHRESH1_SNRMARGIN_101					= const(0xA0) # Default
_RF_AGCTHRESH1_SNRMARGIN_110					= const(0xC0)
_RF_AGCTHRESH1_SNRMARGIN_111					= const(0xE0)

_RF_AGCTHRESH1_STEP1_0						= const(0x00)
_RF_AGCTHRESH1_STEP1_1						= const(0x01)
_RF_AGCTHRESH1_STEP1_2						= const(0x02)
_RF_AGCTHRESH1_STEP1_3						= const(0x03)
_RF_AGCTHRESH1_STEP1_4						= const(0x04)
_RF_AGCTHRESH1_STEP1_5						= const(0x05)
_RF_AGCTHRESH1_STEP1_6						= const(0x06)
_RF_AGCTHRESH1_STEP1_7						= const(0x07)
_RF_AGCTHRESH1_STEP1_8						= const(0x08)
_RF_AGCTHRESH1_STEP1_9						= const(0x09)
_RF_AGCTHRESH1_STEP1_10						= const(0x0A)
_RF_AGCTHRESH1_STEP1_11						= const(0x0B)
_RF_AGCTHRESH1_STEP1_12						= const(0x0C)
_RF_AGCTHRESH1_STEP1_13						= const(0x0D)
_RF_AGCTHRESH1_STEP1_14						= const(0x0E)
_RF_AGCTHRESH1_STEP1_15						= const(0x0F)
_RF_AGCTHRESH1_STEP1_16						= const(0x10) # Default
_RF_AGCTHRESH1_STEP1_17						= const(0x11)
_RF_AGCTHRESH1_STEP1_18						= const(0x12)
_RF_AGCTHRESH1_STEP1_19						= const(0x13)
_RF_AGCTHRESH1_STEP1_20						= const(0x14)
_RF_AGCTHRESH1_STEP1_21						= const(0x15)
_RF_AGCTHRESH1_STEP1_22						= const(0x16)
_RF_AGCTHRESH1_STEP1_23						= const(0x17)
_RF_AGCTHRESH1_STEP1_24						= const(0x18)
_RF_AGCTHRESH1_STEP1_25						= const(0x19)
_RF_AGCTHRESH1_STEP1_26						= const(0x1A)
_RF_AGCTHRESH1_STEP1_27						= const(0x1B)
_RF_AGCTHRESH1_STEP1_28						= const(0x1C)
_RF_AGCTHRESH1_STEP1_29						= const(0x1D)
_RF_AGCTHRESH1_STEP1_30						= const(0x1E)
_RF_AGCTHRESH1_STEP1_31						= const(0x1F)

# _Reg Agc Thresh 2
_RF_AGCTHRESH2_STEP2_0						= const(0x00)
_RF_AGCTHRESH2_STEP2_1						= const(0x10)
_RF_AGCTHRESH2_STEP2_2						= const(0x20)
_RF_AGCTHRESH2_STEP2_3						= const(0x30) # XXX wrong -- Default
_RF_AGCTHRESH2_STEP2_4						= const(0x40)
_RF_AGCTHRESH2_STEP2_5						= const(0x50)
_RF_AGCTHRESH2_STEP2_6						= const(0x60)
_RF_AGCTHRESH2_STEP2_7						= const(0x70) # Default
_RF_AGCTHRESH2_STEP2_8						= const(0x80)
_RF_AGCTHRESH2_STEP2_9						= const(0x90)
_RF_AGCTHRESH2_STEP2_10						= const(0xA0)
_RF_AGCTHRESH2_STEP2_11						= const(0xB0)
_RF_AGCTHRESH2_STEP2_12						= const(0xC0)
_RF_AGCTHRESH2_STEP2_13						= const(0xD0)
_RF_AGCTHRESH2_STEP2_14						= const(0xE0)
_RF_AGCTHRESH2_STEP2_15						= const(0xF0)

_RF_AGCTHRESH2_STEP3_0						= const(0x00)
_RF_AGCTHRESH2_STEP3_1						= const(0x01)
_RF_AGCTHRESH2_STEP3_2						= const(0x02)
_RF_AGCTHRESH2_STEP3_3						= const(0x03)
_RF_AGCTHRESH2_STEP3_4						= const(0x04)
_RF_AGCTHRESH2_STEP3_5						= const(0x05)
_RF_AGCTHRESH2_STEP3_6						= const(0x06)
_RF_AGCTHRESH2_STEP3_7						= const(0x07)
_RF_AGCTHRESH2_STEP3_8						= const(0x08)
_RF_AGCTHRESH2_STEP3_9						= const(0x09)
_RF_AGCTHRESH2_STEP3_10						= const(0x0A)
_RF_AGCTHRESH2_STEP3_11						= const(0x0B) # Default
_RF_AGCTHRESH2_STEP3_12						= const(0x0C)
_RF_AGCTHRESH2_STEP3_13						= const(0x0D)
_RF_AGCTHRESH2_STEP3_14						= const(0x0E)
_RF_AGCTHRESH2_STEP3_15						= const(0x0F)

# _Reg Agc Thresh 3
_RF_AGCTHRESH3_STEP4_0						= const(0x00)
_RF_AGCTHRESH3_STEP4_1						= const(0x10)
_RF_AGCTHRESH3_STEP4_2						= const(0x20)
_RF_AGCTHRESH3_STEP4_3						= const(0x30)
_RF_AGCTHRESH3_STEP4_4						= const(0x40)
_RF_AGCTHRESH3_STEP4_5						= const(0x50)
_RF_AGCTHRESH3_STEP4_6						= const(0x60)
_RF_AGCTHRESH3_STEP4_7						= const(0x70)
_RF_AGCTHRESH3_STEP4_8						= const(0x80)
_RF_AGCTHRESH3_STEP4_9						= const(0x90) # Default
_RF_AGCTHRESH3_STEP4_10						= const(0xA0)
_RF_AGCTHRESH3_STEP4_11						= const(0xB0)
_RF_AGCTHRESH3_STEP4_12						= const(0xC0)
_RF_AGCTHRESH3_STEP4_13						= const(0xD0)
_RF_AGCTHRESH3_STEP4_14						= const(0xE0)
_RF_AGCTHRESH3_STEP4_15						= const(0xF0)

_RF_AGCTHRESH3_STEP5_0						= const(0x00)
_RF_AGCTHRESH3_STEP5_1						= const(0x01)
_RF_AGCTHRESH3_STEP5_2						= const(0x02)
_RF_AGCTHRESH3_STEP5_3						= const(0x03)
_RF_AGCTHRESH3_STEP5_4						= const(0x04)
_RF_AGCTHRESH3_STEP5_5						= const(0x05)
_RF_AGCTHRESH3_STEP5_6						= const(0x06)
_RF_AGCTHRESH3_STEP5_7						= const(0x07)
_RF_AGCTHRES33_STEP5_8						= const(0x08)
_RF_AGCTHRESH3_STEP5_9						= const(0x09)
_RF_AGCTHRESH3_STEP5_10						= const(0x0A)
_RF_AGCTHRESH3_STEP5_11						= const(0x0B) # Default
_RF_AGCTHRESH3_STEP5_12						= const(0x0C)
_RF_AGCTHRESH3_STEP5_13						= const(0x0D)
_RF_AGCTHRESH3_STEP5_14						= const(0x0E)
_RF_AGCTHRESH3_STEP5_15						= const(0x0F)

# _Reg Lna
_RF_LNA_ZIN_50								= const(0x00)
_RF_LNA_ZIN_200								= const(0x80) # Default

_RF_LNA_LOWPOWER_OFF							= const(0x00) # Default
_RF_LNA_LOWPOWER_ON							= const(0x40)

_RF_LNA_CURRENTGAIN							= const(0x08)

_RF_LNA_GAINSELECT_AUTO						= const(0x00) # Default
_RF_LNA_GAINSELECT_MAX						= const(0x01)
_RF_LNA_GAINSELECT_MAXMINUS6					= const(0x02)
_RF_LNA_GAINSELECT_MAXMINUS12				= const(0x03)
_RF_LNA_GAINSELECT_MAXMINUS24				= const(0x04)
_RF_LNA_GAINSELECT_MAXMINUS36				= const(0x05)
_RF_LNA_GAINSELECT_MAXMINUS48				= const(0x06)

# _Reg _Rx Bw
_RF_RXBW_DCCFREQ_000							= const(0x00)
_RF_RXBW_DCCFREQ_001							= const(0x20)
_RF_RXBW_DCCFREQ_010							= const(0x40) # Default
_RF_RXBW_DCCFREQ_011							= const(0x60)
_RF_RXBW_DCCFREQ_100							= const(0x80)
_RF_RXBW_DCCFREQ_101							= const(0xA0)
_RF_RXBW_DCCFREQ_110							= const(0xC0)
_RF_RXBW_DCCFREQ_111							= const(0xE0)

_RF_RXBW_MANT_16								= const(0x00)
_RF_RXBW_MANT_20								= const(0x08)
_RF_RXBW_MANT_24								= const(0x10) # Default

_RF_RXBW_EXP_0								= const(0x00)
_RF_RXBW_EXP_1								= const(0x01)
_RF_RXBW_EXP_2								= const(0x02)
_RF_RXBW_EXP_3								= const(0x03)
_RF_RXBW_EXP_4								= const(0x04)
_RF_RXBW_EXP_5								= const(0x05) # Default
_RF_RXBW_EXP_6								= const(0x06)
_RF_RXBW_EXP_7								= const(0x07)

# _Reg Afc Bw
_RF_AFCBW_DCCFREQAFC_000						= const(0x00)
_RF_AFCBW_DCCFREQAFC_001						= const(0x20)
_RF_AFCBW_DCCFREQAFC_010						= const(0x40)
_RF_AFCBW_DCCFREQAFC_011						= const(0x60)
_RF_AFCBW_DCCFREQAFC_100						= const(0x80) # Default
_RF_AFCBW_DCCFREQAFC_101						= const(0xA0)
_RF_AFCBW_DCCFREQAFC_110						= const(0xC0)
_RF_AFCBW_DCCFREQAFC_111						= const(0xE0)

_RF_AFCBW_MANTAFC_16							= const(0x00)
_RF_AFCBW_MANTAFC_20							= const(0x08) # Default
_RF_AFCBW_MANTAFC_24							= const(0x10)

_RF_AFCBW_EXPAFC_0							= const(0x00)
_RF_AFCBW_EXPAFC_1							= const(0x01)
_RF_AFCBW_EXPAFC_2							= const(0x02)
_RF_AFCBW_EXPAFC_3							= const(0x03) # Default
_RF_AFCBW_EXPAFC_4							= const(0x04)
_RF_AFCBW_EXPAFC_5							= const(0x05)
_RF_AFCBW_EXPAFC_6							= const(0x06)
_RF_AFCBW_EXPAFC_7							= const(0x07)

# _Reg Ook Peak
_RF_OOKPEAK_THRESHTYPE_FIXED					= const(0x00)
_RF_OOKPEAK_THRESHTYPE_PEAK					= const(0x40) # Default
_RF_OOKPEAK_THRESHTYPE_AVERAGE				= const(0x80)

_RF_OOKPEAK_PEAKTHRESHSTEP_000				= const(0x00) # Default
_RF_OOKPEAK_PEAKTHRESHSTEP_001				= const(0x08)
_RF_OOKPEAK_PEAKTHRESHSTEP_010				= const(0x10)
_RF_OOKPEAK_PEAKTHRESHSTEP_011				= const(0x18)
_RF_OOKPEAK_PEAKTHRESHSTEP_100				= const(0x20)
_RF_OOKPEAK_PEAKTHRESHSTEP_101				= const(0x28)
_RF_OOKPEAK_PEAKTHRESHSTEP_110				= const(0x30)
_RF_OOKPEAK_PEAKTHRESHSTEP_111				= const(0x38)

_RF_OOKPEAK_PEAKTHRESHDEC_000				= const(0x00) # Default
_RF_OOKPEAK_PEAKTHRESHDEC_001				= const(0x01)
_RF_OOKPEAK_PEAKTHRESHDEC_010				= const(0x02)
_RF_OOKPEAK_PEAKTHRESHDEC_011				= const(0x03)
_RF_OOKPEAK_PEAKTHRESHDEC_100				= const(0x04)
_RF_OOKPEAK_PEAKTHRESHDEC_101				= const(0x05)
_RF_OOKPEAK_PEAKTHRESHDEC_110				= const(0x06)
_RF_OOKPEAK_PEAKTHRESHDEC_111				= const(0x07)

# _Reg Ook Avg
_RF_OOKAVG_AVERAGETHRESHFILT_00				= const(0x00)
_RF_OOKAVG_AVERAGETHRESHFILT_01				= const(0x40)
_RF_OOKAVG_AVERAGETHRESHFILT_10				= const(0x80) # Default
_RF_OOKAVG_AVERAGETHRESHFILT_11				= const(0xC0)

# _Reg Ook Fix
_RF_OOKFIX_FIXEDTHRESH_VALUE					= const(0x06) # Default

# _Reg Afc Fei
_RF_AFCFEI_FEI_DONE							= const(0x40)
_RF_AFCFEI_FEI_START							= const(0x20)
_RF_AFCFEI_AFC_DONE							= const(0x10)
_RF_AFCFEI_AFCAUTOCLEAR_ON					= const(0x08)
_RF_AFCFEI_AFCAUTOCLEAR_OFF					= const(0x00) # Default

_RF_AFCFEI_AFCAUTO_ON						= const(0x04)
_RF_AFCFEI_AFCAUTO_OFF						= const(0x00) # Default

_RF_AFCFEI_AFC_CLEAR							= const(0x02)
_RF_AFCFEI_AFC_START							= const(0x01)

# _Reg _Rssi Config
_RF_RSSI_FASTRX_ON							= const(0x08)
_RF_RSSI_FASTRX_OFF							= const(0x00) # Default
_RF_RSSI_DONE								= const(0x02)
_RF_RSSI_START								= const(0x01)

# _Reg Dio Mapping 1
_RF_DIOMAPPING1_DIO0_00						= const(0x00) # Default
_RF_DIOMAPPING1_DIO0_01						= const(0x40)
_RF_DIOMAPPING1_DIO0_10						= const(0x80)
_RF_DIOMAPPING1_DIO0_11						= const(0xC0)

_RF_DIOMAPPING1_DIO1_00						= const(0x00) # Default
_RF_DIOMAPPING1_DIO1_01						= const(0x10)
_RF_DIOMAPPING1_DIO1_10						= const(0x20)
_RF_DIOMAPPING1_DIO1_11						= const(0x30)

_RF_DIOMAPPING1_DIO2_00						= const(0x00) # Default
_RF_DIOMAPPING1_DIO2_01						= const(0x04)
_RF_DIOMAPPING1_DIO2_10						= const(0x08)
_RF_DIOMAPPING1_DIO2_11						= const(0x0C)

_RF_DIOMAPPING1_DIO3_00						= const(0x00) # Default
_RF_DIOMAPPING1_DIO3_01						= const(0x01)
_RF_DIOMAPPING1_DIO3_10						= const(0x02)
_RF_DIOMAPPING1_DIO3_11						= const(0x03)

# _Reg Dio Mapping 2
_RF_DIOMAPPING2_DIO4_00						= const(0x00) # Default
_RF_DIOMAPPING2_DIO4_01						= const(0x40)
_RF_DIOMAPPING2_DIO4_10						= const(0x80)
_RF_DIOMAPPING2_DIO4_11						= const(0xC0)

_RF_DIOMAPPING2_DIO5_00						= const(0x00) # Default
_RF_DIOMAPPING2_DIO5_01						= const(0x10)
_RF_DIOMAPPING2_DIO5_10						= const(0x20)
_RF_DIOMAPPING2_DIO5_11						= const(0x30)

_RF_DIOMAPPING2_CLKOUT_32					= const(0x00)
_RF_DIOMAPPING2_CLKOUT_16					= const(0x01)
_RF_DIOMAPPING2_CLKOUT_8						= const(0x02)
_RF_DIOMAPPING2_CLKOUT_4						= const(0x03)
_RF_DIOMAPPING2_CLKOUT_2						= const(0x04)
_RF_DIOMAPPING2_CLKOUT_1						= const(0x05)
_RF_DIOMAPPING2_CLKOUT_RC					= const(0x06)
_RF_DIOMAPPING2_CLKOUT_OFF					= const(0x07) # Default

# _Reg Irq Flags 1
_RF_IRQFLAGS1_MODEREADY						= const(0x80)
_RF_IRQFLAGS1_RXREADY						= const(0x40)
_RF_IRQFLAGS1_TXREADY						= const(0x20)
_RF_IRQFLAGS1_PLLLOCK						= const(0x10)
_RF_IRQFLAGS1_RSSI							= const(0x08)
_RF_IRQFLAGS1_TIMEOUT						= const(0x04)
_RF_IRQFLAGS1_AUTOMODE						= const(0x02)
_RF_IRQFLAGS1_SYNCADDRESSMATCH				= const(0x01)

# _Reg Irq Flags 2
_RF_IRQFLAGS2_FIFOFULL						= const(0x80)
_RF_IRQFLAGS2_FIFONOTEMPTY					= const(0x40)
_RF_IRQFLAGS2_FIFOLEVEL						= const(0x20)
_RF_IRQFLAGS2_FIFOOVERRUN					= const(0x10)
_RF_IRQFLAGS2_PACKETSENT						= const(0x08)
_RF_IRQFLAGS2_PAYLOADREADY					= const(0x04)
_RF_IRQFLAGS2_CRCOK							= const(0x02)
_RF_IRQFLAGS2_LOWBAT							= const(0x01)

# _Reg _Rssi Thresh
_RF_RSSITHRESH_VALUE							= const(0xE4) # Default

# _Reg _Rx Timeout 1
_RF_RXTIMEOUT1_RXSTART_VALUE					= const(0x00) # Default

# _Reg _Rx Timeout 2
_RF_RXTIMEOUT2_RSSITHRESH_VALUE				= const(0x00) # Default

# _Reg Preamble
_RF_PREAMBLESIZE_MSB_VALUE					= const(0x00) # Default
_RF_PREAMBLESIZE_LSB_VALUE					= const(0x03) # Default

# _Reg Sync Config
_RF_SYNC_ON									= const(0x80) # Default
_RF_SYNC_OFF									= const(0x00)

_RF_SYNC_FIFOFILL_AUTO						= const(0x00) # Default -- when sync interrupt occurs
_RF_SYNC_FIFOFILL_MANUAL						= const(0x40)

_RF_SYNC_SIZE_1								= const(0x00)
_RF_SYNC_SIZE_2								= const(0x08)
_RF_SYNC_SIZE_3								= const(0x10)
_RF_SYNC_SIZE_4								= const(0x18) # Default
_RF_SYNC_SIZE_5								= const(0x20)
_RF_SYNC_SIZE_6								= const(0x28)
_RF_SYNC_SIZE_7								= const(0x30)
_RF_SYNC_SIZE_8								= const(0x38)

_RF_SYNC_TOL_0								= const(0x00) # Default
_RF_SYNC_TOL_1								= const(0x01)
_RF_SYNC_TOL_2								= const(0x02)
_RF_SYNC_TOL_3								= const(0x03)
_RF_SYNC_TOL_4								= const(0x04)
_RF_SYNC_TOL_5								= const(0x05)
_RF_SYNC_TOL_6								= const(0x06)
_RF_SYNC_TOL_7								= const(0x07)

# _Reg Sync Value 1-8
_RF_SYNC_BYTE1_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE2_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE3_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE4_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE5_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE6_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE7_VALUE							= const(0x00) # Default
_RF_SYNC_BYTE8_VALUE							= const(0x00) # Default

# _Reg Packet Config 1
_RF_PACKET1_FORMAT_FIXED						= const(0x00) # Default
_RF_PACKET1_FORMAT_VARIABLE					= const(0x80)

_RF_PACKET1_DCFREE_OFF						= const(0x00) # Default
_RF_PACKET1_DCFREE_MANCHESTER				= const(0x20)
_RF_PACKET1_DCFREE_WHITENING					= const(0x40)

_RF_PACKET1_CRC_ON							= const(0x10) # Default
_RF_PACKET1_CRC_OFF							= const(0x00)

_RF_PACKET1_CRCAUTOCLEAR_ON					= const(0x00) # Default
_RF_PACKET1_CRCAUTOCLEAR_OFF					= const(0x08)

_RF_PACKET1_ADRSFILTERING_OFF				= const(0x00) # Default
_RF_PACKET1_ADRSFILTERING_NODE				= const(0x02)
_RF_PACKET1_ADRSFILTERING_NODEBROADCAST		= const(0x04)

# _Reg Payload Length
_RF_PAYLOADLENGTH_VALUE						= const(0x40) # Default

# _Reg Broadcast Adrs
_RF_BROADCASTADDRESS_VALUE					= const(0x00)

# _Reg Auto Modes
_RF_AUTOMODES_ENTER_OFF						= const(0x00) # Default
_RF_AUTOMODES_ENTER_FIFONOTEMPTY				= const(0x20)
_RF_AUTOMODES_ENTER_FIFOLEVEL				= const(0x40)
_RF_AUTOMODES_ENTER_CRCOK					= const(0x60)
_RF_AUTOMODES_ENTER_PAYLOADREADY				= const(0x80)
_RF_AUTOMODES_ENTER_SYNCADRSMATCH			= const(0xA0)
_RF_AUTOMODES_ENTER_PACKETSENT				= const(0xC0)
_RF_AUTOMODES_ENTER_FIFOEMPTY				= const(0xE0)

_RF_AUTOMODES_EXIT_OFF						= const(0x00) # Default
_RF_AUTOMODES_EXIT_FIFOEMPTY					= const(0x04)
_RF_AUTOMODES_EXIT_FIFOLEVEL					= const(0x08)
_RF_AUTOMODES_EXIT_CRCOK						= const(0x0C)
_RF_AUTOMODES_EXIT_PAYLOADREADY				= const(0x10)
_RF_AUTOMODES_EXIT_SYNCADRSMATCH				= const(0x14)
_RF_AUTOMODES_EXIT_PACKETSENT				= const(0x18)
_RF_AUTOMODES_EXIT_RXTIMEOUT					= const(0x1C)

_RF_AUTOMODES_INTERMEDIATE_SLEEP				= const(0x00) # Default
_RF_AUTOMODES_INTERMEDIATE_STANDBY			= const(0x01)
_RF_AUTOMODES_INTERMEDIATE_RECEIVER			= const(0x02)
_RF_AUTOMODES_INTERMEDIATE_TRANSMITTER		= const(0x03)

#_Reg Fifo Thresh
_RF_FIFOTHRESH_TXSTART_FIFOTHRESH			= const(0x00)
_RF_FIFOTHRESH_TXSTART_FIFONOTEMPTY			= const(0x80) # Default

_RF_FIFOTHRESH_VALUE							= const(0x0F) # Default

# _Reg Packet Config 2
_RF_PACKET2_RXRESTARTDELAY_1BIT				= const(0x00) # Default
_RF_PACKET2_RXRESTARTDELAY_2BITS				= const(0x10)
_RF_PACKET2_RXRESTARTDELAY_4BITS				= const(0x20)
_RF_PACKET2_RXRESTARTDELAY_8BITS				= const(0x30)
_RF_PACKET2_RXRESTARTDELAY_16BITS			= const(0x40)
_RF_PACKET2_RXRESTARTDELAY_32BITS			= const(0x50)
_RF_PACKET2_RXRESTARTDELAY_64BITS			= const(0x60)
_RF_PACKET2_RXRESTARTDELAY_128BITS			= const(0x70)
_RF_PACKET2_RXRESTARTDELAY_256BITS			= const(0x80)
_RF_PACKET2_RXRESTARTDELAY_512BITS			= const(0x90)
_RF_PACKET2_RXRESTARTDELAY_1024BITS			= const(0xA0)
_RF_PACKET2_RXRESTARTDELAY_2048BITS			= const(0xB0)
_RF_PACKET2_RXRESTARTDELAY_NONE				= const(0xC0)
_RF_PACKET2_RXRESTART						= const(0x04)

_RF_PACKET2_AUTORXRESTART_ON					= const(0x02) # Default
_RF_PACKET2_AUTORXRESTART_OFF				= const(0x00)

_RF_PACKET2_AES_ON							= const(0x01)
_RF_PACKET2_AES_OFF							= const(0x00) # Default

# _Reg Aes Key 1-16
_RF_AESKEY1_VALUE							= const(0x00) # Default
_RF_AESKEY2_VALUE							= const(0x00) # Default
_RF_AESKEY3_VALUE							= const(0x00) # Default
_RF_AESKEY4_VALUE							= const(0x00) # Default
_RF_AESKEY5_VALUE							= const(0x00) # Default
_RF_AESKEY6_VALUE							= const(0x00) # Default
_RF_AESKEY7_VALUE							= const(0x00) # Default
_RF_AESKEY8_VALUE							= const(0x00) # Default
_RF_AESKEY9_VALUE							= const(0x00) # Default
_RF_AESKEY10_VALUE							= const(0x00) # Default
_RF_AESKEY11_VALUE							= const(0x00) # Default
_RF_AESKEY12_VALUE							= const(0x00) # Default
_RF_AESKEY13_VALUE							= const(0x00) # Default
_RF_AESKEY14_VALUE							= const(0x00) # Default
_RF_AESKEY15_VALUE							= const(0x00) # Default
_RF_AESKEY16_VALUE							= const(0x00) # Default

# _Reg Temp 1
_RF_TEMP1_MEAS_START							= const(0x08)
_RF_TEMP1_MEAS_RUNNING						= const(0x04)
_RF_TEMP1_ADCLOWPOWER_ON						= const(0x01) # Default
_RF_TEMP1_ADCLOWPOWER_OFF					= const(0x00)

# _Reg Test Dagc								= const(0x6F : demodulator config and IO mode config)
_RF_DAGC_NORMAL								= const(0x00) # _Reset value
_RF_DAGC_IMPROVED_LOWBETA1					= const(0x20) #)
_RF_DAGC_IMPROVED_LOWBETA0					= const(0x30) # _Recommended default
# **********************************************************************************
# Wes Calvert, 2015
# This code ported from Felix _Rusu's original work:
# https://github.com/LowPowerLab/_RFM69
# **********************************************************************************
# License
# **********************************************************************************
# This program is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General    
# Public License as published by the Free Software       
# Foundation; either version 2 of the License, or        
# (at your option) any later version.                    
#                                                        
# This program is distributed in the hope that it will   
# be useful, but WITHOUT ANY WARRANTY; without even the  
# implied warranty of MERCHANTABILITY or FITNESS FOR A   
# PARTICULAR PURPOSE.  See the GNU General Public        
# License for more details.                              
#                                                        
# You should have received a copy of the GNU General    
# Public License along with this program; if not, write 
# to the Free Software Foundation, Inc.,                
# 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
#                                                        
# Licence can be viewed at                               
# http:#www.fsf.org/licenses/gpl.txt                    
#
# Please maintain this license information along with authorship
# and copyright notices in any redistribution of this code
# **********************************************************************************

from machine  import Pin, SPI
from base_radio import BaseRadio
import utime as time

# to take advantage of the built in AES/CRC we want to limit the frame size to 
# the internal FIFO size (66 bytes - 3 bytes overhead)
_RF69_MAX_DATA_LEN = 61 

# upper _RX signal sensitivity threshold in dBm for carrier sense access
CSMA_LIMIT      = -90 
_RF69_MODE_SLEEP     = 0 # XTAL OFF
_RF69_MODE_STANDBY       = 1 # XTAL ON
_RF69_MODE_SYNTH     = 2 # PLL ON
_RF69_MODE_RX        = 3 # _RX MODE
_RF69_MODE_TX        = 4 # TX MODE

#available frequency bands
RF69_315MHZ     = 31  
RF69_433MHZ     = 43
RF69_868MHZ     = 86
RF69_915MHZ     = 91

# puts the temperature reading in the ballpark, user can fine tune the returned value
COURSE_TEMP_COEF    = -90
_RF69_BROADCAST_ADDR = 255
_RF69_CSMA_LIMIT_MS  = 1000
_RF69_TX_LIMIT_MS    = 1000
_RF69_FSTEP      = 61.03515625 # == FXOSC/2^19 = 32mhz/2^19 (p13 in DS)

class RFM69(BaseRadio):
    DATA = []
    DATALEN = 0
    SENDERID = 0
    TARGETID = 0
    PAYLOADLEN = 0
    ACK_REQUESTED = False
    ACK_RECEIVED = False
    RSSI = 0
    _mode = 0
    _intPin = 2
    _csPin = 3
    _address = 0
    _promiscuousMode = False
    _powerLevel = 31
    _isRFM69HW = True
    _data_cb = lambda x: x
    
    def __init__(self, isRFM69HW=True, spiBus=0, intPin=2, csPin=3, rstPin=5, debug=False):
        self._isRFM69HW = isRFM69HW
        
        self.spi = SPI(1, baudrate=8000000, phase=0, polarity=0)
        # self.spi.init(baudrate=1000000, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

        self._intPin = Pin(intPin, Pin.IN)
        self._csPin = Pin(csPin, Pin.OUT)
        self._rstPin = Pin(rstPin, Pin.OUT)
        self.start_time = time.time()
        self._packetSentIrq = False # used to make sure we send end_of_transmit interrupt
        self._debug=debug
        self._tail = bytearray([0xFF, 0xFF, 0x00])
        self._plen = 66

    # Convention I want to stick to is a single underscore to indicate "private" methods.
    # I'm grouping all the private stuff up at the beginning.

    def _millis(self):
        delta = time.time() - self.start_time
        return delta * 1000

    def _readReg(self, addr):
        self._select()
        self.spi.write(bytearray([addr & 0x7F]))
        result = self.spi.read(1)[0]
        self._unselect()
        return result
    
    def _writeReg(self, addr, value):
        self._select()
        self.spi.write(bytearray([addr | 0x80, value]))
        #time.sleep(0.01)
        self._unselect()
        
        # Select the transceiver
    def _select(self):
        self._csPin.value(0)

    # Unselect the transceiver chip
    def _unselect(self): 
        self._csPin.value(1)

    def _setMode(self, newMode):
        if newMode == self._mode:
            return
        if newMode == _RF69_MODE_TX:
            self._writeReg(_REG_OPMODE, (self._readReg(_REG_OPMODE) & 0xE3) | _RF_OPMODE_TRANSMITTER)
            if self._isRFM69HW:
                self.setHighPowerRegs(True)
        elif newMode == _RF69_MODE_RX:
            self._writeReg(_REG_OPMODE, (self._readReg(_REG_OPMODE) & 0xE3) | _RF_OPMODE_RECEIVER)
            if self._isRFM69HW:
                self.setHighPowerRegs(False)
        elif newMode == _RF69_MODE_SYNTH:
            self._writeReg(_REG_OPMODE, (self._readReg(_REG_OPMODE) & 0xE3) | _RF_OPMODE_SYNTHESIZER)
        elif newMode == _RF69_MODE_STANDBY:
            self._writeReg(_REG_OPMODE, (self._readReg(_REG_OPMODE) & 0xE3) | _RF_OPMODE_STANDBY)
        elif newMode == _RF69_MODE_SLEEP:
            self._writeReg(_REG_OPMODE, (self._readReg(_REG_OPMODE) & 0xE3) | _RF_OPMODE_SLEEP)

        # we are using packet mode, so this check is not really needed
        # but waiting for mode ready is necessary when going from sleep because the FIFO may not 
        # be immediately available from previous mode

        # Wait for ModeReady
        while (self._mode == _RF69_MODE_SLEEP and (self._readReg(_REG_IRQFLAGS1) & _RF_IRQFLAGS1_MODEREADY) == 0x00): 
            pass
        self._mode = newMode

    def _canSend(self):
        if self._mode == _RF69_MODE_STANDBY:
            self._receiveBegin()
            return True
        #if signal stronger than -100dBm is detected assume channel activity
        #DNU - will ALWAYS return true on second call, no?
        if (self._mode == _RF69_MODE_RX and self.PAYLOADLEN == 0 and self.readRSSI() < CSMA_LIMIT): 
            self._setMode(_RF69_MODE_STANDBY)
            return True
        return False

    def _sendFrame(self, buffer, requestACK=True, sendACK=False):
        #turn off receiver to prevent reception while filling fifo
        self._setMode(_RF69_MODE_STANDBY) 
        while ((self._readReg(_REG_IRQFLAGS1) & _RF_IRQFLAGS1_MODEREADY) == 0x00):
            pass # Wait for ModeReady

        self._writeReg(_REG_DIOMAPPING1, _RF_DIOMAPPING1_DIO0_00) # DIO0 is "Packet Sent"
        self._writeReg(_REG_PACKETCONFIG1, _RF_PACKET1_FORMAT_VARIABLE | _RF_PACKET1_DCFREE_OFF | _RF_PACKET1_CRCAUTOCLEAR_ON | _RF_PACKET1_ADRSFILTERING_OFF)
        self._writeReg( _REG_PAYLOADLENGTH, 0)

        #self._writeReg(_REG_PAYLOADLENGTH, len(buffer) + len(self._tail))

        #write to FIFO
        self._select()
        self.spi.write(bytearray([_REG_FIFO | 0x80]))
        self.spi.write(buffer)
        self.spi.write(self._tail)
        self._unselect()

        # no need to wait for transmit mode to be ready since its handled by the radio
        self._packetSentIrq = False
        self._setMode(_RF69_MODE_TX)
        # wait for DIO0 to turn HIGH signalling transmission finish
        while (self._packetSentIrq == False and (self._readReg(_REG_IRQFLAGS2) & _RF_IRQFLAGS2_PACKETSENT == 0x00)):
            pass
        self._packetSentIrq == False

        self.listen()

    def _interruptHandler(self, pin):
        irqFlags1 = self._readReg(_REG_IRQFLAGS1)
        irqFlags2 = self._readReg(_REG_IRQFLAGS2)
        if self._debug:
            print(self._mode, _RF69_MODE_RX, irqFlags1, irqFlags2, _RF_IRQFLAGS2_PAYLOADREADY)
        if self._mode == _RF69_MODE_TX and (irqFlags2 & _RF_IRQFLAGS2_PACKETSENT !=0):
            self._packetSentIrq = True # let _sendFrame know transmit is done
            return
        if (self._mode == _RF69_MODE_RX and (irqFlags2 & _RF_IRQFLAGS2_PAYLOADREADY)):
            self._setMode(_RF69_MODE_STANDBY)
            self._select()
            self.spi.write(bytearray([_REG_FIFO & 0x7f]))
            self.DATA = self.spi.read(self._plen)
            self._got_data(self.DATA)
            self._unselect()
            self._setMode(_RF69_MODE_RX)
            self.RSSI = self.readRSSI()

    def _got_data(self, data):
        self._data_cb(data)

    def _noInterrupts(self):
        pass

    def _interrupts(self):
        pass

    def _receiveBegin(self):
        self.DATALEN = 0
        self.SENDERID = 0
        self.TARGETID = 0
        self.PAYLOADLEN = 0
        self.ACK_REQUESTED = 0
        self.ACK_RECEIVED = 0
        self.RSSI = 0
        if (self._readReg(_REG_IRQFLAGS2) & _RF_IRQFLAGS2_PAYLOADREADY):
            # avoid _RX deadlocks, but does this throw away an ack?
            self._writeReg(_REG_PACKETCONFIG2, (self._readReg(_REG_PACKETCONFIG2) & 0xFB) | _RF_PACKET2_RXRESTART)
        #set DIO0 to "PAYLOADREADY" in receive mode
        self._writeReg(_REG_DIOMAPPING1, _RF_DIOMAPPING1_DIO0_01) 
        self._setMode(_RF69_MODE_RX)

    def initialize(self):
        config = [
            [ _REG_OPMODE, _RF_OPMODE_SEQUENCER_ON | _RF_OPMODE_LISTEN_OFF | _RF_OPMODE_STANDBY ],
            [ _REG_DATAMODUL, _RF_DATAMODUL_DATAMODE_PACKET | _RF_DATAMODUL_MODULATIONTYPE_FSK | _RF_DATAMODUL_MODULATIONSHAPING_00 ], #no shaping
            [ _REG_BITRATEMSB, 0x06], # 32 MHz / bitrate
            [ _REG_BITRATELSB, 0x83],
            [ _REG_FDEVMSB, _RF_FDEVMSB_25000], #default:5khz, (FDEV + BitRate/2 <= 500Khz)
            [ _REG_FDEVLSB, _RF_FDEVLSB_25000],
            [ _REG_FRFMSB, 0xD9 ], # 868 400 000 / 61 Hz
            [ _REG_FRFMID, 0x1B ],
            [ _REG_FRFLSB, 0x14 ],
            
            # looks like PA1 and PA2 are not implemented on _RFM69W, hence the max output power is 13dBm
            # +17dBm and +20dBm are possible on _RFM69HW
            # +13dBm formula: Pout=-18+OutputPower (with PA0 or PA1**)
            # +17dBm formula: Pout=-14+OutputPower (with PA1 and PA2)**
            # +20dBm formula: Pout=-11+OutputPower (with PA1 and PA2)** and high power PA settings (section 3.3.7 in datasheet)
            #[ _REG_PALEVEL, _RF_PALEVEL_PA0_ON | _RF_PALEVEL_PA1_OFF | _RF_PALEVEL_PA2_OFF | _RF_PALEVEL_OUTPUTPOWER_11111],
            #[ _REG_OCP, _RF_OCP_ON | _RF_OCP_TRIM_95 ], #over current protection (default is 95mA)
            
            # _RXBW defaults are [ _REG_RXBW, _RF_RXBW_DCCFREQ_010 | _RF_RXBW_MANT_24 | _RF_RXBW_EXP_5] (_RxBw: 10.4khz)
            [ _REG_RXBW, _RF_RXBW_DCCFREQ_010 | _RF_RXBW_MANT_16 | _RF_RXBW_EXP_2 ], #(BitRate < 2 * _RxBw)
            # for BR-19200: #* 0x19 */ [ _REG_RXBW, _RF_RXBW_DCCFREQ_010 | _RF_RXBW_MANT_24 | _RF_RXBW_EXP_3 ],
            [ _REG_DIOMAPPING1, _RF_DIOMAPPING1_DIO0_01 ], #DIO0 is the only IRQ we're using
            [ _REG_RSSITHRESH, 220 ], #must be set to dBm = (-Sensitivity / 2) - default is 0xE4=228 so -114dBm
            [ _REG_PREAMBLEMSB, _RF_PREAMBLESIZE_MSB_VALUE ] ,
            [ _REG_PREAMBLELSB, 0 ], # default 3 preamble bytes 0xAAAAAA

            [ _REG_SYNCCONFIG, _RF_SYNC_ON | _RF_SYNC_FIFOFILL_AUTO | _RF_SYNC_SIZE_8 | _RF_SYNC_TOL_0 ],
            [ _REG_SYNCVALUE1, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE2, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE3, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE4, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE5, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE6, 0x99 ^ 0xFF ],
            [ _REG_SYNCVALUE7, 0x55 ^ 0xFF ],
            [ _REG_SYNCVALUE8, 0xAA ^ 0xFF ],
            #[ _REG_SYNCVALUE7, 0xAA ^ 0xFF ],
            #[ _REG_SYNCVALUE8, 0xA9 ^ 0xFF ],

            [ _REG_PACKETCONFIG1, _RF_PACKET1_FORMAT_VARIABLE | _RF_PACKET1_DCFREE_OFF | _RF_PACKET1_CRCAUTOCLEAR_ON | _RF_PACKET1_ADRSFILTERING_OFF ],
            # [ _REG_PACKETCONFIG1, _RF_PACKET1_FORMAT_FIXED | _RF_PACKET1_DCFREE_OFF | _RF_PACKET1_CRCAUTOCLEAR_ON | _RF_PACKET1_ADRSFILTERING_OFF ],
            # [ _REG_PAYLOADLENGTH, self._plen ],
            [ _REG_PAYLOADLENGTH, 0 ],


            [ _REG_FIFOTHRESH, _RF_FIFOTHRESH_TXSTART_FIFOTHRESH | _RF_FIFOTHRESH_VALUE ], #TX on FIFO not empty
            [ _REG_PACKETCONFIG2, _RF_PACKET2_RXRESTARTDELAY_1BIT | _RF_PACKET2_AUTORXRESTART_ON | _RF_PACKET2_AES_OFF ], #_RXRESTARTDELAY must match transmitter PA ramp-down time (bitrate dependent)
            #[ _REG_TESTDAGC, _RF_DAGC_CONTINUOUS ], # run DAGC continuously in _RX mode
            [ _REG_TESTDAGC, _RF_DAGC_IMPROVED_LOWBETA0 ], # run DAGC continuously in _RX mode, recommended default for AfcLowBetaOn=0
        ]

        self._rstPin.value(1)
        time.sleep(.1)
        self._rstPin.value(0)
        time.sleep(.1)

        self._readReg(_REG_IRQFLAGS1)

        while self._readReg(_REG_SYNCVALUE1) != 0xaa:
            self._writeReg(_REG_SYNCVALUE1, 0xaa)
            time.sleep(.1)

        while self._readReg(_REG_SYNCVALUE1) != 0x55:
            self._writeReg(_REG_SYNCVALUE1, 0x55)
        
        for chunk in config:
            self._writeReg(chunk[0], chunk[1])

        self.setEncryptionKey(None)
        self.setHighPower(self._isRFM69HW)
        self._setMode(_RF69_MODE_STANDBY)
        # wait for mode ready
        while (self._readReg(_REG_IRQFLAGS1) & _RF_IRQFLAGS1_MODEREADY) == 0x00:
            pass
        # init interrupt
        self._intPin.irq(trigger=Pin.IRQ_RISING, handler=self._interruptHandler)


    def sleep(self):
        self._setMode(_RF69_MODE_SLEEP)

    def setAddress(self, addr):
        self._address = addr
        self._writeReg(_REG_NODEADRS, self._address)

    # set output power: 0=min, 31=max
    # this results in a "weaker" transmitted signal, and directly results in a lower RSSI at the receiver
    def setPowerLevel(self, powerLevel):
        self._powerLevel = powerLevel
        self._writeReg(_REG_PALEVEL, (_readReg(_REG_PALEVEL) & 0xE0) | (self._powerLevel if self._powerLevel < 31 else 31))

    def send(self, buffer):
        self._writeReg(_REG_PACKETCONFIG2, (self._readReg(_REG_PACKETCONFIG2) & 0xFB) | _RF_PACKET2_RXRESTART) # avoid _RX deadlocks
        now = self._millis()
        while (not self._canSend() and self._millis()-now < _RF69_CSMA_LIMIT_MS):
            self.receiveDone()
        self._sendFrame(buffer)
    
    # Should be polled immediately after sending a packet with ACK request
    def ACKReceived(self, fromNodeID):
        if self.receiveDone():
            if ((self.SENDERID == fromNodeID or fromNodeID == _RF69_BROADCAST_ADDR)
                    and (self.ACK_RECEIVED != 0)):
                return True
        return False

    #check whether an ACK was requested in the last received packet (non-broadcasted packet)
    def ACKRequested(self):
        return (self.ACK_REQUESTED and (self.TARGETID != _RF69_BROADCAST_ADDR)) != 0

    # Should be called immediately after reception in case sender wants ACK
    def sendACK(self, buffer="", bufferSize=0):
        sender = self.SENDERID
        RSSI = self.RSSI #save payload received RSSI value
        self._writeReg(_REG_PACKETCONFIG2, (self._readReg(_REG_PACKETCONFIG2) & 0xFB) | _RF_PACKET2_RXRESTART) # avoid _RX deadlocks
        now = self._millis()
        while not self._canSend():
            self.receiveDone()
        self._sendFrame(sender, buffer, bufferSize, False, True)
        self.RSSI = RSSI #restore payload RSSI

    def listen(self):
        # self._setMode(_RF69_MODE_STANDBY) #enables interrupts>

        self._writeReg(_REG_PACKETCONFIG1, _RF_PACKET1_FORMAT_FIXED | _RF_PACKET1_DCFREE_OFF | _RF_PACKET1_CRCAUTOCLEAR_ON | _RF_PACKET1_ADRSFILTERING_OFF )
        self._writeReg(_REG_PAYLOADLENGTH, self._plen)

        self._receiveBegin()
    
    def receiveDone(self):
        if (self._mode == _RF69_MODE_RX  or self._mode == _RF69_MODE_STANDBY) and (self.PAYLOADLEN > 0):
            self._setMode(_RF69_MODE_STANDBY) #enables interrupts>
            return True
        if (self._readReg(_REG_IRQFLAGS1) & _RF_IRQFLAGS1_TIMEOUT) != 0:
            # https://github.com/russss/rfm69-python/blob/master/rfm69/rfm69.py#L112
            # _Russss figured out that if you leave alone long enough it times out
            # tell it to stop being silly and listen for more packets
            self._writeReg(_REG_PACKETCONFIG2, (self._readReg(_REG_PACKETCONFIG2) & 0xFB) | _RF_PACKET2_RXRESTART)
        elif self._mode == _RF69_MODE_RX:
            # already in _RX no payload yet
            return False
        self._receiveBegin()
        return False
    
    # To enable encryption: radio.encrypt("ABCDEFGHIJKLMNOP")
    # To disable encryption: radio.encrypt(null)
    # KEY HAS TO BE 16 bytes !!!
    def setEncryptionKey(self, key):
        if key is not None:
            if len(key) != 16:
                raise Exception("Key must be exactly 16 bytes!")
            self._setMode(_RF69_MODE_STANDBY)
            keyBytes = []
            self._select()
            self.spi.write(bytearray([_REG_AESKEY1 | 0x80]))
            for i in range(0,16):
                keyBytes.append(ord(key[i]))
                self.spi.write(keyBytes)
            self._unselect()
            self._writeReg(_REG_PACKETCONFIG2, (self._readReg(_REG_PACKETCONFIG2) & 0xFE) | (0 if key is None else 1))

    # The following methods are not required by BaseRadio.
    # They depend too heavily on the specific radio hardware and would not get any benefit from being part of the
    # BaseRadio class.
    
    def readRSSI(self, forceTrigger=False):
        rssi = 0
        if (forceTrigger):
            # RSSI trigger not needed if DAGC is in continuous mode
            self._writeReg(_REG_RSSICONFIG, _RF_RSSI_START)
            while ((self._readReg(_REG_RSSICONFIG) & _RF_RSSI_DONE) == 0x00):
                pass # Wait for _RSSI_Ready
        rssi = -self._readReg(_REG_RSSIVALUE)
        rssi >>= 1
        return rssi

    # ON  = disable filtering to capture all frames on network
    # OFF = enable node+broadcast filtering to capture only frames sent to this/broadcast address
    def setPromiscuous(self, onOff):
        self._promiscuousMode = onOff
        
    def setHighPower(self, onOff):
        self._isRFM69HW = onOff
        self._writeReg(_REG_OCP, _RF_OCP_OFF if self._isRFM69HW else _RF_OCP_ON)
        if (self._isRFM69HW):
            # enable P1 & P2 amplifier stages
            self._writeReg(_REG_PALEVEL, (self._readReg(_REG_PALEVEL) & 0x1F) | _RF_PALEVEL_PA1_ON | _RF_PALEVEL_PA2_ON) 
        else:
            # enable P0 only
            self._writeReg(_REG_PALEVEL, _RF_PALEVEL_PA0_ON | _RF_PALEVEL_PA1_OFF | _RF_PALEVEL_PA2_OFF | self.powerLevel) 

    def setHighPowerRegs(self, onOff):
        self._writeReg(_REG_TESTPA1, 0x5D if onOff else 0x55)
        self._writeReg(_REG_TESTPA2, 0x7C if onOff else 0x70)

    # returns centigrade
    def readTemperature(self, calFactor):  
        self._setMode(_RF69_MODE_STANDBY)
        self._writeReg(_REG_TEMP1, _RF_TEMP1_MEAS_START)
        while ((self._readReg(_REG_TEMP1) & _RF_TEMP1_MEAS_RUNNING)):
            pass
        #'complement'corrects the slope, rising temp = rising val
        # COURSE_TEMP_COEF puts reading in the ballpark, user can add additional correction
        return ~self._readReg(_REG_TEMP2) + COURSE_TEMP_COEF + calFactor 

    def rcCalibration(self):
        _writeReg(_REG_OSC1, _RF_OSC1_RCCAL_START)
        while ((_readReg(_REG_OSC1) & _RF_OSC1_RCCAL_DONE) == 0x00):
            pass



