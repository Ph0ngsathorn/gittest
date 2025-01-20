class ATM :
    passwords = ''
    phonenumbers = ''
    choice = ''
    Account_number = ''
    amounts = 0.0
    def show(self): #ไม่รับค่า ไม่ส่งค่า
        print("1.ถอนเงิน")
        print("2.ฝากเงิน")
        print("3.โอนเงิน")
        print("4.เช็คยอดเงิน")
        
    def Choice(selt): #รับค่า ไม่ส่งค่า
        switcher = input("select : ")
        match switcher :
            case '1' :
                print('ฝากถอน')
            case '2' :
                print('ฝากถอนโอน')
            case '3' :
                print('ฝากถอนถอน')
            case '4' :
                print('ฝากถอน4')
        print(switcher)
        p1.Passwords()

    def Passwords(self): #รับค่า ไม่ส่งค่า
        Pass =  input("Password : ")
        p1.Account_number()
        p1.Phonenumbers()

    def Phonenumbers(self) : #รับค่า ไม่ส่งค่า
        ph = input("Phonenumber : ")
        p1.Amounts()

    def Account_number(self): # ไม่รับค่า ส่งค่า
        print("154-7-63582-6")
        return 0

    def Amounts(self): #รับค่า ส่งค่า
        x = input("amount = ")
        print("Show Amount : ",x)
        return x

p1 = ATM()
p1.show()
p1.Choice()