import numpy as np


print('*' * 20)
alphabet = list(map(lambda i:i, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]}{|;:,.<>/?`~'* \\"))

length = len(alphabet)

_str = input("Enter a message to convert to binary: ")
binary_rep = []

for i in _str:
    if i in alphabet:
        binary_rep.append(bin(alphabet.index(i)))
    else:
        print("Invalid input, Try a gain")


# convert input to binary code.
def block_creator(binary_code):
    # padding
    binary_code = binary_code[2:]
    length = len(binary_code)
    for i in range(length, 11):
        binary_code = "0" + binary_code
    # End of padding
    places = [[0,3], [1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,0], [3,1], [3,2], [3,3]]
    block = np.zeros((4,4), np.int8)
    
    for index, value in enumerate(binary_code):
        row, column = places[index]
        block[row][column] = value
    if (np.count_nonzero(block[:,1]) + np.count_nonzero(block[:,3])) % 2:
        block[0][1] = 1

    if (np.count_nonzero(block[:,2]) + np.count_nonzero(block[:,3])) % 2:
        block[0][2] = 1

    if (np.count_nonzero(block[1]) + np.count_nonzero(block[3])) % 2:
        block[1][0] = 1

    if (np.count_nonzero(block[2]) + np.count_nonzero(block[3])) % 2:
        block[2][0] = 1

    if np.count_nonzero(block)%2:
        block[0][0] = 1

    return block


# convert binary to string
binary_str = ""
for i in range(len(binary_rep)):
    _list = block_creator(binary_rep[i]).flatten(order="F")
    _list = _list.tolist()
    binary_str += "".join([str(i) for i in _list])





print(binary_str)