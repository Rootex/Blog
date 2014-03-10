from flask import Flask, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)


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


@app.route('/login/form')
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
            return login_failed()
    else:
        return login_failed()

@app.route('/login/failed')
def login_failed():
    return 'Sorry you entered the wrong credentials or something went wrong'


@app.route('/logged-in')
def logged_in():
    return 'You have logged in successfully!'


@app.route('/form')
def form_page():
    return 'You need to register'


@app.route('/profile')
def profile():
    return render_template('profile.html')

with app.test_request_context():
    print url_for('index')

if __name__ == "__main__":
    app.debug = True
    app.run()
