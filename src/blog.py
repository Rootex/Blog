from flask import Flask, url_for, request, render_template, redirect, send_from_directory, session
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    DATABASE=os.path.join(app.root_path, 'blog.db'),
    DEBUG=True,
    SECRET_KEY='default',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('PLOG_SETTINGS', silent=True)


@app.route('/')
def home():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return 'Just a test!'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    #fetch post from database and return the post
    return 'Post %d' % post_id


@app.route('/posts')
def show_all_posts():
    return 'All blog posts'


@app.route('/log')
def login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = str(request.form['user'])
    password = str(request.form['passd'])
    if request.method == 'POST':
        if username == 'Plaix' and password == 'Hacker':
            return profile()
        else:
            msg = 'Credentials not correct'
            return error(msg)
    else:
        msg = 'Error: Not POST'
        return error(msg)


@app.route('/login/failed')
def error(msg="error not defined"):
    return msg


@app.route('/logged-in')
def logged_in():
    return 'You have logged in successfully!'


@app.route('/form')
def form_page():
    return 'You need to register'


@app.route('/profile')
def profile():
    name = "Sot"
    return render_template('profile.html', name = name)


def allowed_filename(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/edit', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_filename(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('edit.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


with app.test_request_context():
    print(url_for('index'))

if __name__ == "__main__":
    app.debug = True
    app.run()
