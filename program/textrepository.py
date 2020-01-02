from repository import *
import datetime
from domain import *

class BookTextRepo(RepoBook):
    def __init__(self, file_name):
        super().__init__()
        self.file = file_name
        self._init_books()

    def _init_books(self):
        f = open(self.file, "r")
        for i in f:
            i = i[:-1]
            q = i.split(", ")
            book = Book(q[0], q[1], q[2])
            RepoBook.add_book(self, book)
        f.close()

    def add_book(self, book):
        f = open(self.file, "w")
        RepoBook.add_book(self, book)
        for i in self.books:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.title))
            f.write(" ")
            f.write(str(i.author))
            f.write('\n')

    def update(self, bookid, booktitle, bookauthor):
        f = open(self.file, "w")
        ceva = RepoBook.update(self, bookid, booktitle, bookauthor)
        if ceva == None:
            raise ValueError("No id")
        for i in self.books:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.title))
            f.write(" ")
            f.write(str(i.author))
            f.write('\n')
        return ceva


    def remove(self, Id):
        f = open(self.file, "w")
        ceva = RepoBook.remove(self, Id)
        for i in self.books:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.title))
            f.write(" ")
            f.write(str(i.author))
            f.write('\n')
        return ceva

class ClientTextRepo(RepoClient):
    def __init__(self, file_name):
        super().__init__()
        self.file = file_name
        self._init_clients()

    def _init_clients(self):
        f = open(self.file, "r")
        for i in f:
            i = i[:-1]
            q = i.split(", ")
            client = Client(q[0], q[1])
            RepoClient.add_client(self, client)
        f.close()

    def add_client(self, client):
        f = open(self.file, "w")
        RepoClient.add_client(self, client)
        for i in self.clients:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.name))
            f.write('\n')

    def update(self, clientid, name):
        f = open(self.file, "w")
        ceva = RepoClient.update(self, clientid, name)
        if ceva == None:
            raise ValueError("No id")
        for i in self.clients:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.name))
            f.write('\n')
        return ceva

    def remove(self, Id):
        f = open(self.file, "w")
        ceva = RepoClient.remove(self, Id)
        for i in self.clients:
            f.write(str(i.id))
            f.write(" ")
            f.write(str(i.name))
            f.write('\n')
        return ceva

class RentTextRepo(RepoRental):
    def __init__(self, file_name):
        super().__init__()
        self.file = file_name
        self._init_rent()

    def _init_rent(self):
        f = open(self.file, "r")
        for i in f:
            i = i[:-1]
            q = i.split(", ")
            d2 = q[4]
            d1 = q[3]
            d1 = d1.split(".")
            d2 = d2.split(".")
            d1 = list(map(int, d1))
            d2 = list(map(int, d2))
            date1 = datetime.datetime(d1[2], d1[1], d1[0])
            date2 = datetime.datetime(d2[2], d2[1], d2[0])
            RepoRental.rent_book(self, q[0], q[1], q[2], date1, date2)

    def rent_book(self, rentalid, bookid, clientid, rented, returned):
        f = open(self.file, "w")
        ceva = RepoRental.rent_book(self, rentalid, bookid, clientid, rented, returned)
        for i in self.rent:
            f.write(str(i.rentalid))
            f.write(" ")
            f.write(str(i.bookid))
            f.write(" ")
            f.write(str(i.clientid))
            f.write(" ")
            f.write(str(i.rented))
            f.write(" ")
            f.write(str(i.returned))
            f.write('\n')
        return ceva

    def delete_rent(self, Id):
        f = open(self.file, "w")
        ceva = RepoRental.delete_rent(self, Id)
        for i in self.rent:
            f.write(str(i.rentalid))
            f.write(" ")
            f.write(str(i.bookid))
            f.write(" ")
            f.write(str(i.clientid))
            f.write(" ")
            f.write(str(i.rented))
            f.write(" ")
            f.write(str(i.returned))
            f.write('\n')
        return ceva

