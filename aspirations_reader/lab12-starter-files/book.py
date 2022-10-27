class Book(object):
    """ class for a single Book object """

    def __init__(self, title, author, year, name):
        """ constructor for book object, given ____________________ """
        self.title = title
        self.author = author
        self.year = year
        self.name = name
        self.bookmark = 0

    def __str__(self):
        """ pretty-print info about this object """
        s = f"{self.title:<25}by{self.author:>20} ({self.year})"
        return s
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author
    def getYear(self):
        return self.year
    def getFilename(self):
        return self.name
    def getBookmark(self):
        return self.bookmark
    def setBookmark(self, newMark):
        self.bookmark = newMark
    def getText(self):
        """prints the whole book as a single string"""
        with open(self.name, 'r') as fin:
            firstBook = fin.readlines()
        realBook = ''
        for line in firstBook:
            if line[0] != '#':
                realBook += line
        return realBook



    ###  METHODS TO BE COMPLETED BY YOU  ###



if __name__ == '__main__':

    print("Testing the Book class...")
    myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
    "book-database/gettysburg.txt")

    print("Testing toString...")
    print(myBook)

    print("Testing getFilename...")
    print(myBook.getFilename())

    print("Testing getText...")
    text = myBook.getText()
    print(text[:105])                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())
    ################ Write additional tests below ###################
