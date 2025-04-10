import sys

import math
#sys.path.append("D:\\2025\\pythonMVKProject\\")

import numpy as np


from pythonfmu import Fmi2Slave, Real, Fmi2Causality, Fmi2Variability, Integer, Boolean
from pythonfmu3 import Fmi3Causality, Fmi3Slave, Float64, Int32, Boolean, Fmi3Variability



class TestMVKFMU2(Fmi2Slave):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Parameters Pin, port, ComplexBased IOs
        #self.PinBased = True
        #self.PortBased = False
        #self.ComplexBased = False
        #self.IOLayout = {self.PinBased, self.PortBased, self.ComplexBased}


        self.LED_Off = 0.0
        self.LED_Red = 0.0
        self.LED_Green = 0.0
        self.Sensor_Voltage = 24.0
       # self.Actuator_Voltage = 24.0
        self.author = "Raj Kumar"
        self.description = "A simple description of DIO 8 module from Murrelektronik catalogue"

        self.time = 0.0


       # self.outByte1 = 10
       # self.outByte2 = 10
       # self.inByte1 = 10
       # self.inByte2 = 10
       # self.qualifier_di_8_byte1 = 0
       # self.qualifier_di_8_byte2 = 0
       # self.qualifier_do_8_byte1 = 0
       # self.qualifier_do_8_byte2 = 0

        #Variables for sensor inputs...


        #Variables for actuator variables..


        self.register_variable(Real("time", causality=Fmi2Causality.local))
        self.register_variable(Real("Sensor_Voltage", causality=Fmi2Causality.input, start = 24.0))
        #self.register_variable(Real("Actuator_Voltage", causality=Fmi2Causality.input, start = 24.0))

        #Parameter Declerations
       # self.register_variable(Boolean("PinBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable, description= "Pin based mapping of inputs"))
       # self.register_variable(Boolean("PortBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable))
       # self.register_variable(Boolean("ComplexBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable))





        self.register_variable(Real("LED_Green", causality=Fmi2Causality.output))
        self.register_variable(Real("LED_Red", causality=Fmi2Causality.output))
        self.register_variable(Real("LED_Off", causality=Fmi2Causality.output ))
       # self.register_variable(Int32("outByte1", causality=Fmi3Causality.output))
       # self.register_variable(Int32("outByte2", causality=Fmi3Causality.output))
       # self.register_variable(Int32("qualifier_di_8_byte1", causality=Fmi3Causality.output))
       # self.register_variable(Int32("qualifier_di_8_byte2", causality=Fmi3Causality.output))
       # self.register_variable(Int32("qualifier_do_8_byte1", causality=Fmi3Causality.output))
       # self.register_variable(Int32("qualifier_do_8_byte2", causality=Fmi3Causality.output))


        #self.register_variable(Integer("inByte1", causality=Fmi3Causality.input))
        #self.register_variable(Integer("inByte2", causality=Fmi3Causality.input))


    def do_step(self, current_time, step_size):

        self.LED_Green = 0.0
        self.LED_Red = 0.0
        self.LED_Off = 0.0
        if 17.5 <= self.Sensor_Voltage <= 30.0:
            self.LED_Green = 1.0
            self.LED_Red = 0.0
            self.LED_Off = 0.0
        #
        if 12.5 <= self.Sensor_Voltage <= 17.0:
            self.LED_Green = 0.0
            self.LED_Red = 1.0
            self.LED_Off = 0.0

        if 7.5 <= self.Sensor_Voltage <= 12.0:
            self.LED_Green = 0.0
            frequency = 1.0
            # Generate sine wave
            sine_wave = (np.sin(2 * np.pi * frequency * current_time))
            # Convert to binary (0 and 1)
            if sine_wave > 0:
                self.LED_Red = 1.0
            else:
                self.LED_Red = 0.0
            # binary_wave = (sine_wave > 0).astype(int)
            # self.LED_Red = binary_wave
            self.LED_Off = 0.0
        #
        if self.Sensor_Voltage >= 30.5:
            self.LED_Green = 0.0
            frequency = 5.0
            # Generate sine wave
            sine_wave = (np.sin(2 * np.pi * frequency * current_time))
            # Convert to binary (0 and 1)
            if sine_wave > 0:
                self.LED_Red = 1.0
            else:
                self.LED_Red = 0.0
            self.LED_Off = 0.0

        if self.Sensor_Voltage <= 7.5:
            self.LED_Green = 0.0
            self.LED_Red = 0.0
            self.LED_Off = 1.0


        return True

