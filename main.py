import time
from threading import Event, Thread

from luma.core.interface.serial import parallel
from luma.oled.device import ws0010

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
while True:
	set_state(states.IDLE)
	time.sleep(2)
	set_state(states.HAPPY)
	time.sleep(2)
	set_state(states.SAD)
	time.sleep(2)
	set_state(states.CRY)
	time.sleep(2)
	set_state(states.SHOCK)
	time.sleep(2)
	set_state(states.SLEEP)
	time.sleep(2)
	set_state(states.WINK)
	time.sleep(2)
	set_state(states.CONFUSED)
	time.sleep(2)
	set_state(states.SMIRK)
	time.sleep(2)
	set_state(states.DEAD)
	time.sleep(2)
	set_state(states.ANGRY)
	time.sleep(2)
	set_state(states.LAUGH)
	time.sleep(2)
	set_state(states.LOL)
	time.sleep(2)
	set_state(states.KISS)
	time.sleep(2)
	set_state(states.COOL)
	time.sleep(2)
	set_state(states.WORRIED)
	time.sleep(2)
	set_state(states.ANIME)
	time.sleep(2)
	set_state(states.MONEY)
	time.sleep(2)
	set_state(states.OWO)
	time.sleep(2)
	set_state(states.LOOKING)
	time.sleep(2)
