from cv2 import cv2

import pyautogui
import random
import time


class Actions:
    def importLibs(self):
        from src.config import Config
        from src.log import Log
        from src.recognition import Recognition
        self.config = Config().read()
        self.log = Log()
        self.recognition = Recognition()

    def click(self, x, y, movementInSeconds=0.5, forceTime=False):
        self.importLibs()
        if forceTime == False:
            movementInSeconds = 0.2
        pyautogui.click(x, y, duration=movementInSeconds)

    def clickButton(self, image, name=None, timeout=3, threshold=None):
        self.importLibs()
        if(threshold == None):
            threshold = self.config['threshold']['default']

        if not name is None:
            pass

        start = time.time()
        clicked = False
        while(not clicked):
            matches = self.recognition.positions(image, threshold=threshold)
            if(matches is False):
                hast_timed_out = time.time()-start > timeout
                if(hast_timed_out):
                    if not name is None:
                        pass
                    return False
                continue

            x, y, w, h = matches[0]
            self.click(int(x+(w/2)), int(y+(h/2)))
            return True

    def move(self, x, y, movementInSeconds=1, forceTime=False):
        self.importLibs()
        if forceTime == False:
            movementInSeconds = 0.2
        pyautogui.moveTo(x, y, movementInSeconds,
                         tween=pyautogui.easeInOutQuad)

    def sleep(self, min, max, forceTime=False):
        self.importLibs()
        sleep = random.uniform(min, max)
        if forceTime == False:
            sleep = 0
        return time.sleep(sleep)

    def refreshPage(self):
        self.importLibs()
        self.log.console('Refreshing page', emoji='🔃', color='green')
        pyautogui.hotkey('ctrl', 'shift', 'r')

    def show(self, img):
        cv2.imshow('img', img)
        cv2.waitKey(0)
