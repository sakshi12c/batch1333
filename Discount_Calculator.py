
mrp = float(input("Enter MRP of product: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (mrp * discount) / 100

selling_price = mrp - discount_amount

print("\n--- Result ---")
print("MRP:", mrp)
print("Discount:", discount, "%")
print("Selling Price:", selling_price)


'''output:
Enter MRP of product: 2000
Enter discount percentage: 50

--- Result ---
MRP: 2000.0
Discount: 50.0 %
Selling Price: 1000.0'''