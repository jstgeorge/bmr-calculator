import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, Form
from wtforms.validators import InputRequired, NumberRange, DataRequired
from wtforms.fields.html5 import DateField
from calculator import calculate_bmr
from settings import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class BMRForm(FlaskForm):
    goal_weight = IntegerField('Goal Weight', validators=[InputRequired(), NumberRange(min=1)])
    caloric_intake = IntegerField('Caloric Intake', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    height_ft = IntegerField('Height (feet)', validators=[InputRequired(), NumberRange(min=1)])
    height_in = IntegerField('Height (inches)', validators=[InputRequired(), NumberRange(min=0, max=11)])
    weight = IntegerField('Weight (lbs)', validators=[InputRequired(), NumberRange(min=1)])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=1)])
    activity_level = SelectField('Activity Level', choices=[('sedentary', 'Sedentary'), ('lightly_active', 'Lightly Active'), ('moderately_active', 'Moderately Active'), ('very_active', 'Very Active'), ('extra_active', 'Extra Active')], validators=[InputRequired()])
    submit = SubmitField('Calculate')

from datetime import datetime
from datetime import timedelta
@app.route('/', methods=['GET', 'POST'])
def calculate():
    form = BMRForm()
    bmr_list = []
    if form.validate_on_submit():
        # Get the form data
        goal_weight = form.goal_weight.data
        caloric_intake = form.caloric_intake.data
        gender = form.gender.data
        height_ft = form.height_ft.data
        height_in = form.height_in.data
        weight = form.weight.data
        age = form.age.data
        activity_level = form.activity_level.data
        
        # Calculate BMR and net calories
        bmr = calculate_bmr(gender, height_ft, height_in, weight, age, activity_level)
        net_calories = bmr - caloric_intake

        # Calculate weight loss based on net calories
        # There are approximately 3500 calories in a pound of body weight
        weight_loss = net_calories / 3500
        
        day = 0
        last_weight = None
        while round(weight) > goal_weight and day <= 3652:  # limit to 10 years
            weight -= weight_loss  # decrease weight based on weight loss
            day += 1  # increment the day
            date_for_1lb_loss = datetime.today().date() + timedelta(days=day)  # calculate the date for 1lb loss
            bmr = int(calculate_bmr(gender, height_ft, height_in, round(weight), age, activity_level))
            if last_weight is None or round(weight) != last_weight:
                bmr_list.append((date_for_1lb_loss, round(weight), bmr))  # store the date instead of the day number
                last_weight = round(weight)
        # Print the form data
        print(goal_weight, caloric_intake, gender, height_ft, height_in, weight, age, activity_level)
        print(bmr_list)
    else:
        print(form.errors)    

    # Render the form and pass the BMR result (if any)

    return render_template('form.html', form=form, bmr_list=bmr_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5548)