from colorama import Fore

COLOR = {
    'blue': Fore.BLUE,
    'default': Fore.WHITE,
    'grey': Fore.LIGHTBLACK_EX,
    'yellow': Fore.YELLOW,
    'black': Fore.BLACK,
    'cyan': Fore.CYAN,
    'green': Fore.GREEN,
    'magenta': Fore.MAGENTA,
    'white': Fore.WHITE,
    'red': Fore.RED
}


class Log:
    def importLibs(self):
        from src.config import Config
        from src.date import Date
        self.config = Config().read()
        self.date = Date()

    def console(self, message, emoji=False, color='default'):
        self.importLibs()
        color_formatted = COLOR.get(color.lower(), COLOR['default'])

        formatted_datetime = self.date.dateFormatted()
        console_message = "{} - {}".format(formatted_datetime, message)
        console_message_colorfull = color_formatted + message + Fore.RESET

        if self.config['app']['terminal_colorful'] is True:
            console_message = "{} - {}".format(
                formatted_datetime, console_message_colorfull)

        if emoji is not None and emoji is not False and self.config['app']['emoji'] is True:
            console_message = "{} - {} {}".format(
                formatted_datetime, emoji, message)

            if self.config['app']['terminal_colorful'] is True:
                console_message = "{} - {} {}".format(
                    formatted_datetime, emoji, console_message_colorfull)

        print(console_message)
        return True
