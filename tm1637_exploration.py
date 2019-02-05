import tm1637
import time
import RPi.GPIO as GPIO

# Simply change the CLK and DIO pin numbers of 23 and 24 to match the Pi GPIO pins you've used.
display = tm1637.TM1637(CLK=20, DIO=21, brightness=7)
display.Clear()


key = input("Press the enter key to continue.")


#display.StartClock(min_sec=False)
#key = input("Hour:Min clock mode.... Press the enter key to continue.")
#display.StopClock()
#display.Clear()

display.StartClock(min_sec=True)
key = input("Min:Sec mode...   Press the enter key to continue.")
display.StopClock()
display.Clear()

display.Show(data=[10,11,12,13])
time.sleep(1)
display.Show(data=[14,15,0,1])

key = input("Press the enter key to continue.")

display.ShowScroll(12345)
display.ShowScroll(123)
display.ShowScroll(12)
display.ShowScroll(1)
display.ShowScroll(1234567890)

display.Clear()
GPIO.cleanup()
