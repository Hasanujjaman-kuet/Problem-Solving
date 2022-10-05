
bankdb = dict()
init_acc = 10000

class Account:
    
    bankname = 'TBA'
    def __init__(self, name: str, age: int, email: str, ph: str, address: str) -> None:
        self.name = name
        self.age = age
        self.email = email.replace(' ', '')
        self.ph = ph
        self.addr = address
    
    # Accounts
    def validated(self)-> True:
        namevalid = True if self.name.replace(' ', '').isalpha() and len(self.name)>=5 and len(self.name)<=30 else False
        agevalid = True if (self.age >= 18 and self.age <= 60) else False
        emailvalid = True if self.email.endswith("@gmail.com") else False
        phvalid  = True if (self.ph.isdigit() and len(self.ph) == 11) else False
        return all([namevalid, agevalid, emailvalid, phvalid])
    
    def create_account(self):
        if self.validated():
            global bankdb, init_acc
            self.pin = self.ph[-4:]
            self.balance = 0.0
            self.active = True
            init_acc += 1
            bankdb[init_acc] = self
            return init_acc
        else:
            return False
    
    # Transaction
    def deposit(self, amount:float) -> float:
        if self.active:
            if amount < 0:
                amount = amount*-1
            self.balance += amount
            return self.balance
        return False
        


    def __repr__(self):
        return f'Account(name={self.name})'