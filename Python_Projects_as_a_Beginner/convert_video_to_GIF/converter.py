#execute "pip install moviepy" and import to the project
from moviepy.editor import *

video = VideoFileClip("My_Video.mp4")
video.write_gif("My_Video.gif")