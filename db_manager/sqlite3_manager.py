import sqlite3
import typing

from loggers.json_logger import JsonLogger


class SQLite3Manager:
    def __init__(self,
                 db_name: str):
        self.__db_name = db_name
        self.__logger = JsonLogger(file_log='logs/db.log')

        try:
            connection = sqlite3.connect(db_name)
            cur = connection.cursor()
            self.__logger.info(f'Connected to: {db_name}')
            cur.execute("""CREATE table if not exists scores(
                    name TEXT, 
                    score INTEGER
                )
            """).fetchall()
        except sqlite3.Error as error:
            self.__logger.error(error)
        finally:
            if connection:
                connection.close()

            self.__logger.info('Connection closed')

    def insert(self,
               player_name: str,
               score: int):
        try:
            connection = sqlite3.connect(self.__db_name)
            cur = connection.cursor()
            self.__logger.info(f'Connected to: {self.__db_name}')
            sqlite_insert_query = f"""INSERT INTO scores
                                  VALUES
                                  ('{player_name}', {score})"""
            count = cur.execute(sqlite_insert_query)
            self.__logger.info(f'Inserted Record ({player_name}, {score})')
            connection.commit()
            cur.close()

        except sqlite3.Error as error:
            self.__logger.error(error)
        finally:
            if connection:
                connection.close()

            self.__logger.info('Connection closed')

    def get_scores(self,
                   top: int = 5) -> typing.List[tuple]:
        try:
            connection = sqlite3.connect(self.__db_name)
            cur = connection.cursor()
            self.__logger.info(f'Connected to: {self.__db_name}')
            data = cur.execute("SELECT * FROM scores ORDER BY score").fetchall()
            self.__logger.info(f'SELECTED from scores: {data}')
            data.sort(key=lambda x: x[1], reverse=True)
        except sqlite3.Error as error:
            self.__logger.error(error)
        finally:
            if connection:
                connection.close()

            self.__logger.info('Connection closed')

        return data[: top]


if __name__ == '__main__':
    m = SQLite3Manager(db_name='scores.db')

    # for i in range(10):
    #     m.insert('adss', i)

    print(m.get_scores())