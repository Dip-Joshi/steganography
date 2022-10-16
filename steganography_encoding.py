import cv2
import numpy as np
from PIL import Image
import random
from matplotlib import pyplot as plt

# it convert data in binary format

def data2binary_text(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p

# hide data in given img

def hidedata_text(img, data):
    data += "$$"  # '$$'--> secrete key
    d_index = 0
    b_data = data2binary_text(data)
    len_data = len(b_data)

    # iterate pixels from image and update pixel values
    for value in img:
        for pix in value:
            r, g, b = data2binary_text(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img

# encoding text

def encode_text():
    img_name = input("\nenter image name:")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input("\nenter message:")

    if len(data) == 0:
        raise ValueError("Empty data")
    enc_img = input("\nenter encoded image name:")
    enc_data = hidedata_text(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h), Image.ANTIALIAS)

    # optimize with 65% quality
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)

# encoding image

def encode_image():

    # img1 and img2 are the
    # two input images
    image1 = input("\nenter name of cover image:")
    img1 = cv2.imread(image1)
    image2 = input("\nenter name of message image:")
    img2 = cv2.imread(image2)

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for l in range(3):

                # v1 and v2 are 8-bit pixel values
                # of img1 and img2 respectively
                v1 = format(img1[i][j][l], '08b')
                v2 = format(img2[i][j][l], '08b')

                # Taking 4 MSBs of each image
                v3 = v1[:4] + v2[:4]

                img1[i][j][l] = int(v3, 2)

    enc = input("\nenter name of encoded image:")
    cv2.imwrite(enc, img1)
    cv2.imshow("encoded_image", img1)
    cv2.waitKey()
    # cv2.destroyAllWindows()
    print('Encoding Completed')

# main function
def stegnography_encoding():
    x = 1
    while x != 0:
        print('''\nChoose type of stegnography
       1.Text Steganography
       2.Image Stegranography''')
        u_in = int(input("\n enter your choice:"))

        if u_in == 1:
            encode_text()
        elif u_in == 2:
            encode_image()
        else:
            print("Enter valid input")

        x = int(input("\nenter 1 for continue otherwise 0:"))

stegnography_encoding()