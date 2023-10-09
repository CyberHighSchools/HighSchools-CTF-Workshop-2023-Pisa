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
    filename = sanitize_filename(filename)
    if filename is not None:
        return send_file('images/' + filename)
    else:
        return "Filename not provided."

def sanitize_filename(filename):
    sanitized = filename
    found = sanitized.find("../")
    while found != -1:
        sanitized = sanitized[:found] + sanitized[found + 3:]
        found = sanitized.find("../")

    found = sanitized.find("..\\")
    while found != -1:
        sanitized = sanitized[:found] + sanitized[found + 3:]
        found = sanitized.find("..\\")
    sanitized = sanitized.lstrip()
    sanitized = sanitized.rstrip()
    if sanitized and (sanitized[0] == '/' or sanitized[0] == '\\'):
        sanitized = sanitized[1:]
    return sanitized

if __name__ == '__main__':
    app.run(debug=False)
