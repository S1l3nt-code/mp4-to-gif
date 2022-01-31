import ffmpeg
import os


def video_to_gif():
    user_w = input('Enter width of gif: ')
    user_h = input('Enter height of gif: ')
    user_fps = input('Enter fps: ')
    for file in os.listdir('videos'):
        if file.endswith((".mp4", ".MP4")):
            file_name = file.split('.')[0]
            gif_name = file_name + '.gif'

            stream = ffmpeg.input(f'videos/{file}')
            stream = ffmpeg.trim(stream, start = 0, duration = 10)
            stream = ffmpeg.filter(stream, 'fps',fps= user_fps).filter('scale', w=user_w, h=user_h)
            stream = ffmpeg.output(stream, f'gifs/{gif_name}')
            ffmpeg.run(stream)
        else:
            print('Wrong file extention')

def main():
    video_to_gif()

if __name__ == '__main__':
    main()