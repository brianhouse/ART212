# Data Visualization Basics


## Setup

Open a new Processing sketch in Python mode and save it. Then, download [aio_helper.py](poetic_sensors_demo/aio_helper.py) and add it to the sketch.

In addition, create a new tab by clicking on the down arrow next to the open filename, call it "credentials.py", and include the following:

```py
AIO_USERNAME = "h0use"
AIO_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # <-- your key here
```

## Pulling Data

In your sketch, try the following:

```py
from aio_helper import *

data = pull_data("hall-sensor", now-360000, now)
```
You should see this in your console:
```
Pulling data...
--> success
```

The `pull_data` function connects to AIO and downloads all the sensor data between the start time and the end time. Here, the start time is "now-360000", which means the present time minus 360,000 seconds, which is 10 hours. The end time is simply "now". So every time this sketch is run, it will pull the most recent 10 hours worth of data.

`now` lets us work with relative time in this way. But we can also give the function absolute timestamps. Use this site to convert from "human" dates to a timestamp that the computer can understand: https://www.epochconverter.com

**Remember not to pull data more than every couple seconds.** More on this later.

## Map
