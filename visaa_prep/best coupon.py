bill = int(input())
discount_10_percent = bill * 0.10
flat_discount = 100
final_amount = bill- (discount_10_percent if discount_10_percent> flat_discount else flat_discount)
print(int(final_amount))
