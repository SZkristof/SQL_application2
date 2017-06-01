from flask import Flask, render_template, request
import queries

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<action_id>")
def show_mentors(action_id):
    if action_id:
        show_table = choose_task(action_id)[0]
        length = len(show_table)
        row_length = len(show_table[0])
        page_title = "Mentors and Country"
        table_titles = choose_task(action_id)[1]

        return render_template('show_table.html', length=length, show_table=show_table, row_length=row_length,
                               page_title=page_title, table_titles=table_titles)


def choose_task(action_id):
    try:
        all_queries = {'mentors': queries.task_1,
                       'all-school': queries.task_2,
                       'mentors-by-country': queries.task_3,
                       'contacts': queries.task_4,
                       'applicants': queries.task_5,
                       'applicants-and-mentors': queries.task_6}
        return_value = all_queries[action_id]()
        return return_value
    except TypeError:
        print("fail")

if __name__ == '__main__':
    app.run(debug=True)
