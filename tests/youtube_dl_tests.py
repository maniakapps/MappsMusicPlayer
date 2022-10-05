from __future__ import unicode_literals

import unittest

import youtube_dl


class YTDLLogger(object):
    def debug(self, msg):
        # print(msg)
        pass

    def warning(self, msg):
        # print(msg)
        pass

    @staticmethod
    def error(msg):
        print(msg)


def my_hook(d):
    print(d)
    if d['status'] == 'finished':
        print('Done downloading, now converting...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': YTDLLogger(),
    'progress_hooks': [my_hook],
}


class YouttubeDLTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def test_download_mp3():
        pass
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc', 'https://www.youtube.com/watch?v=bk6Xst6euQk'])

    @staticmethod
    def test_invalid_url():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://invalidauDlnn.com/watch?v=d89a8D89'])
        except youtube_dl.DownloadError as e:
            print("Download Error (which is good :p)")

    @staticmethod
    def test_soundcloud_download():
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(['https://soundcloud.com/mattkali/starboy-matt-kali-remix'])
        except youtube_dl.DownloadError as e:
            print(str(e))


if __name__ == '__main__':
    unittest.main()
