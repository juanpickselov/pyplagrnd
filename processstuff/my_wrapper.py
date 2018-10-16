import subprocess


try:
    result = subprocess.run(['python', 'bonjour_with_arg.py', 'howie mandel', 'comedy', 'lightsabe=False'],
                            shell=True,
                            check=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='ascii')
    print('Return code: ' + str(result.returncode))
    the_output = str(result.stdout)
    print(the_output)
    err_output = str(result.stderr)
    print(err_output)
except IndexError:
    print("You most likely didn't supply an argument for the script you wanted to run.")
except:
    print('Something bad happened')
