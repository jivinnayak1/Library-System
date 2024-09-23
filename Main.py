global booklist
Booklist = []

class Library:
    def Add_Book(self,book):
        if book not in Booklist:
            Booklist.append(book)
            print(f"{book} added succesfully")

    def Show_Book(self):
        print("Available books")
        print("--------------")

        for book in Booklist:
            print(book)

        print("--------------")

    def Borrow_Book(self,book):
        if book in Booklist:
            print(book)
            print(f"Thank you for purchasing {book} book")
            Booklist.remove(book)

MrSubhadeep = Library()

MrSubhadeep.Add_Book("Marvels")
MrSubhadeep.Add_Book("Malgudi_Days")
MrSubhadeep.Show_Book()
MrSubhadeep.Borrow_Book("Marvels")
MrSubhadeep.Show_Book()