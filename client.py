#!/usr/bin/env python

import sys
from libs.QGAConnection import QGAConnection
from libs.Commands import *

if len(sys.argv) < 2 : exit(1)

socketFile = sys.argv[1]

conn = QGAConnection(socketFile)
CommandLine = Entry(conn)
CommandLine.do()

conn.close()
