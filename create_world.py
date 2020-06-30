import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_task(conn, task):
    """
    Create a new task into the tasks table
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' INSERT INTO tasks(task_name, worker_id, time_to_make, resource_name, resource_amount)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def create_worker(conn, worker):
    """
    Create a new worker
    :param conn:
    :param worker:
    :return:
    """

    sql = ''' INSERT INTO Workers(name, status)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, worker)
    return cur.lastrowid


def create_resource(conn, resource):
    """
    Create a new resource
    :param conn:
    :param resource:
    :return:
    """

    sql = ''' INSERT INTO Resources(name, amount)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, resource)
    return cur.lastrowid


def main():
    database = r"world.db"

    sql_create_tasks_table = """CREATE TABLE Tasks (
                                    id INTEGER PRIMARY KEY,
                                    task_name TEXT NOT NULL,
                                    worker_id INTEGER REFERENCES workers(id),
                                    time_to_make INTEGER NOT NULL,
                                    resource_name TEXT NOT NULL,
                                    resource_amount INTEGER NOT NULL
                                );"""

    sql_create_workers_table = """CREATE TABLE IF NOT EXISTS Workers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    status TEXT NOT NULL
                                );"""

    sql_create_resources_table = """CREATE TABLE IF NOT EXISTS Resources (
                                    name TEXT PRIMARY KEY,
                                    amount INTEGER NOT NULL
                                );"""

    task_1 = ('assembling wagons', 1, 2, 'wood', 10)
    task_2 = ('researching nukes', 2, 5, 'metal', 100)

    worker_1 = (1, 'Alice')
    worker_2 = (2, 'Bob')

    resource_1 = ('wood', 50)
    resource_2 = ('metal', 250)

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create tables
        create_table(conn, sql_create_tasks_table)

        create_table(conn, sql_create_workers_table)

        create_table(conn, sql_create_resources_table)

        # add data to tables
        create_task(conn, task_1)
        create_task(conn, task_2)
        create_worker(conn, worker_1)
        create_worker(conn, worker_2)
        create_resource(conn, resource_1)
        create_resource(conn, resource_2)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
