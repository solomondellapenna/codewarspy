import subprocess

def evident():
    permfile = '"abc.pem"' + ' '
    userandip = 'ec2-user@ec2-34-209-91-150.us-west-2.compute.amazonaws.com' + ' '
    output = subprocess.check_output('sudo ssh -i ' + permfile + userandip + '<<END nc -zv 169.254.169.254 80 END', shell=True)
    if 'succeeded' in output:
        return 'Metadata exploitable!'
print evident()