#This code has been build, using different example codes and is still unfinished

import spidev
import time

class MCP3208:
	spi_channel = 0
	   
    	#Enable SPI
	spi = spidev.SpiDev(0, spi_channel)
    	spi.max_speed_hz = 1000000

	# Hardware SPI configuration:
	SPI_PORT   = 0
	SPI_DEVICE = 0
	mcp = Adafruit_MCP3208.MCP3208(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    	def read_adc(adc_channel, Vref = 3.3):
		if adc_channel != 0:
            		adc_channel = 1
			
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
		Voltage = (Vref * adc) / 1024
        
		return Voltage
			
	try:		
		while True:
			spi = MCP3208(0)
			# The read_adc function will get the value of the specified channel (0-1).
			adc_0 = read_adc(0)
			adc_1 = read_adc(1)
			# Print the ADC values.
			print("Ch 0:", round(adc_0, 2), "V Ch 1:", round(adc_1, 2), "V")
			time.sleep(0.5)
	finally:  
		GPIO.cleanup()
