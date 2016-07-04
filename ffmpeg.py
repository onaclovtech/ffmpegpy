import re
import subprocess
import pipes
import os
class ffmpeg:
    
    def getFrameRate(self, filename):
      temp = ''
      path = os.path.dirname(os.path.realpath(__file__))
      path = '\ '.join(path.split(' '))+ '/' + filename
      try:
         temp = subprocess.check_output(['ffmpeg -i ' + path], stderr=subprocess.STDOUT,shell=True)
         # we will expect this to fail, so we'll get data from the exception handler.
         return None
      except subprocess.CalledProcessError as e:
            results = e.output
            match = re.search(r', (\d+(.\d+)?) fps', results)
            if match:
               return match.group(1)
            
    def __init__ (self,filename):
      self.filename = '\ '.join(filename.split(' '))
      self.framerate = self.getFrameRate(self.filename)
      if self.framerate is None:
            raise ValueError("Can't find framerate")
      print self.framerate
      
    def dumpFrames(self, path):
      self.path = path
      try:
         subprocess.check_output(['ffmpeg -i ' + self.filename + ' ' + path + '/Pictures%d.jpg'], stderr=subprocess.STDOUT,shell=True)
      except subprocess.CalledProcessError as e:
            print e.output
      
    def extractAudio(self,output_filename_and_path):
      # Based on this: ffmpeg -i Video.mpg -q:a 0 -map a audio.mp3
      self.audio_file = output_filename_and_path
      subprocess.check_output(['ffmpeg -i ' + self.filename + '-q:a 0 -map a ' + output_filename_and_path], stderr=subprocess.STDOUT,shell=True)
      except subprocess.CalledProcessError as e:
            print e.output
    
    def combineFrames(self, output_filename_and_path):
      print output_filename_and_path
      subprocess.check_output(['ffmpeg', '-framerate', self.framerate, '-i', self.path + 'Pictures%d.jpg', '-i',
                                self.audio_file, '-c:v', 'libx264', '-profile:v', 'high', '-crf', '20', '-pix_fmt',
                                'yuv420p', output_filename_and_path])

