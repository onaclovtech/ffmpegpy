# ffmpegpy
attempts to build a pipeline approach to extracting video as frames, then do something to the frames then recombine.


Example usage:

    from ffmpeg import ffmpeg
    # Instantiate the class with the video you want to use.
    f = ffmpeg('Blondie - Heart Of Glass.mp4')
    # Dump our frames to the folder passed in
    f.dumpFrames('ffmpeg_temp')
    # Extract audio from the video and name it as below
    f.extractAudio('blondie.mp3')
    # Recombine the video to an mp4
    f.combineFrames('blondie.mp4')
