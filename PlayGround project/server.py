from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def blocks():
    return render_template('index1.html') 


@app.route('/play/<number_of_boxes>')
def numBoxes(number_of_boxes):
    repeat = int(number_of_boxes)
    return render_template('index2.html', repeat = repeat)



@app.route('/play/<number_of_boxes>/<color>')
def colors(number_of_boxes, color):
    repeat = (int(number_of_boxes))
    changeColor = color
    return render_template('index3.html', repeat = repeat, changeColor = color)



    
# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 
