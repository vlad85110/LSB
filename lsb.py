from PIL import Image

def encode_lsb(image_path, data_to_hide, output_path):
    img = Image.open(image_path)

    binary_data = ''.join(format(ord(char), '08b') for char in data_to_hide)
    binary_data += '00000000'

    data_index = 0
    for i in range(img.width):
        for j in range(img.height):
            pixel = list(img.getpixel((i, j)))

            if data_index < len(binary_data):
                pixel[0] = pixel[0] & ~1 | int(binary_data[data_index])
                data_index += 1

            img.putpixel((i, j), tuple(pixel))

    img.save(output_path)

def decode_lsb(image_path):
    img = Image.open(image_path)

    binary_data = ''
    data_end = False

    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))

            binary_data += str(pixel[0] & 1)

            if binary_data[-8:] == '00000000':
                data_end = True
                break
        if data_end:
            break

    binary_data = binary_data[:-8]

    decoded_text = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))
    return decoded_text