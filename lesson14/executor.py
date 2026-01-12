from ssh_client import SSHClient

def shell(host, username, password):
    client = SSHClient(host, username, password)
    client.connect()

    while True:
        cmd = input("> ")
        if cmd.lower() in ["exit", "quit"]:
            break
    
        out, err = client.run_command(cmd)
        if out:
            print(out)
        if err:
            print(err)

    client.close()