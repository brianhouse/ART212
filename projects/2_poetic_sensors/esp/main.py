from esp_helper import *

connect_wifi()

while True:
    hall = esp32.hall_sensor()
    print(hall)
    post_data("hall-sensor", hall)
