import psutil
from datetime import datetime
from configparser import ConfigParser
import json
import os.path


def getsnapshot(f):
    "This changes shapshot number"
    with open(f, 'r') as file:
        lines = file.read().splitlines()
        last_line = lines[-1]
        return(last_line.split("_")[1])


def getdict(i):
    "This get system information"
    d = datetime.now(tz=None)
    cpu = psutil.cpu_percent(interval=1)
    jsondict = {"SNAPSHOT _{1}_: {0} CPU load is, %: ".format(d, i): cpu}
    mem = round(psutil.virtual_memory()[3] / (1024.0 ** 2), 1)
    jsondict["SNAPSHOT _{1}_: {0} Mem usage is, %: ".format(d, i)] = mem
    vmem = round(psutil.virtual_memory()[1] / (1024.0 ** 2), 1)
    jsondict["SNAPSHOT _{1}_: {0} Virt mem usage is, %: ".format(d, i)] = vmem
    IO = round(psutil.disk_usage('/')[1] / (1024.0 ** 3), 1)
    jsondict["SNAPSHOT _{1}_: {0} IO used is, Gb: ".format(d, i)] = IO
    sent = psutil.net_io_counters()[0]
    jsondict["SNAPSHOT _{1}_: {0} Byte sent: ".format(d, i)] = sent
    recieved = psutil.net_io_counters()[1]
    jsondict["SNAPSHOT _{1}_: {0} Byte received: ".format(d, i)] = recieved
    return(jsondict)


parser = ConfigParser()
parser.read('simple.ini')
output = parser.get("common", "output")
if output == "txt":
    if os.path.exists("output.txt"):
        snapshot = int(getsnapshot("output.txt")) + 1
    else:
        snapshot = 1
    jsondict = getdict(snapshot)
    with open('output.txt', 'a') as file:
        for item in jsondict:
            file.write(str(item) + str(jsondict[item]) + "\n")
elif output == "json":
    if os.path.exists("output.json"):
        snapshot = int(getsnapshot("output.txt")) + 1
    else:
        snapshot = 1
    jsondict = getdict(snapshot)
    json = json.dumps(jsondict)
    f = open("output.json", "a")
    f.write(json)
    f.write("\n")
    f.close()
else:
    print("Incorrect output format in simple.ini")
