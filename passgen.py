from random import choice, randint, shuffle
from sys import argv

try:
    from pyperclip import copy
except ImportError as exc:
    _ = (str(exc).rsplit(" ")[-1:][0]).replace("'", "")
    _ = input(f"Не найден модуль {_}\nТы можешь попробовать его установить командой: python -m pip install {_}\n\nДля завершения программы нажми Enter... ")
    exit(0)

class PassGen():
    def __init__(self):
        """
        PassGen

        Функции
        ---------
        randgen8020() -> None
            Рандомный пароль от 14 до 24 символов.
        lengthgen8020(str) -> None
            Пароль заданной длины.
        """
        self.LettersNumbers = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        self.SpecialChrctrs = '+-/*!&$#?=@<>'

    def StringShuffler(self, _varString: str) -> str:
        """
        Создает лист из строки, использует метод перетасовки shuffle()
        Обратно создает строку из перетасованного листа и возвращает.
        """
        _ = list(_varString)
        shuffle(_)
        return ''.join(_)

    def randgen8020(self) -> None:
        """
        randgen8020

        Рандомный пароль от 14 до 24 символов.
        ---------
        randgen8020() -> None
            Генерирует случайный пароль состоящий:
            80% буквы, цифры.
            20% спец символы.
            Результат печатает в консоль и сохраняет в буфер обмена.
        """
        PASSWORD = ''
        LENGTH = randint(14, 24)
        LettersNumbers_80 = round((LENGTH / 100) * 80)
        SpecialChrctrs_20 = round((LENGTH / 100) * 20)

        for _ in range(LettersNumbers_80):
            PASSWORD += choice(self.LettersNumbers)
        for _ in range(SpecialChrctrs_20):
            PASSWORD += choice(self.SpecialChrctrs)
        PASSWORD = self.StringShuffler(PASSWORD)
        
        print(f"LENGTH: {LENGTH} [{LettersNumbers_80} ABC | {SpecialChrctrs_20} !@#]\nCOPIED: {PASSWORD}")
        copy(PASSWORD)

    def lengthgen8020(self, length: int) -> None:
        """
        lengthgen8020

        Пароль заданной длины.
        ---------
        lengthgen8020(str) -> None
            Генерирует пароль заданной длины.
            80% буквы, цифры.
            20% спец символы.
            Результат печатает в консоль и сохраняет в буфер обмена.
        """
        PASSWORD = ''
        LENGTH = int(length)
        LettersNumbers_80 = round((LENGTH / 100) * 80)
        SpecialChrctrs_20 = round((LENGTH / 100) * 20)

        for _ in range(LettersNumbers_80):
            PASSWORD += choice(self.LettersNumbers)
        for _ in range(SpecialChrctrs_20):
            PASSWORD += choice(self.SpecialChrctrs)
        PASSWORD = self.StringShuffler(PASSWORD)
        
        print(f"LENGTH: {LENGTH} [{LettersNumbers_80} ABC | {SpecialChrctrs_20} !@#]\nCOPIED: {PASSWORD}")
        copy(PASSWORD)

if __name__ == "__main__":
    P = PassGen()
    if len(argv) > 1:
        P.lengthgen8020(argv[1])
    else:
        P.randgen8020()