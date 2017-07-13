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
print (line)

f = open("color.txt","r")
c = f.read()
f.close()

f = open("saturation.txt","r")
sat = f.read()
sat  = int(sat)
f.close()

try:
    color = int(c)

    if color == 0:
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))
        

    elif color == 1:
        greenbright = int((4 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 2:
        greenbright = int((8 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 3:
        greenbright = int((12 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 4:
        greenbright = int((17 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 5:
        greenbright = int((21 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 6:
        greenbright = int((25 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 7:
        greenbright = int((29 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 8:
        greenbright = int((34 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 9:
        greenbright = int((38 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 10:
        greenbright = int((42 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 11:
        greenbright = int((46 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 12:
        greenbright = int((51 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 13:
        greenbright = int((55 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 14:
        greenbright = int((59 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 15:
        greenbright = int((63 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 16:
        greenbright = int((68 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 17:
        greenbright = int((72 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 18:
        greenbright = int((76 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 19:
        greenbright = int((80 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 20:
        greenbright = int((85 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 21:
        greenbright = int((89 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 22:
        greenbright = int((93 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 23:
        greenbright = int((97 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 24:
        greenbright = int((102 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 25:
        greenbright = int((106 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 26:
        greenbright = int((110 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 27:
        greenbright = int((114 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 28:
        greenbright = int((119 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 29:
        greenbright = int((123 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 30:
        greenbright = int((127 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 31:
        greenbright = int((131 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))
        
    elif color == 32:
        greenbright = int((136 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 33:
        greenbright = int((140 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 34:
        greenbright = int((144 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 35:
        greenbright = int((148 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 36:
        greenbright = int((153 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 37:
        greenbright = int((157 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 38:
        greenbright = int((161 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 39:
        greenbright = int((165 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 40:
        greenbright = int((170 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 41:
        greenbright = int((174 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 42:
        greenbright = int((178 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 43:
        greenbright = int((182 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 44:
        greenbright = int((187 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 45:
        greenbright = int((191 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 46:
        greenbright = int((195 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 47:
        greenbright = int((199 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 48:
        greenbright = int((204 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 49:
        greenbright = int((208 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 50:
        greenbright = int((212 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 51:
        greenbright = int((216 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 52:
        greenbright = int((221 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 53:
        greenbright = int((225 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 54:
        greenbright = int((229 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 55:
        greenbright = int((233 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 56:
        greenbright = int((238 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 57:
        greenbright = int((242 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 58:
        greenbright = int((246 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))
    elif color == 59:
        greenbright = int((250 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 60:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((255 / 100.0) * int(line))

    elif color == 61:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((250 / 100.0) * int(line))

    elif color == 62:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((246 / 100.0) * int(line))

    elif color == 63:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((242 / 100.0) * int(line))

    elif color == 64:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((238 / 100.0) * int(line))

    elif color == 65:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((233 / 100.0) * int(line))

    elif color == 66:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((229 / 100.0) * int(line))

    elif color == 67:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((225 / 100.0) * int(line))

    elif color == 68:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((221 / 100.0) * int(line))
                        
    elif color == 69:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((216 / 100.0) * int(line))

    elif color == 70:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((212 / 100.0) * int(line))

    elif color == 71:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((208 / 100.0) * int(line))

    elif color == 72:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((204 / 100.0) * int(line))

    elif color == 73:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((199 / 100.0) * int(line))

    elif color == 74:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((195 / 100.0) * int(line))

    elif color == 75:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((191 / 100.0) * int(line))

    elif color == 76:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((187 / 100.0) * int(line))

    elif color == 77:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((182 / 100.0) * int(line))

    elif color == 78:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((178 / 100.0) * int(line))

    elif color == 79:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((174 / 100.0) * int(line))
                        
    elif color == 80:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((170 / 100.0) * int(line))
                                            
    elif color == 81:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((165 / 100.0) * int(line))
                                            
    elif color == 82:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((161 / 100.0) * int(line))
                                            
    elif color == 83:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((157 / 100.0) * int(line))
                                            
    elif color == 84:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((153 / 100.0) * int(line))
                                            
    elif color == 85:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((148 / 100.0) * int(line))
                                            
    elif color == 86:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((144 / 100.0) * int(line))
                                            
    elif color == 87:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((140 / 100.0) * int(line))
                                            
    elif color == 88:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((136 / 100.0) * int(line))
                                            
    elif color == 89:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((131 / 100.0) * int(line))
                        
    elif color == 90:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((127 / 100.0) * int(line))
                                            
    elif color == 91:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((123 / 100.0) * int(line))
                                            
    elif color == 92:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((119 / 100.0) * int(line))
                                            
    elif color == 93:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((114 / 100.0) * int(line))
                                            
    elif color == 94:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((110 / 100.0) * int(line))
                                            
    elif color == 95:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((106 / 100.0) * int(line))
                                            
    elif color == 96:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((102 / 100.0) * int(line))
                                            
    elif color == 97:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((97 / 100.0) * int(line))
                                            
    elif color == 98:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((93 / 100.0) * int(line))
                                            
    elif color == 99:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((89 / 100.0) * int(line))
                                                                
    elif color == 100:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((85 / 100.0) * int(line))
                                            
    elif color == 101:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((80 / 100.0) * int(line))
                                                                
    elif color == 102:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((76 / 100.0) * int(line))
                                                                
    elif color == 103:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((72 / 100.0) * int(line))
                                                                
    elif color == 104:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((68 / 100.0) * int(line))
                                                                
    elif color == 105:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((63 / 100.0) * int(line))
                                                                
    elif color == 106:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((59 / 100.0) * int(line))
                                                                
    elif color == 107:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((55 / 100.0) * int(line))
                        
    elif color == 108:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((51 / 100.0) * int(line))
                                                               
    elif color == 109:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((46 / 100.0) * int(line))
                                                                
    elif color == 110:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((42 / 100.0) * int(line))
                                                                
    elif color == 111:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((38 / 100.0) * int(line))
                                                                                    
    elif color == 112:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((34 / 100.0) * int(line))
                                                                                    
    elif color == 113:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((29 / 100.0) * int(line))
                                                                                    
    elif color == 114:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((25 / 100.0) * int(line))
                                                                                    
    elif color == 115:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((21 / 100.0) * int(line))
                                                                                    
    elif color == 116:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((17 / 100.0) * int(line))
                                                                                    
    elif color == 117:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((12 / 100.0) * int(line))
                                                                                    
    elif color == 118:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((8 / 100.0) * int(line))
                                                                                    
    elif color == 119:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((4 / 100.0) * int(line))
                                                                                    
    elif color == 120:
        greenbright = int((255 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))

    elif color == 121:
        bluebright = int((4 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 122:
        bluebright = int((8 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 123:
        bluebright = int((12 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 124:
        bluebright = int((17 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 125:
        bluebright = int((21 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 126:
        bluebright = int((25 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 127:
        bluebright = int((29 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 128:
        bluebright = int((34 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 129:
        bluebright = int((38 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 130:
        bluebright = int((42 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 131:
        bluebright = int((46 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 132:
        bluebright = int((51 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 133:
        bluebright = int((55 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 134:
        bluebright = int((59 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 135:
        bluebright = int((63 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 136:
        bluebright = int((68 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 137:
        bluebright = int((72 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 138:
        bluebright = int((76 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 139:
        bluebright = int((80 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 140:
        bluebright = int((85 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 141:
        bluebright = int((89 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 142:
        bluebright = int((93 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 143:
        bluebright = int((97 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 144:
        bluebright = int((102 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 145:
        bluebright = int((106 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 146:
        bluebright = int((110 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 147:
        bluebright = int((114 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 148:
        bluebright = int((119 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 149:
        bluebright = int((123 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 150:
        bluebright = int((127 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 151:
        bluebright = int((131 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))
        
    elif color == 152:
        bluebright = int((136 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 153:
        bluebright = int((140 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 154:
        bluebright = int((144 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 155:
        bluebright = int((148 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 156:
        bluebright = int((153 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 157:
        bluebright = int((157 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 158:
        bluebright = int((161 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 159:
        bluebright = int((165 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 160:
        bluebright = int((170 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 161:
        bluebright = int((174 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 162:
        bluebright = int((178 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 163:
        bluebright = int((182 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 164:
        bluebright = int((187 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 165:
        bluebright = int((191 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 166:
        bluebright = int((195 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 167:
        bluebright = int((199 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 168:
        bluebright = int((204 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 169:
        bluebright = int((208 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 170:
        bluebright = int((212 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 171:
        bluebright = int((216 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 172:
        bluebright = int((221 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 173:
        bluebright = int((225 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 174:
        bluebright = int((229 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 175:
        bluebright = int((233 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 176:
        bluebright = int((238 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 177:
        bluebright = int((242 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 178:
        bluebright = int((246 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))
    elif color == 179:
        bluebright = int((250 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 180:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((255 / 100.0) * int(line))

    elif color == 181:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((250 / 100.0) * int(line))

    elif color == 182:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((246 / 100.0) * int(line))

    elif color == 183:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((242 / 100.0) * int(line))

    elif color == 184:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((238 / 100.0) * int(line))

    elif color == 185:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((233 / 100.0) * int(line))

    elif color == 186:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((229 / 100.0) * int(line))

    elif color == 187:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((225 / 100.0) * int(line))

    elif color == 188:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((221 / 100.0) * int(line))
                        
    elif color == 189:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((216 / 100.0) * int(line))

    elif color == 190:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((212 / 100.0) * int(line))

    elif color == 191:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((208 / 100.0) * int(line))

    elif color == 192:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((204 / 100.0) * int(line))

    elif color == 193:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((199 / 100.0) * int(line))

    elif color == 194:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((195 / 100.0) * int(line))

    elif color == 195:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((191 / 100.0) * int(line))

    elif color == 196:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((187 / 100.0) * int(line))

    elif color == 197:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((182 / 100.0) * int(line))

    elif color == 198:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((178 / 100.0) * int(line))

    elif color == 199:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((174 / 100.0) * int(line))
                        
    elif color == 200:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((170 / 100.0) * int(line))
                                            
    elif color == 201:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((165 / 100.0) * int(line))
                                            
    elif color == 202:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((161 / 100.0) * int(line))
                                            
    elif color == 203:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((157 / 100.0) * int(line))
                                            
    elif color == 204:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((153 / 100.0) * int(line))
                                            
    elif color == 205:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((148 / 100.0) * int(line))
                                            
    elif color == 206:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((144 / 100.0) * int(line))
                                            
    elif color == 207:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((140 / 100.0) * int(line))
                                            
    elif color == 208:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((136 / 100.0) * int(line))
                                            
    elif color == 209:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((131 / 100.0) * int(line))
                        
    elif color == 210:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((127 / 100.0) * int(line))
                                            
    elif color == 211:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((123 / 100.0) * int(line))
                                            
    elif color == 212:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((119 / 100.0) * int(line))
                                            
    elif color == 213:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((114 / 100.0) * int(line))
                                            
    elif color == 214:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((110 / 100.0) * int(line))
                                            
    elif color == 215:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((106 / 100.0) * int(line))
                                            
    elif color == 216:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((102 / 100.0) * int(line))
                                            
    elif color == 217:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((97 / 100.0) * int(line))
                                            
    elif color == 218:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((93 / 100.0) * int(line))
                                            
    elif color == 219:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((89 / 100.0) * int(line))
                                                                
    elif color == 220:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((85 / 100.0) * int(line))
                                            
    elif color == 221:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((80 / 100.0) * int(line))
                                                                
    elif color == 222:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((76 / 100.0) * int(line))
                                                                
    elif color == 223:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((72 / 100.0) * int(line))
                                                                
    elif color == 224:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((68 / 100.0) * int(line))
                                                                
    elif color == 225:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((63 / 100.0) * int(line))
                                                                
    elif color == 226:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((59 / 100.0) * int(line))
                                                                
    elif color == 227:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((55 / 100.0) * int(line))
                        
    elif color == 228:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((51 / 100.0) * int(line))
                                                               
    elif color == 229:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((46 / 100.0) * int(line))
                                                                
    elif color == 230:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((42 / 100.0) * int(line))
                                                                
    elif color == 231:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((38 / 100.0) * int(line))
                                                                                    
    elif color == 232:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((34 / 100.0) * int(line))
                                                                                    
    elif color == 233:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((29 / 100.0) * int(line))
                                                                                    
    elif color == 234:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((25 / 100.0) * int(line))
                                                                                    
    elif color == 235:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((21 / 100.0) * int(line))
                                                                                    
    elif color == 236:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((17 / 100.0) * int(line))
                                                                                    
    elif color == 237:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((12 / 100.0) * int(line))
                                                                                    
    elif color == 238:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((8 / 100.0) * int(line))
                                                                                    
    elif color == 239:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((4 / 100.0) * int(line))
                                                                                    
    elif color == 240:
        bluebright = int((255 / 100.0) * int(line))
        redbright = int((0 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))

    elif color == 241:
        redbright = int((4 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 242:
        redbright = int((8 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 243:
        redbright = int((12 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 244:
        redbright = int((17 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 245:
        redbright = int((21 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 246:
        redbright = int((25 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 247:
        redbright = int((29 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 248:
        redbright = int((34 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 249:
        redbright = int((38 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 250:
        redbright = int((42 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 251:
        redbright = int((46 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 252:
        redbright = int((51 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 253:
        redbright = int((55 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 254:
        redbright = int((59 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 255:
        redbright = int((63 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 256:
        redbright = int((68 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))
        
    elif color == 257:
        redbright = int((72 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 258:
        redbright = int((76 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 259:
        redbright = int((80 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 260:
        redbright = int((85 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 261:
        redbright = int((89 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 262:
        redbright = int((93 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 263:
        redbright = int((97 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 264:
        redbright = int((102 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 265:
        redbright = int((106 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 266:
        redbright = int((110 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 267:
        redbright = int((114 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 268:
        redbright = int((119 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 269:
        redbright = int((123 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 270:
        redbright = int((127 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 271:
        redbright = int((131 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))
        
    elif color == 272:
        redbright = int((136 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 273:
        redbright = int((140 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 274:
        redbright = int((144 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 275:
        redbright = int((148 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 276:
        redbright = int((153 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 277:
        redbright = int((157 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 278:
        redbright = int((161 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 279:
        redbright = int((165 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 280:
        redbright = int((170 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 281:
        redbright = int((174 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 282:
        redbright = int((178 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 283:
        redbright = int((182 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 284:
        redbright = int((187 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 285:
        redbright = int((191 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 286:
        redbright = int((195 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 287:
        redbright = int((199 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 288:
        redbright = int((204 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 289:
        redbright = int((208 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 290:
        redbright = int((212 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 291:
        redbright = int((216 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 292:
        redbright = int((221 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 293:
        redbright = int((225 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 294:
        redbright = int((229 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 295:
        redbright = int((233 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 296:
        redbright = int((238 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 297:
        redbright = int((242 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 298:
        redbright = int((246 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))
        
    elif color == 299:
        redbright = int((250 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 300:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((255 / 100.0) * int(line))

    elif color == 301:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((250 / 100.0) * int(line))

    elif color == 302:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((246 / 100.0) * int(line))

    elif color == 303:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((242 / 100.0) * int(line))

    elif color == 304:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((238 / 100.0) * int(line))

    elif color == 305:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((233 / 100.0) * int(line))

    elif color == 306:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((229 / 100.0) * int(line))

    elif color == 307:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((225 / 100.0) * int(line))

    elif color == 308:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((221 / 100.0) * int(line))
                        
    elif color == 309:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((216 / 100.0) * int(line))

    elif color == 300:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((212 / 100.0) * int(line))

    elif color == 311:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((208 / 100.0) * int(line))

    elif color == 312:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((204 / 100.0) * int(line))

    elif color == 313:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((199 / 100.0) * int(line))

    elif color == 314:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((195 / 100.0) * int(line))

    elif color == 315:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((191 / 100.0) * int(line))

    elif color == 316:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((187 / 100.0) * int(line))

    elif color == 317:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((182 / 100.0) * int(line))

    elif color == 318:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((178 / 100.0) * int(line))

    elif color == 319:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((174 / 100.0) * int(line))
                        
    elif color == 320:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((170 / 100.0) * int(line))
                                            
    elif color == 321:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((165 / 100.0) * int(line))
                                            
    elif color == 322:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((161 / 100.0) * int(line))
                                            
    elif color == 323:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((157 / 100.0) * int(line))
                                            
    elif color == 324:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((153 / 100.0) * int(line))
                                            
    elif color == 325:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((148 / 100.0) * int(line))
                                            
    elif color == 326:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((144 / 100.0) * int(line))
                                            
    elif color == 327:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((140 / 100.0) * int(line))
                                            
    elif color == 328:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((136 / 100.0) * int(line))
                                            
    elif color == 329:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((131 / 100.0) * int(line))
                        
    elif color == 330:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((127 / 100.0) * int(line))
                                            
    elif color == 331:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((123 / 100.0) * int(line))
                                            
    elif color == 332:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((119 / 100.0) * int(line))
                                            
    elif color == 333:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((114 / 100.0) * int(line))
                                            
    elif color == 334:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((110 / 100.0) * int(line))
                                            
    elif color == 335:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((106 / 100.0) * int(line))
                                            
    elif color == 336:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((102 / 100.0) * int(line))
                                            
    elif color == 337:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((97 / 100.0) * int(line))
                                            
    elif color == 338:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((93 / 100.0) * int(line))
                                            
    elif color == 339:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((89 / 100.0) * int(line))
                                                                
    elif color == 340:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((85 / 100.0) * int(line))
                                            
    elif color == 341:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((80 / 100.0) * int(line))
                                                                
    elif color == 342:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((76 / 100.0) * int(line))
                                                                
    elif color == 343:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((72 / 100.0) * int(line))
                                                                
    elif color == 344:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((68 / 100.0) * int(line))
                                                                
    elif color == 345:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((63 / 100.0) * int(line))
                                                                
    elif color == 346:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((59 / 100.0) * int(line))
                                                                
    elif color == 347:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((55 / 100.0) * int(line))
                        
    elif color == 348:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((51 / 100.0) * int(line))
                                                               
    elif color == 349:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((46 / 100.0) * int(line))
                                                                
    elif color == 350:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((42 / 100.0) * int(line))
                                                                
    elif color == 351:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((38 / 100.0) * int(line))
                                                                                    
    elif color == 352:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((34 / 100.0) * int(line))
                                                                                    
    elif color == 353:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((29 / 100.0) * int(line))
                                                                                    
    elif color == 354:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((25 / 100.0) * int(line))
                                                                                    
    elif color == 355:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((21 / 100.0) * int(line))
                                                                                    
    elif color == 356:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((17 / 100.0) * int(line))
                                                                                    
    elif color == 357:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((12 / 100.0) * int(line))
                                                                                    
    elif color == 358:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((8 / 100.0) * int(line))
                                                                                    
    elif color == 359:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((4 / 100.0) * int(line))
                                                                                    
    elif color == 360:
        redbright = int((255 / 100.0) * int(line))
        greenbright = int((0 / 100.0) * int(line))
        bluebright = int((0 / 100.0) * int(line))

except:
    print (c)


if sat > 15:
    print (greenbright)
    print (bluebright)
    print (redbright)
    pi.set_PWM_dutycycle(22, greenbright)
    pi.set_PWM_dutycycle(24, bluebright)
    pi.set_PWM_dutycycle(27, redbright)
