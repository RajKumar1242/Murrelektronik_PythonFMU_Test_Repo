
import numpy as np
from pythonfmu3 import Fmi3Causality, Fmi3Slave, Float64, Int32, Boolean, Fmi3Variability

from Modules.QualifierDI8 import qualifier_di_8
from Modules.QualifierDO8 import qualifier_do_8
from Modules.MVKLEDConfig import led
from Modules.DI8 import digital_inputs
from Modules.DO8 import digital_outputs



class MVK54531(Fmi3Slave):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        #Parameters Pin, port, ComplexBased IOs
        self.PinBased = True
        self.PortBased = False
        self.ComplexBased = False
        #self.IOLayout = {self.PinBased, self.PortBased, self.ComplexBased}


        self.LED_Off = 0.0
        self.LED_Red = 0.0
        self.LED_Green = 0.0
        self.Sensor_Voltage = 24.0
        self.Actuator_Voltage = 24.0
        self.author = "Raj Kumar"
        self.description = "A simple description of DIO 8 module from Murrelektronik catalogue"

        self.time = 0.0


        self.outByte1 = 10
        self.outByte2 = 10
        self.inByte1 = 10
        self.inByte2 = 10
        self.qualifier_di_8_byte1 = 0
        self.qualifier_di_8_byte2 = 0
        self.qualifier_do_8_byte1 = 0
        self.qualifier_do_8_byte2 = 0

        #Variables for sensor inputs...
        self.X0_2 = 1
        self.X0_4 = 1
        self.X1_2 = 1
        self.X1_4 = 1
        self.X2_2 = 1
        self.X2_4 = 1
        self.X3_2 = 1
        self.X3_4 = 1

        #Variables for actuator variables..
        self.X4_2 = 1
        self.X4_4 = 1
        self.X5_2 = 1
        self.X5_4 = 1
        self.X6_2 = 1
        self.X6_4 = 1
        self.X7_2 = 1
        self.X7_4 = 1

        self.register_variable(Float64("time", causality=Fmi3Causality.independent))
        self.register_variable(Float64("Sensor_Voltage", causality=Fmi3Causality.input))
        self.register_variable(Float64("Actuator_Voltage", causality=Fmi3Causality.input))

        #Parameter Declerations
        self.register_variable(Boolean("PinBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable, description= "Pin based mapping of inputs"))
        self.register_variable(Boolean("PortBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable))
        self.register_variable(Boolean("ComplexBased", causality=Fmi3Causality.parameter,variability=Fmi3Variability.tunable))


        self.register_variable(Int32("X0_2", causality=Fmi3Causality.output))
        self.register_variable(Int32("X0_4", causality=Fmi3Causality.output))
        self.register_variable(Int32("X1_2", causality=Fmi3Causality.output))
        self.register_variable(Int32("X1_4", causality=Fmi3Causality.output))
        self.register_variable(Int32("X2_2", causality=Fmi3Causality.output))
        self.register_variable(Int32("X2_4", causality=Fmi3Causality.output))
        self.register_variable(Int32("X3_2", causality=Fmi3Causality.output))
        self.register_variable(Int32("X3_4", causality=Fmi3Causality.output))


        self.register_variable(Float64("LED_Green", causality=Fmi3Causality.output))
        self.register_variable(Float64("LED_Red", causality=Fmi3Causality.output))
        self.register_variable(Float64("LED_Off", causality=Fmi3Causality.output))
        self.register_variable(Int32("outByte1", causality=Fmi3Causality.output))
        self.register_variable(Int32("outByte2", causality=Fmi3Causality.output))
        self.register_variable(Int32("qualifier_di_8_byte1", causality=Fmi3Causality.output))
        self.register_variable(Int32("qualifier_di_8_byte2", causality=Fmi3Causality.output))
        self.register_variable(Int32("qualifier_do_8_byte1", causality=Fmi3Causality.output))
        self.register_variable(Int32("qualifier_do_8_byte2", causality=Fmi3Causality.output))

        self.register_variable(Int32("X4_2", causality=Fmi3Causality.input))
        self.register_variable(Int32("X4_4", causality=Fmi3Causality.input))
        self.register_variable(Int32("X5_2", causality=Fmi3Causality.input))
        self.register_variable(Int32("X5_4", causality=Fmi3Causality.input))
        self.register_variable(Int32("X6_2", causality=Fmi3Causality.input))
        self.register_variable(Int32("X6_4", causality=Fmi3Causality.input))
        self.register_variable(Int32("X7_2", causality=Fmi3Causality.input))
        self.register_variable(Int32("X7_4", causality=Fmi3Causality.input))
        self.register_variable(Int32("inByte1", causality=Fmi3Causality.input))
        self.register_variable(Int32("inByte2", causality=Fmi3Causality.input))


    def do_step(self, current_time, step_size):

        #This folowing section is to convert bits to bytes...i.e sensor values to a bit..
        #DI 8
        self.outByte1,self.outByte2 = digital_inputs(np.array([self.X4_2, self.X4_4, self.X5_2, self.X5_4, self.X6_2, self.X6_4, self.X7_2, self.X7_4]), self.PinBased, self.PortBased, self.ComplexBased)


        #The following section is to convert byte to bits....triggering the actuator values.
        #DO 8
        self.X0_2, self.X0_4, self.X1_2, self.X1_4, self.X2_2, self.X2_4, self.X3_2, self.X3_4 = digital_outputs(self.inByte1, self.inByte2, self.PinBased, self.PortBased, self.ComplexBased)


        #LED Config behaviour
        self.LED_Green,self.LED_Red,self.LED_Off = led(self.Sensor_Voltage, current_time)
      #  self.LED_Green = 0.0
      #  self.LED_Red = 0.0
      #  self.LED_Off = 0.0
      #  if 17.5 <= self.Sensor_Voltage <= 30.0:
      #      self.LED_Green = 1.0
      #      self.LED_Red = 0.0
      #      self.LED_Off = 0.0
      #  #
      #  if 12.5 <= self.Sensor_Voltage <= 17.0:
      #      self.LED_Green = 0.0
      #      self.LED_Red = 1.0
      #      self.LED_Off = 0.0
#
      #  if 7.5 <= self.Sensor_Voltage <= 12.0:
      #      self.LED_Green = 0.0
      #      frequency = 1.0
      #      # Generate sine wave
      #      sine_wave = (np.sin(2 * np.pi * frequency * current_time))
      #      # Convert to binary (0 and 1)
      #      if sine_wave > 0:
      #          self.LED_Red = 1.0
      #      else:
      #          self.LED_Red = 0.0
      #      # binary_wave = (sine_wave > 0).astype(int)
      #      # self.LED_Red = binary_wave
      #      self.LED_Off = 0.0
      #  #
      #  if self.Sensor_Voltage >= 30.5:
      #      self.LED_Green = 0.0
      #      frequency = 5.0
      #      # Generate sine wave
      #      sine_wave = (np.sin(2 * np.pi * frequency * current_time))
      #      # Convert to binary (0 and 1)
      #      if sine_wave > 0:
      #          self.LED_Red = 1.0
      #      else:
      #          self.LED_Red = 0.0
      #      self.LED_Off = 0.0
      #  #
      #  if self.Sensor_Voltage <= 7.5:
      #      self.LED_Green = 0.0
      #      self.LED_Red = 0.0
      #      self.LED_Off = 1.0

        #Qualifier DI
        self.qualifier_di_8_byte1,self.qualifier_di_8_byte2 = qualifier_di_8([1,1,1,1,1,1,1,1], self.PinBased, self.PortBased, self.ComplexBased)

        #Qualifier DO
        self.qualifier_do_8_byte1, self.qualifier_do_8_byte2 = qualifier_do_8(self.inByte1, self.inByte2, [1,1,1,1,1,1,1,1], self.PinBased, self.PortBased, self.ComplexBased)

        #LED behaviour

        #System State.


        return True

