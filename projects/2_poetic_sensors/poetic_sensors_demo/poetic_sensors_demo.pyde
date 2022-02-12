from aio_helper import *

data = pull_data("hall-sensor", now-360000, now)

# def setup():
#     global start_time
#     size(800, 600)
#     background(255)
#     start_time = 0

    
# def draw():
#     global start_time
#     elapsed_time = time.time() - start_time
#     if elapsed_time > 15:
#         update()
#         start_time = elapsed_time
    
    
# def update():    
#     data = pull_data("hall-sensor", now-360000, now)

#     strokeWeight(5)
#     beginShape()
#     for datapoint in data:
#         x = map(datapoint['time'], 0, 150, 0, width)
#         y = map(datapoint['value'], 0, 100, 0, height)
#         curveVertex(x, y)
#     endShape()
    
#     # could be the speed of something
#     # could be the number of agents
#     # could just show on or off (get last datapoint)
