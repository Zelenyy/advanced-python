import subprocess

command = """Hello
exit
"""

if __name__ == '__main__':
    process = subprocess.Popen(["python", "example_subprocess.py"],
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               text=True
                               )
    try:
        out, err = process.communicate(input= command
                                       , timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        out, err = process.communicate()
    print(out)
    print(err)
