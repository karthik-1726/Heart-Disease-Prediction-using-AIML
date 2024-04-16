from flask import Flask, render_template, request, redirect, url_for, session, flash
from DiseaseaPrediction import DiseasesPrediction
from UserEntry import UserEntry
from FeedBack import FeedBack
from AddData import AddData

app = Flask(__name__, template_folder='templates', static_folder="templates/static")
app.secret_key="4ac4285dab04a0616a1e6e35d4a3de3c"
ue = UserEntry()
dp = DiseasesPrediction()
add_data = AddData()


@app.route('/')
def index():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if ue.login_user(email, password):
            flash('√ Logged in successfully!','success')
            return redirect(url_for('index'))
        else:
            flash('× email or password is wrong!','error')
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if ue.register_user(name, email, password):
            flash('√ Registerd successfully!','success')
            return redirect(url_for('login'))
        else:
            flash('× User already exists!! Try another email', 'error')
    return render_template('register.html')

@app.route('/Predict', methods=['GET','POST'])
def input():
    sex = int(request.form['nSex2'])
    resting_blood_pressure = int(request.form['nRestbp2'])
    thalium_stress_test_max_heart_rate = int(request.form['nThalach2'])
    major_vessels_colored = int(request.form['nCa2'])
    chest_pain_type = int(request.form['nCp2'])
    peak_exercise_st_segment = int(request.form['nSlope2'])
    thalium_test = int(request.form['nThal2'])
    input_data = [sex, resting_blood_pressure, thalium_stress_test_max_heart_rate,
                      major_vessels_colored, chest_pain_type, peak_exercise_st_segment, thalium_test]
    dp = DiseasesPrediction()
    my_prediction = dp.predict_diseases(input_data)
    add_data.add_new_data(input_data)
    return render_template('after.html', data=my_prediction)

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['feed-back']
    Feedback = FeedBack()
    if Feedback.submit_feedback(name, email, phone, message):
        flash('☺ submitted successfully!!! thank you','success')
        return redirect(url_for('index'))
    else:
        flash("☹ Could'nt submit your feed back, try again",'error')
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
