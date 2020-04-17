import pyautogui as auto
import time as t
import random
import sys


class Tinder_bot:
    def __init__(self, swipe_number):
        self.constant = 0.008
        self.stepsize_vals = (19, 50)
        self.thirstiness = 2
        self.swipe_number = swipe_number

    def _sleeper(self):
        return t.sleep(self.constant * random.randint(self.stepsize_vals[0], self.stepsize_vals[1]))

    def _spacing(self):
        for i in range(0, random.randint(0, self.thirstiness)):
            self._sleeper()
            auto.press('space')

    def _reject(self):
        self._sleeper()
        auto.press('left')

    def swipe(self):
        for i in range(0, self.swipe_number):
            self._spacing()
            self._sleeper()
            auto.press('right')
            self._sleeper()

        print('I swiped {} times before swiping left'.format(self.swipe_number))


if __name__ == "__main__":
    swipes = int(sys.argv[1])
    loops = int(sys.argv[2])
    a = Tinder_bot(swipes)
    for k in range(0, loops):
        a.swipe()
        a._reject()
