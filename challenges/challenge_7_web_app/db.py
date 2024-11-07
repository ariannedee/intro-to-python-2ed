import sqlite3


def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Return dict instead of tuple
    return conn


def get_num_clicks(button_id, update=False):
    connection = get_connection()
    cursor = connection.cursor()
    button_clicks = cursor.execute("SELECT * FROM clicks WHERE button_id = ?", (button_id,)).fetchone()

    if button_clicks is None:
        cursor.execute("INSERT INTO clicks (button_id, num) VALUES (?, 0)", (button_id,))
        connection.commit()
        num_clicks = 0
    else:
        num_clicks = button_clicks['num']

    if update:
        num_clicks += 1
        cursor.execute("UPDATE clicks SET num = ? WHERE button_id = ?", (num_clicks, button_id))
        connection.commit()
    return num_clicks


def create_and_init_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS clicks;")
    cursor.execute("CREATE TABLE clicks(button_id STRING, num INTEGER)")
    connection.commit()


if __name__ == '__main__':
    create_and_init_table()
