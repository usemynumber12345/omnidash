import os
import subprocess
from pathlib import Path
from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment
from PIL import Image

def combine_media(files, output_file):
    video_clips = []
    audio_clips = []
    image_clips = []

    for file in files:
        ext = Path(file).suffix.lower()
        if ext in ['.mp4', '.avi', '.mov']:
            video_clips.append(VideoFileClip(file))
        elif ext in ['.mp3', '.wav', '.aac']:
            audio_clips.append(AudioSegment.from_file(file))
        elif ext in ['.jpg', '.png', '.jpeg']:
            image_clips.append(Image.open(file))

    if video_clips:
        combined_video = concatenate_videoclips(video_clips)
        combined_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
    elif audio_clips:
        combined_audio = sum(audio_clips)
        combined_audio.export(output_file, format="mp3")
    elif image_clips:
        image_clips[0].save(output_file, save_all=True, append_images=image_clips[1:])
    else:
        print("No compatible media files found.")

def main():
    input_folder = input("Enter the path to the folder containing media files: ")
    output_file = input("Enter the output file name with extension: ")

    files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    combine_media(files, output_file)
    print(f"Combined media file created at {output_file}")

if __name__ == "__main__":
    main()