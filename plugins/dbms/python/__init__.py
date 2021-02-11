#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import DBMS
from lib.core.settings import MYSQL_SYSTEM_DBS
from lib.core.unescaper import unescaper
from plugins.dbms.python.enumeration import Enumeration
from plugins.dbms.python.filesystem import Filesystem
from plugins.dbms.python.fingerprint import Fingerprint
from plugins.dbms.python.syntax import Syntax
from plugins.dbms.python.takeover import Takeover
from plugins.generic.misc import Miscellaneous

class PYTHONMap(Syntax, Fingerprint, Enumeration, Filesystem, Miscellaneous, Takeover):
    """
    This class defines MySQL methods
    """

    def __init__(self):
        self.excludeDbsList = MYSQL_SYSTEM_DBS
        self.sysUdfs = {
            # UDF name: UDF return data-type
            "sys_exec": {"return": "int"},
            "sys_eval": {"return": "string"},
            "sys_bineval": {"return": "int"}
        }

        for cls in self.__class__.__bases__:
            cls.__init__(self)

    unescaper[DBMS.PYTHON] = Syntax.escape
