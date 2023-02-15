"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    how_are_you = ''
    while how_are_you != 'хорошо':
        try:
            how_are_you = input("Как дела? ").lower()
        except KeyboardInterrupt:
            print("\nПока!")
            break

    
if __name__ == "__main__":
    hello_user()
