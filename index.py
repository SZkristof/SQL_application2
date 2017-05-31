from flask import Flask, render_template, request
import queries

app = Flask(__name__)


@app.route("/")
def index():
    show_table = queries.show_table()
    length = len(show_table)
    row_length = len(show_table[0])
    return render_template('index.html', length=length, show_table=show_table, row_length=row_length)


if __name__ == '__main__':
    app.run(debug=True)
