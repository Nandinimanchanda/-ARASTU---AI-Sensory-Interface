from flask import Flask, render_template

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/virtualcompanion')
def run_python_program():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\ai_companion.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 


@app.route('/ai_mouse')
def ai_mouse():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\HandGestures.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 

@app.route('/ascii_art')
def ascii_art():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\ascii.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 
   

@app.route('/snake')
def HandGestures():
    import subprocess
    result = subprocess.run(['python', 'D:\\python 3.8\\projects\\snakeGame.py'], capture_output=True, text=True)

    # Return the output of the Python script execution

    return result.stdout 


if __name__ == '__main__':
    app.run(debug=True)
