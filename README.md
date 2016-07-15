# ffmpegpy
attempts to build a pipeline approach to extracting video as frames, then do something to the frames then recombine.


Example usage:

    input_folder = 'temp' + str(int(time.time())) + '/'
    output_folder = input_folder[:-1] + '_output/'
    # 'Getting Framerate and instantiating the class'
    f = ffmpeg(video, '-y')
    # 'Dumping video'
    f.dumpFrames(input_folder, '-y')
    # 'Extracting Audio'
    f.extractAudio(video[:-1] + '3', '-y')
    # 
    #perform function on all the frames that you want.
    
    # 'Combining the frames we have processed and making a video
    f.combineFrames(video[:-4] + '_mosiac'  + input_folder[4:-1] + '.mp4', path=output_folder,force ='-y')
