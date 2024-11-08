from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from db import get_num_clicks

app = Flask(__name__)
app.secret_key = b'_5#y2L"wlej8923nF4Q8z\n\xec]/'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']

    num_buttons = 12

    buttons = {}
    for i in range(1, num_buttons + 1):
        buttons[f'button_{i}'] = get_num_clicks(f'button_{i}')

    context = {
        'name': session.get('name', ''),
        'buttons': buttons,
    }
    return render_template('index.html', **context)


@app.route("/reset")
def reset():
    session['name'] = ''
    return redirect(url_for('index'))


@app.route("/click/<btn_id>", methods=['POST'])
def click(btn_id):
    num_clicks = get_num_clicks(btn_id, update=True)
    return {'num_clicks': num_clicks}


if __name__ == '__main__':
    app.run(debug=True, port=8080)
