import os
import random
import string
import subprocess
import time

commit_message = ["add", "edit", "fix", "hotfix", "hack", "merge"]

commit_num = 10


def MakeCommit():
    files = os.listdir()
    files.remove(os.path.basename(__file__))

    edit = random.choice(files)

    rand = random.choice(string.ascii_letters + string.digits)

    with open(edit, 'w') as f:
        f.write(rand)

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", random.choice(commit_message)+" : " + rand])


def Push():
    subprocess.run(["git", "push"])
    print("Push")


if __name__ == "__main__":
    for i in range(commit_num):
        MakeCommit()
        time.sleep(1)
        if (i % 10):
            Push()
