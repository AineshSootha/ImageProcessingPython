'''Rotation Program'''
def rotation(img, n):
    try:
        #This function rotates the image given 4 different degrees: 0 (a mirror), 90, 180, 270
        im2=[]      #Creates an empty list that the new values can be sorted into
        if n==90:
            for i in range(0,len(img[0])):      #creates the width of the new image using the height of the original
                new_row=[]
                for j in range(0,len(img)):     #creates the height of the new image using the width of the original
                    new_row.append(img[-j-1][i])        #"rotates" the image by transcribing the i and j values of the image's matrix and adds it to a list
                        
                im2.append(new_row)
                    
            return im2
        elif n==0:
            for i in range(0,len(img)):
                new_row=[]
                for j in range(0,len(img[0])):      #Retains original height and width
                    new_row.append(img[i-1][-j-1])      #Appends list by flipping the original i and j locations
                        
                im2.append(new_row)
                    
            return im2
        elif n==180:
            for i in range(0,len(img)):
                new_row=[]
                for j in range(0,len(img[0])):      
                    new_row.append(img[-i][-j])     #Flips i and j values by making them negative
                        
                im2.append(new_row)
                    
            return im2
        elif n==270:
            for i in range(0,len(img[0])):
                new_row=[]
                for j in range(0,len(img)):
                    new_row.append(img[j][-i-1])        #is the opposite of a 90 degree rotation, where j is positive, and i is -i-1
                    
                im2.append(new_row)
                    
            return im2
    except:
        return False