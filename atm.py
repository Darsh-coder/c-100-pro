


class Atm (object) :
    def __init__(self,pinnumber,cardnumber,balance) :
        self.pinnumber = pinnumber
        self.cardnumber = cardnumber
        self.balance = balance
    
    def cashWithdrawl (self,amount) :
        self.balance = self.balance-amount
        print("avilabe balance now is ",self.balance)

    def  balanceEnquiry   (self) : 
        print("balance in the account is ",(self.balance))

atmcustomer1 = Atm("254163","1478-5236-9874-5214 visa " , 2540056)
print (atmcustomer1.balance)
print (atmcustomer1.cardnumber)

atmcustomer1.balanceEnquiry()
atmcustomer1.cashWithdrawl(25896)
atmcustomer1.balanceEnquiry()