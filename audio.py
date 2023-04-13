from moviepy.editor import *




input_file = "Your video"
output_file = "myvoice.wav"
sound = AudioFileClip(input_file)
sound.write_audiofile(output_file, 44100, 2, 2000,"pcm_s32le")