from pico_i2c_lcd import I2cLcd
from machine import I2C, Pin
from time import sleep

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

sda = Pin(8, Pin.PULL_UP)

scl = Pin(9, Pin.PULL_UP)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
print(i2c.scan())
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


add = Pin(6, Pin.IN, Pin.PULL_DOWN)
sub = Pin(7, Pin.IN, Pin.PULL_DOWN)
bal = Pin(5, Pin.IN, Pin.PULL_DOWN)

num0 = Pin(10, Pin.IN, Pin.PULL_DOWN)
num1 = Pin(11, Pin.IN, Pin.PULL_DOWN)
num2 = Pin(12, Pin.IN, Pin.PULL_DOWN)
num3 = Pin(13, Pin.IN, Pin.PULL_DOWN)
num4 = Pin(14, Pin.IN, Pin.PULL_DOWN)
num5 = Pin(15, Pin.IN, Pin.PULL_DOWN)
num6 = Pin(16, Pin.IN, Pin.PULL_DOWN)
num7 = Pin(17, Pin.IN, Pin.PULL_DOWN)
num8 = Pin(18, Pin.IN, Pin.PULL_DOWN)
num9 = Pin(19, Pin.IN, Pin.PULL_DOWN)

back = Pin(20, Pin.IN, Pin.PULL_DOWN)
enter = Pin(21, Pin.IN, Pin.PULL_DOWN)

def KeyPad():
    value = ""
    flag = 0
    let = 0
    while True:
        sleep(0.15)
        if sub.value()==1:
            flag = flag + 1
            if flag > 2:
                flag = 0
                
        if add.value()==1:
            let = let - 1
            if let < 0:
                let = 2
                
        if bal.value()==1:
            let = let + 1
            if let > 2:
                let = 0
                
        if back.value()==1:
            value = value[0:len(value)-1]
            lcd.clear()
            lcd.putstr(value)
        
        if flag == 0:
            if num0.value()==1:
                value = value + "0"
                lcd.clear()
                lcd.putstr(value)
                
            elif num1.value()==1:
                value = value + "1"
                lcd.clear()
                lcd.putstr(value)
                
            elif num2.value()==1:
                value = value + "2"
                lcd.clear()
                lcd.putstr(value)
                
            elif num3.value()==1:
                value = value + "3"
                lcd.clear()
                lcd.putstr(value)
                
            elif num4.value()==1:
                value = value + "4"
                lcd.clear()
                lcd.putstr(value)
                
            elif num5.value()==1:
                value = value + "5"
                lcd.clear()
                lcd.putstr(value)
                
            elif num6.value()==1:
                value = value + "6"
                lcd.clear()
                lcd.putstr(value)
                
            elif num7.value()==1:
                value = value + "7"
                lcd.clear()
                lcd.putstr(value)
                
            elif num8.value()==1:
                value = value + "8"
                lcd.clear()
                lcd.putstr(value)
                
            elif num9.value()==1:
                value = value + "9"
                lcd.clear()
                lcd.putstr(value)
                
            elif enter.value()==1:
                lcd.clear()
                return value
            
        elif flag == 1:
            if num0.value()==1:
                value = value + " "
                lcd.clear()
                lcd.putstr(value)
            
            if let == 0:
                if num1.value()==1:
                    value = value + "A"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "B"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "C"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "D"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "E"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "F"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "G"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "H"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num9.value()==1:
                    value = value + "I"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value
                
            elif let == 1:
                if num1.value()==1:
                    value = value + "J"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "K"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "L"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "M"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "N"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "O"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "P"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "Q"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num9.value()==1:
                    value = value + "R"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value
                
            elif let == 2:
                if num1.value()==1:
                    value = value + "S"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "T"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "U"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "V"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "W"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "X"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "Y"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "Z"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value

        elif flag == 2:
            if num0.value()==1:
                value = value + " "
                lcd.clear()
                lcd.putstr(value)
            
            if let == 0:
                if num1.value()==1:
                    value = value + "a"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "b"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "c"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "d"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "e"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "f"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "g"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "h"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num9.value()==1:
                    value = value + "i"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value
                
            elif let == 1:
                if num1.value()==1:
                    value = value + "j"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "k"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "l"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "m"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "n"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "o"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "p"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "q"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num9.value()==1:
                    value = value + "r"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value
                
            elif let == 2:
                if num1.value()==1:
                    value = value + "s"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num2.value()==1:
                    value = value + "t"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num3.value()==1:
                    value = value + "u"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num4.value()==1:
                    value = value + "v"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num5.value()==1:
                    value = value + "w"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num6.value()==1:
                    value = value + "x"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num7.value()==1:
                    value = value + "y"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif num8.value()==1:
                    value = value + "z"
                    lcd.clear()
                    lcd.putstr(value)
                    
                elif enter.value()==1:
                    lcd.clear()
                    return value        