import time
import pyi2c
from pyi2c import SMBus

bus_number = 1
device_address = 0x23

with SMBus(bus_number) as bus:
    while True:
        # Read data from sensor
        data = bus.read_i2c_block_data(device_address, 0x20, 2)

        # Convert data to lux
        raw_value = (data[1] + (256 * data[0]))
        lux = raw_value / 1.2

        # Determine light level
        if lux > 100000:
            message = "Too bright"
        elif lux > 1000:
            message = "Bright"
        elif lux > 100:
            message = "Medium"
        elif lux > 10:
            message = "Dark"
        else:
            message = "Too dark"

        # Print the data and message
        print("Light level: {} lux - {}".format(lux, message))

        # Wait before taking another measurement
        time.sleep(1)
