from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
app = Flask(__name__)
app.config['SECRET_KEY'] = "afafafafas2131"
Bootstrap5(app)

class NewTask(FlaskForm):
    task=StringField(label="New Task:",validators=[DataRequired()],render_kw={"placeholder": "Your Task"})
    submit=SubmitField(label='Add',)

@app.route("/", methods=['GET','POST'])
def main():
    form=NewTask()
    if form.validate_on_submit():
        return form.task.data
    return render_template('test.html',form=form)



@app.route("/todo")
def todo():
    return render_template('todo.html')




if __name__ == "__main__":
    app.run(debug=True)