from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Lairon Souza'
    age = 32

    user_data = {
        'name': name,
        'age': age
    }

    return jsonify(user_data)




if __name__ == "__main__":
    app.run()

