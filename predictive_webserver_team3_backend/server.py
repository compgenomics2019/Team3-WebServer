from flask import Flask
app = Flask(__name__)

# Check Flask documentation
# http://flask.pocoo.org/docs/1.0/quickstart
# For how to write API endpoints and return JSON

@app.route('/')
def run():
    return 'Running!'


@app.route('/about')
def hello():
    return 'About'

@app.route('/login')
def login():
    return 'login'

# Example
# http://127.0.0.1:5000/user/sreeni
# Will display "User sreeni"
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# http://127.0.0.1:5000/post/1
# Will display "Post 1"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

