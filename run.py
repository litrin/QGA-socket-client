import os

from libs.Service import LongPollingService
from libs.Configuration import Configuration
import gevent


CFG = Configuration("etc/qga_agent.conf")

def getAllQGA():
    socketPath = CFG.getOption("qga", "path")
    socket = set()

    for filename in os.listdir(socketPath):
        socket.add(os.path.join(socketPath , filename))

    return socket

def buildWorker(indication, hostname, filename):
    obj =  eval(indication)
    return obj(hostname,filename)

def getLogger():
    type = CFG.getOption("qga", "logger")
    cls = "from Dispatcher.%s import Collection" % type
    exec (cls)

    handle = Collection(CFG.getSection(type))
    return handle

def setJob(service, hostname, files):
    for filename in files:
        for indication in CFG.getOption("qga", "indexes").split(","):
            if (len(indication) == 0) : continue
            worker = buildWorker(indication, hostname, filename)
            service.add(worker)

def main():
    fetch_interval = float(CFG.getOption("qga", "fetch_interval"))
    hostname = CFG.getOption("qga", "hostname")

    service = LongPollingService(fetch_interval)

    loggerHandle = getLogger()

    service.setLogger(loggerHandle)
    fileList = orignal = getAllQGA()
    setJob(service, hostname, fileList)

    service.start()
    checkSockeInterval = int(CFG.getOption('qga', 'check_socket_interval'))

    while True:
        #new sockets checker, if added 1 newer, push to Q
        gevent.sleep(checkSockeInterval)
        fileList = getAllQGA()
        if fileList != orignal:
            setJob(service, hostname, fileList - orignal)
            orignal = fileList

    service.join()

if __name__ == '__main__':
    main()