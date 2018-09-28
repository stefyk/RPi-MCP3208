# RPi-MCP3208
Very simple code, composed of other codes, aiming interface between MCP3208 and RPi. It can be used with MCP3008 as well, as long as the ADC Resolution is 1024.

The code was initially made for MCP3008, so the information is designed to sent through 10 bits, however MCP3208 uses 12 bits, so instead we receive data that is 2^2=4 times less than the real one, so this is why I am changing the resolution of the adc from 1024 to 256 to compensate for that loss. However, if we have to be exact, you can transform the code to send 12 bits instead of 10 by looking at the data sheet of MCP3208 and changing this part of the code: 

  data = 0b11
	data = ((data << 1) + adc_channel) << 5
	data = [data, 0b00000000]
	#Performs the SPI transaction and assigns the data to "reply"
	reply = spi.xfer2(data)
	# Construct single integer out of the reply (2 bytes)
	adc = 0
	for n in reply:
		adc = (adc << 8) + n
	# Last bit (0) is not part of ADC value, shift to remove it
	adc = adc >> 1
  
  If you want to work MCP3008, the just change the ADC resolution from 256 back to 1024.
