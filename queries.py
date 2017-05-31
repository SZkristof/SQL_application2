import psycopg2


def user_data():
    with open("user.txt") as file:
        data = file.read()
        data = data.split(',')
        return data


def fetch_database(query):
    try:
        data = user_data()
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if conn:
            conn.close()


def modify_database(query):
    try:
        data = user_data()
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query)

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if conn:
            conn.close()


def show_table():
    return fetch_database("""SELECT * FROM schools;""")


def task_1():
    return fetch_database("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name),
                          schools.name,schools.country FROM mentors
                          LEFT JOIN schools ON mentors.city=schools.city""")


def task_2():
    return fetch_database("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name),
                          schools.name,schools.country FROM mentors
                          FULL JOIN schools ON mentors.city=schools.city
                          ORDER BY mentors.id""")


def task_3():
    return fetch_database("""SELECT schools.country,COUNT(mentors.first_name) AS Counts
                          FROM mentors LEFT JOIN schools ON mentors.city=schools.city
                          GROUP BY schools.country""")


def task_4():
    return fetch_database("""SELECT schools.name,CONCAT(mentors.first_name,' ',mentors.last_name)
                          FROM mentors JOIN schools ON schools.contact_person=mentors.id""")
