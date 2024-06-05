import subprocess

def get_ip():
    result = subprocess.run(['curl', 'ipinfo.io/ip'], stdout=subprocess.PIPE)
    ip = result.stdout.decode('utf-8').strip()
    return ip

if __name__ == "__main__":
    ip_address = get_ip()
    print(f"My IP address is: {ip_address}")
