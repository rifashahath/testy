import os

def run_cmd(user_command):
    # Vulnerable to command injection (CWE-78)
    os.system(user_command)
