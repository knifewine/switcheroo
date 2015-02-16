import subprocess
from os import devnull


def branch_for_path(path):
    # open devnull to eat stderr if something goes wrong trying to shell out to git
    with open(devnull) as dn:
        try:
            output = subprocess.check_output(["git", "status"], stderr=dn, cwd=path).split("\n")[0]
        except (subprocess.CalledProcessError, OSError):
            return 'git error! is git installed? is the directory a git repository?'

        return output
