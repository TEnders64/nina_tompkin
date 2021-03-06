from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

def createcheckerboard():
    pass

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html',rows=4,cols=4)

@app.route('/<num_rows>')
def checkerboard_row(num_rows):
    # if (num_rows % 2 == 1):
    return render_template('index.html',rows=int(num_rows),cols=4)

@app.route('/<num_rows>/<num_cols>')
def checkerboard_mult(num_rows,num_cols):
    return render_template('index.html',rows=int(num_rows),cols=int(num_cols))

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
