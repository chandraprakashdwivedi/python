class Account:


    def __init__(self,filepath):
        self.filepath=filepath
        with open (filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance- amount

    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        with open (self.filepath,'w') as file:
            file.write(str(self.balance))


"""
Here we are using inheritance as checking is a amount which is used to transfer the amount on another account 
"""

class checking(Account):

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee=fee
        
    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee



checking=checking("balance.txt",90)
checking.transfer(800)
checking.commit()
print(checking.balance)

        



