from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    string to hex
    """
    toHex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])
    return (toHex(payload)) if payload else payload


