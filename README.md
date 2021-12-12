# Silicium
![tests](https://github.com/SamimiesGames/Silicium/actions/workflows/tests.yaml/badge.svg)

Silicium is an ahead-of-time interpreted all-language compiler in Python3.

# Quick start.
Silicium uses Python3 as it's main language.
To get started using Silicium install the required dependencies for your system.

## Dependencies
To start with Silicium you need to make sure Python 3.6 is installed. 

Here are some one liners that you can use to set it all up.

### Linux

Debian based (Ubuntu, Kubuntu, KDE Neon):

`sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3.6 python3-pip`

RHEL Based (Redhat, Fedora, Cent-OS):

`sudo dnf upgrade && sudo dnf install python36`

Arch Based (Manjaro, Garuda, EndeavourOS):

For arch make sure you have the yay package manager installed.
If you do not you can do so with this line in bash:

`sudo pacman -S git && cd /opt && sudo git clone https://aur.archlinux.org/yay-git.git && sudo chown -R $(whoami):$(whoami) ./yay-git && cd yay-git && makepkg -si`

`sudo yay -Syu --devel --timeupdate && yay -S python36`

### Windows

For windows you can download python3.6 from [this link](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe)


## Installation

To download Silicium run `git clone https://github.com/SamimiesGames/silicium.git` in the folder you would like to keep it in.

# Silicium-Web is a progressive, declarative web technologies framework made in Python.

Silicium-Web is a progressive, declarative web technologies framework using Silicium as a base.

It is included in the Silicium package by default and to start using it just head into ./src inside the main silicium package.
The main.py is an example builder. You can either modify it to make it your own or you can create a new file and use the silicium\_web import.
