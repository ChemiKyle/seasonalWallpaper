import os, random, datetime


loc = "/path/to/directories/"

date = datetime.datetime.now()

month = str(date.month)
day = str(date.day)

# precede the date with a 0 if it's before the 10th; otherwise the first 9 days of every month are winter!
if int(day) <= 9:
	day = "0" + day

# fetch month and date as strings, concatenate, redefine as integer
dateNum = int(month + day)
print(str(date.day))

# Check date against concatenated dates of seasons, rename season accordingly
if dateNum >= 1221 or dateNum < 320:
	season = "winter/"
elif dateNum >= 922:
	season = "autumn/"
elif dateNum >= 621:
	season = "summer/"
elif dateNum >= 320:
	season = "spring/"

# night friendly mode
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
