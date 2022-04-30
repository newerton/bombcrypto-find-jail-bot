from colorama import init, Fore, Style

from src.application import Application
from src.log import Log
from src.multi_account import MultiAccount

init()

banner = """
*****************************************************************************************
** BOMBCRYPTO - BOT - FIND JAIL
**
** Please consider buying me a coffee :)
** BCOIN: 0x4847C29561B6682154E25c334E12d156e19F613a
** SEN: 0x4847C29561B6682154E25c334E12d156e19F613a
** PIX: 08912d17-47a6-411e-b7ec-ef793203f836
*****************************************************************************************
** Press CTRL + C to kill the bot.
** Some configs can be found in the https://github.com/newerton/bombcrypto-find-jail-bot
*****************************************************************************************
"""

print(Fore.GREEN + banner + Style.RESET_ALL)

application = Application()
log = Log()
multi_account = MultiAccount()

def main():
    application.start()
    multi_account.botSingle()


if __name__ == '__main__':
    try:
            main()
    except KeyboardInterrupt:
        log.console('Shutting down the bot',
                    services=True, emoji='😓', color='red')
        exit()
