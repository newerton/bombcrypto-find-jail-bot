class TreasureHunt:
    def importLibs(self):
        from src.actions import Actions
        from src.auth import Auth
        from src.desktop import Desktop
        from src.images import Images
        from src.log import Log
        from src.recognition import Recognition
        self.actions = Actions()
        self.auth = Auth()
        self.desktop = Desktop()
        self.images = Images()
        self.recognition = Recognition()
        self.log = Log()

    def goToMap(self):
        self.importLibs()
        currentScreen = self.recognition.currentScreen()

        treasure_hunt_banner = self.images.image('treasure_hunt_banner')
        close_button = self.images.image('close_button')

        self.log.console('Entering treasure hunt', emoji='▶️', color='yellow')

        if currentScreen == "main":
            self.actions.clickButton(treasure_hunt_banner)
        if currentScreen == "character":
            if self.actions.clickButton(close_button):
                self.actions.clickButton(treasure_hunt_banner)
        if currentScreen == "unknown":
            self.auth.checkLogout()
        self.actions.sleep(1, 1, forceTime=True)


    def findJail(self):
        self.importLibs()
        chest_jail_closed = self.images.image(
            'chest_jail_closed', newPath='./images/themes/default/chests/')

        screenshot = self.desktop.printScreen()
        jail = self.recognition.positions(chest_jail_closed, 0.7, screenshot)
        if jail is not False:
            self.log.console(f'Jail found', emoji='🎉', color='green')
            return True

        return False
