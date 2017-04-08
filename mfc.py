import time
import datetime

# Import the ADS1x15 module.
import Adafruit_ADS1x15


# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()

GAIN = 4

adc.start_adc_comparator(0,  # Channel number
                         20000, 5000,  # High threshold value, low threshold value
                         active_low=True, traditional=True, latching=False,
                         num_readings=1, gain=GAIN)

file = open("data2.csv", 'a')
print "timestamp, reading (mV)\n"
  
data = list()
i = 0
count = 0
mx = 20


while True:
    value = adc.get_last_result() * 0.0078125
    line = datetime.datetime.now().strftime("%D %H:%M:%S") + ", " + str(value)
    file.write(line + "\n")
    file.flush()
    if count < mx:
        data.append(value)
        count = count + 1
    else:
        data = data[1:]
        data.append(value)
        i = i + 1
        i = (i)%mx
        
    print line
    time.sleep(5)
