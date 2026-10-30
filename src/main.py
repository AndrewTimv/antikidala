# Точка входа

import sys

from loguru import logger

from vk_bot.bot import bot


def main():
    """
    Запуск бота
    """
    args =sys.argv

    if len(args) > 0:
        env_file = args[0]

    bot.run()



if __name__ == '__main__':
    main()
