import time
from threading import Event, Thread

from luma.core.interface.serial import parallel
from luma.oled.device import ws0010

import face_tracking

import states
from emotions import *

event = Event()

# Change the state to an emotion or animation
def set_state(state=states.IDLE):
	event.set()
	time.sleep(.1)
	d.clear()

	event.clear()
	t = Thread(target=globals()[state].play, args=[d, event])
	t.start()

p = parallel(RS=7, E=8, PINS=[25,24,23,27])
d = ws0010(p, selected_font=0)
d.text = 'Welcome to Bit\nNow loading...'

time.sleep(1)

set_state(states.FACE_TRACKING)
