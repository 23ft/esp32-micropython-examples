import uasyncio
from machine import Pin
import sys


broke = False
button = Pin(4, Pin.IN)


# Task 2
async def buttonStop():
    global broke
    
    buttonPress = 0
    while True:
        if button.value():
            buttonPress += 1
            print("press: ", buttonPress)
            if buttonPress == 5:
                broke = True
                await uasyncio.sleep_ms(300)
                sys.exit()
                
            await uasyncio.sleep(1)
        await uasyncio.sleep_ms(10)
        
        
# Task 1
async def blink(led, period_ms):
    global broke
    print("function main")
    while True:
        if broke:
            print("xd")
            led.off()
            break
        led.on()
        await uasyncio.sleep_ms(3000)
        led.off()
        await uasyncio.sleep_ms(period_ms)
        
        
        
# Bucle de eventos.
async def main(led1, led2, led3):
    print("main")
    
    # create a task a partir de una corrutina dada.
    # with .create_task(corutine)
    #~~~~~
    ## uasyncio.create_task(blink(led1, 1000))
    ## uasyncio.create_task(blink(led2, 1000))
    ## uasyncio.create_task(blink(led3, 1000))
    ## print("change")
    ## await uasyncio.sleep_ms(10_000)
    ## print("endx")
    ## await uasyncio.sleep_ms(10000)
    ## print("popis\n\n")
    ## await uasyncio.sleep_ms(10000)
    
    t1 = blink(led1, 1000)
    t2 = blink(led2, 1000)
    t3 = blink(led3, 1000)
    buttonFunction = buttonStop() 
    
    await uasyncio.gather(t1, t2,t3, buttonFunction)
    print("before await gather")

# Running on a generic board
uasyncio.run(main(Pin(5, Pin.OUT), Pin(2, Pin.OUT), Pin(19, Pin.OUT)))
print("popo")
