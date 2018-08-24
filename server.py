from flask import Flask, render_template, redirect, request, session
request
import random
app = Flask(__name__)
app.secret_key = 'henlobilo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    loc = request.form['location']
    location_map = {
        'cave' : random.randint(3,7),
        'house' : random.randint(2,5),
        'farm' : random.randint(7,15),
        'casino' : random.randint(-50,50)
    }

    print loc
    print location_map[loc]
    curr_gold = location_map[loc]

    if not 'gold' in session:
        session['gold'] = curr_gold
    else:
        session['gold'] += curr_gold
    
    if curr_gold > 0:
        message = {
            'class' : 'green',
            'content' : "You won {} golds at the {}".format
                (curr_gold, loc)
        }

    else:
        message = {
            'class' : 'red',
            'content' : "You lost {} golds at the {}".format
                (curr_gold, loc)
        }

    if not 'activities' in session:
        session['activities'] = [message]
      
    else:
        session['activities'].append(message)
        session.modified = True


    return redirect('/')



app.run(debug=True)