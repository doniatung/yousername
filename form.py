from flask import Flask, render_template, request, session

my_app = Flask(__name__)
my_app.secret_key = 'rAndOmmstRInG'

currentUser = 'name'
currentPass = 'word' 


@my_app.route('/', methods = ['GET', 'POST'])
def root():
    if session.has_key('user') == True:
        return render_template('salutations.html', name = session['user'])
    else:
        return render_template('form.html') 

@my_app.route('/response', methods = ['POST', 'GET'])
def response():
    username = request.form['user']
    password = request.form['pass']
    
    if username == currentUser and password == currentPass:
        return render_template('salutations.html',name = username)
    
    elif username != currentUser:
        return render_template('uhoh.html', message = 'wrong username!')

    else:
        return render_template('uhoh.html', message = 'wrong password')
    

@my_app.route('/logout', methods = ['POST', 'GET'])
def logout():
    session.clear()
    return render_template('form.html')
    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
