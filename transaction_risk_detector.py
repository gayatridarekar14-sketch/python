low = medium = high = 0

for i in range (0):
    ammount = int(input("enter the ammount :"))
    
if ammount < 1000:
   low += 1
elif ammount < 5000 :
   medium += 1
else:
    high+=1
    
print("low:",low)
print("medium:",medium)
print("high:",high)