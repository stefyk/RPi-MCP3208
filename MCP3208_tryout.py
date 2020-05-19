#This code has been developed, using 
#https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input

import spidev
import time

spi_channel = 0
	   
#Enable SPI
spi = spidev.SpiDev(0, spi_channel)
spi.max_speed_hz = 100000

# Hardware SPI configuration (wiring explained in README file):
#SPI_PORT   = 0
#SPI_DEVICE = 0

def read_adc(adc_channel, Vref = 3.3):
	adc_channel = 0
			
	data = 0b11
	
    	adc = spi.xfer2([6+((4&adc_channel)>>2),(3&adc_channel)<<6,0])
    	data = ((adc[1]&15) << 8) + adc[2]
    	return data
	#Performs the SPI transaction and assigns the data to "reply"
	reply = spi.xfer2(data)
	
	# Construct single integer out of the reply (2 bytes)
	adc = 0
	for n in reply:
		adc = (adc << 8) + n

	# Last bit (0) is not part of ADC value, shift to remove it
	adc = adc >> 1

	# Calculate voltage form ADC value
	Voltage = (Vref * adc) / 4095
        
	return Voltage
try:			
	while True:
		# The read_adc function will get the value of the specified channel (0-1).
		adc_0 = read_adc(0)
		# Print the ADC values.
		print("The amplitude of V from Ch.0 is:", round(adc_0, 2),"V")
		time.sleep(0.5)
finally:
	#closing the SPI channel
	close()
