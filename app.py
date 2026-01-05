from flask import Flask, render_template

# Initialize Flask app
# template_folder='.' allows serving the HTML file from the current directory
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('integration_vhdl.html', title="VHDL Integration Tool")

if __name__ == '__main__':
    app.run(debug=True)