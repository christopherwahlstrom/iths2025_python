import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="172.17.0.2", username="msfadmin", password="msfadmin")

stdin, stdout, stderr = ssh.exec_command("id")

print(stdout.read().decode())

ssh.close()