# Conditionals
#### Write a program to check value in variable x is even or odd
x = 10
if x % 2 == 0:
    print(x, "is even number")
else:
    print(x, "is odd number")

#### Write a program to accept age of visitor and allows him to PM's party only if he is above 60 years or below 18 years of age
x = int(input("Enter your age : "))
if x <= 18 or x >= 60 :
    print("Welcome to party")
else:
    print("Sorry!! you do not fit in PM's age criteria")

#### Write a program which offers various discounts on purchase bills
shoppinng_total = 5500

if shoppinng_total >= 5000:
    print("You won a discount voucher of flat 1000 on next purchase")
elif shoppinng_total >= 2500:
    print("You won a discount voucher of flat 500 on next purchase")
elif shoppinng_total >= 1000:
    print("You won a discount voucher of flat 100 on next purchase")    
else:
    print("OOPS!! no discount for you!!!")


# Write a program to check if India makes into finals
world_cups = {2019 : ['England', 'New-Zeland'], 
              2015:["Australia", "New Zeland"], 
              2011 : ["India", "Sri Lanka"], 
              2007: ["Australia", "Sri Lanka"], 
              2003: ["Australia", "India"]}

year = int(input("Enter year to check India made it to Finals in 20th century : "))

if year in world_cups :
    if "India" in world_cups[year] :
        print("India made it to Finals")
    else:
        print("India could not make it to Finals")   
else:
    print("World cup wasnt played in", year)