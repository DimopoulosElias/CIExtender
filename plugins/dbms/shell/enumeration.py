#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""
from lib.core.common import getLimitRange
from lib.core.common import isAdminFromPrivileges
from lib.core.common import isInferenceAvailable
from lib.core.common import isNoneValue
from lib.core.common import isNumPosStrValue
from lib.core.common import isTechniqueAvailable
from lib.core.compat import xrange
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.data import queries
from lib.core.enums import CHARSET_TYPE
from lib.core.enums import DBMS
from lib.core.enums import EXPECTED
from lib.core.enums import PAYLOAD
from lib.core.exception import SqlmapNoneDataException
from lib.core.settings import CURRENT_USER
from lib.request import inject
from plugins.generic.enumeration import Enumeration as GenericEnumeration
from lib.core.common import unArrayizeValue

class Enumeration(GenericEnumeration):
    #pass
    def getRoles(self, query2=False):
        infoMsg = "fetching running user."
        logger.info(infoMsg)
        logger.info(conf.user)
        if conf.user:
          user = conf.user
        else:
          if not len(kb.data.cachedUsers):
            user = self.getCurrentUser()
          else:
            user = kb.data.cachedUsers

        infoMsg = "fetching running user's roles"
        logger.info(infoMsg)

        rootQuery = queries[DBMS.SHELL].roles
        query = rootQuery.inband.query
        values = unArrayizeValue(inject.getValue(query))
        kb.data.cachedUsersRoles[user] = list(map(str, values.split()))

        return kb.data.cachedUsersRoles
