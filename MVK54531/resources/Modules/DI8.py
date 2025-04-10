import numpy as np


def digital_inputs(bits, pinBased, portBased, complexBased):

    # This folowing section is to convert bits to bytes...i.e sensor values to a bit..
    if len(bits) == 8:

        # Combine the bits into a single byte using bitwise operations
        byte1 = 0
        byte2 = 0
        if pinBased == True and portBased == False and complexBased ==False:
            dummyarray = [0,0,0,0]
            #Concatinate and reverse arrays
            bitsforbyte1 =  np.concatenate((bits[::2],dummyarray))[::-1]
            bitsforbyte2 = np.concatenate((bits[1::2],dummyarray,))[::-1]

            for i, bit in enumerate(bitsforbyte1):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                byte1 |= (bit << (7 - i))  # Shift the bit to its correct position

            for i, bit in enumerate(bitsforbyte2):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                byte2 |= (bit << (7 - i))  # Shift the bit to its correct position

        elif pinBased == False and portBased == True and complexBased == False:
            #reverse array first(See: Handbook for the bit arrangement in the array)
            bits = bits[::-1]
            #Shuffle positions of values in array(bits) (shuffle int: X4_2, X4_4, X5_2, X5_4, X6_2, X6_4, X7_2, X7_4)
            bits[0], bits[1],bits[2],bits[3],bits[4],bits[5],bits[6],bits[7] = bits[1], bits[0],bits[3],bits[2],bits[5],bits[4],bits[7],bits[6]
            for j, bit in enumerate(bits):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                byte2 |= (bit << (7 - j))  # Shift the bit to its correct position

        elif pinBased == False and portBased == False and complexBased == True:
            # reverse array first(See: Handbook for the bit arrangement in the array)
            bits = bits[::-1]
            # Shuffle positions of values in array(bits) (shuffle int: X4_2, X4_4, X5_2, X5_4, X6_2, X6_4, X7_2, X7_4)
            bits[0], bits[1], bits[2], bits[3], bits[4], bits[5], bits[6], bits[7] = bits[1], bits[0], bits[3], bits[2], \
            bits[5], bits[4], bits[7], bits[6]

            for k, bit in enumerate(bits):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                byte1 |= (bit << (7 - k))  # Shift the bit to its correct position

        else:
            raise ValueError("Two or more types of IO mappings are selected or none are selected")

    else:
        raise ValueError("Input must be a list of exactly 8 bits (0s and 1s).")

    bytes = np.array([byte1,byte2])

    return bytes