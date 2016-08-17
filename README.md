# seasonalWallpaper
Python script to change wallpaper depending on the season, and time of day.
After searching for this I found a few overcomplicated plugins for doing something that was well within reach of an amateur python dev and far simpler.

Requires a master folder containing a subfolder of pictures for each season, and one for night with 2 subfolders for snowy and non-snowy pictures

As of initial commit interval is not defined within the script since I run it with bash commands (cd to folder containing script first)
while true; do python seasonalWallpaper.py; sleep <interval-in-seconds>; done
