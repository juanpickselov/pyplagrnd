import subprocess
import sys


try:
    result = subprocess.run(['python', 'bonjour_with_arg.py'] + [sys.argv[1]],
                            shell=True,
                            check=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='ascii')
    print('Return code: ' + str(result.returncode))
    the_output = str(result.stdout)
except IndexError:
    print("You most likely didn't supply an argument for the script you wanted to run.")
except:
    print('Something bad happened')

print(the_output)
