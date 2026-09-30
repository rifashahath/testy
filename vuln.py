# vuln.py - Fixed to use safe argument list without shell execution
import subprocess

def run_cmd(user_command):
    subprocess.run(["echo", user_command], shell=False, check=True)
