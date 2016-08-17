import os, random, datetime

# Define the location of files
loc = "/home/user/path/to/files/"

date = datetime.datetime.now()

# Fetch month and date as strings, concatenate, redefine as integer to compare against seasons
dateNum = int(str(date.month) + str(date.day))


# Check date against concatenated dates of seasons, rename season accordingly
if dateNum >= 1221 or dateNum < 320:	# Winter defined as between 12/21 and 3/20
	season = "winter/"
elif dateNum >= 922:			# Autumn defined as after 9/22
	season = "autumn/"
elif dateNum >= 621:			# Summer defined as after 6/21
	season = "summer/"
elif dateNum >= 320:			# Spring defined as after 3/20
	season = "spring/"

# Night friendly mode, with inclusions for seasonality in terms of snow
if date.hour >= 20 or date.hour <= 6:		# If it's between 8pm and 6am, consider it night
	if dateNum >= 1115 or dateNum <= 405:	# If it's between 11/15 and 4/05, choose from snowy night images
		season = "night/snow/"
	else:
		season = "night/nosnow/"
else:
	season = season


# Pick a random picture
pic = random.choice(os.listdir(loc + season))

# This works for ubuntu, will be testing in debian environments next
os.system("gsettings set org.gnome.desktop.background picture-uri file://" + loc + season + pic)
print("Changed to " +  pic)
