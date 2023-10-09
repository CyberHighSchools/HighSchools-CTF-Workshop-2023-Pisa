from flask import Flask, render_template, request, send_file

app = Flask(__name__)

images = [
    {"filename": "painting1.png", "link": "image1"},
    {"filename": "painting2.jpg", "link": "image2"},
    {"filename": "painting3.jpg", "link": "image3"},
]

@app.route('/')
def index():
    return render_template('index.html', images=images)

@app.route('/serve_file')
def serve_file():
    filename = request.args.get('filename')
    if filename is not None:
        return send_file('images/' + filename)
    else:
        return "Filename not provided."

if __name__ == '__main__':
    app.run(debug=False)
