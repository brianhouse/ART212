from aio_helper import *

def setup():
    global start_time, value
    size(800, 600)
    background(255)
    start_time = 0
    value = 0

def draw():
    global start_time, value
    elapsed_time = time.time() - start_time
    if elapsed_time > 15:
        start_time = elapsed_time

    # data = pull_data("hall-sensor", now-360000, now)
    # data = pull_data("temperature", 1644308086, 1644390886)# print(data)    

    # last_data_point = data[-1]
    # value = data['value']
    
        value = random(30, 80)
    
    min_value = 30 # degrees fahrenheit
    max_value = 80
    
    interp = map(value, min_value, max_value, 0, 1)
    
    noStroke()
    c = lerpColor(color(0, 0, 255), color(255, 0, 0), interp)
    fill(c)
    rect(0, 0, width, height)

#     # could be the speed of something
#     # could be the number of agents
#     # could just show on or off (get last datapoint)
