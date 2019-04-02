from flask import Flask, session, redirect, url_for, escape, request

import os
import sys

FRONT_END = os.path.join(os.path.dirname(__file__), "../frontend/")
app = Flask(
        __name__,
        static_url_path = "",
        static_folder = FRONT_END
    )

# Check Flask documentation
# http://flask.pocoo.org/docs/1.0/quickstart
# For how to write API endpoints and return JSON

@app.route('/flask')
def test_flask():
    return "hello flask!"

#@app.route('/')
#def run():
#    return 'Running!'
#
#
#@app.route('/about')
#def hello():
#    return 'About'
#
## Example
## http://127.0.0.1:5000/projects
#@app.route('/projects/')
#def projects():
#    return 'The project page'
#
## http://127.0.0.1:5000/login
## Just for sample - can be changed later
#@app.route('/login')
#def login():
#    if request.method == 'GET':
#        return 'login'
#    elif request.method == 'POST':
#        if valid_login(request.form['username'],
#                       request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
#    return 'login'
#
#    def valid_login(username, password):
#        # Placeholder
#        return True
#
#    def log_the_user_in():
#        # Placeholder
#        return True
#
## Example
## http://127.0.0.1:5000/user/sreeni
## Will display "User sreeni"
#@app.route('/user/<username>')
#def show_user_profile(username):
#    # show the user profile for that user
#    return 'User %s' % username
#
## http://127.0.0.1:5000/post/1
## Will display "Post 1"
#
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#    # show the post with the given id, the id is an integer
#    return 'Post %d' % post_id
#
## For uploading a file
## POST to this endpoint with
## the file as POST parameter in the request
#@app.route('/upload', methods=['GET', 'POST'])
#def upload_file():
#    if request.method == 'POST':
#        f = request.files['the_file']
#        f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == "__main__":
    app.run()
