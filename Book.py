class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author= author
        self.price = price

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setPrice(self, price):
        self.price = price

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author  
        
    def getPrice(self):
        return self.price    

    def __str__(self):
        return " Book entitled " + self.title + " Author "+ self.author + " Price " + str(self.price)  