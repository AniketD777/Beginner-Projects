#Create a library class for different genre=> Methods: DisplayBooks, IssueBook, ReturnBook, AddNewBook.

class library:
    BooksList={}
    def __init__(self,BooksList):
        self.BooksList={key:"Available" for key in BooksList}
    
    def DisplayBooks(self):
        print("")
        for book,check in self.BooksList.items():
            print(f'-{book} -> {check}')
        print("")
    
    def IssueBook(self,BookName):
        if BookName not in self.BooksList.keys():
            print("\nNo Such Book Available!\n")
        elif(self.BooksList[BookName]=="Available"):
            self.BooksList[BookName]="Currently Unavailable"
            print("\nMake sure to return it within 14 days.\nHappy Reading!!\n")
        else:
            print("\nSorry the Book is already issued and unavailable for now. Do check out for other books.\n")
    
    def ReturnBook(self,BookName):
        if(BookName not in self.BooksList.keys()):
            print("\nThis Book doesn't belong to this library. But to add it use AddNewBook functionality.\n")
        elif(self.BooksList[BookName]=="Available"):
            print("\nThis book is already available and doesn't belong here.\n")
        elif(self.BooksList[BookName]=="Currently Unavailable"):
            self.BooksList[BookName]="Available"
            print("\nThanks for returning.\nMake sure to visit books section once to check our new collections.\n")
            
    def AddNewBook(self,BookName):
        if BookName in self.BooksList.keys(): 
            print("\nSorry we already have one.\n")
        else:
            self.BooksList[BookName]="Available"
            print("\nBook Successfully Added!\n")

def main():
    ScienceFiction=library(['The Foundation Trilogy','The Time Machine','Snow Crash','Solaris'])
    Novels=library(['The Lord of the Rings','The Hobbit','Jane Eyre','The Invisible Man','Frankenstein'])
    
    AvailableSections={"ScienceFiction":ScienceFiction,"Novels":Novels}
    print("Available Sections=>")
    for key,value in AvailableSections.items(): 
        print(f'-{key}')
    SelectSection=input("\nSelect Section OR 'Exit' to leave: ")
    while(SelectSection!="Exit"):
        if SelectSection not in AvailableSections.keys():
            print("\nInvalid Section! Try Again.")
        else:
            print(f'\n              **************Inside "{SelectSection}" Section:***************\n')
            print("Options: DisplayBooks, IssueBook, ReturnBook, AddNewBook\n")
            SelectOption=input("Select Option OR 'Back' to go back to Section Selection: ")
            while(SelectOption!="Back"):
                if(SelectOption=="DisplayBooks"):
                    AvailableSections[SelectSection].DisplayBooks()
                elif(SelectOption=="IssueBook"):
                    WhichBook=input("Enter BookName:")
                    AvailableSections[SelectSection].IssueBook(WhichBook)
                elif(SelectOption=="ReturnBook"):
                    WhichBook=input("Enter BookName to Return: ")
                    AvailableSections[SelectSection].ReturnBook(WhichBook)
                elif(SelectOption=="AddNewBook"):
                    WhichBook=input("Enter BookName to be Added: ")
                    AvailableSections[SelectSection].AddNewBook(WhichBook)
                else:
                    print("Invalid Option! Try Again.")
                print(f'\n              **************Inside "{SelectSection}" Section:***************\n')
                print("Options: DisplayBooks, IssueBook, ReturnBook, AddNewBook\n")             
                SelectOption=input("Select Option OR 'Back' to go back to Section Selection: ")
        print("\nAvailable Sections=>")
        for key,value in AvailableSections.items(): 
            print(f'{key}')
        SelectSection=input("\nSelect Section OR 'Exit' to leave: ")
        
if __name__=="__main__":
    main()



