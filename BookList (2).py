from Book import Book
mylist = []
for i in range(4):
    print("Input info of Book " + str(i+1))
    title =input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))

    book = Book(title, author, price)
    mylist.append(book)

maxprice = mylist[0].getPrice()
minprice = mylist[0].getPrice()
book_maxprice = mylist[0]
book_minprice = mylist[0]

for i in range(1,4):
    if maxprice < mylist[i].getPrice():
        book_maxprice = mylist[i]
        maxprice = mylist[i].getPrice()

    if minprice > mylist[i].getPrice():
        book_minprice = mylist[i]
        minprice = mylist[i].getPrice()

print("The most expensive book is "+ book_maxprice.__str__())
print("The cheapest book is "+ book_minprice.__str__())
