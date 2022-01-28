from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secure'

# Read up on HTTP request/response cycle, GET/POST, and sessions 9/16/21


@app.route('/')
def index():
    
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
        
    print(session['visits'])
    return render_template('index.html')

@app.route('/+2')
def addTwo():
    if 'visits' not in session:
        session['visits'] = 2
    else:
        session['visits'] += 2

    return render_template('index.html')


@app.route('/destroy_session')
def destroy():
    # session.clear()  #NOTE: this clears all keys.
    # session.pop('visits')  #NOTE: this clears a specific key, in this case -> 'visits'
    if 'visits' in session:
        session.clear()
    else:
        raise ValueError('no visits')

    return render_template('index.html')

#NOTE: the above code, satisfies counter assignment request 1-4. Doesnt satisfy any of the additional bonus questions. 

if __name__== '__main__':
    app.run(debug=True)