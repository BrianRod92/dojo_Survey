from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'watagatapitusberry'

@app.route('/')
def index():
    return render_template("index.html")

# The code below processes the form data inputed by the user and stores the information in session
@app.route('/processing', methods=['POST'])
def processing():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')  # This redirects our user to the results page on Submit. The user never sees this '/processing' url

# After Submit on form "results.html" is rendered and displayed to the user
@app.route('/results')
def results():
    return render_template("results.html")

# In order to not have previous session information stored, this code below removes the session, and redirects back to the index route
@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)