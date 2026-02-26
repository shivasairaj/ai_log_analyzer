import random
from datetime import datetime, timedelta

normal_ips = [f"10.0.0.{i}" for i in range(1, 40)]
brute_ips = ["185.220.101.5", "45.33.32.156"]
scan_ips = ["103.21.244.12"]
anomaly_ips = ["172.16.99.200"]

urls = ["/home", "/products", "/about", "/contact"]
login_url = "/login"
admin_urls = ["/admin", "/wp-admin", "/config", "/.env"]

methods = ["GET", "POST"]
status_normal = [200]
status_fail = [401, 403]

start_time = datetime.now()

lines = []

def random_time():
    return (start_time + timedelta(seconds=random.randint(1, 3600))).strftime("%d/%b/%Y:%H:%M:%S")

# Normal traffic
for _ in range(150):
    ip = random.choice(normal_ips)
    url = random.choice(urls)
    method = random.choice(methods)
    status = random.choice(status_normal)

    lines.append(f'{ip} - - [{random_time()}] "{method} {url} HTTP/1.1" {status} 512')

# Brute force attacks (many failed logins)
for _ in range(60):
    ip = random.choice(brute_ips)
    status = random.choice(status_fail)

    lines.append(f'{ip} - - [{random_time()}] "POST {login_url} HTTP/1.1" {status} 256')

# Scanning attempts (multiple admin paths)
for _ in range(50):
    ip = scan_ips[0]
    url = random.choice(admin_urls)

    lines.append(f'{ip} - - [{random_time()}] "GET {url} HTTP/1.1" 404 128')

# High-frequency anomaly traffic
for _ in range(80):
    ip = anomaly_ips[0]
    url = random.choice(urls + admin_urls)
    method = random.choice(methods)
    status = random.choice(status_normal + status_fail)

    lines.append(f'{ip} - - [{random_time()}] "{method} {url} HTTP/1.1" {status} 1024')

random.shuffle(lines)

with open("realistic_attack_test.log", "w") as f:
    for line in lines:
        f.write(line + "\n")

print("Log file generated: realistic_attack_test.log")