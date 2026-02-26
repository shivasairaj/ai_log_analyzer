from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    features = df.groupby('IP').agg({
        'Request': 'count',
        'Status': lambda x: (x == 401).sum()
    })

    model = IsolationForest(contamination=0.2, random_state=42)
    model.fit(features)

    features['anomaly'] = model.predict(features)

    anomalies = features[features['anomaly'] == -1]
    return anomalies.index.tolist()