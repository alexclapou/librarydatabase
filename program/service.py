from repository import *
from textrepository import  BookTextRepo
from undo1 import *
from domain import *
class BookService:
    def __init__(self, undo, bookrepo, rentrepo):
        self.undo = undo
        self.bookrepo = bookrepo
        self.rentrepo = rentrepo

    def init_books(self):
        books_name = ["Orasul Bantuit", "Pariul Pierdut", "Cartea", "01", "451 Fahrenheit", "Jurnalul", "Amintiri din Copilarie", "Cartea", "Padurea Fermecata", "Fermecata", "Stralucirea"]
        authors_name = ["Stephen King", "Creanga", "Eminescu", "Rebreanu", "Ion", "Rowling", "Tolkien", "George", "Martin","Cooper"]
        index = 0
        while index < 9:
            random_book = random.randint(0, 9)
            random_name = random.randint(0, 9)
            index = index + 1
            self.bookrepo.books.append(Book(index, books_name[random_book], authors_name[random_name]))

    def duplicated_id(self, Id):
        for i in self.bookrepo.books:
            if i.id == Id:
                raise ValueError("id duplicated!")

    def existId(self, Id):
        found = 0
        for i in self.bookrepo.books:
            if i.id == Id:
                found = 1
        if found == 0:
            raise ValueError("no id!")

    def search_by_id(self, Id):
        match = []
        for i in self.bookrepo.books:
            if i.id == Id:
                match.append(i)
        return match

    def search_by_title(self, title):
        match = []
        title = title.casefold()
        for i in self.bookrepo.books:
            if title in i.title.casefold():
                match.append(i)
        return match

    def search_by_author(self, author):
        match = []
        author = author.casefold()
        for i in self.bookrepo.books:
            if author in i.author.casefold():
                match.append(i)
        return match

    def another_book(self, Id, rent_list):
        number_rent = 0
        for i in self.bookrepo.books:
            if i.id == Id:
                autor = i.author
        for i in rent_list:
            for j in self.bookrepo.books:
                if autor == j.author and i[0] == j.id:
                    number_rent = number_rent + i[1]
        return number_rent

    def create(self, bookid, title, author):
        book = self.bookrepo.add_book(Book(bookid, title, author))
        book = Book(bookid, title, author)
        undo = FunctionCall(self.bookrepo.remove, bookid)
        redo = FunctionCall(self.bookrepo.add_book, book)
        op = Operation(undo, redo)
        self.undo.recordOperation(op)

    def deletekefaki(self, Id):
        #delete book
        used = []
        book = self.bookrepo.remove(Id)
        undo = FunctionCall(self.bookrepo.add_book, book)
        redo = FunctionCall(self.bookrepo.remove, Id)
        op = Operation(undo, redo)
        used.append(op)
        new_list = self.rentrepo.delete_rent_book(Id)
        for i in new_list:
            undo = FunctionCall(self.rentrepo.rent_book, i.rentalid, i.bookid, i.clientid, i.rented, i.returned)
            redo = FunctionCall(self.rentrepo.delete_rent_book, Id)
            op = Operation(undo, redo)
            used.append(op)
        functions = CascadeOperation(used) 
        self.undo.recordOperation(functions)

    def updateone(self, bookid, booktitle, bookauthor):
        book = self.bookrepo.update(bookid, booktitle, bookauthor)
        undo = FunctionCall(self.bookrepo.update, bookid, book.title, book.author)
        redo = FunctionCall(self.bookrepo.update, bookid, booktitle, bookauthor)
        op = Operation(undo, redo)
        self.undo.recordOperation(op)

    def most_rented_author(self, new_list):
        #new_list = a list which contains books id and rent times 
        maxim = 0
        author_id = 0
        for i in self.bookrepo.books:
            ap = 0
            for j in new_list:
                if i.id == j[0]:
                    ap = ap  + self.another_book(i.id, new_list)
            if ap > maxim:
                author_id = i.id
                maxim = ap
        for i in self.bookrepo.books:
            if i.id == author_id:
                return i.author

