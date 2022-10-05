try:
    from setuptools import setup, find_packages
except ImportError as e:
    from distutils.core import setup

__version__ = "1.0.0-alpha"

config = {
    'name': 'mapps-music-player',
    'version': __version__,
    'description': 'Remote music player',
    'long_description': open('README.md').read(),
    'author': 'Manuel Pizano',
    'author_email': 'manuel_pizano@gmx.us',
    'classifiers': [
        'Development Status :: 1 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Private',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    'url': 'https://bit.ly/3S7RKwI',
    'download_url': 'https://github.com/MelleDijkstra/PythonMusicPlayer',
    'license': 'MIT',
    'install_requires': [
        'typing==3.7.4.3',
        'youtube-dl-2021.12.17',
        'python_vlc==3.0.101',
        'setuptools==38.4.0',
        'tinytag==0.18.0',
        'grpcio==1.8.4',
        'grpcio-tools==1.8.4',
        'protobuf==4.21.7',
        'mutagen==1.40.0',
        'google==3.0.0',
        'tox==3.26.0',
    ],
    'packages': find_packages(exclude=['docs', 'tests']),
}

setup(**config)
