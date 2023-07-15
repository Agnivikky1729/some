from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    x = ('vijay', 'vamshi')
    word = str(x)
    return render_template('test.html', word=word)

if __name__ == "__main__":
    app.run(port = '4000', debug = True)