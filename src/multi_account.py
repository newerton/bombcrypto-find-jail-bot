import sys


class MultiAccount:
    def importLibs(self):
        from src.actions import Actions
        from src.application import Application
        from src.auth import Auth
        from src.error import Errors
        from src.recognition import Recognition
        from src.treasure_hunt import TreasureHunt
        self.actions = Actions()
        self.application = Application()
        self.auth = Auth()
        self.errors = Errors()
        self.recognition = Recognition()
        self.treasure_hunt = TreasureHunt()

    def botSingle(self):
        self.importLibs()
        while True:
            self.steps()

    def steps(self):
        currentScreen = self.recognition.currentScreen()

        if currentScreen == "login":
            self.auth.login()

        self.errors.verify()

        if currentScreen == "main":
            self.treasure_hunt.goToMap()

        if currentScreen == "treasure_hunt":
            if self.treasure_hunt.findJail() is True:
                exit()
            else:
                if self.application.createNewAccount() is False:
                    self.actions.refreshPage()

        self.auth.checkLogout()
        sys.stdout.flush()
        self.actions.sleep(1, 1)
