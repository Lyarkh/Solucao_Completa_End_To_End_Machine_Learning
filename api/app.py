from flask import Flask


app = Flask(__name__)

@app.route('/predicao/<parametro>', methods=['GET'])
def root(parametro):
    return {'online': f'{parametro}'}


if __name__ == '__main__':
    app.run(debug=True)
