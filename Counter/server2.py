from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'secure'

# Read up on HTTP request/response cycle, GET/POST, and sessions 9/16/21


@app.route('/')
def index():
    count = 0
    if 'count' not in session:
        session['count'] = 0
    
    if 'visits' not in session:
        session['visits'] = 0
        
    else:
        session['visits'] += 1
        session['count'] += 1
        
    print(session['visits'])
    return render_template('index2.html', count = session['count'])
    #count=session['count']

@app.route('/addtwo', methods=['POST'] )
def add2():
    if 'visits' not in session:
        session['visits'] = 1
        
    else:
        session['visits'] += 1
        session['count'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def destroy():
    session.pop('visits', None) 
    
    return redirect('/')

@app.route('/userincr', methods=['POST'])
def userAdd():
    session['visits'] += (int(request.form['num']) - 1)
    session['count'] += (int(request.form['num']) - 1)
    return redirect('/')


#NOTE: line 12 raises an error when i try to reset the count. also, if i set session['count'] = count, then count no longer increments likes I want it to. will need to ask as to why. 
# also, just had to comment out all the counts because once i deleted the cookie, all hell broke loose. and then once i did get it working agian, somehow my solution for count no longer was working... UUUGGGGHH. 9/16/21

@app.route('/resetcount', methods=['POST'])
def destroy2():
    session.pop('count', None)
    session.pop('visits', None)

    return redirect('/')

if __name__== '__main__':
    app.run(debug=True)