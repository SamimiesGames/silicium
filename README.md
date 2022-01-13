# Silicium

Silicium is an ahead-of-time interpreted all-language compiler in Python 3.

# To Start

**`pip install silicium`**

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

Download python3.7 from [this link](https://www.python.org/ftp/python/3.7.0/)
