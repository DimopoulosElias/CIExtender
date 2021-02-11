#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.enums import DBMS
from lib.core.settings import MYSQL_SYSTEM_DBS
from lib.core.unescaper import unescaper
from plugins.dbms.php.enumeration import Enumeration
from plugins.dbms.php.filesystem import Filesystem
from plugins.dbms.php.fingerprint import Fingerprint
from plugins.dbms.php.syntax import Syntax
from plugins.dbms.php.takeover import Takeover
from plugins.generic.misc import Miscellaneous

class PHPMap(Syntax, Fingerprint, Enumeration, Filesystem, Miscellaneous, Takeover):
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

    unescaper[DBMS.PHP] = Syntax.escape
