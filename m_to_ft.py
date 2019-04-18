from flask import Flask

app = Flask(__name__)

@app.route('/')
def base_page():
    return 'Meters to Feet Convert'

@app.route('/meters/<int:meters>')
def km_to_fathoms(meters):
    feet = meters * 3.28084
    return f"{meters} meters equals {feet} feet."


if __name__ =="__main__":
    app.run()
