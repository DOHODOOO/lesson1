from flask import Flask

app = Flask(__name__)
@app.route('/<a>')
def head_low(a):
    return f'<h1>Hello {a} world!</h1><p>Im eblan</p><p>My name is huesos</p>'

if __name__ == '__main__':
    app.run(debug=True)
