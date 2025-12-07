class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        """Return all contracts for this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all unique books for this author"""
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        """Create a new contract and return it"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum royalties from all author contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        """Return all contracts for this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all unique authors for this book"""
        return list({contract.author for contract in self.contracts()})


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate types
        if not isinstance(author, Author):
            raise Exception("author must be Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts matching a date, in creation order"""
        return [contract for contract in cls.all if contract.date == date]
