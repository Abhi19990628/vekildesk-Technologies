from typing import List, Dict, Callable


def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    grouped_data = {}
    for entry in data:
        group_key = entry[key]  # Directly accesses the key
        if group_key not in grouped_data:
            grouped_data[group_key] = []
        grouped_data[group_key].append(entry)

    return {k: aggregator(v) for k, v in grouped_data.items()}

# Sample data
data = [
    {'category': 'A', 'value': 30},
    {'category': 'A', 'value': 40},
    {'category': 'B', 'value': 30},
    {'category': 'B', 'value': 20},
    {'category': 'C', 'value': 40},
    {'category': 'C', 'value': 20},
    {'category': 'C', 'value': 30},
    {'category': 'B', 'value': 10},
    {'category': 'A', 'value': 10},
]

# Define an aggregator function to sum the values
def sum_values(entries):
    return sum(entry['value'] for entry in entries)

# Call the aggregate_data function (Second Version)
result = aggregate_data(data, 'category', sum_values)

# Print the result
print(result)



