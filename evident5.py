import subprocess

def evident():
    permfile = '"abc.pem"' + ' '
    userandip = 'ec2-user@ec2-34-209-91-150.us-west-2.compute.amazonaws.com' + ' '
    output = subprocess.check_output('sudo ssh -i ' + permfile + userandip + '<<END nc -zv 169.254.169.254 80 END', shell=True, timeout=1) 
    if 'succeeded' in output:
        subprocess.Popen('sudo ssh -i ' + permfile + userandip + '<<HELL sudo iptables -A INPUT -i eth0 -p tcp --source-port 80 -s 169.254.169.254 -j DROP', shell=True)
    else:
        return "No metadata security issues"


evident()


