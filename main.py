from menu import *


class Bankcard:
    def __init__(self):
        pass

    def psw(self):
        print(f"Беларусьбанк \n Добро пожаловать\n")
        self.i = input(f"Введите свой пин код\n")

        if self.i == Card1().card_pin or self.i == Card2().card_pin2:
            return Menu().menu2()

        elif self.i != Card1().card_pin or self.i != Card2().card_pin2:
            print(f"Пин код введен не правильно \n повторите попытку1")
            self.a = input(f"Введите свой пин код\n")
            if self.a == Card1().card_pin or self.a == Card2().card_pin2:
                return Menu().menu2()
            elif self.a != Card1().card_pin or self.a != Card2().card_pin2:
                print(f"Пин код введен не правильно \n повторите попытку2")
                self.b = input(f"Введите свой пин код\n")
                if self.b == Card1().card_pin or self.b == Card2().card_pin2:
                    return Menu().menu2()
                elif self.b != Card1().card_pin or self.b != Card2().card_pin2:    
                        print(f"Вы ввели неправельный пин код 3 раза \nваша карта заблокирована")
                        return self.psw
            
        
            

class Menu:
    def __init__(self):
        pass

    def menu2(self):
        print(f"1. Смена ПИН-кода \n"
              f"2. Перевод денежных средств со счета на счет\n"
              f"3. Операция для выписка по карте\n"
              f"4. Просмотр остатка денежных средств на счете\n"
              f"5. Остальные операции\n")

        self.menuinp = str(input('Выберите свой вариант: '))

        if self.menuinp == "1":
            return Psw_refresh().psw_res()
        elif self.menuinp == "2":
            return Perevod().perevod()
        elif self.menuinp == "3":
            return Funcii().vipisska()
        elif self.menuinp == "4":
            return Ostat().ost()
        elif self.menuinp == "5":
            return Ostal().ostalnie()
        else:
            print(f"")
            return Menu().menu2()


class Psw_refresh():
    def psw_res(self):
        self.pin = Card2().card_pin2
        print(f"Вы хотите сменить пароль\n")
        self.pin_code = input(f"Введите новый пин код\n")
        self.pin = self.pin_code
        print(f"операция проwла успешна")
        chek = str(input(f"Хотите взять чек?\n"))
        if chek == "Да" or chek == "да":
            print(f"Ваш пороль был изменет на: {self.pin_code}\n")
            return Bankcard().psw()
        elif chek == "Нет" or chek == "нет":
            return Bankcard().psw()



class Ostal:
    def __init__(self):
        pass

    def ostalnie(self):
        print(f"1. Операция для перевода денег наблаготворительный фонд\n"
              f"2. оплата телефона\n")
        self.inp = input(f"выбери нажную операцию")
        if self.inp == "1":
            return Fond().fond()
        elif self.inp == "2":
            return PayTel().payTel()
        else:
            print(f"")
            return Menu().menu2()




class Psw_refresh():
    def psw_res(self):
        self.pin = Card2().card_pin2
        print(f"Вы хотите сменить пароль\n")
        self.pin_code = input(f"Введите новый пин код\n")
        self.pin = self.pin_code
        print(f"операция проwла успешна")
        chek = str(input(f"Хотите взять чек?\n"))
        if chek == "Да" or chek == "да":
            print(f"Ваш пороль был изменет на: {self.pin_code}\n")
            return Bankcard().psw()
        elif chek == "Нет" or chek == "нет":
            return Bankcard().psw()


if __name__ == '__main__':
    bk = Bankcard()
    bk.psw()
