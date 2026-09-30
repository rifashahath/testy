import os
import flask

app = flask.Flask(__name__)

@app.route("/run")
def run_command():
    # Untrusted request input flowing to shell sink -> CWE-78
    cmd = flask.request.args.get("cmd")
    os.system(cmd)

def run_cmd(user_command):
    os.system(user_command)
