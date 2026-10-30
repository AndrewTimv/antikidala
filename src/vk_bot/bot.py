# Инициализация бота

from vkbottle.bot import Bot

from vk_bot.settings import settings


bot = Bot(settings.VK_TOKEN.get_secret_value())

@bot.on.message()
async def handler(_) -> str:
    return 'Hello!'
