from lsb import encode_lsb

image_path = input("enter input file name: ")
output_path = input("enter output file name: ")
data_to_hide = input("enter string to insert: ")

encode_lsb(image_path, data_to_hide, output_path)