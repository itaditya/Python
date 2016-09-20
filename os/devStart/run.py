import subprocess

cmds = [
    "git pull",
    "subl .",
    "gulp"
]
if False:
    print "Manual Git selected"
else:
    for cmd in cmds:
        query = cmd.split()
        process = subprocess.Popen(query, stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output

print "Let's Get Cracking !"
