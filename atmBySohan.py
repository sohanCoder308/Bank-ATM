# ATM BY SOHAN ! --> by Sohan
class Atm():
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
        self.currentBankAmount = 50000

    def checkBalance(self):
        print(str(self.currentBankAmount))

    def depositMoney(self, dAmount):
        dNewAmount = self.currentBankAmount + dAmount
        print("You have deposited " + str(dAmount))
        print("Your new balance is " + str(dNewAmount))

    def withdrawMoney(self, amount):
        newAmount = self.currentBankAmount - amount
        print("You have withdrawn " + str(amount))
        print("Your remaining balance is " + str(newAmount))

def main():
    card_number = input("Enter your card number:- ")
    pin_number = input("Enter your ATM pin number:- ")

    newUser = Atm(card_number, pin_number)

    print("Choose what you want to do:- ")
    print("Enter 1 for Checking Bank Balance")
    print("Enter 2 for Withdrawing Money")
    print("Enter 3 for Depositing Money")

    chosen = int(input("Enter your chosen number on above basis:- "))

    if(chosen == 1):
        newUser.checkBalance()
    elif(chosen == 2):
        withdraw_amount = int(input("Enter amount to be withdrawn:- "))
        newUser.withdrawMoney(withdraw_amount)
    elif(chosen == 3):
        deposit_amount = int(input("Enter amount to be deposited:- "))
        newUser.depositMoney(deposit_amount) 
    else:
        print("Enter a valid number.") 

if __name__ == "__main__":
     main()                 