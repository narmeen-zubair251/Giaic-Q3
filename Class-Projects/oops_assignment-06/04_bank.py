class Bank:
    bank_name = "State Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
print(b1.bank_name)
Bank.change_bank_name("Habib Bank")
print(b1.bank_name)