def detect_bruteforce(df):
    failed = df[df['Status'] == 401]
    grouped = failed.groupby('IP').size()
    suspicious = grouped[grouped > 3]
    return suspicious.index.tolist()


def detect_scanning(df):
    grouped = df.groupby('IP')['Request'].nunique()
    scanners = grouped[grouped > 3]
    return scanners.index.tolist()