from book import *


def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for book in infile:
        # TODO: read in book info (title, author, year published)
        bookList = book.split(',')
        newBook = Book(bookList[0], bookList[1], bookList[2], bookList[3][:-1])
        availableBooks.append(newBook)
        print(newBook)
        # TODO: using the information just obtained from the file, create a
        # Book object with this data and add it to the availableBooks list
    return availableBooks


class Swindle(object):
    """ class for a single Swindle object """

    def __init__(self, owner):
        """ constructor for swindle object, given ________________________ """
        self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
        self.owner = owner
        self.bought = []
        self.pageLength = 20

    def __str__(self):
        """ pretty-print info about this object """
        s = ""
        s = f"Owned: {showOwned}\n"
        s += f"Available: {showAvailable}\n"
        return s

    def getLetter(self):
        """ This method determines what the user wants to do next """
        validChoices = ['n', 'p', 'q']
        while True:
            readingChoice = str(input("\nn (next); p (previous); q (quit): "))
            if readingChoice in validChoices:
                return readingChoice
            print("invalid input, try again")

    def displayPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        for i in range(pageStart, pageEnd):
            print(bookLinesList[i])
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, numPages))
        return

    def displayText(self, book):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        while True:
            self.displayPage(book)
            currentPage = book.getBookmark()
            choice = self.getLetter()       # user chooses to quit or read the next/previous page
            if choice == "q":               # quit reading and return to ereader
                return book
            elif choice == "n":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:                               # return to previous page in the book
                book.setBookmark(currentPage-1)
        return
    def showAvailable(self):
        for i, book in enumerate(self.availableBooks):
            if book not in self.bought:
                print(f"{i + 1}: {book}")
    def buy(self):
        bookList = []
        for i, book in enumerate(self.availableBooks):
            #if the book hasn't been bought yet, it is available to be bought
            if book not in self.bought:
                print(f"{i + 1}: {book}")
                bookList.append(book)
        print(bookList)
        chosenBook = properInt(input("Enter the number of the book you want to buy: "), 1, len(bookList))
        self.bought.append(bookList[chosenBook - 1])
    def showOwned(self):
        for i, book in enumerate(self.bought):
            print(f"{i + 1}: {book}")
    def getOwner(self):
        return self.owner
    def read(self):
        self.showOwned()
        chosenBook = properInt(input("Enter the number of the book you want to read: "), 1, len(self.bought))
        self.displayText(self.bought[chosenBook - 1])


def properInt(str, min, max):
    try:
        return int(str)
    except ValueError:
        str = input("Must be an integer: ")
    else:
        if int(str) < min or int(str) > max:
            str = input(f"Must be between {min} and {max}: ")
        else:
            return int(str)

if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Lionel"
    myswindle = Swindle(owner)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testingsldjs showOwned...")
    myswindle.showOwned()

    print("Testing buy...")
    myswindle.buy()

    print("Testing read...")

    myswindle.read()
    ################ Write additional tests below ###################
