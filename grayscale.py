import math

#This function returns the square root of sums of squares of a list of 3 integers(r,g and b)
#This converts an RGB pixel to a greyscale pixel
def mag(rgb):
    #This statement creates a variable mag2
    mag2 = 0
    for i in range(0,len(rgb)):
        #The R, G and B values are squared and added to mag2 (which is initially 0)
        mag2+=rgb[i]**2
    #Return the square root of mag2
    return math.sqrt(mag2)


#This function is used to convert the color image to a greyscale image.
#It requires a list of lists(matrix) as an argument
def greyscale1(img): #img is a matrix of (r,g,b) tuples
    #This statement creates img2, a copy of the img matrix
    img2 = img
    for i in range(0,len(img2)):
        for j in range(0,len(img2[i])):
            #This statement calls the mag() function which returns the distance formula of a list of 3 integers,
            #which effectively converts the RGB to greyscale.
            greyval = mag(img2[i][j])
            #This statement changes the pixel at the positions i,j in img2 to greyscale 
            img2[i][j] = [int(greyval),int(greyval),int(greyval)]
    #Return the new matrix(img2)
    return img2


'''
These are other algorithms for greyscale that are not currently being used.

def mag2(rgb):
    mag2 = 0
    for i in range(0,len(rgb)):
        mag2+=rgb[i]
        
    return mag2/3

def greyscale2(img): #img is a matrix of (r,g,b) tuples
    img2 = img
    for i in range(0,len(img2)):
        for j in range(0,len(img2[i])):
            greyval = mag2(img2[i][j])
            img2[i][j] = int(greyval)
    return img2

def greyscale3(img):
    img2 = img
    for i in range(0,len(img2)):
        for j in range(0,len(img2[i])):
            img2[i][j] = [img[i][j][0]*0.3,img[i][j][1]*0.59,img[i][j][2]*0.11]
    return img2

'''
