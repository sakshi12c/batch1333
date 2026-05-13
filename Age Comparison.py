jay = int(input("Enter Jay's age: "))
viru = int(input("Enter Viru's age: "))
gabbar = int(input("Enter Gabbar's age: "))
if jay > viru and jay > gabbar:
    print("Jay is the oldest.")
elif viru > jay and viru > gabbar:
    print("Viru is the oldest.")
else:
    print("Gabbar is the oldest.")

'''output:
Enter Jay's age: 12
Enter Viru's age: 45
Enter Gabbar's age: 90
Gabbar is the oldest. '''
