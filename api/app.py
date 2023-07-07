from flask import Flask


app = Flask(__name__)

@app.route('/predicao')
def root():
    return {'online': 'funcionando'}


if __name__ == '__main__':
    app.run(debug=True)
