import cv2
import numpy as np
from PIL import Image
import random
from matplotlib import pyplot as plt

# decoding text message

def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p

def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]

def decode_text():
    img_name = input("\nEnter Image name : ")
    image = cv2.imread(img_name)
    img=Image.open(img_name,'r')
    msg = find_data(image)
    print(msg)

# decoding image

def decode_image():
      
    # Encrypted image

    img = cv2.imread(input("Enter the name of encoded image:")) 
    width = img.shape[0]
    height = img.shape[1]
      
    # img1 and img2 are two blank images
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)
      
    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '08b')
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                  
                # Appending data to img1 and img2
                img1[i][j][l]= int(v2, 2)
                img2[i][j][l]= int(v3, 2)
      
    # These are two images produced from
    # the encrypted image
    cv2.imwrite('lebel.png', img1)
    cv2.imwrite('message.png', img2)
    cv2.imshow('Decoded cover image',img1)
    cv2.imshow('Decoded message image',img2)
    cv2.waitKey()
    print('Decoding Completed')

# main function
def stegnography_decoding():
    x = 1
    while x != 0:
        print('''\nChoose type of stegnography you want to decode
       1.Text Steganography
       2.Image Stegranography''')
        u_in = int(input("\n enter your choice:"))

        if u_in == 1:
            decode_text()
        elif u_in == 2:
            decode_image()
        else:
            print("Enter valid input")

        x = int(input("\nenter 1 for continue otherwise 0:"))

stegnography_decoding()