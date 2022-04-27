import os

class Errors:
    def importLibs(self):
        from src.actions import Actions
        from src.auth import Auth
        from src.config import Config
        from src.recognition import Recognition
        from src.images import Images
        from src.log import Log
        self.actions = Actions()
        self.auth = Auth()
        self.config = Config().read()
        self.recognition = Recognition()
        self.images = Images()
        self.log = Log()

    def verify(self):
        self.importLibs()
        thresholdError = self.config['threshold']['error_message']

        title_error = self.images.image('title_error', theme=True)
        ok_button = self.images.image('ok_button')
        connect_wallet_button = self.images.image('connect_wallet_button')

        if self.recognition.positions(title_error, thresholdError) is not False:
            self.log.console('Error detected, trying to resolve', emoji='💥', color='red')
            self.actions.clickButton(ok_button)
            self.actions.refreshPage()
            self.recognition.waitForImage(connect_wallet_button)
            self.auth.login()
        else:
            return False
