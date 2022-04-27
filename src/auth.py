import pyautogui
import os

login_attempts = 0


class Auth:
    def importLibs(self):
        from src.actions import Actions
        from src.error import Errors
        from src.images import Images
        from src.recognition import Recognition
        from src.log import Log
        self.actions = Actions()
        self.errors = Errors()
        self.images = Images()
        self.recognition = Recognition()
        self.log = Log()

    def login(self):
        global login_attempts
        self.importLibs()

        connect_wallet_button = self.images.image('connect_wallet_button')
        connect_metamask_button = self.images.image('connect_metamask_button')
        metamask_sign_button = self.images.image('metamask_sign_button')
        metamask_unlock_button = self.images.image('metamask_unlock_button')
        treasure_hunt_banner = self.images.image('treasure_hunt_banner')

        if self.actions.clickButton(connect_wallet_button):
            self.log.console(
                'Connect game button detected', emoji='👍', color='green')
            self.actions.sleep(1, 2)
            self.recognition.waitForImage(connect_metamask_button)

        if self.actions.clickButton(connect_metamask_button):
            self.log.console(
                'Connect metamask button detected, logging in!', emoji='🎉', color='green')
            self.actions.sleep(1, 2)
            self.recognition.waitForImage(
                (metamask_sign_button, metamask_unlock_button), multiple=True)

        metamask_unlock_coord = self.recognition.positions(
            metamask_unlock_button)
        if metamask_unlock_coord is not False:
            self.log.console(
                'Metamask locked! But login with password is disabled, exiting', emoji='🔒', color='red')
            exit()

        if self.actions.clickButton(metamask_sign_button):
            self.log.console(
                'Found sign button. Waiting to check if logged in', emoji='✔️', color='green')
            self.actions.sleep(5, 7, forceTime=True)

            if self.actions.clickButton(metamask_sign_button):
                self.log.console(
                    'Found glitched sign button. Waiting to check if logged in', emoji='✔️', color='yellow')
            self.recognition.waitForImage(treasure_hunt_banner, timeout=30)
            self.errors.verify()

        if self.recognition.currentScreen() == "main":
            self.log.console('Logged in', emoji='🎉', color='green')
            return True
        else:
            self.log.console('Login failed, trying again',
                             emoji='😿', color='red')
            login_attempts += 1

            if (login_attempts > 2):
                self.log.console('+3 login attempts, retrying',
                                 emoji='🔃', color='red')
                login_attempts = 0
                self.errors.verify()
                self.actions.refreshPage()
                self.actions.sleep(1, 1, forceTime=True)
            self.login()

        self.errors.verify()

    def checkLogout(self):
        self.importLibs()

        connect_wallet_button = self.images.image('connect_wallet_button')
        metamask_cancel_button = self.images.image('metamask_cancel_button')
        metamask_sign_button = self.images.image('metamask_sign_button')

        currentScreen = self.recognition.currentScreen()
        if currentScreen == "unknown":
            if self.recognition.positions(connect_wallet_button) is not False:
                self.log.console('Logout detected', emoji='😿', color='red')
                self.actions.refreshPage()
                self.actions.sleep(4, 4, forceTime=True)
                self.recognition.waitForImage(connect_wallet_button)
                self.login()
            elif self.recognition.positions(metamask_sign_button):
                self.log.console('Sing button detected',
                                 emoji='✔️', color='green')
                if self.actions.clickButton(metamask_cancel_button):
                    self.log.console(
                        'Metamask is glitched, fixing', emoji='🙀', color='yellow')
            else:
                return False

        else:
            return False
