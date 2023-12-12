from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  # Check if the form was submitted
  if request.method == 'POST':
    # Get the selected source and destination from the form data
    source = request.form.get('source')
    destination = request.form.get('destination')

    # Store the values in a Python variable
    flight_data = {
      'source': source,
      'destination': destination,
    }

    # Print the selected source and destination for debugging purposes
    print(f"Selected source: {flight_data['source']}")
    print(f"Selected destination: {flight_data['destination']}")

    # Further processing with flight_data (e.g., search for flights)
    # ... (your flight search logic here)

    # Return the template with a message if desired
    return render_template('UI.html', message="Flight data received!")
  else:
    # Render the form if it wasn't submitted
    return render_template('UI.html')

if __name__ == "__main__":
  app.run(debug=True)
