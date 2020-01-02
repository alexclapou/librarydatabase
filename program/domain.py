class Book:
    def __init__(self, ID, title, author):
        self.id = ID
        self.title = title
        self.author = author

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        try:
            value = int(value)
        except:
            raise TypeError("ID must be an integer")
        if value < 0:
            raise TypeError("ID must be > 0")
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if len(value) < 2:
            raise ValueError("name is too short!")
        if any(char.isdigit() for char in value) == 1:
            raise ValueError("name has at least 1 digit!")
        self._author = value

    def __str__(self):
        return "book id: " + str(self._id) + ", title: '" + str(self._title) + "', author: " + str(self.author)

class Client:
    def __init__(self, ID, name):
        self.id = ID
        self.name = name
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        try:
            value = int(value)
        except:
            raise ValueError("id must be an integer!")
        if value < 0:
            raise TypeError("id must be > 0!")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("name is too short!")
        if any(char.isdigit() for char in value) == 1:
            raise ValueError("name has at least 1 digit!")
        self._name = value

    def __str__(self):
        return "client id: " + str(self._id) + ", name: " + str(self._name) 

class Rental:
    def __init__(self, rentalid, bookid, clientid, rented, returned):
        self.rentalid = rentalid
        self.bookid = bookid
        self.clientid = clientid
        self.rented = rented
        self.returned = returned

    @property
    def rentalid(self):
        return self._rentalid

    @rentalid.setter
    def rentalid(self, value):
        try:
            value = int(value)
        except:
            raise ValueError("bad id") # change to classes
        self._rentalid =value 

    @property
    def bookid(self):
        return self._bookid

    @bookid.setter
    def bookid(self, value):
        try:
            value = int(value)
        except:
            raise ValueError("bad id!") # change to classes
        self._bookid = value

    @property
    def clientid(self):
        return self._clientid

    @clientid.setter
    def clientid(self, value):
        try:
            value = int(value)
        except:
            raise ValueError("invalid id!") # change to classes
        self._clientid = value

    @property
    def rented(self):
        return self._rented

    @rented.setter
    def rented(self, value):
        self._rented = value

    @property
    def returned(self):
        return self._returned

    @returned.setter
    def returned(self, value):
        self._returned = value

    def __str__(self):
        return ("rentalid: ") + str(self.rentalid) + ", clientid: " + str(self.clientid) + ", bookid: " + str(self.bookid) + ", rented: " + str(self.rented.strftime("%d")) + " " +  str(self.rented.strftime("%B")) + " " + str(self.rented.strftime("%Y"))+ ", returned: " + str(self.returned.strftime("%d")) + " " + str(self.returned.strftime("%B")) + " " + str(self.returned.strftime("%Y"))

def testBook():
    book1 = Book(1, "titlu carte", "Alex")
    assert book1.id == 1
    assert book1.title == "titlu carte"
    assert book1.author == "Alex"

def testClient():
    client1 = Client(1, "Alex")
    assert client1.id == 1
    assert client1.name == "Alex"

testBook()
testClient()
