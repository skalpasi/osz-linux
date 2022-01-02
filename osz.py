import os
import sys
import subprocess as sp

if len(sys.argv)==1:
    print("Usage: python3 osz.py osu-beatmap.osz")
else:
    folder = sys.argv[1][0:len(sys.argv[1])-4];
    user = sp.getoutput('whoami')
    osu_dir = "\"/home/" + user + "/.local/share/osu-wine/OSU/Songs/" + folder + "\""
    query = "7za x -y \"" + sys.argv[1] + "\" -o" + osu_dir
    os.system(query)
    os.system("rm \"/home/" + user + "/" + sys.argv[1] + "\"")
