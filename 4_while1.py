"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            print('Поздравляю, но не от всего сердца')
            break
        else:
            print('Такой ответ не подходит')

   
if __name__ == "__main__":
    hello_user()
