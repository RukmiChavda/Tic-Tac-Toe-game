import machine
import utime

#<<<<<<<<<<<<<<<<<<<<<<<<pin confugration>>>>>>>>>>>>>>>>>>>>>>>>
green = [16,15,13,4,10,9,2,0,6]    #green led connection
blue = [17,14,12,5,11,8,1,18,7]    #blue led connection
player = [19,20]                   #player toggle led connection

# <<<<<<<<<<<<<<<<<<<<<<<<<<pin define>>>>>>>>>>>>>>>>>>>>>>>>>>>
button_select = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)   # button input
button_ok     = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)   # button input
player_1 = machine.Pin(player[1], machine.Pin.OUT)                       # player toggle output
player_2 = machine.Pin(player[0], machine.Pin.OUT)                       # player toggle output
led_red = machine.Pin(3, machine.Pin.OUT)                                # red led output
led_green1 = machine.Pin(green[0], machine.Pin.OUT)                      # green led output
led_green2 = machine.Pin(green[1], machine.Pin.OUT)
led_green3 = machine.Pin(green[2], machine.Pin.OUT)
led_green4 = machine.Pin(green[3], machine.Pin.OUT)
led_green5 = machine.Pin(green[4], machine.Pin.OUT)
led_green6 = machine.Pin(green[5], machine.Pin.OUT)
led_green7 = machine.Pin(green[6], machine.Pin.OUT)
led_green8 = machine.Pin(green[7], machine.Pin.OUT)
led_green9 = machine.Pin(green[8], machine.Pin.OUT)
led_blue1 = machine.Pin(blue[0], machine.Pin.OUT)                       # blue led output  
led_blue2 = machine.Pin(blue[1], machine.Pin.OUT)
led_blue3 = machine.Pin(blue[2], machine.Pin.OUT)
led_blue4 = machine.Pin(blue[3], machine.Pin.OUT)
led_blue5 = machine.Pin(blue[4], machine.Pin.OUT)
led_blue6 = machine.Pin(blue[5], machine.Pin.OUT)
led_blue7 = machine.Pin(blue[6], machine.Pin.OUT)
led_blue8 = machine.Pin(blue[7], machine.Pin.OUT)
led_blue9 = machine.Pin(blue[8], machine.Pin.OUT)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<Function>>>>>>>>>>>>>>>>>>>>>>>>>>>>   
def green_off():                                                     # initally off green led 
    led_green1.value(0)
    led_green2.value(0) 
    led_green3.value(0) 
    led_green4.value(0) 
    led_green5.value(0) 
    led_green6.value(0) 
    led_green7.value(0) 
    led_green8.value(0) 
    led_green9.value(0)
    utime.sleep(3)
    starting()
    
def blue_off():                                            # intially off blue leds
    led_blue1.value(0) 
    led_blue2.value(0) 
    led_blue3.value(0) 
    led_blue4.value(0) 
    led_blue5.value(0) 
    led_blue6.value(0) 
    led_blue7.value(0) 
    led_blue8.value(0) 
    led_blue9.value(0)
    utime.sleep(3)
    starting()
    
def starting():                                           # game starting function
    led_green1.value(0)
    led_green2.value(0) 
    led_green3.value(0) 
    led_green4.value(0) 
    led_green5.value(0) 
    led_green6.value(0) 
    led_green7.value(0) 
    led_green8.value(0) 
    led_green9.value(0)
    led_blue1.value(0) 
    led_blue2.value(0) 
    led_blue3.value(0) 
    led_blue4.value(0) 
    led_blue5.value(0) 
    led_blue6.value(0) 
    led_blue7.value(0) 
    led_blue8.value(0) 
    led_blue9.value(0)
    for i in range(3):
        led_red.value(1)
        utime.sleep(0.5)
        led_red.value(0)
        utime.sleep(0.5)
        player_1.value(1)
        player_2.value(0)
        
