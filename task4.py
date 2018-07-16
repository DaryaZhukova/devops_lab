from configparser import ConfigParser
from datetime import datetime
import psutil
import time


class Snapshot(object):
    "Class that operates snapshots"
    snapshot_count = 1

    def __init__(self, logtype, interval, sysdata):
        self.logtype = logtype
        self.interval = interval
        self.sysdata = self.getdict(Snapshot.snapshot_count)

    def getdict(self, i):
        "This get system information"
        d = datetime.now(tz=None)
        cpu = psutil.cpu_percent(interval=1)
        self.sysdata = {"SNAPSHOT {1}: {0} CPU load is, %: ".format(d, i): cpu}
        mem = round(psutil.virtual_memory()[3] / (1024.0 ** 2), 1)
        self.sysdata["SNAPSHOT {1}: {0} Mem usage is, %: ".format(d, i)] = mem
        vmem = round(psutil.virtual_memory()[1] / (1024.0 ** 2), 1)
        self.sysdata["SNAPSHOT {1}: {0} Virt mem is, %: ".format(d, i)] = vmem
        IO = round(psutil.disk_usage('/')[1] / (1024.0 ** 3), 1)
        self.sysdata["SNAPSHOT {1}: {0} IO used is, Gb: ".format(d, i)] = IO
        sent = psutil.net_io_counters()[0]
        self.sysdata["SNAPSHOT {1}: {0} Byte sent: ".format(d, i)] = sent
        rec = psutil.net_io_counters()[1]
        self.sysdata["SNAPSHOT {1}: {0} Byte received: ".format(d, i)] = rec
        return (self.sysdata)

    def __str__(self):
        listdata = []
        for k, v in self.sysdata.items():
            listdata.extend([k, v])
        return ("{} {}\n" * 6).format(*listdata)

    def writetxt(self, f):
        with open(f, 'a') as file:
            file.write(str(system_snapshot))

    def writejson(self, f):
        with open(f, 'a') as file:
            file.write(system_snapshot.sysdata)
            file.write("\n")


parser = ConfigParser()
parser.read("simple1.ini")
logtype = parser.get("common", "output")
interval = parser.get("common", "interval")
system_snapshot = Snapshot(logtype, interval, {})
print("System data will be collected %s times" % parser.get("common", "times"))
for n in range(int(parser.get("common", "times"))):
    if system_snapshot.logtype == "txt":
        print(system_snapshot)
        system_snapshot.writetxt("output.txt")
    elif system_snapshot.logtype == "json":
        print(system_snapshot)
        system_snapshot.writejson("output.json")
    else:
        print("Incorrect output format in simple.ini")
    Snapshot.snapshot_count += 1
    system_snapshot.getdict(Snapshot.snapshot_count)
    time.sleep(60 * int(system_snapshot.interval))
else:
    print("task finished please rerun")
