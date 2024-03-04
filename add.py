income=int(input("Enter your income:"))
if income <=10000:
    tax_pay = 0
elif income <=20000:
    tax_pay = (income-10000)*0.1
else:
    income=income-20000
    tax_pay=10000*0+10000*0.1+income*0.2
print(tax_pay)
print("Tax to be paid is:",tax_pay)
