#!/bin/bash

path="/home/$USER/Pictures/Wallpapers/seasons/"
concatDate="$(date +%m%d)"

if [ "$concatDate" -gt "1222" ] || [ "$concatDate" -lt "320" ]; then
	path="${path}winter/"
elif [ "$concatDate" -gt "921" ]; then
	path="${path}autumn/"
elif [ "$concatDate" -gt "620" ]; then
	path="${path}summer/"
elif [ "$concatDate" -gt "319" ]; then
	path="${path}spring/"
fi

gsettings set org.gnome.desktop.background picture-uri file://"$path"
