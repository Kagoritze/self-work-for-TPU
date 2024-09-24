import psycopg2
import random
from datetime import datetime, timedelta
from config import host, user, password, db_name


class DataBaseManager():

    def __init__(self, host, user, password, db_name):
        self.connection = psycopg2.connect(dbname=db_name,
                                           user=user,
                                           password=password,
                                           host=host)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """Создание связанных таблиц"""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS Authors (
                author_id SERIAL PRIMARY KEY,
                name VARCHAR(100)
            );
            """, """
            CREATE TABLE IF NOT EXISTS Publishers (
                publisher_id SERIAL PRIMARY KEY,
                name VARCHAR(100)
            );
            """, """
            CREATE TABLE IF NOT EXISTS Categories (
                category_id SERIAL PRIMARY KEY,
                name VARCHAR(100)
            );
            """, """
            CREATE TABLE IF NOT EXISTS Books (
                book_id SERIAL PRIMARY KEY,
                title VARCHAR(100),
                author_id INT REFERENCES Authors(author_id),
                publisher_id INT REFERENCES Publishers(publisher_id),
                category_id INT REFERENCES Categories(category_id),
                year INT
            );
            """, """
            CREATE TABLE IF NOT EXISTS BookLoans (
                loan_id SERIAL PRIMARY KEY,
                book_id INT REFERENCES Books(book_id),
                loan_date DATE,
                return_date DATE
            );
            """
        ]
        for query in queries:
            self.cursor.execute(query)
        self.connection.commit()
        print("Таблицы созданы.")

    def insert_random_data(self):
        authors = [
            'Panil Danitsky', 'Nikita Churka', 'Sanya Tumen',
            'Maksauni Starosta', 'Egor Bugor'
        ]
        publishers = ['TPU', 'TSU', 'Elan', 'Mektep', 'Almaty kitap']
        categories = ['Fiction', 'Science', 'History', 'Biography', 'Fantasy']

        for name in authors:
            self.cursor.execute("INSERT INTO Authors (name) VALUES (%s);",
                                (name, ))
        self.connection.commit()
        print("Авторы вставлены.")

        for name in publishers:
            self.cursor.execute("INSERT INTO Publishers (name) VALUES (%s);",
                                (name, ))
        self.connection.commit()
        print("Издатели вставлены.")

        for name in categories:
            self.cursor.execute("INSERT INTO Categories (name) VALUES (%s);",
                                (name, ))
        self.connection.commit()
        print("Категории вставлены.")

        self.cursor.execute("SELECT COUNT(*) FROM Authors;")
        author_count = self.cursor.fetchone()[0]
        print(f"Количество авторов: {author_count}")
        self.cursor.execute("SELECT COUNT(*) FROM Publishers;")
        publisher_count = self.cursor.fetchone()[0]
        print(f"Количество издателей: {publisher_count}")
        self.cursor.execute("SELECT COUNT(*) FROM Categories;")
        category_count = self.cursor.fetchone()[0]
        print(f"Количество категорий: {category_count}")

        for _ in range(10):
            title = f"Book {_}"
            author_id = random.randint(1, author_count)
            publisher_id = random.randint(1, publisher_count)
            category_id = random.randint(1, category_count)
            year = random.randint(1990, 2023)
            self.cursor.execute(
                """
                INSERT INTO Books (title, author_id, publisher_id, category_id, year)
                VALUES (%s, %s, %s, %s, %s);
            """, (title, author_id, publisher_id, category_id, year))

        self.connection.commit()
        print("Книги вставлены.")

        for _ in range(5):
            book_id = random.randint(1, 10)
            loan_date = datetime.now() - timedelta(days=random.randint(0, 30))
            return_date = loan_date + timedelta(days=random.randint(1, 15))
            loan_date_str = loan_date.strftime('%Y-%m-%d')
            return_date_str = return_date.strftime('%Y-%m-%d')
            self.cursor.execute(
                """
                INSERT INTO BookLoans (book_id, loan_date, return_date)
                VALUES (%s, %s, %s);
            """, (book_id, loan_date_str, return_date_str))

        self.connection.commit()
        print("Выдачи книг вставлены.")

    def fetch_books_with_authors_and_publishers(self):
        """Вывод книг с их авторами и издателями"""
        query = """
            SELECT Books.title, Authors.name AS author_name, Publishers.name AS publisher_name
            FROM Books
            JOIN Authors ON Books.author_id = Authors.author_id
            JOIN Publishers ON Books.publisher_id = Publishers.publisher_id;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            print(f"Книга: {row[0]}, Автор: {row[1]}, Издатель: {row[2]}")

    def fetch_loans(self):
        """Вывод всех выдач книг"""
        query = """
            SELECT Books.title, BookLoans.loan_date, BookLoans.return_date
            FROM BookLoans
            JOIN Books ON BookLoans.book_id = Books.book_id;
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        for row in results:
            print(
                f"Книга: {row[0]}, Дата выдачи: {row[1]}, Дата возврата: {row[2]}"
            )

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    db_manager = DataBaseManager(host=host,
                                 user=user,
                                 password=password,
                                 db_name=db_name)

    # Создание таблиц
    db_manager.create_tables()

    # Вставка случайных данных
    db_manager.insert_random_data()

    # Выполнение запросов
    print("Книги с авторами и издателями:")
    db_manager.fetch_books_with_authors_and_publishers()

    print("\nВыдачи книг:")
    db_manager.fetch_loans()

    # Закрытие соединения с базой данных
    db_manager.close()
