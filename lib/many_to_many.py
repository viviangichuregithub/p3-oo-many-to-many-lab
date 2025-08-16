class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self.name = name
        type(self).all.append(self)

    def contracts(self):
        """Return a list of contracts for this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books associated with this author."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new contract with the given book, date, and royalties."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties from all contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        """Return a list of contracts for this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return a list of authors associated with this book."""
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts matching the given date."""
        return [contract for contract in cls.all if contract.date == date]
