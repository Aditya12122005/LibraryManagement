books = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Java Programming"},
    {"id": 3, "name": "Data Structures"}
]

def search_book(keyword):
    return [
        book for book in books
        if keyword.lower() in book["name"].lower()
    ]

if __name__ == "__main__":
    print(search_book("Python"))