def condition():                                              # geme winning conditions                                                                                        
    if led_green1.value() == 1 and led_green2.value() == 1 and led_green3.value() == 1:                                                                                   
        led_green4.value(0) 
        led_green5.value(0)
        led_green6.value(0)
        led_green7.value(0) 
        led_green8.value(0) 
        led_green9.value(0)
        blue_off()
    elif led_blue1.value() == 1 and led_blue2.value() == 1 and led_blue3.value() ==  1:                   
        led_blue4.value(0)
        led_blue5.value(0) 
        led_blue6.value(0) 
        led_blue7.value(0) 
        led_blue8.value(0) 
        led_blue9.value(0)
        green_off()                                                                                           
    elif led_green4.value() == 1 and led_green5.value() == 1 and led_green6.value() == 1:                                                                                        
        led_green1.value(0) 
        led_green2.value(0) 
        led_green3.value(0)
        led_green7.value(0) 
        led_green8.value(0) 
        led_green9.value(0) 
        blue_off()
    elif led_blue4.value() == 1 and led_blue5.value() == 1 and led_blue6.value() ==  1:                   
        led_blue1.value(0) 
        led_blue2.value(0) 
        led_blue3.value(0)  
        led_blue7.value(0) 
        led_blue8.value(0) 
        led_blue9.value(0)
        green_off()                                                                                          
    elif led_green7.value() == 1 and led_green8.value() == 1 and led_green9.value() == 1:                                                                                         
        led_green1.value(0) 
        led_green2.value(0) 
        led_green3.value(0) 
        led_green4.value(0) 
        led_green5.value(0) 
        led_green6.value(0)
        blue_off()
    elif led_blue7.value() == 1 and led_blue8.value() == 1 and led_blue9.value() ==  1:                   
        led_blue1.value(0) 
        led_blue2.value(0) 
        led_blue3.value(0)
        led_blue4.value(0) 
        led_blue5.value(0) 
        led_blue6.value(0) 
        green_off()                                                                                        
    elif led_green1.value() == 1 and led_green4.value() == 1 and led_green7.value() == 1:                                                                                        
        led_green2.value(0) 
        led_green3.value(0)
        led_green5.value(0) 
        led_green6.value(0) 
        led_green8.value(0) 
        led_green9.value(0)
        blue_off()
    elif led_blue1.value() == 1 and led_blue4.value() == 1 and led_blue7.value() ==  1:                   
        led_blue2.value(0) 
        led_blue3.value(0) 
        led_blue5.value(0) 
        led_blue6.value(0) 
        led_blue8.value(0) 
        led_blue9.value(0)
        green_off()                                                                                          
    elif led_green2.value() == 1 and led_green5.value() == 1 and led_green8.value() == 1:                                                                                         
        led_green1.value(0)  
        led_green3.value(0)
        led_green4.value(0) 
        led_green6.value(0)
        led_green7.value(0) 
        led_green9.value(0)
        blue_off()
    elif led_blue2.value() == 1 and led_blue5.value() == 1 and led_blue8.value() ==  1:                   
        led_blue1.value(0) 
        led_blue3.value(0)
        led_blue4.value(0)
        led_blue6.value(0) 
        led_blue7.value(0) 
        led_blue9.value(0)
        green_off()                                                                                            
    elif led_green3.value() == 1 and led_green6.value() == 1 and led_green9.value() == 1:                                                                           
        led_green1.value(0)
        led_green2.value(0)
        led_green4.value(0) 
        led_green5.value(0) 
        led_green7.value(0) 
        led_green8.value(0)
        blue_off()
    elif led_blue3.value() == 1 and led_blue6.value() == 1 and led_blue9.value() ==  1:                   
        led_blue1.value(0) 
        led_blue2.value(0) 
        led_blue4.value(0) 
        led_blue5.value(0)
        led_blue7.value(0)
        led_blue8.value(0) 
        green_off()                                                                                           
    elif led_green1.value() == 1 and led_green5.value() == 1 and led_green9.value() == 1:                                                                                
        led_green2.value(0) 
        led_green3.value(0) 
        led_green4.value(0)
        led_green6.value(0) 
        led_green7.value(0) 
        led_green8.value(0)
        blue_off()
    elif led_blue1.value() == 1 and led_blue5.value() == 1 and led_blue9.value() ==  1:                   
        led_blue2.value(0) 
        led_blue3.value(0) 
        led_blue4.value(0) 
        led_blue6.value(0) 
        led_blue7.value(0) 
        led_blue8.value(0)
        green_off()                                                                                           
    elif led_green3.value() == 1 and led_green5.value() == 1 and led_green7.value() == 1:                                                                                        
        led_green1.value(0)
        led_green2.value(0) 
        led_green4.value(0)  
        led_green6.value(0)
        led_green8.value(0) 
        led_green9.value(0)
        blue_off()
    elif led_blue3.value() == 1 and led_blue5.value() == 1 and led_blue7.value() ==  1:                   
        led_blue1.value(0) 
        led_blue2.value(0) 
        led_blue4.value(0)  
        led_blue6.value(0)  
        led_blue8.value(0) 
        led_blue9.value(0)
        green_off()
        
