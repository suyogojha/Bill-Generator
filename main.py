# module mane: main
import read
import purchase
import write

again = "Y"
while again.upper() == "Y":
    a = read.read_file()
    b = purchase.purchase(a)
    write.over_write(a, b)
    again = input("\nAre there any new customers waiting to buy product? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")
