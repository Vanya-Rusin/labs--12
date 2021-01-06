class TBankomat:
    def __init__(self,n5,n10,n20,n50,n100,n200):
        self.n5 = n5
        self.n10 = n10
        self.n20 = n20
        self.n50 = n50
        self.n100 = n100
        self.n200 = n200

    @property
    def max(self):
        return self.n5 * 5 + self.n10 * 10 + self.n20 * 20 + self.n50 * 50 + self.n100 * 100 + self.n200 * 200

    def profit_from_robbery(self):
        return self.max

    def min_money_to_take(self):
        if self.n5 != 0:
            return 5
        elif self.n10 != 0:
            return 10
        elif self.n20 != 0:
            return 20
        elif self.n50 != 0:
            return 50
        elif self.n100 != 0:
            return 100
        elif self.n200 != 0:
            return 200
        else:
            return "нема"

    def take_some_money(self,value):
        '''число має бути кратне 5'''
        if value > self.max:
            print('недостатньо грошей')
        if value % 5 == 0:
            money = [0 for i in range(6)]
            while value != 0:
                if value >= 200 and self.n200 != 0:
                    value -= 200
                    money[0] += 1
                    self.n200 -= 1
                elif value >= 100 and self.n100 != 0:
                    value -= 100
                    money[1] += 1
                    self.n100 -= 1
                elif value >= 50 and self.n50 != 0:
                    value -= 50
                    money[2] += 1
                    self.n50 -= 1
                elif value >= 20 and self.n20 != 0:
                    value -= 20
                    money[3] += 1
                    self.n20 -= 1
                elif value >= 10 and self.n10 != 0:
                    value -= 10
                    money[4] += 1
                    self.n10 -= 1
                elif value >= 5 and self.n5 != 0:
                    value -= 5
                    money[5] += 1
                    self.n5 -= 1
            print('200:{0}\n100:{1}\n50:{2}\n20:{3}\n10:{4}\n5:{5}'.format(money[0],money[1],money[2],money[3],money[4],money[5]))
        else:
            print('операція неможлива')



Bankomat1 = TBankomat(10,10,10,10,10,10)
Bankomat1.take_some_money(1150)