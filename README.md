# Silicium

Silicium is an ahead-of-time interpreted all-language compiler in Python 3.

# Quick Start
1. Install `Python3.7+`
2. Run `git clone https://github.com/SamimiesGames/silicium.git`
3. Run `pip install -e .`

### Linux

Debian based (Ubuntu, Kubuntu, KDE Neon):
```
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3.7 python3-pip
```

RHEL Based (Redhat, Fedora, Cent-OS):
```
sudo dnf upgrade && sudo dnf install python37
```

Arch Based (Manjaro, Garuda, EndeavourOS):

For arch make sure you have the yay package manager installed.
If you do not you can do so with this line in bash:
```
sudo pacman -S git && cd /opt && sudo git clone https://aur.archlinux.org/yay-git.git && sudo chown -R $(whoami):$(whoami) ./yay-git && cd yay-git && makepkg -si
```

```
sudo yay -Syu --devel --timeupdate && yay -S python37
```

### Windows

For windows you can download python3.6 from [this link](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)
