import numpy as np

from pythonfmu import Fmi2Slave, Real, Fmi2Causality, Fmi2Variability, Integer, Boolean

class TestMVKFMU2(Fmi2Slave):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.LED_Off = 0.0
        self.LED_Red = 0.0
        self.LED_Green = 0.0
        self.Sensor_Voltage = 24.0
       # self.Actuator_Voltage = 24.0
        self.author = "Raj Kumar"
        self.description = "A simple description of DIO 8 module from Murrelektronik catalogue"

        self.time = 0.0

        self.register_variable(Real("time", causality=Fmi2Causality.local))
        self.register_variable(Real("Sensor_Voltage", causality=Fmi2Causality.input, start = 24.0))

        self.register_variable(Real("LED_Green", causality=Fmi2Causality.output))
        self.register_variable(Real("LED_Red", causality=Fmi2Causality.output))
        self.register_variable(Real("LED_Off", causality=Fmi2Causality.output ))
      
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

