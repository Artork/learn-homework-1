"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# My_new_planetBOT

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(update, context):
    print('Вызван/start')
   
    print(update)
    update.message.reply_text('Hello World')

def find_constellation (update, context):

  planet_dict = {
    'mercury': ephem.Mercury('2000/01/01'),
    'menus': ephem.Venus('2000/01/01'),
    'moon': ephem.Moon('2000/01/01'),
    'mars': ephem.Mars('2000/01/01'),
    'jupiter': ephem.Jupiter('2000/01/01'),
    'uranus': ephem.Uranus('2000/01/01'),
    'neptune': ephem.Neptune('2000/01/01'),
    'pluto': ephem.Pluto('2000/01/01')
}
  planet = planet_dict[context.args[0].lower()]
  update.message.reply_text(f'планета {context.args[0]} находилась 1 января 2000 года в созвездии {(ephem.constellation(planet)[1])}')

  
  

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_constellation))
    logging.info('start bot')
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
