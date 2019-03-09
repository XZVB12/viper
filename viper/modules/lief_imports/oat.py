import sys
try:
    import lief
    HAVE_LIEF = True
except:
    HAVE_LIEF = False

if not HAVE_LIEF:
    self.log("error", "Missing dependency, install lief (pip3 install lief)")
    sys.exit(1)

OAT_HEADER_KEYS = {
    lief.OAT.HEADER_KEYS.BOOT_CLASS_PATH    :   "BOOT_CLASS_PATH",
    lief.OAT.HEADER_KEYS.CLASS_PATH         :   "CLASS_PATH",
    lief.OAT.HEADER_KEYS.COMPILER_FILTER    :   "COMPILER_FILTER",
    lief.OAT.HEADER_KEYS.CONCURRENT_COPYING :   "CONCURRENT_COPYING",
    lief.OAT.HEADER_KEYS.DEBUGGABLE         :   "DEBUGGABLE",
    lief.OAT.HEADER_KEYS.DEX2OAT_CMD_LINE   :   "DEX2OAT_CMD_LINE",
    lief.OAT.HEADER_KEYS.DEX2OAT_HOST       :   "DEX2OAT_HOST",
    lief.OAT.HEADER_KEYS.HAS_PATCH_INFO     :   "HAS_PATCH_INFO",
    lief.OAT.HEADER_KEYS.IMAGE_LOCATION     :   "IMAGE_LOCATION",
    lief.OAT.HEADER_KEYS.NATIVE_DEBUGGABLE  :   "NATIVE_DEBUGGABLE",
    lief.OAT.HEADER_KEYS.PIC                :   "PIC"
}

OAT_INSTRUCTION_SETS = {
    lief.OAT.INSTRUCTION_SETS.ARM       :   "ARM",
    lief.OAT.INSTRUCTION_SETS.ARM_64    :   "ARM_64",
    lief.OAT.INSTRUCTION_SETS.MIPS      :   "MIPS",
    lief.OAT.INSTRUCTION_SETS.MIPS_64   :   "MIPS_64",
    lief.OAT.INSTRUCTION_SETS.NONE      :   "NONE",
    lief.OAT.INSTRUCTION_SETS.THUMB2    :   "THUMB2",
    lief.OAT.INSTRUCTION_SETS.X86       :   "x86",
    lief.OAT.INSTRUCTION_SETS.X86_64    :   "x86_64"
}

OAT_BINARY_TYPES = {
    lief.ELF.ELF_CLASS.CLASS32  :   "CLASS32",
    lief.ELF.ELF_CLASS.CLASS64  :   "CLASS64",
    lief.ELF.ELF_CLASS.NONE     :   "NONE",
}
