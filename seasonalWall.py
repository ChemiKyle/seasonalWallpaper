import os, random, datetime


loc = "/home/kyle/Pictures/Wallpapers/branches/"

date = datetime.datetime.now()

# fetch month and date as strings, concatenate, redefine as integer
dateNum = int(str(date.month) + str(date.day))


# Check date against concatenated dates of seasons, rename season accordingly
if dateNum >= 1221 or dateNum < 320:
	season = "winter/"
elif dateNum >= 922:
	season = "autumn/"
elif dateNum >= 621:
	season = "summer/"
elif dateNum >= 320:
	season = "spring/"

# Night friendly mode
if date.hour >= 20 or date.hour <= 6:
	if dateNum >= 1115 or dateNum <= 405:
		season = "night/snow/"
	else:
		season = "night/nosnow/"
else:
	season = season


# pick a random picture
pic = random.choice(os.listdir(loc + season))


os.system("gsettings set org.gnome.desktop.background picture-uri file://" + loc + season + pic)
print("Changed to " +  pic)
