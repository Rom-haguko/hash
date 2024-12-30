class Rabin:
    q = 10**9+7 #Для длинных строк (до 500000 символов) и латинского алфавита это идеальный выбор
    b = 131 #так как используются только латинские буквы

    def __init__(self, pt, tx):
        self.pt = pt
        self.tx = tx
        self.m = len(self.tx)
        self.n = len(self.pt)

    def __get_hash(self, tx):
        rs = 0
        for i in range(len(tx)):
            rs = (rs*self.b + ord(tx[i]))%self.q
        return rs

    def __get_pt(self):
        self.ls = list()
        for i in range(self.m-self.n+1):
            if self.__get_hash(self.pt) == self.__get_hash(self.tx[i:i+self.n]):
                if self.pt == self.tx[i:i+self.n]:
                    self.ls.append(i)
        return self.ls

    def __str__(self):
        return f'строка pattern встречается в строке text по таким индексам как: {self.__get_pt()}'



px1 = Rabin('aba', 'abacaba')
print(px1)
print()

px2 = Rabin('Test', 'testTesttesT')
print(px2)
print()

px3 = Rabin('aaaaa', 'baaaaaaa')
print(px3)
