# Основной обработчик событий

from vkbottle.bot import BotLabeler, Message


main_labeler = BotLabeler


@main_labeler.message()
async def find_cheater_handler(message: Message):
    """
    Поиск кидалы по тексту
    """
    user_text = message.text