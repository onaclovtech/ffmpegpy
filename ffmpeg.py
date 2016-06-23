import subprocess

class ffmpeg:
    
    def getFrameRate(self, filename):
      print filename
      temp = ''
      temp = subprocess.call(['ffmpeg', '-i', filename], shell=True)
      print temp
      
    def __init__ (self,filename):
      self.filename = filename
      self.framerate = self.getFrameRate(self.filename)
      
    def dumpFrames(self, path):
      self.path = path
      subprocess.check_output(['ffmpeg', '-i', self.filename,  path + 'Pictures%d.jpg'])
      
    def extractAudio(self,output_filename_and_path):
      # Based on this: ffmpeg -i Video.mpg -q:a 0 -map a audio.mp3
      self.audio_file = output_filename_and_path
      subprocess.check_output(['ffmpeg', '-i', self.filename, '-q:a', '0', '-map', 'a', output_filename_and_path])
    
    def combineFrames(self, output_filename_and_path):
      subprocess.check_output(['ffmpeg', '-framerate', self.framerate, '-i', self.path + 'Pictures%d.jpg', '-i', 
                                self.audio_file, '-c:v', 'libx264', '-profile:v', 'high', '-crf', '20', '-pix_fmt', 
                                'yuv420p', output_filename_and_path])
