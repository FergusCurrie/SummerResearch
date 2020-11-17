import subprocess


process = subprocess.run('gg.sh', shell=True, check=True, timeout=10)

print("what up cu")