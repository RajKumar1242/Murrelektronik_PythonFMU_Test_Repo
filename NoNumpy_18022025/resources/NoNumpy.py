import os
#import numpy as np
from pythonfmu3 import Fmi3Causality, Fmi3Slave, Float64, Int32, Boolean, Fmi3Variability

#from Modules.QualifierDI8 import qualifier_di_8
#from Modules.QualifierDO8 import qualifier_do_8
#from Modules.MVKLEDConfig import led
#from Modules.DI8 import digital_inputs
#from Modules.DO8 import digital_outputs

#numpy_path = os.path.dirname(np.__file__)

class NoNumpy(Fmi3Slave):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)



        self.LED_Off = 0.0
        self.LED_Red = 0.0
        self.LED_Green = 0.0
        self.Sensor_Voltage = 24.0
        self.Actuator_Voltage = 24.0
        self.author = "Raj Kumar"
        self.description = "A simple description of DIO 8 module from Murrelektronik catalogue"

        self.time = 0.0

        self.register_variable(Float64("time", causality=Fmi3Causality.independent))
        self.register_variable(Float64("Sensor_Voltage", causality=Fmi3Causality.input))
        self.register_variable(Float64("Actuator_Voltage", causality=Fmi3Causality.input))

        self.register_variable(Float64("LED_Green", causality=Fmi3Causality.output))
        self.register_variable(Float64("LED_Red", causality=Fmi3Causality.output))
        self.register_variable(Float64("LED_Off", causality=Fmi3Causality.output))



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
#
        if 7.5 <= self.Sensor_Voltage <= 12.0:
            self.LED_Green = 0.0

            self.LED_Red = 1.0
            self.LED_Off = 0.0
        #
        if self.Sensor_Voltage >= 30.5:
            self.LED_Green = 0.0

            self.LED_Off = 0.0
            self.LED_Red = 1.0
        #
        if self.Sensor_Voltage <= 7.5:
            self.LED_Green = 0.0
            self.LED_Red = 0.0
            self.LED_Off = 1.0




        return True

