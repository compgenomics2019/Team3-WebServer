from flask import Flask, session, redirect, url_for, escape, request
import flask

import os
import sys
import tempfile
import subprocess
import base64

SCRIPT_DIR = os.path.dirname(__file__)
FRONT_END = os.path.join(SCRIPT_DIR, "../frontend/")
app = Flask(
        __name__,
        static_url_path = "",
        static_folder = FRONT_END
    )

# Check Flask documentation
# http://flask.pocoo.org/docs/1.0/quickstart
# For how to write API endpoints and return JSON


@app.route('/')
def serve_root():
    return app.send_static_file('index.html')

@app.route('/flask')
def test_flask():
    return "hello flask!"

def run_pipeline(params):
    # run the pipeline here
    # if the process is successful or failed, run update_status() or echo something > RES_DIR/STATUS
    ### Parameters for the pipeline
    RES_DIR = params['RES_DIR']
    RES_ID = params['RES_ID']
    INPUT_forward = params['INPUT_forward']
    INPUT_reverse = params['INPUT_reverse']
    INPUT_unpaired = params['INPUT_unpaired']
    INPUT_kmer = params['kmer']
    INPUT_email = params['email']

    ### Using Popen, the process will run even python stops.
    subprocess.Popen([os.path.join(SCRIPT_DIR, "scripts/assembly.sh"), "-a", INPUT_forward, "-b", INPUT_reverse, "-c", INPUT_unpaired, "-o", RES_DIR, "-k", INPUT_kmer])

    ### OUTPUT files should be saved inside RES_DIR
    update_status(RES_DIR, "pipeline launched")

    return True

def update_status(res_dir, status):
    ## @status should be string, such as "running", "success", "failed", etc.
    status_file = os.path.join(res_dir, "STATUS")
    with open(status_file, "w") as f:
        f.write(status)
    return True

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        ## Check files exist
        for file in ['forward', 'reverse', 'unpaired']:
            if file not in request.files:
                return flask.jsonify({"ok": False, "res_id": "", "message": "Missing file part",
                                      "formdata": request.form})
            the_file = request.files[file]
            if the_file.filename == "":
                return flask.jsonify({"ok": False, "res_id": "", "message": "No selected file",
                                      "formdata": request.form})
        ## TODO: check kmer parameter

        input_file_forward = request.files['forward']
        input_file_reverse = request.files['reverse']
        input_file_unpaired = request.files['unpaired']
        input_kmer = request.form['kmer']
        if input_kmer == "":
            input_kmer = "71,73,75,79"

        ## RES_DIR will be returned and used later
        RES_DIR = tempfile.mkdtemp()
        RES_ID = base64.b64encode(RES_DIR.encode()).decode()

        pipeline_params = {}
        pipeline_params['RES_DIR'] = RES_DIR
        pipeline_params['RES_ID'] = RES_ID
        pipeline_params['INPUT_forward'] = os.path.join(RES_DIR, "INPUT_forward.fastq")
        pipeline_params['INPUT_reverse'] = os.path.join(RES_DIR, "INPUT_reverse.fastq")
        pipeline_params['INPUT_unpaired'] = os.path.join(RES_DIR, "INPUT_unpaired.fastq")
        pipeline_params['kmer'] = input_kmer

        ## TODO
        pipeline_params['email'] = "jialin@gatech.edu"

        input_file_forward.save(pipeline_params['INPUT_forward'])
        input_file_reverse.save(pipeline_params['INPUT_reverse'])
        input_file_unpaired.save(pipeline_params['INPUT_unpaired'])

        update_status(RES_DIR, "init")
        run_pipeline(pipeline_params)
        update_status(RES_DIR, "running")

        return flask.jsonify({"ok": True, "res_id": RES_ID,
                              "message": "", "formdata": request.form,
                              "pipeline_params": pipeline_params,
                              "result_link": "/result/" + RES_ID})
    return flask.render_template("upload.html", title = "Start the pipeline")

def ResId2Dir(RES_ID):
    if RES_ID == "test1":
        return os.path.join(app.root_path, 'sample_res')
    else:
        return base64.b64decode(RES_ID).decode()

@app.route('/result/<RES_ID>')
def show_result(RES_ID):
    "OUTPUT.gff3"
    RES_DIR = ResId2Dir(RES_ID)
    return flask.render_template("result.html", title = "Pipeline Result", RES_DIR = RES_DIR,
                                 RES_ID = RES_ID)

@app.route('/result/<RES_ID>/<filename>')
def get_res_content(RES_ID, filename):
    RES_DIR = ResId2Dir(RES_ID)
    return flask.send_from_directory(RES_DIR, filename)

if __name__ == "__main__":
    app.run()
