from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<path:subpath>')
def say_route(subpath):
    if subpath == "flask":
        return 'Hi Flask!'
    if subpath == "michael":
        return 'Hi Michael!'
    if subpath == "john":
        return 'Hi John!'
    else:
        return 'Sorry! No response. Try again.'


@app.route('/repeat/<path:subpath>')
def repeat_route(subpath):
    if subpath == "hello":
        return 'hello <br>'*int(35)   
    if subpath == "bye":
        return 'bye <br>'*int(80)
    if subpath == "dogs":
        return 'dogs <br>'*int(99)
    else:
        return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)