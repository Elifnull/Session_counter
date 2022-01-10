from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "helloha"


@app.route("/")
def index():
    if "count" in session:
        return render_template("index.html")
    else:
        session['count'] = 0
        return render_template('index.html')

@app.route('/count+')
def count():
    session['count'] += 1
    return redirect("/")

@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/double')
def double():
    session['count'] += 2
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)