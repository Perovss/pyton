import subprocess


def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True, reply.stdout
    else:
        return False, reply.stderr

print(ping_ip('www.ya.ru'))
print(ping_ip('a'))