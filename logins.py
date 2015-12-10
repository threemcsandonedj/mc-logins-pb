import pushbullet
import time

log = "/home/minecraft/multicraft/servers/server7/logs/latest.log"

keyfile = open("/home/snowman/Projects/pb/pb.key")
key = keyfile.readline()
keyfile.close()

pb = pushbullet.Pushbullet(key.rstrip())
logfile = open(log)

while 1:
    where = logfile.tell()
    line = logfile.readline()
    if not line:
        time.sleep(1)
        logfile.seek(where)
    else:
        if "logged" in line:
            sline = line.split()
            pb.push_note("Minecraft Login", sline[3])
    
    if( time.ctime(time.time())[11:16] == "12:00"):
        logfile.close()
        logfile = open(log)

    if (time.ctime(time.time())[11:16] == "02:11"):
        logfile.close()
        logfile = open(log)

