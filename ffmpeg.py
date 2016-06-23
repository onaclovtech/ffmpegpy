import subprocess

def getFrameRate(self, filename):
  temp = subprocess.check_output(['ffmpeg', '-i', 'filename'])
  print temp
  
def __init__ (filename):
  self.filename = filename
  self.framerate = getFramerate(self.filename)
  
def dumpFrames(self, path):
  self.path = path
  subprocess.check_output(['ffmpeg', '-i', self.filename,  path + 'Pictures%d.jpg'])
  
def extractAudio(self,output_filename_and_path):
  # Based on this: ffmpeg -i Video.mpg -q:a 0 -map a audio.mp3
  self.audio_file = output_filename_and_path
  subprocess.check_output(['ffmpeg', '-i', self.filename, '-q:a', '0', '-map', 'a', output_filename_and_path])

def combineFrames(self, output_filename_and_path):
  subprocess.check_output(['ffmpeg', '-framerate', self.framerate, '-i', path + 'Pictures%d.jpg', '-i', 
                            self.audio_file, '-c:v', 'libx264', '-profile:v', 'high', '-crf', '20', '-pix_fmt', 
                            'yuv420p', output_filename_and_path])
  
  
