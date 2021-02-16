import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("Paramore Decode.mp4"))
video.audio.write_audiofile(os.path.join("Paramore.mp3"))
