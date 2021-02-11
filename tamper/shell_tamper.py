from lib.core.enums import PRIORITY

__priority__ = PRIORITY.HIGHEST

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Octal bash execution
    """

    return ('& bash -c "eval $\''+''.join(map(lambda c: ('\\'+str(oct(ord(c))[2:]) if (c != ' ') else '\' $\''), payload))+'\'"') if payload else payload


