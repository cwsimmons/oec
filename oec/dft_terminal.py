"""
DFT Terminal
"""

from enum import Enum, auto


class InterfaceStates(Enum):
    """Interface States"""
    DISCONNECTED = auto()
    CONNECTED_IDLE = auto()
    CONNECTED_ACTIVE = auto()


class TCAFields(Enum):
    """Terminal Control Area Fields"""

    # Device owned area.
    DPASTAT = (0x00, 0x01)  # Asynchronous status present flag
    DPSSTAT = (0x01, 0x01)  # Synchronous status present flag
    DSSV = (0x02, 0x01)     # Synchronous status value
    DSSP = (0x03, 0x01)     # Synchronous status paramenter 1
    DSSP2 = (0x04, 0x01)    # Synchronous status paramenter 2
    DSSP3 = (0x05, 0x01)    # Synchronous status paramenter 3
    DALTAD = (0x06, 0x01)   # Logical Terminal Address
    DAEV = (0x07, 0x01)     # Asyncronous status event value
    DAEP = (0x08, 0x01)     # Asyncronous status event parameter 1
    DAEP2 = (0x09, 0x01)    # Asyncronous status event parameter 2
    DAEP3 = (0x0a, 0x01)    # Asyncronous status event parameter 3
    DAEP4 = (0x0b, 0x01)    # Asyncronous status event parameter 4
    DTID1 = (0x0c, 0x01)    # Terminal ID
    DTID2 = (0x0d, 0x01)    # Product ID Qualifier
    DTID3 = (0x0e, 0x01)    # Reserved
    DTID4 = (0x0f, 0x01)    # Reserved
    DBUF = (0x10, 0x02)     # Device buffer size in bytes (Valid after POR)
    # Bytes 0x12..0x1f Reserved
    EXFLT = (0x20, 0x01)    # LT Address
    EXFRQ = (0x21, 0x01)    # Expedited Status value
    EXFP1 = (0x22, 0x01)    # Expedited Status paramenter 1
    EXFP2 = (0x23, 0x01)    # Expedited Status paramenter 2
    EXFP3 = (0x24, 0x01)    # Expedited Status paramenter 3
    EXFP4 = (0x25, 0x01)    # Expedited Status paramenter 4
    EXFAK = (0x26, 0x01)    # Post/Acknowledgement flag byte
    # Bytes 0x27..0x3f Reserved

    # Controller owned area.
    CUDP = (0x40, 0x02)     # Data address within the device buffer
    CULTAD = (0x42, 0x01)   # Logical Terminal Address
    CUFRV = (0x44, 0x01)    # Syncronous function request value
    CUSYN = (0x45, 0x01)    # Request synchronization switch (toggle)
    CUFRP1 = (0x46, 0x01)   # Synchronous Function Request Paramenter 1
    CUFRP2 = (0x47, 0x01)   # Synchronous Function Request Paramenter 2
    CUFRP3 = (0x48, 0x01)   # Synchronous Function Request Paramenter 3
    CUFRP4 = (0x49, 0x01)   # Synchronous Function Request Paramenter 4
    # Bytes 0x4a..0x4f Reserved
    CUDPORT = (0x50, 0x01)  # Device Port Number (0 - 31)
    CUAT = (0x51, 0x01)     # Control unit host attachment protocol
    CUDSER = (0x52, 0x02)   # Error code value for last-ditch-command-queue
    CULTA1 = (0x54, 0x01)   # LT Address 1
    CULTA2 = (0x55, 0x01)   # LT Address 2
    CULTA3 = (0x56, 0x01)   # LT Address 3
    CULTA4 = (0x57, 0x01)   # LT Address 4
    CULTA5 = (0x58, 0x01)   # LT Address 5
    # Bytes 0x59..0x5b Reserved
    EXFD1 = (0x5c, 0x01)    # Expedited Status Response paramenter 1 (if needed)
    EXFD2 = (0x5d, 0x01)    # Expedited Status Response paramenter 2 (if needed)
    EXFD3 = (0x5e, 0x01)    # Expedited Status Response paramenter 3 (if needed)
    EXFD4 = (0x5f, 0x01)    # Expedited Status Response paramenter 4 (if needed)
    EXTIME = (0x60, 0x01)   # Host transaction timing
    CUDSL = (0x61, 0x01)    # DSL Type
    # Bytes 0x62..0x7d Reserved
    CUSLVL = (0x7e, 0x02)   # Controller TCA Support Level
    CUDATA = (0x80, 0x01)   # Data Area

# 4.2 Synchronous Event Synchronization
# The CU prepares a function request by performing the following:
# * DPSSTAT is set to X'OO' to acknowledge Synchronous Status, or DPASTAT is
#   set to X'OO' to acknowledge Asynchronous Status.
# * The data address, if any, is written into CUDP.
# * The function request value is written into CUFRV.
# * The request synchronization flag at CUSYN is toggled.
# * Any associated parameters are written into CUFRPl-4.
# * The data, if any, is written in the CUDATA area pointed to by CUDP.
# * Expedited Status, EXTIME, may be updated.
