import random



def assign_price():
    return round(random.uniform(1, 1.99),2)


itemsoffered = ["grapes", "banana_juice", "orange_juice", "apple_juice", "ice_cream", "oreos", "coke", "sprite", "water", "sparkling_water",]
itemsdict = {}
for x in itemsoffered:
  itemsdict[x] = assign_price()

def ask_user():
    print("Hello, here's what we have available:")
    for x in itemsdict:
        print(f"{x}: ${itemsdict[x]}")
    want = input("What would you like?")
    while want.lower().replace(" ", "") not in itemsdict:        
        want = input("Error: Please enter what you would like again:")
    return itemsdict[want.lower().replace(" ", "")]

payment_dict = {
  "penny": .01,
  "nickel": .05,
  "dime": .1,
  "quarter": .25,
  "1dollarbill": 1.00,
  "5dollarbill": 5.00,
  "10dollarbill": 10.00,
  "20dollarbill": 20.00,
  "50dolalrbill": 50.00,
  "100dollarbill": 100.00
}
payment_list = ["Penny", "Nickel", "Dime", "Quarter", "1 Dollar Bill", "5 Dollar Bill", "10 Dollar Bill", "20 Dollar Bill", "50 Dollar Bill", "100 Dollar Bill"]

def ask_payment(amountdue):
    print(f"Here are your payment options(You need to pay ${round(amountdue,2)}):")
    for x in payment_list:
        print(x)
    while amountdue > 0:
        paid = input("Please enter payment into the vending machine, one coin or bill at a time:")
        while paid.lower().replace(" ", "") not in payment_dict:        
            paid = input("Error: Please enter what you would like again:")
        amountdue = amountdue - payment_dict[paid.lower().replace(" ", "")]
        if amountdue > 0:
            print(f"Thanks for paying, you still need to pay ${round(amountdue,2)}.")
    if amountdue < 0:
        amountdue = abs(amountdue)
        print(f"Thank you for your payment. You are being refunded the extra amount of {amountdue}")
        result = ""
        for x in reversed(payment_dict):
            amount = 0
            while amountdue >= payment_dict[x]:
                amount += 1
                amountdue = round(amountdue-payment_dict[x],2)
            if amount > 0:
                result += str(amount)+" * "+str(x)+"\n"
        print(result)

Run = True
while Run:
    payment_needed = ask_user()
    ask_payment(payment_needed)
    tobedeleted = None
    while tobedeleted != "yes" and tobedeleted != "no":
        tobedeleted = input("Would you like anything else?(Yes/No)").lower().replace(" ", "")
        if tobedeleted != "yes" and tobedeleted != "no":
            print("Error: Invalid Output. Please enter a valid output(Yes/No)")
    if tobedeleted == "no":
        print("Thanks for using our signature vending machines, great quality at great prices!")
        Run = False
    del(tobedeleted)

