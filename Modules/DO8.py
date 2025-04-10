import numpy as np

def digital_outputs(byte1, byte2, pinBased, portBased, complexBased):
    # final bits
    bits = []

    # The following section is to convert byte to bits....triggering the actuator values.
    if  (0 <= byte1 and byte2 <= 255):

        if pinBased == True and portBased == False and complexBased == False:
            bits1 = [(byte1 >> i) & 1 for i in range(3, -1, -1)]
            bits2 = [(byte2 >> i) & 1 for i in range(3, -1, -1)]

            #reverse bits (See Handbook for bits mapping)
            bits1 = bits1[::-1]
            bits2 = bits2[::-1]
            bits = np.concatenate((bits1, bits2))
            #Rearrange bis according to mapping in  Handbook
            bits[0], bits[1], bits[2], bits[3], bits[4], bits[5], bits[6], bits[7] = bits[0], bits[2], bits[4], bits[6], \
            bits[1], bits[3], bits[5], bits[7]

        elif pinBased ==False and portBased == True and complexBased ==False:
            bits = [(byte1 >> i) & 1 for i in range(7, -1, -1)]
            #reverse bits to allign with the bits mapping in handbook
            bits = bits[::-1]

        elif pinBased == False and portBased ==False and complexBased == True:
            bits = [(byte1 >> i) & 1 for i in range(7, -1, -1)]
            # reverse bits to allign with the bits mapping in handbook
            bits = bits[::-1]

        else:
            raise ValueError("Two or more output mapping are selected or noone is selected")

    else:
        raise ValueError("Input must be a single byte (0-255).")
            # Extract each bit using bitwise operations
        #bits = [(byte1 >> i) & 1 for i in range(7, -1, -1)]



    return bits