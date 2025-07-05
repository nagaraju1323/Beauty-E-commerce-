from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/response')
def response(): 
    return render_template('response.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

