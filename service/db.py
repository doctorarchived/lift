from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class SQLiteDatabase(Database):
    import sqlite3

    connection = sqlite3.connect('test.db')

    def save(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass


class NoOpDatabase(Database):
    def save(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass
