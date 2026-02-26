import re
import pandas as pd

log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'

def parse_log(file_path):
    logs = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                ip = match.group(1)
                timestamp = match.group(2)
                request = match.group(3)
                status = int(match.group(4))
                size = int(match.group(5))

                logs.append([ip, timestamp, request, status, size])

    df = pd.DataFrame(logs, columns=["IP", "Timestamp", "Request", "Status", "Size"])
    return df