class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber=cardNumber
        self.pin=pin
    def checkBalance(self):
        print('Your balance is 80000')
    def withdrawing(self,amount):
        newAmount=80000-amount
        print('You have withdrawn amount'+string(amount)+'Your remaining balance is'+string(newAmount))
def main():
    card_number=input('Enter card number')
    Pin=input('Enter pin')
    newUser=Atm(card_number,Pin)
    print('Choose your activity')
    print('1.balance 2.withdrawn')
    activity=int(input('Enter the activity number'))
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input('Enter the amount'))
        newUser.withdrawing(amount)
    else:
        print('Enter a valid number')
        
main()

        