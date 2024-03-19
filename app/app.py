import os
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from calculator import calculate_bmr

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
class BMRForm(FlaskForm):
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')], validators=[InputRequired()])
    height_ft = IntegerField('Height (feet)', validators=[InputRequired(), NumberRange(min=1)])
    height_in = IntegerField('Height (inches)', validators=[InputRequired(), NumberRange(min=0, max=11)])
    weight = IntegerField('Weight (lbs)', validators=[InputRequired(), NumberRange(min=1)])
    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=1)])
    activity_level = SelectField('Activity Level', choices=[('sedentary', 'Sedentary'), ('lightly_active', 'Lightly Active'), ('moderately_active', 'Moderately Active'), ('very_active', 'Very Active'), ('extra_active', 'Extra Active')], validators=[InputRequired()])
    submit = SubmitField('Calculate')

@app.route('/', methods=['GET', 'POST'])
def calculate():
    form = BMRForm()
    bmr = None
    if form.validate_on_submit():
        # Get the form data
        gender = form.gender.data
        height_ft = form.height_ft.data
        height_in = form.height_in.data
        weight = form.weight.data
        age = form.age.data
        activity_level = form.activity_level.data
        
        # Print the form data
        print(gender, height_ft, height_in, weight, age, activity_level)

        # Perform the calculation
        bmr = calculate_bmr(gender, height_ft, height_in, weight, age, activity_level)
    else:
        print(form.errors)    

    # Render the form and pass the BMR result (if any)
    return render_template('form.html', form=form, bmr=bmr)

if __name__ == '__main__':
    app.run(debug=True)