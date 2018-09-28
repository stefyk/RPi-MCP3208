#This code has been developed, using 
#https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input

import spidev
import time

spi_channel = 0
	   
#Enable SPI
spi = spidev.SpiDev(0, spi_channel)
spi.max_speed_hz = 1000000

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
	

def read_adc(adc_channel, Vref = 3.3):
	adc_channel = 0
			
	msg = 0b11
	msg = ((msg << 1) + adc_channel) << 5
	msg = [msg, 0b00000000]
	reply = spi.xfer2(msg)
	
	# Construct single integer out of the reply (2 bytes)
	adc = 0
	for n in reply:
		adc = (adc << 8) + n

	# Last bit (0) is not part of ADC value, shift to remove it
	adc = adc >> 1

	# Calculate voltage form ADC value
	Voltage = (3.3 * adc) / 1024
        
	return Voltage
				
	while True:
		# The read_adc function will get the value of the specified channel (0-1).
		adc_0 = read_adc(0)
		adc_1 = read_adc(1)
		# Print the ADC values.
		print("The amplitude of V from Ch.0 is:", round(adc_0, 2),"V")
		time.sleep(0.5)
