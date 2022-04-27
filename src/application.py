import pyautogui


class Application:
    def importLibs(self):
        from src.actions import Actions
        from src.images import Images
        from src.log import Log
        from src.recognition import Recognition
        self.actions = Actions()
        self.images = Images()
        self.log = Log()
        self.recognition = Recognition()

    def start(self):
        self.importLibs()
        pyautogui.FAILSAFE = False
        input('Press Enter to start the bot...\n')
        self.log.console('Starting bot...', emoji='🤖', color='green')

    def createNewAccount(self):
        self.importLibs()
        option_networks = self.images.image('option_networks')

        if self.clickAndWaitNextImage(clickImage='app_metamask_button', nextImage='option_networks', textClickImage="App Metamask", textNextImage="Option Network") is True:
            option_networks_position = self.recognition.positions(
                option_networks, returnArray=True)

            if option_networks_position is not False:
                [option_network_x, option_network_y,
                    _, _] = option_networks_position[0]
                x = option_network_x + 60
                y = option_network_y + 15
                self.actions.move(x, y)
                self.actions.click(x, y)

            create_account_button = self.images.image('create_account_button')
            if self.recognition.waitForImage(create_account_button, timeout=30) is not True:
                return False
            if self.clickAndWaitNextImage(clickImage='create_account_button', nextImage='create_button', textClickImage="[+ Create Account]", textNextImage="Create Button") is not True:
                return False
            if self.clickAndWaitNextImage(clickImage='create_button', nextImage='not_connected_status', textClickImage="Create Button", textNextImage="Not connected status") is not True:
                return False
            if self.clickAndWaitNextImage(clickImage='not_connected_status', nextImage='connect_link', textClickImage="Not connected status", textNextImage="Connect link") is not True:
                return False
            if self.clickAndWaitNextImage(clickImage='connect_link', nextImage='close_submodal_metamask', textClickImage="Connect link", textNextImage="Close submodal") is not True:
                return False

            close_submodal_metamask = self.images.image(
                'close_submodal_metamask')
            if self.actions.clickButton(close_submodal_metamask) is not True:
                return False

            app_metamask_button = self.images.image('app_metamask_button')
            if self.actions.clickButton(app_metamask_button) is not True:
                return False

            connect_wallet_button = self.images.image('connect_wallet_button')
            if self.recognition.waitForImage(connect_wallet_button, timeout=60) is not True:
                return False

            return True

    def clickAndWaitNextImage(self, clickImage, nextImage, textClickImage, textNextImage):
        click_image = self.images.image(clickImage)
        click_image_position = self.recognition.positions(click_image)
        if click_image_position is not False:
            if self.actions.clickButton(click_image) is True:
                next_image = self.images.image(nextImage)
                if self.recognition.waitForImage(next_image, timeout=60) is True:
                    return True
                else:
                    self.log.console("{} not found [waitForImage]".format(
                        textNextImage), emoji='❌', color='red')
                    return False
            else:
                self.log.console("{} not clicked [clickButton]".format(
                    textClickImage), emoji='❌', color='red')
                return False
        else:
            self.log.console("{} not found [positions]".format(
                textClickImage), emoji='❌', color='red')
            return False
