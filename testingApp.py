from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    print('in side hello method ..........')
    return 'Hello, World! This is my first Flask app on Render.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)