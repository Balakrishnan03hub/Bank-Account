Acc=100000
user=input("[Deposit/Withdraw]?")
if "Deposit"==user:
    d=int(input("Enter the amount"))
    a=d+Acc
    print("Existing balance:",Acc)
    print("Balance:",a)
elif "Withdraw"==user:
    x=int(input("Enter the amount:"))
    if x<=100000:
        print("Withdraw")
        y=100000-x
        print("Balance:",y)
    elif x>=100000:
        print("Insufficient")
