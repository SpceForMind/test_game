import sqlite3


class SQLite3Manager:
    def __init__(self,
                 db_name: str):
        self.__db_name = db_name

        try:
            connection = sqlite3.connect(db_name)
            cur = connection.cursor()
            cur.execute("""CREATE table if not exists scores(
                    name TEXT, 
                    score INTEGER
                )
            """).fetchall()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()

    def insert(self,
               player_name: str,
               score: int):
        try:
            connection = sqlite3.connect(self.__db_name)
            cur = connection.cursor()
            sqlite_insert_query = f"""INSERT INTO scores
                                  VALUES
                                  ('{player_name}', {score})"""
            count = cur.execute(sqlite_insert_query)
            connection.commit()
            cur.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()

    def get_scores(self,
                   top: int = 5):
        try:
            connection = sqlite3.connect(self.__db_name)
            cur = connection.cursor()
            data = cur.execute("SELECT * FROM scores ORDER BY score").fetchall()
            data.sort(key=lambda x: x[1], reverse=True)
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()
        print(data[: top])

        return data[: top]


if __name__ == '__main__':
    m = SQLite3Manager(db_name='scores.db')

    # for i in range(10):
    #     m.insert('adss', i)

    print(m.get_scores())