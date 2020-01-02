from ui import *
from init_files import FilesInit
from textrepository import *
import pickle
import configparser

u = UndoController()
config = configparser.ConfigParser()
config.read("settings_text.ini")
#assume that every repo has the same extension
FilesInit("book.txt", "client.txt", "rent.txt")#restore the file values
if config['repositories']['books'].endswith(".txt"):
    Books = BookTextRepo("book.txt")
    Rentals = RentTextRepo("rent.txt")
    Clients = ClientTextRepo("client.txt")
elif config['repositories']['books'].endswith(".pickle"):
    pass
else:
    Books = RepoBook()
    Clients = RepoClient()
    Rentals = RepoRental()

b = BookService(u, Books, Rentals)
c = ClientService(u,Clients, Rentals)
r = RentService(Rentals, u)
ui = UI(b, c, r, u)
ui.start()

