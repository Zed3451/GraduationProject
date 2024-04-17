import smbus
import time

# Initialize the I2C bus
bus = smbus.SMBus(1)
address = 0x48  # ADS1115 address

# Read analog value from channel 0 (A0)


def read_adc(channel):
    data = bus.read_i2c_block_data(address, 0x01, 2)
    value = (data[0] << 8) + data[1]
    return value


try:
    while True:
        raw_value = read_adc(0)  # Read from channel 0
        voltage = raw_value * 3.3 / 65536  # Convert to voltage
        print(f"Heart rate voltage: {voltage:.4f} V")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user.")
