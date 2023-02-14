from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'watagatapitusberry'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/processing', methods=['POST'])
def processing():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("results.html")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)