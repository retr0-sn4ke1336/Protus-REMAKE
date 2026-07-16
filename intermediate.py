from modules.portscanner import Module1
from modules.dnslookup import Module2
from modules.subdomain_finder import Module3
import subprocess
import json
import os

def intermediateFile(args):
    while True:
        user_arguments = args
        if "scan" in user_arguments:
            proc = subprocess.run(["./modules/modules_parser", *user_arguments], capture_output=True, text=True)
            if proc.returncode != 0:
                print("Parser error:", proc.stderr.strip() or proc.stdout.strip())
                break
            try:
                with open("communication.json", "r") as f:
                    data = json.load(f)
            except Exception as ex:
                print("Error decoding JSON from parser: ", ex)
                break

            else:
                host = data.get("host")
                first_port = data.get("first_port")
                last_port = data.get("last_port")
                time = data.get("time", 0)
                if "show" not in data:
                    show = "all"
                else:
                    show = data.get("show")

                os.system('clear')
                Module1.run(host, first_port, last_port, time, show)
                subprocess.run("rm communication.json", text=True, shell=True)
                break

        elif "look" in user_arguments:
            proc = subprocess.run(["./modules/modules_parser", *user_arguments], capture_output=True, text=True)
            if proc.returncode != 0:
                print("Parser error:", proc.stderr.strip() or proc.stdout.strip())
                break
            try:
                with open("communication.json") as f:
                    data = json.load(f)
            except Exception as ex:
                print("Error decoding JSON from parser: ", ex)
                break

            else:
                domain = data.get("domain")

                DNSLookUp = Module2

                os.system("clear")
                DNSLookUp.run(domain)
                subprocess.run("rm communication.json", text=True, shell=True)
                break

        elif "find" in user_arguments:
            proc = subprocess.run(["./modules/modules_parser", *user_arguments], capture_output=True, text=True)
            if proc.returncode != 0:
                print("Parser error: ", proc.stderr.strip() or proc.stdout.strip())
                break
            try:
                with open("communication.json") as f:
                    data = json.load(f)
            except Exception as ex:
                print("Error decoding JSON from parser: ", ex)
                break

            else:
                domain = data.get("domain")
                speed = data.get("speed", 1)
                if speed not in {1, 2, 3, 4, 5}:
                    speed = 1

                os.system("clear")
                Module3.run(domain, speed)
                subprocess.run("rm communication.json", text=True, shell=True)
                break

        elif "list" in user_arguments or "protus" in user_arguments:
            result = subprocess.run(["./core/protus_parser", *user_arguments], capture_output=True, text=True)
            if result.returncode != 0:
                print("Parser error:", result.stderr.strip() or result.stdout.strip())
                break
            else:
                print(result.stdout, end="")
                break

        elif "-h" in user_arguments:
            help = subprocess.run(["./core/protus_parser", *user_arguments], capture_output=True, text=True)
            help2 = subprocess.run(["./modules/modules_parser", *user_arguments], capture_output=True, text=True)
            if help.returncode != 0 or help2.returncode != 0:
                print("Parser error: ", help.stderr.strip() or help.stdout.strip())
                print("Parser error: ", help2.stderr.strip() or help2.stdout.strip())
                break
            else:
                print(help.stdout)
                print(help2.stdout, end="")
                break