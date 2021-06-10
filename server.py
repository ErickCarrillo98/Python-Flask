from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/Dojo')
def dojo():
    return "Dojo"


@app.route('/hi/<name>')
def say(name):
    return f'hi {name}'


@app.route('/repeat/<num>/<string>')
def repeat(num,string):
    string_repeat = str(string) * int(num)
    return string_repeat


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
        # Run the app in debug mode.



