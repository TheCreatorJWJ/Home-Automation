import pigpio
import os

pi = pigpio.pi()

greenbright = pi.get_PWM_dutycycle(22)
bluebright = pi.get_PWM_dutycycle(24)
redbright = pi.get_PWM_dutycycle(27)

os.chdir("/home/pi/HAP-NodeJS/accessories/brightness")
f = open("percent.txt","r")
line = f.read()
f.close()

greenbright = int((greenbright / float(line)) * 12)
bluebright = int((bluebright / float(line)) * 12)
redbright = int((redbright / float(line)) * 12)

f = open("percent.txt","w")
f.write("12")
f.close()

pi.set_PWM_dutycycle(22, greenbright)
pi.set_PWM_dutycycle(24, bluebright)
pi.set_PWM_dutycycle(27, redbright)
