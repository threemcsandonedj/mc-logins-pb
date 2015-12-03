import pushbullet
import time

keyfile = open("/home/snowman/Projects/pb/pb.key")
key = keyfile.readline()
keyfile.close()

pb = pushbullet.Pushbullet(key.rstrip())
logfile = open("/home/minecraft/multicraft/servers/server7/logs/latest.log")

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
    
