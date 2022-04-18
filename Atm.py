class Atm:
    def __init__(money, cardNumber, pinNumber):
         money.cardNumber = cardNumber
         money.pinNumber = pinNumber
    
    def accountBalance(money):
        print("Account Balance: We checked your account balance, turns out, you're rich💰🪙")
    
    def cashWithdrawl(money):
        print("Cash withdrawl: Wanna withdraw some money for that new Gucci bag? we gotchu!👜😁")

    def balanceEnquiry(money):
        print("Balance Enquiry: You wanna know how much money you have with ya? Just lettin' you know, you're still rich!🙂")
    
Card = Atm("1234567890123456" , "1970")
print("Here is your Pin Number, Remember, Don't tell this to anybody🤫: " + Card.pinNumber)
print("Here is your Card Number, Remember, Don't tell this to anybody🤫: " + Card.cardNumber)
Card.accountBalance()    
Card.balanceEnquiry()
Card.cashWithdrawl()