from bottle import route, run, template

import wiringpi
import time

GPIO_DICT = {'1':4, '2':17, '3':27}

def gpio_process(led_pin):
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(led_pin, 1)
    wiringpi.digitalWrite(led_pin, 1)

    time.sleep(1)
    wiringpi.digitalWrite(led_pin, 0)

@route('/api/<number>')
def index(number):
    led_pin = GPIO_DICT[number]
    gpio_process(led_pin)

run(host='localhost', port=8080, debug=True, reloader=True)
