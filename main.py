from flask import render_template, Flask, redirect, request
from create_form import CreateAddForm
from home_form import CreateHomeForm
from choosen_form import CreateChoosenForm
import glob
from config import Config
import execute_signal

import del_DB

app = Flask(__name__)
app.config.from_object(Config)

execute_query = execute_signal
deleteDB = del_DB

@app.route('/', methods = ['POST', 'GET'])
def index():
    form = CreateHomeForm()
    if form.validate_on_submit():
        name = form.basename.data
        deleteDB.Del(name)
        return redirect('/')
    db = {}
    for file in glob.glob("*.db"):
        db[file] = file
    return render_template('home.html', data = db, form = form)

@app.route('/enter_new', methods = ['POST', 'GET'])
def new_DB():
    form = CreateAddForm()
    if form.validate_on_submit():
        name = form.basename.data
        query = form.execute.data
        execute_query.Execute(name,query)
        return redirect('/')
    return render_template('new_DB.html', form = form)

@app.route('/choosen_db/<id>',methods = ['POST', 'GET'])
def choose(id):
    form = CreateChoosenForm()
    table = execute_query.ShowInfo(id)
    if form.validate_on_submit():
        query = form.execute.data
        data1 = execute_query.Execute(id, query)
        table = execute_query.ShowInfo(id)
        return render_template('database.html', form=form, data=id, table_name=table[0], info = table[1], database = data1)
    return render_template('database.html', form = form, data = id, table_name = table[0], info = table[1])

if __name__ == "__main__":
    app.run(debug=True)