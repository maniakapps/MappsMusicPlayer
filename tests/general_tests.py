import os
import unittest


class GeneralTests(unittest.TestCase):

    @staticmethod
    def test_renaming():
        file = r"C:\Users\MAPC\PycharmProject\MappsMusicPlayer2\tests\testfiles\testfile.txt"
        newname = "Eddie Vedder - Long Nights"
        filename, ext = os.path.splitext(file)
        os.rename(file, os.path.dirname(file) + os.sep + newname + ext)
        assert r"C:\Users\MAPC\PycharmProject\MappsMusicPlayer2\tests\testfiles\testfile.txt" != os.path.dirname(
            filename)
