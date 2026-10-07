balance = float(input("Enter your balance: "))
amount = float(input("Enter your amount: "))
amount_type = input("Enter amount type: ")
transaction_type = int(input("Enter transaction type: "))

if amount <= 0:
    print("Transaction is not allowed")

elif transaction_type == "deposit":
    balance = balance + amount
    print("Transaction is done")

elif transaction_type == "withdraw":
    if amount <= balance:
        balance = balance - amount
        print("Transaction is done")
    else:
        print("Your balance is insufficient")

elif amount_type == "current":
    print("Transaction is not allowed")

else:
    print("Invalid data")