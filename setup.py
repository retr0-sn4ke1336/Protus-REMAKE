import pathlib
import subprocess

def verify_distro():
    if "debian" in subprocess.run(f"grep '^ID=' /etc/os-release | cut -d= -f2") or "ubuntu" in subprocess.run(f"grep '^ID=' /etc/os-release | cut -d= -f2"):
        return "debian_based"
    
    if "fedora" in subprocess.run(f"grep '^ID=' /etc/os-release | cut -d= -f2"):
        return "fedora_based"

    if "arch" in subprocess.run(f"grep '^ID=' /etc/os-release | cut -d= -f2"):
        return "arch_based"

    else:
        return "unknown"
    

def setupProtus():
    binaries_list = ["gcc", "g++", "clang", "clang++"]
    for c in binaries_list:
        pathway = pathlib.Path("/usr/bin") / c
        if pathway.is_file():
            print("{} is already installed!".format(c.upper()))
        else:
            distro = verify_distro()
            if distro == "debian_based":
                subprocess.run(f"sudo apt install base-devel clang clang++ -y", text=True, shell=True)
            elif distro == "fedora_based":
                subprocess.run(f"sudo dnf install base-devel clang clang++ -y", text=True, shell=True)
            elif distro == "arch_based":
                subprocess.run(f"sudo pacman -S base-devel clang clang++ -y")
            else:
                print("Unknown distro detected!")         

    subprocess.run("pip install -r requirements.txt --break-system-packages && clang++ --std=c++20 modules/modules_parser.cpp -o modules/modules_parser && clang++ --std=c++20 core/protus_parser.cpp -o core/protus_parser", shell=True)  

setupProtus()
