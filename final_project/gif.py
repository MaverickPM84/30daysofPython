import imageio.v3 as iio

#In our Python program, we'll create a list that contains the locations of the image files. 
#We also need to create an empty list that will be used to store the actual image data from these files.


filenames = ['aditya-1.jpeg', 'aditya-2.jpeg', 'aditya-3.jpeg']

images = []

#for loop to go through the file paths and read the images using imageio library’s .imread() method:

for filename in filenames:
  images.append(iio.imread(filename))


#The .imread() method loads an image based on the file path. So now, our images variable has all the images!

# Lastly, let’s use the .imwrite() method to turn the images into a GIF:

iio.imwrite('spiderman.gif', images, duration = 500, loop = 0)


# This takes in four arguments:

# 'team.gif': This is the name you want to give to your new GIF file.
# images: The list containing the image data.
# duration = 500: How long each picture should show in the GIF, in milliseconds.
# loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).