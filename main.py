import blur, grayscale, rotation
from os import path

def error():
    print("We ran into an unkown error. Please Try again")

def main():
    #Take the user input for file name and store it in file_name
    file_name = input("Enter the name of the file: ")
    if not (path.exists(file_name)):
        print ("File not found")
        main()
        #sootha.read() reads the given file name (image) and returns a list of rows of pixels (Each pixel has RGB values)
        #img stores the list of rows of RGB values
    else:
        img = sootha.read(file_name)
    file_out_name = "ppppppppppppp"
    while file_out_name[-3] != "j":
        file_out_name = input("Enter the name of the output save file (with .jpg extension):  ")

    user=0
    while(user != '1' and user!= '2' and user!= '3' and user != '4'):
        user = input("What would you like to do? Type 1 for greyscale, 2 for rotation, 3 for Blur Filter, and 4 to exit:    ")
        if(user != '1' and user!='2' and user!= '3' and user !='4'):
            print("PLEASE CHOOSE FROM 1,2 or 3!\n")
        if(user=='1'):
            grey = virani.greyscale1(img)
            if not (grey):
                error()
                break
            sootha.write(grey,file_out_name)
            sootha.show(grey)
        elif(user=='2'):
            rot=0
            while(rot!='90' and rot!='180' and rot!='270'):
                rot=input("What angle would you like to rotate the image by? (90, 180, 270, 0): ")
                #The angle '0' returns a mirrored image
                rot_img = breslin.rotation(img,int(rot))
                if not (rot_img):
                    error()
                    break
                sootha.write(rot_img, file_out_name)
                sootha.show(rot_img)
        elif(user=='3'):    
            blur_img=sootha.blur(img)
            if not (blur_img):
                    error()
                    break
            sootha.show(blur_img)
            sootha.write(blur_img,file_out_name)
        elif (user == '4'):
            break

if __name__ == "__main__":
    main()