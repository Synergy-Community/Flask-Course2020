from flask import render_template, make_response, request, Flask, redirect, url_for, session
from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, update, delete, select
import os
app = Flask(__name__)
app.secret_key = os.urandom(24) # for security

engine = create_engine('sqlite:///07Database/SQLAlchemy/database.db', echo = True)
meta = MetaData()

students = Table(
   'details', meta, 
   Column('name', String, primary_key = True), 
   Column('colour', String), 
   Column('opinion', String), 
)
meta.create_all(engine)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    connection = engine.connect()
    s = select([students])
    all_rows = connection.execute(s).fetchall()
    if request.method == 'POST':
        colour = str(request.form['colour'])
        name = str(request.form['name'])
        opinion = str(request.form['opinion'])
        try:
            result = connection.execute(students.insert(), {'name' : name, 'colour' : colour, 'opinion' : opinion})
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. \nArguments: {ex.args}"
            replacements = [',', '(', ')']
            for _ in replacements:
                message = message.replace(_, '')
            print(message)

            connection.rollback()
        finally:
            print('Something happened in def insert()')
            return redirect(url_for('insert'))

    return render_template('insert.html', all_rows = all_rows)

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    connection = engine.connect()
    s = select([students])
    all_rows = connection.execute(s).fetchall()
    st = select([students.c.name])
    name_rows = connection.execute(st).fetchall()
    if request.method == 'POST':
        try:
            colour = str(request.form['colour'])
            opinion = str(request.form['opinion'])
            name = str(request.form['name'])
            s = update(students).where(students.c.name== name).values(colour = colour, opinion = opinion)
            result = connection.execute(s)
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. \nArguments: {ex.args}"
            replacements = [',', '(', ')']
            for _ in replacements:
                message = message.replace(_, '')
            print(message)
            connection.rollback()
        finally:
            print('Something happened in def edit()')
            return redirect(url_for('edit'))

    return render_template('edit.html', name_rows = name_rows, all_rows = all_rows)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    connection = engine.connect()
    s = select([students])
    all_rows = connection.execute(s).fetchall()
    if request.method == 'POST':
        name = request.form['name']
        try:
            st = students.delete().where(students.c.name==name)
            result = connection.execute(st)
        except Exception as ex:
            message = f"An exception of type {type(ex).__name__} occurred. \nArguments: {ex.args}"
            replacements = [',', '(', ')']
            for _ in replacements:
                message = message.replace(_, '')
            print(message)
            connection.rollback()
        finally:
            print('Something happened in def delete()')
            return redirect(url_for('delete'))

    return render_template('delete.html', all_rows = all_rows)


@app.route('/results', methods=['GET', 'POST'])
def results():
    connection = engine.connect()
    s = select([students])
    all_rows = connection.execute(s).fetchall()
    return render_template('result.html', all_rows = all_rows)

if __name__ == '__main__':
    app.run(debug=True)


