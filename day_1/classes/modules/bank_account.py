class BankAccount:
    def __init__(self, input_holder_name,  
    input_balance, input_account_type):
        self.holder_name  =  input_holder_name
        self.balance  = input_balance
        self.account_type = input_account_type
        self._rates = {
            "business": 50,
            "personal": 10,
            "savings": -5
        }
    
    def pay_in(self, amount):
        self.balance += amount
    
    def pay_monthly_fee(self):
        self.balance  -= self._rates[self.account_type]
    
    # def pay_monthly_fee(self):
    #     if self.account_type == "business":
    #         self.balance -= 50
    #     else:
    #         self.balance -= 10
    
