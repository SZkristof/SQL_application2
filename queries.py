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

'''
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
'''

def task_1():
    sql = fetch_database("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name),
                         schools.name,schools.country FROM mentors
                         LEFT JOIN schools ON mentors.city=schools.city;""")
    table_titles = ("Mentor", "School", "Country")
    result = [(sql), (table_titles)]
    return result


def task_2():
    sql = fetch_database("""SELECT CONCAT(mentors.first_name,' ',mentors.last_name),
                          schools.name,schools.country FROM mentors
                          FULL JOIN schools ON mentors.city=schools.city
                          ORDER BY mentors.id;""")
    table_titles = ("Mentor", "School", "Country")
    result = [(sql), (table_titles)]
    return result


def task_3():
    sql = fetch_database("""SELECT schools.country,COUNT(mentors.first_name) AS Counts
                          FROM mentors LEFT JOIN schools ON mentors.city=schools.city
                          GROUP BY schools.country;""")
    table_titles = ("Country", "Count")
    result = [(sql), (table_titles)]
    return result


def task_4():
    sql = fetch_database("""SELECT schools.name,CONCAT(mentors.first_name,' ',mentors.last_name)
                          FROM mentors JOIN schools ON schools.contact_person=mentors.id;""")
    table_titles = ("School", "Contact")
    result = [(sql), (table_titles)]
    return result


def task_5():
    # doesn't work properly
    sql = fetch_database("""SELECT applicants.first_name,applicants.application_code,
                          applicants_mentors.creation_date
                          FROM applicants
                          LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.mentor_id
                          WHERE applicants_mentors.creation_date > '2016-01-01'
                          ORDER BY applicants_mentors.creation_date DESC;""")
    table_titles = ("Applicant", "Application code", "Date")
    result = [(sql), (table_titles)]
    return result


def task_6():
    sql = fetch_database("""SELECT applicants.application_code,
                          CONCAT(applicants.first_name,' ',applicants.last_name),
                          CONCAT(mentors.first_name,' ',mentors.last_name)
                          FROM applicants
                          LEFT JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
                          LEFT JOIN mentors ON mentors.id=applicants_mentors.mentor_id;""")
    table_titles = ("Application code", "Applicant", "Mentor")
    result = [(sql), (table_titles)]
    return result
