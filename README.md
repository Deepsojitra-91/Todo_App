# To-Do List App 📝

This is a simple **To-Do List** web application built using **Flask** for beginners. The app allows you to manage tasks with functionalities such as adding, editing, deleting, and filtering tasks by priority.  

---

## Features 🌟

- **View all tasks**: Displays a list of all your tasks in priority order.
- **Add tasks**: Create a new task with a title, description, and priority (High, Medium, Low).
- **Edit tasks**: Modify the title, description, or priority of an existing task.
- **Delete tasks**: Remove tasks you no longer need.
- **Filter by priority**: View tasks based on their priority level.

---

## Tech Stack 💻

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML, Tailwind CSS

---

## How to Run 🚀

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Install Dependencies**:
    Make sure you have Python and pip installed.
    ```bash
    pip install flask pymysql
    ```

3. **Set Up the Database**:
    - Create a MySQL database named `todo_app`.
    - Use the following table schema:
      ```sql
      CREATE TABLE tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each task
        title VARCHAR(255) NOT NULL,             -- Title of the task
        description TEXT,                        -- Description of the task
        priority INT NOT NULL,                   -- Priority of the task
    );
      ```
    - Update your MySQL credentials in the `config.py` file.

4. **Run the App**:
    ```bash
    python app.py
    ```
    Access the app at: [http://localhost:8000](http://localhost:8000)
