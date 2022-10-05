import random
from typing import List, Union

from mappsmusicplayer.models import SongModel


class Stack:
    """
    Stack class
    """

    def __init__(self, limit: int = None):
        if isinstance(limit, int):
            self._limit = limit
        self._items = []

    def is_empty(self) -> bool:
        """Checks whether the stack is empty or not"""
        return self._items == []

    def push(self, item):
        """
        Push an item into the stack
        :param item the item to push
        """
        if self.size() < self._limit:
            self._items.append(item)

    def pop(self):
        """Removes the top item in thestack"""
        return self._items.pop()

    def peek(self):
        """Returns the element in the top of the stack"""
        return self._items[len(self._items) - 1]

    def size(self) -> int:
        """Returns the size of the Stack"""
        return len(self._items)

    def limit(self) -> int:
        """Returns the Stack limit size"""
        return self._limit


class MusicQueue:
    """
    A music queue which acts like every other MusicQueue
    It keeps a pointer to the current song

    Attributes:
        _pointer    Points to the current index of the queue

    """

    def __init__(self, songs=None, limit=30):
        if isinstance(limit, int):
            self._limit = limit
        self._pointer = 0
        if isinstance(songs, list) and len(songs) > 0:
            self._queue = songs  # type: List[SongModel]
            self._played_songs = []
        else:
            self._queue = []

    def add(self, song: SongModel):
        """Inserts a song into the song queue"""
        self._queue.append(song)
        if self.size() > self._limit:
            # if the queue is too big then remove the first played item
            del self._queue[0]

    def add_next(self, song: SongModel):
        """Adds the next song to play"""
        self._queue.insert(self._pointer + 1, song)
        # if the list is too big then remove the first item in the list, which was played first
        if self.size() > self._limit:
            del self._queue[0]

    def next(self) -> Union[SongModel, None]:
        """returns the next song"""
        if self._pointer + 1 < len(self._queue):
            self._pointer += 1
            return self.current()
        return None

    def has_next(self) -> bool:
        """Checks whether there is a next song"""
        if self._pointer + 1 < len(self._queue):
            return True
        return False

    def previous(self) -> Union[SongModel, None]:
        """Returns the previous song"""
        if self._pointer - 1 >= 0:
            self._pointer -= 1
            return self.current()
        return None

    def has_previous(self) -> bool:
        """Checks whether there is a previous song"""
        if self._pointer - 1 >= 0:
            return True
        return False

    def current(self) -> Union[SongModel, None]:
        """Returns the current song"""
        if len(self._queue) > 0:
            self._played_songs.append(self._pointer)
            return self._queue[self._pointer]
        return None

    def size(self) -> int:
        """
        Returns the size of the queue
        :return int siz of the queue
        """
        return len(self._queue)

    @staticmethod
    def _generate_random(start, stop):
        return random.randrange(start, stop)

    def shuffle(self):
        """Shuffles the current queue"""
        # When using random it is possible an earlier track gets returned
        self._pointer = self._generate_random(0, len(self._queue))
        # Checks whether the random song has been played yet or not
        if self._pointer in self._played_songs:
            self._pointer = self._generate_random(0, len(self._queue))
        return self.current()

    def clear(self):
        """Clears the songs in the list"""
        self._queue.clear()
        self._pointer = 0

    def __repr__(self):
        return str(self._queue)

    def latest(self, song: SongModel):
        """Adds the song as the last song"""
        self.add(song)
        self._pointer = len(self._queue) - 1

    def replace_all(self, songlist: List[SongModel], pointer: int):
        """Replaces all songs"""
        self._queue = songlist
        if 0 < pointer < len(songlist):
            self._pointer = pointer
        else:
            self._pointer = 0
