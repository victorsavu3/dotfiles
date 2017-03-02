#!/bin/bash -e

cat $HOME/dotfiles/i3/i3.general $HOME/dotfiles/i3/i3.machine > $HOME/dotfiles/i3/config
cat $HOME/dotfiles/i3/i3pystatus/conf.head.py $HOME/dotfiles/i3/i3pystatus/conf.machine.py $HOME/dotfiles/i3/i3pystatus/conf.tail.py > $HOME/dotfiles/i3/i3pystatus/conf.py 
