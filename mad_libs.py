import random
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

def check_idnumber(id_number):
    if id_number == '1' or id_number == '2':
        word = random.choice(name)
    elif id_number == '3':
        word = random.choice(place)
    elif id_number == '4' or id_number == '5':
        word = random.choice(plural_noun)
    elif id_number == '6' or id_number == '11':
        word = random.choice(adjective)
    elif id_number == '7':
        word = random.choice(vehicle_type)
    elif id_number == '8' or id_number == '12':
        word = random.choice(noun)
    elif id_number == '9':
        word = random.choice(occupation)
    elif id_number == '10':
        word = random.choice(female_name)
    return word

name = ['Alfred', 'Arinze', 'Micheal', 'Tracy']
place = ['Tokyo', 'Japan', 'Nigeria', 'Canada', 'Usa']
plural_noun = ['Bags', 'Fishes', 'Pots', 'Houses']
adjective = ['Sweet', 'Tall', 'Ahead', 'Amazing']
vehicle_type = ['Bus', 'Train', 'SUV', 'Van']
noun = ['Car', 'Drink', 'Foot', 'Leg', 'Tree', 'Woman']
occupation = ['Software Engineer', 'Teacher', 'Doctor', 'Lawyer', 'Carpenter']
female_name = ['Stacy', 'Ada', 'Brittney', 'Jeniffer', 'Sarah', 'Esther']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/random_process', methods=['POST'])
def random_word():
    id_number = request.form['id']
    word = check_idnumber(id_number)
    return jsonify({'random_word' : word})
    

@app.route('/story', methods=['POST'])
def story():
    missing_words = {'name1':request.form['name1'], 'name2':request.form['name2'],
    'place':request.form['place'], 'plural_noun1':request.form['plural_noun1'],
    'plural_noun2':request.form['plural_noun2'], 'adjective1':request.form['adjective1'] ,
    'vehicle':request.form['vehicle'], 'noun1':request.form['noun1'], 'occupation':request.form['occupation'],
    'female_name':request.form['female_name'], 'adjective2':request.form['adjective2'],
    'noun2':request.form['noun2']
    }
    return render_template('story.html', title='Story', missing_words=missing_words)

if __name__ == '__main__':
    app.run(debug=True)