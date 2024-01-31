def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
hrs = input("35")
rate = input("2.75")

if hrs <= 40:
    print(hrs*rate)
else:
    print((hrs-40)*(1.5*rate) + (40*rate));

    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
