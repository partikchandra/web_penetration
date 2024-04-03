from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory(".", "form.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        url = request.form.get('url')  # Using .get() method to avoid KeyError if 'url' is not found
        if url:
            print("Submitted URL:", url)
            return "URL submitted successfully!"
        else:
            return "URL not found in form data!"
    else:
        return "Method not allowed!"

if __name__ == '__main__':
    app.run(debug=True)
