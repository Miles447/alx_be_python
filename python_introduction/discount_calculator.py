purchase_amount = float(input("Enter purchase amount: "))
# Determine discount based on purchase amount
if purchase_amount >= 1000:
    discount = 0.2  # 20% discount
elif purchase_amount >= 500:
    discount = 0.1  # 10% discount
else:
    discount = 0  # No discount
# Calculate final amount after discount
final_amount = purchase_amount * (1 - discount)
print (f"Final amount after discount: ${final_amount:.2f}")