from flask import Flask, session, redirect, url_for, escape, request
import flask

import os
import sys
import tempfile

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

def run_pipeline(res_dir):
    # run the pipeline here
    # if the process is successful or failed, run update_status() or echo something > RES_DIR/STATUS
    return True

def update_status(res_dir, status):
    ## @status should be string, such as "running", "success", "failed", etc.
    status_file = os.path.join(res_dir, "STATUS")
    with open(status_file, "w") as f:
        f.write(status)
    return True

@app.route('/service/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return flask.jsonify({"ok": False, "res_id": "", "message": "No file part"})
        input_file = request.files['file']

        # if user does not select file, browser also submit an empty part without filename
        if input_file.filename == '':
            return flask.jsonify({"ok": False, "res_id": "", "message": "No selected file"})

        ## RES_DIR will be returned and used later
        RES_DIR = tempfile.mkdtemp()
        input_file_path = os.path.join(RES_DIR, "INPUT.fastq")

        input_file.save(input_file_path)
        update_status(RES_DIR, "init")

        run_pipeline(RES_DIR)
        update_status(RES_DIR, "running")

        return flask.jsonify({"ok": True, "res_id": RES_DIR, "message": ""})
    return '''
    <!doctype html>
    <title>Upload new File (testing)</title>
    <h1>Upload new File (testing)</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run()
