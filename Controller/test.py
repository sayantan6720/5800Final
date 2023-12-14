from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    source = None
    destination = None

    if request.method == 'POST':
        source = request.form.get('source')
        destination = request.form.get('destination')

    return render_template('UI.html', source=source, destination=destination)

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
  app.run(debug=True)
