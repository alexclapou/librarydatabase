import datetime
import random
from domain import *
from copy import deepcopy
from undo1 import *
import configparser
class RepoBook:
    def __init__(self):
        self.books = []
        config = configparser.ConfigParser()
        config.read("settings_text.ini")
        if config['repositories']['books'].endswith(".txt") != 1 and config['repositories']['books'].endswith(".pickle") != 1:
            self.init_books()

    def add_book(self, book):
        '''
        add a book to the list
        params:
            book- a new book
        '''
        self.books.append(book)

    def remove(self, bookid):
        '''
        remove a book from the list
        params:
            bookid - id of the book we want to remove
        '''
        c = 0
        for i in self.books:
            if i.id == bookid:
                x = self.books[c]
                del self.books[c]
                return x
            c = c + 1
        raise ValueError("No book!")

    def update(self, bookid, booktitle, bookauthor):
        '''
        update a book
        params:
            bookid - book we want to update
            booktitle - new title
            bookauthor - new author
        '''
        try:
            for i in self.books:
                if i.id == bookid:
                    ceva = deepcopy(i)
                    i.title = booktitle
                    i.author = bookauthor
                    return ceva
        except:
            raise ValueError("invalid id")

    def init_books(self):
        books_name = ["Orasul Bantuit", "Pariul Pierdut", "Cartea", "01", "451 Fahrenheit", "Jurnalul", "Amintiri din Copilarie", "Cartea", "Padurea Fermecata", "Fermecata", "Stralucirea"]
        authors_name = ["Stephen King", "Creanga", "Eminescu", "Rebreanu", "Ion", "Rowling", "Tolkien", "George", "Martin","Cooper"]
        index = 0
        while index < 9:
            random_book = random.randint(0, 9)
            random_name = random.randint(0, 9)
            index = index + 1
            self.books.append(Book(index, books_name[random_book], authors_name[random_name]))

class RepoClient:
    def __init__(self):
        self.clients = []
        config = configparser.ConfigParser()
        config.read("settings_text.ini")
        if config['repositories']['books'].endswith(".txt") != 1 and config['repositories']['books'].endswith(".pickle") != 1:
            self.init_clients()

    def add_client(self, client):
        '''
        add a client to list
        params:
            client - new client
        '''
        self.clients.append(client)
        return client

    def remove(self, clientid):
        '''
        remove a client from the list
        params:
            clientid - id of the client we delete
        '''
        c = 0
        for i in self.clients:
            if i.id == clientid:
                x = self.clients[c]
                del self.clients[c]
                return x
            c = c + 1
        raise ValueError("No client!")

    def update(self, clientid, clientname):
        '''
        update a client
        params:
            clientid - the client id
            clientname - new name
        '''
        try:
            for i in self.clients:
                if i.id == clientid:
                    ceva = deepcopy(i)
                    i.name = clientname
                    return ceva
        except:
            raise ValueError("invalid id!")
    def init_clients(self):
        names = ["Makai", "Alex", "Adi", "Razvan", "Andreea", "Maia", "Denisa", "Gabi", "Flavia", "Andrei", "Sergiu"]
        index = 0
        while index < 9:
            random_name = random.randint(0, 9)
            index = index + 1
            self.clients.append(Client(index, names[random_name]))



class RepoRental:
    def __init__(self):
        self.rent = []
        config = configparser.ConfigParser()
        config.read("settings_text.ini")
        if config['repositories']['books'].endswith(".txt") != 1 and config['repositories']['books'].endswith(".pickle") != 1:
            self.init_rent()

    def rent_book(self, rentid, bookid, clientid, rentdate, returndate):
            self.rent.append(Rental(rentid, bookid, clientid, rentdate, returndate))
            return Rental(rentid, bookid, clientid, rentdate, returndate)

    def return_book_list(self, book):
        listnew = []
        for i in self.rent:
            print(i.bookid, book)
            if i.bookid == book:
                listnew = listnew.deepcopy(i)
        return listnew

    def return_book(self, client, book, returned):
        c = 0
        for i in self.rent:
            if i.bookid == book and i.clientid == client and returned == i.returned:
                del self.rent[c]
            c = c + 1
    def delete_rent_client(self, client):
        new_list = []
        while True:
            c = 0
            found = 0
            for i in self.rent:
                if i.clientid == client:
                    deepcopy(new_list.append(i))
                    del self.rent[c]
                    found = 1
                c = c + 1
            if found == 0:
                break
        return new_list
        
    def delete_rent_book(self, book):
        new_list = []
        while True:
            c = 0
            found = 0
            for i in self.rent:
                if i.bookid == book:
                    deepcopy(new_list.append(i))
                    del self.rent[c]
                    found = 1
                c = c + 1
            if found == 0:
                break
        return new_list
    def init_rent(self):
        index = 0 
        while index < 9:
            bookid = random.randint(1, 9)
            clientid = random.randint(1, 9)
            day1 = random.randint(1, 27)
            month1 = random.randint(1, 12)
            month2 = random.randint(1, 12)
            day2 = random.randint(1, 27)
            if month1 > month2:
                change = month1
                month1 = month2
                month2 = change
            elif month2 == month1:
                if day1 > day2:
                    changed = day1
                    day1 = day2
                    day2 = changed
            if day1 == day2:
                day2 = day2 + 1
            year = random.randint(2010, 2020)
            d1 = datetime.datetime(year, month1, day1) 
            d2 = datetime.datetime(year, month2, day2) 
            for i in self.rent:
                if i.bookid == bookid:
                    if (d1 > i.rented and d1 < i.returned) or (d2 > i.rented and d2 < i.returned):
                        year = year + 10
                        d1 = datetime.datetime(year, month1, day1) 
                        d2 = datetime.datetime(year, month2, day2) 
            index = index + 1
            self.rent.append(Rental(index, bookid, clientid, d1, d2))

