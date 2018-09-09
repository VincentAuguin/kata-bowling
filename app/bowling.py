from abc import ABCMeta, abstractmethod

class BowlingGame(object):

    def __init__(self):
        self.frames = {}

    def open_frame(self, firstThrow, secondThrow):
        self.__add_frame__(OpenFrame(firstThrow, secondThrow))

    def spare(self, firstThrow, secondThrow):
        self.__add_frame__(SpareFrame(firstThrow, secondThrow))

    def strike(self):
        self.__add_frame__(StrikeFrame())

    def __add_frame__(self, frame):
        next_throw = self.__throws_count__() + 1
        self.frames[next_throw] = frame

        # if it is not the first throw
        previous_throw = next_throw - 1
        if previous_throw > 0:
            previous_frame = self.frames[previous_throw]
            if isinstance(previous_frame, FutureFrame):
                previous_frame.next_frame = frame

    def __throws_count__(self):
        return len(self.frames.keys())

    def score(self):
        score = 0
        for frame in self.frames.values():
            score += frame.score()

        return score

class Frame:
    __metaclass__ = ABCMeta

    def __init__(self, first, second):
        self.first = first
        self.second = second

    @abstractmethod
    def score(self):
        pass

class OpenFrame(Frame):

    def score(self):
        return self.first + self.second

class FutureFrame(Frame):
    __metaclass__ = ABCMeta
    next_frame = None

class SpareFrame(FutureFrame):

    def score(self):
        if self.next_frame:
            return 10 + self.next_frame.first

class StrikeFrame(FutureFrame):

    def __init__(self):
        self.first = 10
        self.second = 0
    
    def score(self):
        if self.next_frame:
            return 10 + self.next_frame.first + self.next_frame.second