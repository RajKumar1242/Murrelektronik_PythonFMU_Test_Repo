import numpy as np

def System_State(qualifier_di_byte1, qualifier_di_byte2, qualifier_do_byte1, qualifier_do_byte2, no_actuator_supply, actuator_warning, sensor_voltage, actuator_voltage ):

    # 4 System state bytes

    #Byte1 bits
    #bit0 = Sensor undervoltage
    ss_byte1_bit0 = 0
    #bit1 = Actuator undervoltage
    ss_byte1_bit1 = 0
    #bit2 = No actuator supply
    ss_byte1_bit2 = 0
    #bit3 = Reserved
    ss_byte1_bit3 = 0
    #bit4 = Sensor short circuit on at least one channel
    ss_byte1_bit4 = 0
    #bit5 = Actuator short circuit on at least one channel
    ss_byte1_bit5 = 0
    #bit6 = Actuator warning on at least one channel
    ss_byte1_bit6 = 0
    #bit7 = Reserved
    ss_byte1_bit7 = 0

    # Byte2 bits
    # bit0 = Internal communication error
    ss_byte2_bit0 = 0
    # bit1 = Reserved
    ss_byte2_bit1 = 0
    # bit2 = Sensor overvoltage
    ss_byte2_bit2 = 0
    # bit3 = Actuator overvoltage
    ss_byte2_bit3 = 0
    # bit4 = Reserved
    ss_byte2_bit4 = 0
    # bit5 = Reserved
    ss_byte2_bit5 = 0
    # bit6 = Reserved
    ss_byte2_bit6 = 0
    # bit7 = Reserved
    ss_byte2_bit7 = 0

    #The remaining bits in system state are Reserved.

    system_state_byte1 = 0
    ss_byte_1_bits = [ss_byte1_bit7, ss_byte1_bit6, ss_byte1_bit5, ss_byte1_bit4, ss_byte1_bit3, ss_byte1_bit2,
                      ss_byte1_bit1, ss_byte1_bit0]
    system_state_byte2 = 0
    ss_byte_2_bits = [ss_byte2_bit7, ss_byte2_bit6, ss_byte2_bit5, ss_byte2_bit4, ss_byte2_bit3, ss_byte2_bit2,
                      ss_byte2_bit1, ss_byte2_bit0]
    system_state_byte3 = 0
    system_state_byte4 = 0

    #Structure bits for System State byte 1
    #ss_byte1_bit0, ss_byte2_bit2 sensor over or under voltage building
    if sensor_voltage <= 23.5:
        ss_byte1_bit0 = 1
    elif sensor_voltage >= 24.5:
        ss_byte2_bit2 = 1
    else:
        ss_byte2_bit2 = 0
        ss_byte1_bit0 = 0

    #ss_byte1_bit1, ss_byte2_bit3 actuator over or under voltage building
    if actuator_voltage <= 23.5:
        ss_byte1_bit1 = 1
    elif actuator_voltage >= 24.5:
        ss_byte2_bit3 = 1
    else:
        ss_byte2_bit3 = 0
        ss_byte1_bit1 = 0

    #

    return True