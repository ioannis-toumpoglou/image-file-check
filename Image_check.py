try:
    with open('imag', 'rb') as bf:
        data = bf.read()
        numbers = list()
        
        for i in data[0:3]:
            hex_number = hex(i)
            int_number = int(hex_number,16)
            print(int_number, hex_number)
            numbers.append(int_number)

        print()
        if numbers[0] != 255 and numbers[1] != 216 and numbers[2] != 255:
            print('This is not a jpeg file')
        else:
            print('This is a jpeg file')
                
except FileNotFoundError:
    print('Error: File not found...')

except:
    print('Error processing the file...')
