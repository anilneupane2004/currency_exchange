with open('currencyData.txt') as f:
    file_read = f.readlines()
print(file_read)

currencyDict = {}
for line in file_read :
    parsed = line.split("\t")
    currencyDict[parsed[0]]= parsed[1]

Amount = int(input("Enter the amount:\n"))
print("Enter the name of the currency you want to convert ? available options:\n",currencyDict.keys())
([print(item)for item in currencyDict.keys()])
currency = (input('please enter one of these value:\n'))
print(f"{Amount} NPR is equal to {Amount *float(currencyDict[currency])} {currency}")


    
