from flask import Flask, render_template, request, redirect, url_for
import pymysql
from config import get_db_connection

app = Flask(__name__)

# Home page: View all tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    priority_filter = request.args.get('priority')  # Get selected priority from query params

    conn = get_db_connection()
    with conn.cursor() as cursor:
        if priority_filter:
            # If a priority is selected, filter tasks by priority
            cursor.execute('SELECT * FROM tasks WHERE priority = %s ORDER BY priority DESC', (priority_filter,))
        else:
            # If no priority is selected, show all tasks
            cursor.execute('SELECT * FROM tasks ORDER BY priority DESC')
        tasks = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', tasks=tasks, selected_priority=priority_filter)

# Add a new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO tasks (title, description, priority) VALUES (%s, %s, %s)', 
                           (title, description, priority))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_task.html')

# Edit an existing task
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM tasks WHERE id = %s', (id,))
        task = cursor.fetchone()
    conn.close()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute('UPDATE tasks SET title = %s, description = %s, priority = %s WHERE id = %s', 
                           (title, description, priority, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

# Delete a task
@app.route('/delete/<int:id>')
def delete_task(id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM tasks WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=8000)
