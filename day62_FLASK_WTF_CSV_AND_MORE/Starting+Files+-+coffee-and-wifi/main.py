from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, IntegerField
from wtforms.validators import DataRequired, NumberRange, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = URLField('URL', validators=[DataRequired(), URL(message="Please provide a URL")])
    open_time = TimeField('Open Time', validators=[DataRequired()])
    close_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = IntegerField('Coffee Rating ☕',
                                 validators=[DataRequired(),
                                             NumberRange(min=1, max=5, message="Choose from range of 1 to 5")])
    wifi_rating = IntegerField('WiFi Rating 💪',
                               validators=[DataRequired(),
                                           NumberRange(min=1, max=5, message="Choose from range of 1 to 5")])
    power_outlet_rating = IntegerField('Power Outlet Rating 🔌',
                                       validators=[DataRequired(),
                                                   NumberRange(min=1, max=5, message="Choose from range of 1 to 5")])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("Saving the Data")
        new_row = [form.cafe.data, form.url.data, form.open_time.data, form.close_time.data, "☕"*int(form.coffee_rating.data),
                   "💪"*int(form.wifi_rating.data), "🔌"*int(form.power_outlet_rating.data)]

        with open('cafe-data.csv', newline='', mode="a", encoding='UTF8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_row)

        return redirect(url_for('add_cafe'))



    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='UTF8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows[1:])


if __name__ == '__main__':
    app.run(debug=True)
