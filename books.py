import csv


FILENAME = 'books.csv'

class Books():
    def __init__(self,book_id,title,author,genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def to_list(self):
        return [self.book_id,self.title,self.author,self.genre]

def create_book(book_id,title,author,genre):
    b = Books(book_id,title,author,genre)
    try:
        with open(FILENAME,'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(b.to_list())
    except(FileNotFoundError):
        data = []
    print('Book Created Successfully')

def read_books():
    with open(FILENAME,'r',newline='') as f:
        data = csv.reader(f)
        print(list(data))

def update_book(idk,n_book_id,n_title,n_author,n_genre):
    f = open(FILENAME,'r',newline='')
    data = list(csv.reader(f))

    UPDATED = False

    for book in data:
        if book[0] == str(idk):
            book[0] = n_book_id
            book[1] = n_title
            book[2] = n_author
            book[3] = n_genre
            UPDATED = True

    if UPDATED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print('Book Updated Successfully...')
    else:
        print('Invalid Book...')

def delete_user(idd):
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))

    DELETED = False

    for book in data:
        if book[0] == str(idd):
            data.remove(book)
            DELETED = True

    if DELETED:
        with open(FILENAME,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print("Deleted User Successfully....")
    else:
        print('Invalid book....')

def search_book(n_genre):
    with open(FILENAME,'r',newline='') as f:
        data = list(csv.reader(f))

    for book in data:
        if book[3] == n_genre:
            print(book)

def main():
    print('Welcome to the Library.')
    print('Press 1 to Create the Book.')
    print('Press 2 to Read all the Books..')
    print('Press 3 to Update the Book...')
    print('Press 4 to Delete the Book....')
    print('Press 5 to Search a Specified Book.....')
    choice = int(input('Enter the Choice:\n'))
    if choice == 1:
        book_id = int(input('Enter the Book Id:\n'))
        title = input('Enter the Title of the Book:\n')
        author = input('Enter the Author of the Book:\n')
        genre = input('Enter the Genre of the Book:\n')
        create_book(book_id,title,author,genre)
    elif choice == 2:
        read_books()
    elif choice == 3:
        idk = int(input('Enter the book id to be updated:\n'))
        n_book_id = int(input('Enter the new Book id:\n'))
        n_title = input('Enter the new title of the Book:\n')
        n_author = input('Enter the new Author of the Book:\n')
        n_genre = input('Enter the new genre of the Book:\n')
        update_book(idk,n_book_id,n_title,n_author,n_genre)
    elif choice == 4:
        idd = int(input('Enter the book to be Deleted:\n'))
        delete_user(idd)
    elif choice == 5:
        n_genre = input('Enter the genre of the book to search:\n')
        search_book(n_genre)
    else:
        print('Invalid Choice.......')

if __name__ == '__main__':
    main()
    