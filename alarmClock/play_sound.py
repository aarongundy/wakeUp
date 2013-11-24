# """PyAudio Example: Play a WAVE file."""

# import pyaudio
# import wave
# import sys
# import os

# # class audio(object):
# # 	"""docstring for ClassName"""
# # 	def __init__(self, file):
# # 		super(ClassName, self).__init__()
# # 		self.file = file

# def playFile(file):	
# 	CHUNK = 1024

# 	# if len(sys.argv) < 2:
# 	#     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
# 	#     sys.exit(-1)

# 	wf = wave.open(file, 'rb')

# 	p = pyaudio.PyAudio()

# 	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
# 	                channels=wf.getnchannels(),
# 	                rate=wf.getframerate(),
# 	                output=True)

# 	data = wf.readframes(CHUNK)

# 	while data != '':
# 	    stream.write(data)
# 	    data = wf.readframes(CHUNK)

# 	stream.stop_stream()
# 	stream.close()

# 	p.terminate()
"""
This code is modified from this gist: https://gist.github.com/THeK3nger/3624478
"""
import os
import wave
import threading
# import sys
 
# PyAudio Library
import pyaudio
 
class playAlarmLoop(threading.Thread) :
	"""
	A simple class based on PyAudio to play wave loop.

	It's a threading class. You can play audio while your application
	continues to do its stuff. :)
	"""

	CHUNK = 1024

	def __init__(self,filepath):
		"""
		Initialize `WavePlayerLoop` class.

		PARAM:
		    -- filepath (String) : File Path to wave file.
		    -- loop (boolean)    : True if you want loop playback. 
		                           False otherwise.
		"""
		super(playAlarmLoop, self).__init__()
		self.filepath = filepath #os.path.abspath(filepath)
		self.loop = True

	def run(self):
	# Open Wave File and start play!
		wf = wave.open(self.filepath, 'rb')
		player = pyaudio.PyAudio()

		# Open Output Stream (basen on PyAudio tutorial)
		stream = player.open(format = player.get_format_from_width(wf.getsampwidth()),
		    channels = wf.getnchannels(),
		    rate = wf.getframerate(),
		    output = True)

		# PLAYBACK LOOP
		data = wf.readframes(self.CHUNK)
		while self.loop :
		  stream.write(data)
		  data = wf.readframes(self.CHUNK)
		  if data == '' : # If file is over then rewind.
		    wf.rewind()
		    data = wf.readframes(self.CHUNK)

		stream.close()
		player.terminate()


	def play(self) :
		"""
		Just another name for self.start()
		"""
		self.start()

	def stop(self) :
		"""
		Stop playback. 
		"""
		self.loop = False

if __name__ == "__main__":
    play = playAlarmLoop("bomb_siren.wav")
    play.start()
    into = raw_input("Enter Command: ")
    if into == 'q':
    	play.stop()