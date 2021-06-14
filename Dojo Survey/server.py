from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def next_page():
    print("resquest.form")
    name_from_form = request.form['name']
    location_on_form = request.form['location']
    language_on_form = request.form['language']
    comment_on_form = request.form['comment']
    return render_template("show.html", name_template=name_from_form, location_result = location_on_form, language_result = language_on_form, comment_result = comment_on_form)


if __name__ == "__main__":
    app.run(debug=True)
