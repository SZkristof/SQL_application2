from flask import Flask, render_template, request
import queries

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/mentors")
def show_mentors():
    show_table = queries.task_1()
    length = len(show_table)
    row_length = len(show_table[0])

    page_title = "Mentors and Country"
    table_titles = ("Mentor", "School", "Country")

    return render_template('show_table.html', length=length, show_table=show_table, row_length=row_length,
                           page_title=page_title, table_titles=table_titles)


if __name__ == '__main__':
    app.run(debug=True)
