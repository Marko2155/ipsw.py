import argparse
import urllib.request
import shutil
import json
import os
parser = argparse.ArgumentParser(prog="ipsw.py", description="Lets you download IPSWs from Python.")
parser.add_argument("--device", required=True)
parser.add_argument("--version", required=False)
args = parser.parse_args()
buildSpecified = False

def error(text):
    raise Exception(text)

if args.device == None:
    error("Device (example of format: iPad3,1) not specified.")
    exit(0)
else:
    if not os.path.exists("./temp"):
        os.mkdir("./temp")
        
    urllib.request.urlretrieve("https://api.ipsw.me/v4/device/" + args.device + "?type=ipsw", "./temp/temp.json")
    if not args.version:
        with open("./temp/temp.json", "r") as temp:
            j = json.loads(temp.read())
            fl = j["firmwares"]
            fl2 = fl[0]
            f = fl2["url"]
            print("Downloading iOS/iPadOS " + str(fl2["version"]) + " for iDevice " + str(args.device))
            urllib.request.urlretrieve(f, "./" + args.device + " - " + fl2["version"] + ".ipsw")
            print("Done")
    else:
        with open("./temp/temp.json", "r") as temp:
            j = json.loads(temp.read())
            fl = j["firmwares"]
            for flt in fl:
                if flt["version"] == args.version:
                    fl2 = flt
                    break
            f = fl2["url"]
            print("Downloading iOS/iPadOS " + str(fl2["version"]) + " for iDevice " + str(args.device))
            urllib.request.urlretrieve(f, "./" + args.device + " - " + fl2["version"] + ".ipsw")
            print("Done")
    shutil.rmtree("./temp")
