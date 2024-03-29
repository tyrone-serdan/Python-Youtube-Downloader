import pytube as yt
# from re import match
import requests
import os


DEFAULT_PATH = os.path.join(os.environ['USERPROFILE'], 'Downloads')

def obtain_video_data(video: yt.YouTube) -> list:
    video_data = [
        video.thumbnail_url,
        remove_special_characters(video.title),
        video.author
    ]

    return video_data

def remove_special_characters(string: str) -> list:
    # TODO: add support for removing
    # emojis from title
    special_characters = set(r'/\:*?"<>| ')

    for character in special_characters:
        string = string.replace(character, "-")
        
    return string

# def is_valid_url(url: str):
#     REGEX = (
#         r'(https?://)?(www\.)?'
#         '(youtube|youtu|youtube-nocookie)\.(com|be)/'
#         '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
#     )

#     return match(REGEX, url) is not None


class Video:
    def __init__(self, url: str, download_path: str = None):
        self.video = yt.YouTube(url=url)
        self.data = obtain_video_data(self.video)
        self.path = download_path if download_path else DEFAULT_PATH

    def update_download_path(self, new_path: str):
        self.path = new_path

    def download_video(self):
        self.video.streams.first().download(output_path=self.path)
        os.startfile(self.path)

    def download_thumbnail(self):
        thumbnail_url: str = self.data[0]
        file_name: str = self.data[1]
        file_name = file_name.replace(" ", "-")

        thumbnail_path = f"{os.getcwd()}\\thumbnails\\{file_name}.jpg"

        image_data = requests.get(thumbnail_url).content
        saved_image = open(thumbnail_path, 'wb')
        saved_image.write(image_data)
        saved_image.close()

        return thumbnail_path


