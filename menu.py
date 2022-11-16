class Card1():
    def __init__(self):
        self.card_username = "Жавлон"
        self.card_number = 1
        self.card_name = "карта1"
        self.card_schet = "schet1"
        self.card_schet2 = "schet2"
        self.card_pin = '1234'
        self.card_balance = 1000
        self.schet_balance = 1000
        self.schet_balance2 = 1000
        self.vipiska = ""


class Card2():
    def __init__(self):
        self.ard_username2 = "Жавлон"
        self.card_number2 = 2
        self.card_name2 = "карта2"
        self.card_pin2 = '1111'
        self.card_balance2 = 1000



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
            return psw_refresh
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


def psw_refresh(self):
    i = input("Введите новый пароль")
    Card1().card_pin = i


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

class Funcii:
    def __init__(self):
        self.vipiska = ""

    def vipisska(self):
        self.name_card = Card1().card_name
        self.number_card = Card1().card_number
        self.username = Card1().card_username
    	

        print(f"Выписка по карте:\n"
        	  f"Наименование вашей карты: {self.name_card}\n"	
        	  f"Номер вашей карты: {self.number_card}\n"
        	  f"Имя пользователя: {self.username}\n" 
              f"Последняя операция: {self.vipiska}\n")
        return Check().back()

class Check():
    def back(self):
        g = input(str(f"хотите выполнить другие операции"))
        if g == "Да" or g == "да":
            return Menu().menu2()
        elif g == "Нет" or g == "нет":
            print("Операция успешна, До свидание")

class PayTel():
    def payTel(self):
        self.vipis = Funcii().vipiska
        self.balance = Card1().card_balance

        self.tel = input(f"Введите свой номер телеофна \n")
        i = int(input(f"Введите сумму для оплаты \n"))
        if i <= int(self.balance):
            self.balance -= i
            print(f"операция проwла успешна")
            chek = str(input(f"Хотите взять чек?\n"))
            if chek == "Да" or chek == "да":
                print(f"Номер телефона: {self.tel}")
                print(f"Сумма заполнение: {i}")
                Funcii().vipiska = (f"операция оплаты телефона{self.tel}")
                self.summ = f"{i}"
                return Check().back()
            elif chek == "Нет" or chek == "нет":
                return Check().back()
        else:
            print(f"На вашей карте недостаточно средств")
            print(f"Баланс вашей карты состовляет: {self.balance}")
            return Check().back()       


class Ostat():
    def ost(self):
        self.balance = Card1().card_balance
        print(f"Баланс вашей карты состовляет: \n {self.balance}")
        return Check().back()



class Fond():
    def fond(self):
        self.vipis = Card1().vipiska
        self.balance = Card1().card_balance
        self.fon = input(f"Введите название благотворительного фонда \n")
        i = int(input(f"Введите сумму для оплаты \n"))
        if i <= int(self.balance):
            self.balance -= i
            print(f"операция проwла успешна")
            chek = str(input(f"Хотите взять чек?\n"))
            if chek == "Да" or chek == "да":
                print(f"Название благотворительного фонда: {self.fon}")
                print(f"Сумма заполнение: {i}")
                self.vipis = (f"Название благотворительного фонда: {self.fon} \n Сумма заполнения: {i}")
                return Check().back()
            elif chek == "Нет" or chek == "нет":
                return Check().back()
        else:
            print(f"На вашей карте недостаточно средств")
            print(f"Баланс вашей карты состовляет: {self.balance}")
            return Check().back()


class Popolnenie():
    def popolnen(self):
        self.vipiska = Card1().vipiska
        self.balance = Card1().card_balance
        i = int(input(f"Введите сумму для пополнение карты \n"))
        if i <= int(self.balance):
            self.balance += i
            print(f"операция проwла успешна")
            chek = str(input(f"Хотите взять чек?\n"))
            if chek == "Да" or chek == "да":
                print(f"Сумма пополнение состовляет: {i}")
                print(f"Ваш баланс состовляет: {self.balance}")
                self.vipis = (f"Сумма пополнения: {i}")
                return Check().back()
            elif chek == "Нет" or chek == "нет":
                return Check().back()


class Perevod():
    def perevod(self):
        self.vipiska = Card1().vipiska
        self.balance = Card1().schet_balance
        self.balance2 = Card1().schet_balance2
        self.name_card = Card1().card_schet
        self.name_card2 = Card1().card_schet2


        self.cart1 = input(f"Введите намер своей счета \n")
        self.cart2 = input(f"Введите намер своей счета \n")
        i = int(input(f"Введите сумму для перевода \n"))

        if self.cart1 == self.cart2:
            print(f"Вы не можете перевести на один и тот же счет")
            return self.perevod()

        if self.cart1 == "счет1":
            if i <= self.balance:
                self.balance -= i
                self.balance2 += i
                print(f"операция перевода денег на счет 2 прошла успешна")
                chek = str(input(f"Хотите взять чек?\n"))
                if chek == "Да" or chek == "да":
                    print(f"Операция перевода:\n"
                        f"Перевод на {self.cart1}\n"
                        f"Сумма перевода: {i}\n"
                        f"Сумма вашего счета состовляет: {self.balance}")
                    self.vipis = (f" Сумма заполнения на карту 2: {i}")
                    return Check().back()
                elif chek == "Нет" or chek == "нет":
                    return Check().back()
            else:
                print(f"На вашей карте недостаточно средств")
                print(f"Баланс вашей карты состовляет: {self.balance}")
                return Check().back()
        elif self.cart1 == "счет2":
            if i <= self.balance:
                self.balance += i
                self.balance2 -= i
                print(f"операция перевода денег на карту1 прошла успешна")
                self.vipis = (f" Сумма заполнения на карту 1: {i}")
                chek2 = str(input(f"Хотите взять чек?\n"))
                if chek2 == "Да" or chek2 == "да":
                    print(f"Операция перевода:\n"
                        f"Перевод на {self.cart1}\n"
                        f"Сумма перевода: {i}\n"
                        f"Сумма вашего счета состовляет: {self.balance}")
                    return Check().back()
                elif chek2 == "Нет" or chek2 == "нет":
                    return Check().back()
            else:
                print(f"На вашей карте недостаточно средств")
                print(f"Баланс вашей карты состовляет{self.balance}")
                return Check().back()
 