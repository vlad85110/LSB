from lsb import decode_lsb

output_path = input("enter file to decode: ")
decoded_text = decode_lsb(output_path)
print(f"decoded string: {decoded_text}")