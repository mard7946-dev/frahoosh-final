import sqlite3
from pathlib import Path


DB_NAME = "frahoosh.db"


class Database:

    def __init__(self):

        self.path = Path(DB_NAME)

        self.conn = sqlite3.connect(
            self.path,
            check_same_thread=False
        )

        self.create_tables()


    def create_tables(self):

        cursor = self.conn.cursor()


        # اطلاعات مدرسه
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS school_info(
                id INTEGER PRIMARY KEY,
                school_name TEXT,
                manager TEXT,
                academic_year TEXT
            )
            """
        )


        # کاربران
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                role TEXT,
                name TEXT
            )
            """
        )


        # دانش آموزان
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT,
                family TEXT,
                grade TEXT,
                class_name TEXT,
                parent_phone TEXT
            )
            """
        )


        # دبیران
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS teachers(
                id INTEGER PRIMARY KEY,
                name TEXT,
                subject TEXT,
                phone TEXT
            )
            """
        )


        # پرداخت ها
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS payments(
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                amount INTEGER,
                date TEXT,
                status TEXT
            )
            """
        )


        # پیام ها
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY,
                sender TEXT,
                receiver TEXT,
                text TEXT,
                date TEXT,
                status TEXT
            )
            """
        )


        self.conn.commit()


    def execute(
        self,
        query,
        params=()
    ):

        cursor = self.conn.cursor()

        cursor.execute(
            query,
            params
        )

        self.conn.commit()

        return cursor
