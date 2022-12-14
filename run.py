import os
import random
import string
import subprocess
import time

commit_message = ["add", "edit", "fix", "hotfix", "hack", "merge"]
random_cpp = [
"#include <windows.h>",
"#include <iostream>",
"#include <string>",
"#include <vector>",
"#include <stdio>",
"font_size.dwFontSize.Y = 13;",
"int main(){",
"return 0;",
'std::cout << "Hello, World" << std::endl;',
'void run(){'
'}',
'int i = 1;',
'bool flag == true;'
'int i = nullptr;'
'int array_[3] = { 0, 0, 0 };',
'ptr_array = array_;'
'std::cout << "ptr_array " << ptr_array << std::endl;',
'template <typename T1, typename T2>',
'class Clock',
'this->hour = hour % 24;',
'printf("%02d:%02d\n", hour, minute);',
'c.set(6, 30);',
'public:',
]

commit_num = 300


def MakeCommit():
    files = os.listdir()
    files.remove(os.path.basename(__file__))
    files.remove(".git")

    edit = random.choice(files)

    rand = random.choice(random_cpp) + "\n" + random.choice(random_cpp) + "\n" + random.choice(random_cpp) + "\n"
    print(edit)

    with open(edit, 'a') as f:
        f.write(rand)

    subprocess.run(["git", "add", "."])
    subprocess.run(
        ["git", "commit", "-m", random.choice(commit_message)+" : " + rand])


if __name__ == "__main__":
    for i in range(commit_num):
        MakeCommit()
        time.sleep(3)
