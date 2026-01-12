import paramiko

class SSHClient:
    def __init__(self, host, username, password, timeout=5):
        self.host = host
        self.username = username
        self.password = password
        self.timeout = timeout

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(
            hostname=self.host,
            username=self.username,
            password=self.password,
            timeout=self.timeout
        )
    
    def try_login(self):
        try:
            self.connect()
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception:
            return None

    def run_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        self.client.close()