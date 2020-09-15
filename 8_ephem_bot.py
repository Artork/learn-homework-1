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
  print('planet')
  user_text = update.message.text
  print(user_text)

  planet_dict = {
    'Mercury': ephem.Mercury('2000/01/01'),
    'Venus': ephem.Venus('2000/01/01'),
    'Moon': ephem.Moon('2000/01/01'),
    'Mars': ephem.Mars('2000/01/01'),
    'Jupiter': ephem.Jupiter('2000/01/01'),
    'Uranus': ephem.Uranus('2000/01/01'),
    'Neptune': ephem.Neptune('2000/01/01'),
    'Pluto': ephem.Pluto('2000/01/01')
    }
  planet = user_text.split()[1]
  planetlow = planet.lower()
  print(f'Пользователь выбрал планету {planetlow}')
  from_planet_dict = planet_dict[planetlow]
  planet1 = planet_dict[planetlow]
  print(planet1)
  constallation = ephem.constellation(planet1)
  update.message.reply_text(f'планета {planet} находилась 1 января 2000 года в созвездии {constallation[1]}')

  
  

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