class ClientService:
    def __init__(self, undo, clientrepo, rentrepo):
        self.clientrepo = clientrepo
        self.undo = undo
        self.rentrepo = rentrepo

    def init_clients(self):
        names = ["Makai", "Alex", "Adi", "Razvan", "Andreea", "Maia", "Denisa", "Gabi", "Flavia", "Andrei", "Sergiu"]
        index = 0
        while index < 9:
            random_name = random.randint(0, 9)
            index = index + 1
            self.clientrepo.clients.append(Client(index, names[random_name]))

    def duplicated_id(self, Id):
        for i in self.clientrepo.clients:
            if i.id == Id:
                raise ValueError("id duplicated!")

    def existId(self, Id):
        found = 0
        for i in self.clientrepo.clients:
            if i.id == Id:
                found = 1
        if found == 0:
            raise ValueError("No id!")

    def search_by_id(self, Id):
        match = []
        for i in self.clientrepo.clients:
            if i.id == Id:
                match.append(i)
        return match

    def create(self, clientid, name):
        client = self.clientrepo.add_client(Client(clientid, name))
        undo = FunctionCall(self.clientrepo.remove, clientid)
        redo = FunctionCall(self.clientrepo.add_client, client)
        op = Operation(undo, redo)
        self.undo.recordOperation(op)
        return client 

    def deletekefaki(self, Id):
        #delete client
        used = []
        client = self.clientrepo.remove(Id)
        undo = FunctionCall(self.clientrepo.add_client, client)
        redo = FunctionCall(self.clientrepo.remove, Id)
        op = Operation(undo, redo)
        used.append(op)
        new_list = self.rentrepo.delete_rent_client(Id)
        for i in new_list:
            undo = FunctionCall(self.rentrepo.rent_book, i.rentalid, i.bookid, i.clientid, i.rented, i.returned)
            redo = FunctionCall(self.rentrepo.delete_rent_book, Id)
            op = Operation(undo, redo)
            used.append(op)
        functions = CascadeOperation(used) 
        self.undo.recordOperation(functions)

    def updateone(self, clientid, name):
        client = self.clientrepo.update(clientid, name)
        undo = FunctionCall(self.clientrepo.update, clientid, client.name)
        redo = FunctionCall(self.clientrepo.update, clientid, name)
        op = Operation(undo, redo)
        self.undo.recordOperation(op)
        return client 
 
    def search_by_name(self, name):
        match = []
        name = name.casefold()
        for i in self.clientrepo.clients:
            if name in i.name.casefold():
                match.append(i)
        return match

class RentService:
    def __init__(self, rentrepo, undorepo):
        self.rentrepo = rentrepo
        self.undo = undorepo
   
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
            for i in self.rentrepo.rent:
                if i.bookid == bookid:
                    if (d1 > i.rented and d1 < i.returned) or (d2 > i.rented and d2 < i.returned):
                        year = year + 10
                        d1 = datetime.datetime(year, month1, day1) 
                        d2 = datetime.datetime(year, month2, day2) 
            index = index + 1
            self.rentrepo.rent.append(Rental(index, bookid, clientid, d1, d2))

    def already_rented(self, bookid, rentdate, returndate):
        for i in self.rentrepo.rent:
            if i.bookid == bookid:
                if (rentdate > i.rented and rentdate < i.returned) or (returndate > i.rented and returndate < i.returned):
                    raise ValueError("can't rent t his!")

    def search_for_rent(self, client, book, returned):
        found = 0 
        for i in self.rentrepo.rent:
            if i.bookid == book and i.clientid == client and returned == i.returned:
                found = 1
        if found == 0:
            raise ValueError("no rent!")

    def duplicated_id(self, Id):
        for i in self.rentrepo.rent:
            if i.rentalid == Id:
                raise ValueError("id duplicated!")

    def most_rented_book(self):
        new_list = []
        for i in self.rentrepo.rent:
            element = []
            if len(new_list) == 0:
                element.append(i.bookid)
                element.append(1)
                new_list.append(element)
            else:
                found = 0
                for j in new_list:
                    if j[0] == i.bookid:
                        j[1] = j[1] + 1
                        found = 1
                if found == 0:
                    element.append(i.bookid)
                    element.append(1)
                    new_list.append(element)
        return new_list
    
    def active_clients(self):
        lista = []
        for i in self.rentrepo.rent:
            element = []
            if len(lista) == 0:
                element.append(i.clientid)
                element.append((i.returned - i.rented).days)
                lista.append(element)
            else:
                found = 0
                for j in lista:
                    if j[0] == i.clientid:
                        j[1] = j[1] + (i.returned - i.rented).days
                        found = 1
                if found == 0:
                    element.append(i.clientid)
                    element.append((i.returned - i.rented).days)
                    lista.append(element)
        return lista



    def create(self, rentid, bookid, clientid, rented, returned):
        rent = self.rentrepo.rent_book(rentid, bookid, clientid, rented, returned)
        undo = FunctionCall(self.rentrepo.return_book, clientid, bookid, returned)
        redo = FunctionCall(self.rentrepo.rent_book, rentid, bookid, clientid, rented, returned)
        op = Operation(undo, redo)
        self.undo.recordOperation(op)
        return rent 
