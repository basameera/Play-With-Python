import subprocess

if __name__ == "__main__":

    

    cmd = 'python 1_test.py -a 100'
    cmd_list = cmd.replace('"', '').split(' ')
    result = subprocess.run(cmd_list, stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')
    print(float(result))