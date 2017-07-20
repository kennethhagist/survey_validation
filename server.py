from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'SecretValidation'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey', methods=['POST'])
def survey():
    print request.form['name', 'location', 'language', 'comment']
    if len(request.form['name']) < 1:
        flash("blank name error message")
    elif len(request.form['comment']) < 1:
        flash("blank comment error message")
    elif len(request.form['comment']) > 121:
        flash("comment too long error message")
        return redirect('/')

    session['name', 'location', 'language', 'comment'] = request.form['name', 'location', 'language', 'comment']
    return redirect('/result')

app.route('/result')
def result():
    return render_template('result.html') #, survey = request.form)

app.run(debug=True)
