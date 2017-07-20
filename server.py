from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'SecretValidation'

@app.route('/')
def index():
    return render_template("index.html")

#@app.route('/survey')
#def survey():
    #print request.form['name', 'location', 'language', 'comment']
    #session['name', 'location', 'language', 'comment'] = request.form['name', 'location', 'language', 'comment']
    #return redirect('/result')

@app.route('/result', methods=['POST'])
def result():
    print request.form
    if len(request.form['name']) and len(request.form['comment']) > 0 and len(request.form['comment']) > 121:
        return render_template('result.html', user = request.form)
    else:
        flash("Name or Comment field is blank or Comment field exceeds 120 characters")
        return redirect('/')

app.run(debug=True)
