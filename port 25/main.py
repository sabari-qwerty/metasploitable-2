import click
import socket


def CheckUser(host, port, wordlist):
    res = []
    try:
        smtp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        smtp.settimeout(10)
        smtp.connect((host, port))

        initial_response = smtp.recv(1024)
        print(initial_response.decode('utf-8'))

        with open(wordlist, 'r') as file:
            for data in file.readlines():
                name = data.replace('\n', '\r\n')
                payload = f"VRFY {name}"
                smtp.send(payload.encode('utf-8'))
                _data = smtp.recv(1024)
                code = str(_data).split(' ')[0].split('\'')
                user = str(_data).split(' ')[-1]
                if '252' in code:
                    res.append(user.split('\\')[0])
        smtp.close()
    except TimeoutError:
        print("Exited Users")
        print(", ".join(res))
        pass


@click.command()
@click.option("--host", help="The host IP address example.py --port xxx.xxx.xxx.xxx ", type=str)
@click.option("--port", default=25, help="The port number [default: 21] [oprional]", type=int)
@click.option("--wordlist", help="path of wordlist example ./data/text.txt", type=str)
def main(host, port, wordlist):
    """
        Try Hader
    """
    if not host or not port or not wordlist:
        print("help: python filename.py --help")
        return None

    return CheckUser(host, port, wordlist)


if __name__ == "__main__":
    main()
