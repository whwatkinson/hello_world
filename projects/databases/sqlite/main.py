from sqlite3 import connect


def main() -> None:

    with connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT "Hello, World!"')
        print(cursor.fetchall()[0][0])

if __name__ == "__main__":
    main()
