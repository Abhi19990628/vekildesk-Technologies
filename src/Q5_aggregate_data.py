from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    for entry in data:
        group_key = entry[key]
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(entry)

    return {k: aggregator(v) for k, v in grouped_data.items()}
