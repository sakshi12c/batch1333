name = input("Enter Customer Name: ")

pizza = int(input("Enter Pizza Price: "))
burger = int(input("Enter Burger Price: "))
coldrink = int(input("Enter Coldrink Price: "))

total = pizza + burger + coldrink

if total >= 1000:
    discount = 100
else:
    discount = 50

final_bill = total - discount

print("="*6 , "Restaurant Bill" , "="*6)
print(f"Customer Name : {name}")
print(f"Food Item       Price")
print("="*30)
print(f"Pizza          {pizza}")
print(f"Burger         {burger}")
print(f"Coldrink       {coldrink}")
print("="*30)
print(f"Total Bill     : {total}")
print(f"Discount       : {discount}")
print("="*30)
print(f"Final Bill     : {final_bill}")


'''output:
Enter Customer Name: Shreya Sharma
Enter Pizza Price: 200
Enter Burger Price: 160
Enter Coldrink Price: 80
====== Restaurant Bill ======
Customer Name : Shreya Sharma
Food Item       Price
==============================
Pizza          200
Burger         160
Coldrink       80
==============================
Total Bill     : 440
Discount       : 50
==============================
Final Bill     : 390'''