def player1_toggle():                       # player changing
    player_1.value(1)
    player_2.value(0)
    utime.sleep(0.275)
    
def player2_toggle():                       # player changing
    player_1.value(0)
    player_2.value(1)
    utime.sleep(0.275)
    
def selection():                            # selectiion and ok button function 
    while led_blue1.value() == 0 and led_green1.value() == 0:
        led_blue1.value(1)
        led_green1.value(1)
        utime.sleep(0.3)
        led_blue1.value(0)
        led_green1.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue1.value(1)
            condition()
            player2_toggle()             
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green1.value(1)
            condition()
            player1_toggle()
    while led_blue2.value() == 0 and led_green2.value() == 0:
        led_blue2.value(1)
        led_green2.value(1)
        utime.sleep(0.3)
        led_blue2.value(0)
        led_green2.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue2.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green2.value(1)
            condition()
            player1_toggle()
    while led_blue3.value() == 0 and led_green3.value() == 0:
        led_blue3.value(1)
        led_green3.value(1)
        utime.sleep(0.3)
        led_blue3.value(0)
        led_green3.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue3.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green3.value(1)
            condition()
            player1_toggle()
    while led_blue4.value() == 0 and led_green4.value() == 0:
        led_blue4.value(1)
        led_green4.value(1)
        utime.sleep(0.3)
        led_blue4.value(0)
        led_green4.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue4.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green4.value(1)
            condition()
            player1_toggle()
    while led_blue5.value() == 0 and led_green5.value() == 0:
        led_blue5.value(1)
        led_green5.value(1)
        utime.sleep(0.3)
        led_blue5.value(0)
        led_green5.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue5.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green5.value(1)
            condition()
            condition()
            player1_toggle()
    while led_blue6.value() == 0 and led_green6.value() == 0:
        led_blue6.value(1)
        led_green6.value(1)
        utime.sleep(0.3)
        led_blue6.value(0)
        led_green6.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue6.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green6.value(1)
            condition()
            player1_toggle()
    while led_blue7.value() == 0 and led_green7.value() == 0:
        led_blue7.value(1)
        led_green7.value(1)
        utime.sleep(0.3)
        led_blue7.value(0)
        led_green7.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue7.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green7.value(1)
            condition()
            player1_toggle()
    while led_blue8.value() == 0 and led_green8.value() == 0:
        led_blue8.value(1)
        led_green8.value(1)
        utime.sleep(0.3)
        led_blue8.value(0)
        led_green8.value(0)
        utime.sleep(0.3)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue8.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green8.value(1)
            condition()
            player1_toggle()
    while led_blue9.value() == 0 and led_green9.value() == 0:
        led_blue9.value(1)
        led_green9.value(1)
        utime.sleep(0.3)
        led_blue9.value(0)
        led_green9.value(0)
        utime.sleep(0.275)
        if button_select.value() == 1:
            break
        if button_ok.value() == 1 and player_1.value() == 1:
            led_blue9.value(1)
            condition()
            player2_toggle()
        if button_ok.value() == 1 and player_2.value() == 1:
            led_green9.value(1)
            condition()
            player1_toggle()
            
starting()                # gmae starting function calling
# infinity loop
while True:
    selection()          