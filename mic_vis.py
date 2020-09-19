from luma.core.render import canvas
import pyaudio
import numpy as np

RATE = 48000
CHUNK = int(RATE/5) # 5 readings per second

def play(d, event):
	d.text = 'Loading mic...'

	p = pyaudio.PyAudio()
	stream = p.open(
		format=pyaudio.paInt32,
		channels=1,
		rate=RATE,
		input=True,
		frames_per_buffer=CHUNK
	)

	while True:
		# Get frame data
		data = np.frombuffer(stream.read(CHUNK,exception_on_overflow=False),dtype=np.int32)
		fft_data = np.abs(np.fft.rfft(data))
		fft_data = fft_data[:CHUNK] * 2 / (256 * CHUNK)

		# Group ranges into 120 bands
		n = fft_data.size // 120
		bands = [sum(fft_data[i:(i + n)]) for i in range(0, fft_data.size, n)]
		norm = lambda b: min(int((b/3000)*8),8)
		# Remove lowest 10 frequency bands
		bands = list(map(norm, bands[11:111]))

		with canvas(d) as drw:
			x = 0
			for band in bands:
				drw.rectangle((x, 9, x, 9+band), fill='white') #down
				drw.rectangle((x, 8, x, 8-band), fill='white') #up
				x += 1

		if event.is_set():
			stream.stop_stream()
			stream.close()
			p.terminate()
			break
