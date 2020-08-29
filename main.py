import time
from threading import Event, Thread

from luma.core.interface.serial import parallel
from luma.oled.device import ws0010

import states
from animations import blink, cry, sleep
from emotions import happy, sad, shock, wink

event = Event()

# Change the state to an emotion or animation
def set_state(state):
	event.set()
	time.sleep(.5)

	event.clear()
	t = Thread(target=globals()[state].play, args=[d, event])
	t.start()

p = parallel(RS=7, E=8, PINS=[25,24,23,27])
d = ws0010(p, selected_font=0)
d.text = 'Welcome to Bit\nNow loading...'
time.sleep(.3)
set_state(states.WINK)
