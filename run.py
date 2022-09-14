import os
import random
import string
import subprocess
import time

commit_message = ["add", "edit", "fix", "hotfix", "hack", "merge"]

commit_num = 200


def MakeCommit():
    files = os.listdir()
    files.remove(os.path.basename(__file__))
    files.remove(".git")

    print(files)

    edit = random.choice(files)

    rand = random.choice(string.ascii_letters + string.digits)

    with open(edit, 'w') as f:
        f.write(rand)

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", random.choice(commit_message)+" : " + rand])


if __name__ == "__main__":
    for i in range(commit_num):
        MakeCommit()
        time.sleep(5)
