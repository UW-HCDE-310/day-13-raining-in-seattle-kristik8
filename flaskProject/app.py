from flask import Flask
import urllib.request

# Initialize Flask app
app = Flask(__name__)


# Define route to check rain status
@app.route('/')
def check_rain():
    url = 'https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/'

    # Call the "Is it raining" API
    with urllib.request.urlopen(url) as response:
        rain_status = response.read().decode().strip().lower()  # "true" or "false"

    # Return appropriate HTML based on rain status
    if rain_status == "true":
        return "<h1>Yes, it's raining in Seattle!</h1>"
    else:
        return "<h1>No, it's not raining in Seattle.</h1>"


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
