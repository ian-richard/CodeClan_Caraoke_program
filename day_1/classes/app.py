from modules.bank_account import *
import pdb

# account = {
#     "holder_name":  "Colin",
#     "balance": 100,
#     "type": "business"
# }

bank_account = BankAccount("Colin", 100, "business")
bank_account2 = BankAccount("John", 100, "personal")
bank_account3 = BankAccount("Hannah", 100, "savings")
# pdb.set_trace()


#1 make a pay_monthly_fee method for a 
# BankAccount which will decrease money by 50
#call to test and print  value

bank_account.pay_monthly_fee()
bank_account2.pay_monthly_fee()
bank_account3.pay_monthly_fee()
print(bank_account.balance)
print(bank_account2.balance)
print(bank_account3.balance)


#2  Modify pay_monthly_fee to only deduct 50 
#for business accounts. Deduct  10  for  any other
#test by calling  method and printing  the results


