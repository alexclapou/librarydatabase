import datetime
from operator import itemgetter
from service import *
from repository import *
from undo1 import *
class UI:
    def __init__(self, bookservice, clientservice, rentservice, undoservice):
        self.bookservice = bookservice
        self.clientservice = clientservice
        self.rentservice = rentservice
        self.undo = undoservice

    def print_main_menu(self):
        print("     menu")
        print(" 1.manage the lists")
        print(" 2.rent or return a book")
        print(" 3.search for clients of books")
        print(" 4.create statistics")
        print(" 5.undo")
        print(" 6.redo")
        print(" 7.exit")

    def print_manage_list(self):
        print("1. add to book/client")
        print("2. update book/client")
        print("3. remove book/client")
        print("4. list books/clients")

    def print_what_to_list(self):
        print("1. books")
        print("2. clients")

    def print_rentreturn(self):
        print("1. rent")
        print("2. return")
        print("3. list")

    def print_search(self):
        print("1. books")
        print("2. clients")

    def print_search_book(self):
        print("1. by id")
        print("2. by title")
        print("3. by author")

    def print_search_client(self):
        print("1. by id")
        print("2. by name")

    def print_statistics(self):
        print("1. most rented book")
        print("2. most active client")
        print("3. most rented author")

    def add_book(self):
        Id = int(input("id: "))
        title = input("title: ")
        author = input("author: ")
        self.bookservice.duplicated_id(Id)
        self.bookservice.create(Id, title, author)

    def add_client(self):
        Id = int(input("id: "))
        name = input("name: ")
        self.clientservice.duplicated_id(Id)
        self.clientservice.create(Id, name)

    def remove_book(self):
        Id = int(input("id: "))
        self.bookservice.existId(Id)
        self.bookservice.deletekefaki(Id)

    def remove_client(self):
        Id = int(input("id: "))
        self.clientservice.existId(Id)
        self.clientservice.deletekefaki(Id)

    def update_book(self):
        i = int(input("id: "))
        t = input("title: ")
        a = input("author: ")
        self.bookservice.updateone(i, t, a)

    def update_client(self):
        i = int(input("id: "))
        n = input("name: ")
        self.clientservice.updateone(i, n)

    def print_books(self):
        if len(self.bookservice.bookrepo.books) == 0:
            raise ValueError("no books!")
        for i in self.bookservice.bookrepo.books:
            print(i)

    def print_clients(self):
        if len(self.clientservice.clientrepo.clients) == 0:
            raise ValueError("no clients!")
        for i in self.clientservice.clientrepo.clients:
            print(i)

    def rent_book(self):
        i = int(input("id: "))
        b = int(input("book: "))
        c = int(input("client: "))
        d1 = input("rent: ")
        d2 = input("return: ")
        d1 = d1.split('.')
        d2 = d2.split('.')
        d1 = list(map(int, d1))
        d2 = list(map(int, d2))
        try:
            d1 = datetime.datetime(d1[2], d1[1], d1[0])
            d2 = datetime.datetime(d2[2], d2[1], d2[0])
        except:
            raise ValueError("invalid date")
        if d2 < d1:
            raise ValueError("invalid date!")
        found = 0
        for q in self.bookservice.bookrepo.books:
            if q.id == b:
                found = 1
        if found == 0:
            raise ValueError("book not found!")
        found = 0
        for o in self.clientservice.clientrepo.clients:
            if o.id == c:
                found = 1
        if found == 0:
            raise ValueError("client not found!")
        self.rentservice.duplicated_id(i)
        self.rentservice.already_rented(b, d1, d2)
        self.rentservice.create(i, b, c, d1, d2)

    def return_book(self):
        c = int(input("client: "))
        b = int(input("book: "))
        d = input("date: ")
        d = d.split(".")
        d = list(map(int, d))
        try:
            d = datetime.datetime(d[2], d[1], d[0])
        except:
            raise ValueError("invalid date!")
        self.rentservice.search_for_rent(c, b, d)
        self.rentservice.rentrepo.return_book(c, b, d)

    def print_rent(self):
        if len(self.rentservice.rentrepo.rent) == 0:
            raise ValueError("no rents!")
        for i in self.rentservice.rentrepo.rent:
            print(i)
    
    def search_book_id(self):
        Id = int(input("id: "))
        match = self.bookservice.search_by_id(Id)
        for i in match:
            print(i)
        if len(match) == 0:
            raise ValueError("no matching")

    def search_book_title(self):
        title = input("title: ")
        match = self.bookservice.search_by_title(title)
        for i in match:
            print(i)
        if len(match) == 0:
            raise ValueError("no matching")

    def search_book_author(self):
        author = input("author: ")
        match = self.bookservice.search_by_author(author)
        for i in match:
            print(i)
        if len(match) == 0:
            raise ValueError("no matching")

    def search_client_id(self):
        Id = int(input("id: "))
        match = self.clientservice.search_by_id(Id)
        for i in match:
            print(i)
        if len(match) == 0:
            raise ValueError("no matching")

    def search_client_name(self):
        name = input("name: ")
        match = self.clientservice.search_by_name(name)
        for i in match:
            print(i)
        if len(match) == 0:
            raise ValueError("no matching")

    def most_rented_book(self):
        new_list = self.rentservice.most_rented_book()
        print(new_list)
        new_list = sorted(new_list, key=itemgetter(1))
        new_list = list(reversed(new_list))
        for i in new_list:
            for j in self.bookservice.bookrepo.books:
                if i[0] == j.id:
                    print(j.author +"'s " +  j.title + " rented " + str(i[1]) + " times")

    def most_rented_author(self):
        whattoprint = self.bookservice.most_rented_author(self.rentservice.most_rented_book())
        print(whattoprint)

    def active_clients(self):
        activ = self.rentservice.active_clients()
        activ = sorted(activ, key=itemgetter(1))
        activ = list(reversed(activ))
        for i in activ:
            for j in self.clientservice.clientrepo.clients:
                if i[0] == j.id:
                    print(j.name + " " + str(i[1]) + " days")

    def undoO(self):
        self.undo.undo()
    def redoO(self):
        self.undo.redo()
    def start(self):
        while True:
            try:
                self.print_main_menu()
                choice = input("command: ")
                if choice == "1":
                    self.print_manage_list()
                    choice = input("command: ")
                    if choice == "1":
                        self.print_what_to_list()
                        choice = input("command: ")
                        if choice == "1":
                            self.add_book()
                        if choice == "2":
                            self.add_client()
                    elif choice == "2":
                        self.print_what_to_list()
                        choice = input("command: ")
                        if choice == "1":
                            self.update_book()
                        if choice == "2":
                            self.update_client()
                    elif choice == "3":
                        self.print_what_to_list()
                        choice = input("command: ")
                        if choice == "1":
                            self.remove_book()
                        if choice == "2":
                            self.remove_client()
                    elif choice == "4":
                        self.print_what_to_list()
                        choice = input("command: ")
                        if choice == "1":
                            self.print_books()
                        if choice == "2":
                            self.print_clients()
                elif choice == "2":
                    self.print_rentreturn()
                    choice = input("command: ")
                    if choice == "1":
                        self.rent_book()
                    elif choice == "2":
                        self.return_book()
                    elif choice == "3":
                        self.print_rent()
                elif choice == "3":
                    self.print_search()
                    choice = input("command: ")
                    if choice == "1":
                        self.print_search_book()
                        choice = input("command: ")
                        if choice == "1":
                            self.search_book_id()
                        elif choice == "2":
                            self.search_book_title()
                        elif choice == "3":
                            self.search_book_author()
                    elif choice == "2":
                        self.print_search_client()
                        choice = input("command: ")
                        if choice == "1":
                            self.search_client_id()
                        elif choice == "2":
                            self.search_client_name()
                elif choice == "4":
                    self.print_statistics()
                    choice = input("command: ")
                    if choice == "1":
                        self.most_rented_book()
                    elif choice == "2":
                        self.active_clients()
                    elif choice == "3":
                        self.most_rented_author()
                elif choice == "5":
                    self.undoO()
                elif choice == "6":
                    self.redoO()
                elif choice == "7":
                    return
            except ValueError as m:
                print(m)
'''
u = UndoController()
Books = RepoBook()
Rentals = RepoRental()
Clients = RepoClient()
b = BookService(u, Books, Rentals)
c = ClientService(u,Clients, Rentals)
r = RentService(Rentals)
ui = UI(b, c, r, u)
ui.start()
'''
