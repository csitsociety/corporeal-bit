from luma.core.interface.serial import parallel
from luma.oled.device import ws0010
from luma.core.render import canvas

p = parallel(RS=7, E=8, PINS=[25,24,23,27])
d = ws0010(p, selected_font='FT01')

# Draw a simple face
with canvas(d) as drw:
	drw.rectangle((43, 10, 44, 11), fill='white')
	drw.rectangle((45, 12, 54, 13), fill='white')
	drw.rectangle((55, 10, 56, 11), fill='white')
	drw.rectangle((18, 2, 27, 10),  fill='white')
	drw.rectangle((72, 2, 81, 10),  fill='white')
