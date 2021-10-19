import subprocess

cmd = r"C:\Program Files\Nuke13.0v4\Nuke13.0.exe -x D:\Projects\nuke13-nuke11\nuke13_v002.nk 1-42"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)

while True:
  inchar = process.stdout.readline().decode(encoding="utf-8")
  if inchar:
    print(str(inchar), end='')
  else:
    print('')
    break



