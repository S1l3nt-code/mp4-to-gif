import ffmpeg
import os

def video_to_gif():
    for file in os.listdir('videos'):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split('.')[0]
            gif_name = file_name + '.gif'

            stream = ffmpeg.input(f'videos/{file}')
            stream = ffmpeg.filter(stream, 'fps',fps=5)
            stream = ffmpeg.output(stream, f'gifs/{gif_name}')
            ffmpeg.run(stream)
        else:
            print('Wrong file extention')

def main():
    video_to_gif()

if __name__ == '__main__':
    main()