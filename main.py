from datetime import datetime, timezone

def convert_iso_to_millis(iso_timestamp):
    # Convert ISO timestamp to milliseconds
    dt = datetime.fromisoformat(iso_timestamp.replace('Z', '+00:00'))
    return int(dt.timestamp() * 1000)

def merge_data(data1, data2):
    # Merge the two datasets into unified format
    merged = {}

    for item in data1:
        ts = convert_iso_to_millis(item['timestamp'])
        merged[ts] = {'timestamp': ts, 'value': item['value']}

    for item in data2:
        ts = item['timestamp']
        if ts in merged:
            merged[ts]['value'] += item['value']
        else:
            merged[ts] = {'timestamp': ts, 'value': item['value']}

    # Return sorted list by timestamp
    return [merged[ts] for ts in sorted(merged)]
