'''
create an init class so we don't have to add first 10 books/clients/rents everytime
comment the operation inside the appstart and we have the file before this
created to work easier
'''

class FilesInit:
    def __init__(self, book_file, client_file, rent_file):
        self.bookfile = book_file
        self.clientfile = client_file
        self.rent_file = rent_file
        self.init_book_file(book_file)
        self.init_client_file(client_file)
        self.init_rent_file(rent_file)

    def init_book_file(self, book_file):
        f = open(book_file, "w")
        b = []
        b.append("123, Pacienta tacuta, Alex Michaelides\n")
        b.append("401, Ion, Liviu Rebreanu\n")
        b.append("42, Harry Potter, Joanne Rowling\n")
        b.append("100, Dincolo de stele, Kristin Hannah\n")
        b.append("50, Vaduva de safir, Dinah Jefferies\n")
        b.append("150, Urzeala tronurilor, George Martin\n")
        b.append("1, Poezii, Mihai Eminescu\n")
        b.append("10, Amintiri din copilarie, Ion Creanga\n")
        b.append("13, Stralucirea, Stephen King\n")
        b.append("4, Sotia imperiala, Irina Reyn\n")
        for i in b:
            f.write(i)

    def init_client_file(self, client_file):
        f = open(client_file, "w")
        b = []
        b.append("1, Alex\n")
        b.append("2, Adi\n")
        b.append("3, Carmen\n")
        b.append("4, Maka\n")
        b.append("5, Semaca\n")
        b.append("6, Defe\n")
        b.append("7, Makelele\n")
        b.append("8, Oana\n")
        b.append("9, Denisa\n")
        b.append("10, Razvan\n")
        for i in b:
            f.write(i)

    def init_rent_file(self, rent_file):
        f = open(rent_file, "w")
        b = []
        b.append("103, 123, 1, 10.10.2013, 10.12.2013\n")
        b.append("104, 123, 1, 10.10.2014, 10.12.2014\n")
        b.append("105, 42, 4, 1.2.2015, 1.10.2015\n")
        b.append("106, 123, 5, 1.4.2004, 10.4.2004\n")
        b.append("107, 50, 2, 3.4.2017, 4.7.2017\n")
        b.append("109, 1, 7, 4.4.2019, 4.10.2019\n")
        b.append("110, 4, 9, 10.10.1999, 10.10.2000\n")
        b.append("111, 10, 8, 11.10.2011, 11.11.2011\n")
        b.append("112, 100, 1, 10.10.1980, 1.2.1983\n")
        b.append("113, 13, 4, 10.3.200, 10.4.2003\n")
        for i in b:
            f.write(i)

