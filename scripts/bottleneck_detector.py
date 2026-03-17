def detect_bottlenecks(data):
    """
    Analyzes the given data to detect bottlenecks.
    Args:
        data (list of dict): A list of dictionaries where each dictionary represents an operation with its duration.
    Returns:
        list: A list of detected bottlenecks with details.
    """
    bottlenecks = []
    duration_threshold = 10  # Example threshold in seconds for bottleneck detection

    for operation in data:
        if operation['duration'] > duration_threshold:
            bottlenecks.append(operation)

    return bottlenecks

# Example usage
if __name__ == '__main__':
    operations_data = [
        {'name': 'operation1', 'duration': 5},
        {'name': 'operation2', 'duration': 12},
        {'name': 'operation3', 'duration': 8},
    ]
    detected_bottlenecks = detect_bottlenecks(operations_data)
    print("Detected Bottlenecks:", detected_bottlenecks)
