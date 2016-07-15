import re
import subprocess
import pipes
import os
class ffmpeg:
    
    def getFrameRate(self, filename, force=''):
      temp = ''
      path = os.path.dirname(os.path.realpath(__file__)).strip('ffmpegpy')
      path = '\ '.join(path.split(' '))+ '/' + filename
      try:
         print 'ffmpeg ' + force + ' -i ' + path
         temp = subprocess.check_output(['ffmpeg ' + force + ' -i ' + path], stderr=subprocess.STDOUT,shell=True)
         # we will expect this to fail, so we'll get data from the exception handler.
         return None
      except subprocess.CalledProcessError as e:
            results = e.output
            match = re.search(r', (\d+(.\d+)?) fps', results)

            if match:
               return match.group(1)
            
    def __init__ (self,filename, force=''):
      self.filename = '\ '.join(filename.split(' '))
      self.framerate = self.getFrameRate(self.filename, force=force)
      if self.framerate is None:
            raise ValueError("Can't find framerate")
      
    def dumpFrames(self, path, force=''):
      self.path = path
      try:
         if not os.path.exists(path):
            os.mkdir(path)
         subprocess.check_output(['ffmpeg ' + force + ' -i ' + self.filename + ' ' + path + '/Pictures%04d.jpg'], stderr=subprocess.STDOUT,shell=True)
      except subprocess.CalledProcessError as e:
            print 'dumpFrames'
            print e.output
      
    def extractAudio(self,output_filename_and_path, force=''):
      # Based on this: ffmpeg -i Video.mpg -q:a 0 -map a audio.mp3
      self.audio_file = '\ '.join(output_filename_and_path.split(' '))
      try:
         print 'ffmpeg ' + force + ' -i ' + self.filename + ' -q:a 0 -map a ' + self.audio_file
         subprocess.check_output(['ffmpeg ' + force + ' -i ' + self.filename + ' -q:a 0 -map a ' + self.audio_file], stderr=subprocess.STDOUT,shell=True)
      except subprocess.CalledProcessError as e:
            print 'extractAudio'
            print e.output
    
    def combineFrames(self, output_filename_and_path, path = None, audio_file = None, framerate = None, force=''):
      if path is not None:
        self.path = path
      if audio_file is not None:
        self.audio_file = audio_file
      if framerate is not None:
        self.framerate = framerate
      out_file = '\ '.join(output_filename_and_path.split(' '))
      print self.path
      print 'ffmpeg ' + force + ' -framerate ' + self.framerate + ' -i ' + self.path + '/Pictures%04d.jpg' + ' -i ' +       self.audio_file + ' -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p ' + out_file
      try:
         subprocess.check_output(['ffmpeg ' + force + ' -framerate ' + self.framerate + ' -i ' + self.path + '/Pictures%04d.jpg' + ' -i ' +
                                self.audio_file + ' -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p ' + out_file], stderr=subprocess.STDOUT,shell=True)
      except subprocess.CalledProcessError as e:
            print 'combineFrames'
            print e.output
