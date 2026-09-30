# vuln.py - Fixed to use safe argument list without shell execution
import subprocess

# Synthetic test token for Secret Detection testing (CWE-798)
DUMMY_GITHUB_TOKEN = "ghp_111111111111111111111111111111111111"

def run_cmd(user_command):
    subprocess.run(["echo", user_command], shell=False, check=True)
