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
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

 
def planet_user(update, context):
    now = datetime.datetime.now()
    text = update.message.text.split(' ')
    planet = text[-1].lower()
    if planet == 'mars':
        planet_name = ephem.Mars(now)
    elif planet == 'uranus':
        planet_name = ephem.Uranus(now)
    elif planet == 'mercury':
        planet_name = ephem.Mercury(now)
    elif planet == 'venus':
        planet_name = ephem.Venus(now)
    elif planet == 'jupiter':
        planet_name = ephem.Jupiter(now)
    elif planet == 'saturn':
        planet_name = ephem.Saturn(now)
    elif planet == 'neptune':
        planet_name = ephem.Neptune(now)
    elif planet == 'pluto':
        planet_name = ephem.Pluto(now)
    constellation = ephem.constellation(planet_name)
    const = constellation[-1]
    update.message.reply_text(const)


def main():
    mybot = Updater('TOKEN', use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user)) 
    dp.add_handler(CommandHandler('planet', planet_user))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
