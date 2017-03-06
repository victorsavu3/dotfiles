#!/bin/bash -e

rm $HOME/.vimrc || true
rm $HOME/.screenrc || true
rm $HOME/.Xresources || true
rm -r $HOME/.config/i3 || true

ln -s $HOME/dotfiles/.vimrc $HOME/.vimrc
ln -s $HOME/dotfiles/.screenrc $HOME/.screenrc
ln -s $HOME/dotfiles/.Xresources $HOME/.Xresources
ln -s $HOME/dotfiles/i3 $HOME/.config/i3

xrdb $HOME/.Xresources
./i3/i3concat.sh
