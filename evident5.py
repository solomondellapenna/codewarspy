import subprocess

permfile = '"abc.pem"' + ' '
userandip = 'ec2-user@ec2-34-209-91-150.us-west-2.compute.amazonaws.com' + ' '
#p = Popen('sudo ssh -i ' + permfile + userandip + '<<END nc -zv 169.254.169.254 80 END', stdout=PIPE, stderr=PIPE, stdin=PIPE)
output = p.stdout.read()
p.stdin.write(input)
subprocess.check_output(
"ls non_existent_file; exit 0",
stderr=subprocess.STDOUT,
shell=True)