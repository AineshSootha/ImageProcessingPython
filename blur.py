import matplotlib as m
import numpy as n


#This function reads the image using matplotlib and stores it into a list of rows (Each row contains lists of RGB values)
#It requires the name of the image as a parameter
#It returns the image as a list of lists (matrix)
def read(name):
    img = m.image.imread(name)
    return n.ndarray.tolist(img)

#This function calculates the size of the image (HeightxWidth) or the shape of the image
#It requires the name of the image as a parameter
def size(name):
    img = m.image.imread(name)
    return img.shape


#This function saves the list (passed as parameter) as an image using matplotlib
#It requires the matrix (list of lists) and the name of image to be saved as parameters
def write(mat,name):
    img = n.asarray(mat,dtype=n.uint8)
    m.image.imsave(name, img, cmap = "Greys_r")


#This function displays the image using matplotlib
#It requires the matrix (list of lists) as the parameter
def show(mat):
    imgplot = m.pyplot.imshow(mat)
    m.pyplot.show()

#This function blurs the image by dividing all neighbouring pixels by 9 and adding them
#It requires the matrix as a parameter    
def blur(a):
    b=a
    for i in range(1,len(a)-1):
        for j in range(1,len(a[i])-1):
            b[i][j][0]=int(int(a[i-1][j-1][0])/9 + int(a[i-1][j][0])/9 + int(a[i-1][j+1][0])/9 + int(a[i][j-1][0])/9 + int(a[i][j][0])/9 + int(a[i][j+1][0])/9 + int(a[i+1][j-1][0])/9 + int(a[i+1][j][0])/9+ int(a[i+1][j+1][0])/9)
            b[i][j][1]=int(int(a[i-1][j-1][1])/9 + int(a[i-1][j][1])/9 + int(a[i-1][j+1][1])/9 + int(a[i][j-1][1])/9 + int(a[i][j][1])/9 + int(a[i][j+1][1])/9 + int(a[i+1][j-1][1])/9 + int(a[i+1][j][1])/9+ int(a[i+1][j+1][1])/9)
            b[i][j][2]=int(int(a[i-1][j-1][2])/9 + int(a[i-1][j][2])/9 + int(a[i-1][j+1][2])/9 + int(a[i][j-1][2])/9 + int(a[i][j][2])/9 + int(a[i][j+1][2])/9 + int(a[i+1][j-1][2])/9 + int(a[i+1][j][2])/9+ int(a[i+1][j+1][2])/9)
            if(b[i][j][0]>255):
                b[i][j][0]=255
            if(b[i][j][1]>255):
                b[i][j][1]=255
            if(b[i][j][2]>255):
                b[i][j][2]=255
            
            
    return b

