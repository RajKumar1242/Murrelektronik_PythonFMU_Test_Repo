import numpy as np

def led(Sensor_Voltage, current_time):

            green = 0.0
            red = 0.0
            off = 0.0
            if 17.5 <= Sensor_Voltage <= 30.0:
                green = 1.0
                red = 0.0
                off = 0.0
            #
            if 12.5 <= Sensor_Voltage <= 17.0:
                green = 0.0
                red = 1.0
                off = 0.0

            if 7.5 <= Sensor_Voltage <= 12.0:
                green = 0.0
                frequency = 1.0
                # Generate sine wave
                sine_wave = (np.sin(2 * np.pi * frequency * current_time))
                # Convert to binary (0 and 1)
                if sine_wave > 0:
                    red = 1.0
                else:
                    red = 0.0
                # binary_wave = (sine_wave > 0).astype(int)
                # self.LED_Red = binary_wave
                off = 0.0
            #
            if Sensor_Voltage >= 30.5:
                green = 0.0
                frequency = 5.0
                # Generate sine wave
                sine_wave = (np.sin(2 * np.pi * frequency * current_time))
                # Convert to binary (0 and 1)
                if sine_wave > 0:
                    red = 1.0
                else:
                    red = 0.0
                off = 0.0
            #
            if Sensor_Voltage <= 7.5:
                green = 0.0
                red = 0.0
                off = 1.0


            ledarray = np.array([green,red,off])

            return ledarray
