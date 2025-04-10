import numpy as np


def qualifier_do_8(inbyte1, inbyte2, short_circuit_actuator_trigger_as_bits, pinBased, portBased, complexBased):

    #output bytes.
    qualifier_di_8_byte1 = 0
    qualifier_di_8_byte2 = 0

    #Initialise half empty arrays to concatenate later with the short circuit bits.
    qualifier_bits_for_byte_1 = [0, 0, 0, 0]
    qualifier_bits_for_byte_2 = [0, 0, 0, 0]

    # The following section is to convert byte to bits....triggering the short circuit values.
    if  (0 <= inbyte1 and inbyte2 <= 255):

        if pinBased == True and portBased == False and complexBased == False:
            #Seperate even  bits to bits_for_byte1 and odd bits to bits_for_byte_2
            short_circuit_bits_for_byte1 = short_circuit_actuator_trigger_as_bits[::2]
            short_circuit_bits_for_byte2 = short_circuit_actuator_trigger_as_bits[1::2]

            #mapp input bytes from PLC to bits just upto the size of 4
            bits1 = [(inbyte1 >> i) & 1 for i in range(3, -1, -1)]
            bits2 = [(inbyte2 >> i) & 1 for i in range(3, -1, -1)]

            #Short_circuit_check with and opeartor and store them again as Qualifier bytes
            for i in range(4):
                if bits1[i] == short_circuit_bits_for_byte1[i]:
                    qualifier_bits_for_byte_1[i] = 0
                else:
                    qualifier_bits_for_byte_1[i] = 1

                if bits2[i] == short_circuit_bits_for_byte2[i]:
                    qualifier_bits_for_byte_2[i] = 0
                else:
                    qualifier_bits_for_byte_2[i] = 1
            #Concatinate with an empty array of size 4 to make it full array of 8 bits.
            qualifier_bits_for_byte_1 = np.concatenate((qualifier_bits_for_byte_1, [0, 0, 0, 0]))
            #Convert to final bytes
            for i, bit in enumerate(qualifier_bits_for_byte_1):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                qualifier_di_8_byte1 |= (bit << (7 - i))  # Shift the bit to its correct position

            qualifier_bits_for_byte_2 = np.concatenate((qualifier_bits_for_byte_2, [0, 0, 0, 0]))
            for i, bit in enumerate(qualifier_bits_for_byte_2):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                qualifier_di_8_byte2 |= (bit << (7 - i))  # Shift the bit to its correct position

        elif (pinBased == False and portBased == True and complexBased == False) or (pinBased == False and portBased == False and complexBased == True):

            bits1 = [(inbyte1 >> i) & 1 for i in range(7, -1, -1)]
            qualifier_bits_for_byte_1 = [0, 0, 0, 0, 0, 0, 0, 0]
            qualifier_bits_for_byte_2 = [0, 0, 0, 0, 0, 0, 0, 0]
            # Short_circuit_check with and opeartor and store them again as Qualifier bytes
            for i in range(8):
                if bits1[i] == short_circuit_actuator_trigger_as_bits[i]:
                    qualifier_bits_for_byte_1[i] = 0
                else:
                    qualifier_bits_for_byte_1[i] = 1

            for i, bit in enumerate(qualifier_bits_for_byte_1):
                if bit not in (0, 1):
                    raise ValueError("Each bit must be either 0 or 1.")
                qualifier_di_8_byte1 |= (bit << (7 - i))  # Shift the bit to its correct position

        else:
            raise ValueError("Two ore more values are set as True or none are set as True")
    else:
        raise ValueError("Input must be a single byte (0-255).")

    return qualifier_di_8_byte1, qualifier_di_8_byte2