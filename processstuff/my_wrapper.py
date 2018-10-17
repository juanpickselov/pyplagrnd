import subprocess


try:
    result = subprocess.run(['python', 'bonjour_with_arg.py', 'lou ferrigno', 'comedy', 'lightsabe=False'],
                            shell=False,
                            check=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='ascii')
    print('Return code of: ' + str(result.returncode))
    the_output = str(result.stdout)
    print(the_output)
    err_output = str(result.stderr)
    print(err_output)
except ChildProcessError:
    print("The child process had a problem!")
except IndexError:
    print("You most likely didn't supply an argument for the script you wanted to run.")
except ValueError:
    print("Value error")
except:
    print('Something bad happened')
