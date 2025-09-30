import pandas as pd

def mex_hat_counter(csv_path, y_threshold):
    # Import CSV file
    data = pd.read_csv(csv_path)
    print("CSV Data Loaded:")
    print(data.head())

    # Assuming the CSV contains columns 'Distance_(pixels)' and 'Gray_Value' for graph data
    if 'Distance_(pixels)' not in data.columns or 'Gray_Value' not in data.columns:
        raise ValueError("CSV file must contain 'Distance_(pixels)' and 'Gray_Value' columns representing the graph data.")

    # Extract instances where the graph intersects the horizontal line at y_threshold
    intersections = []
    for i in range(len(data) - 1):
        y1, y2 = data['Gray_Value'][i], data['Gray_Value'][i + 1]
        if (y1 <= y_threshold <= y2) or (y2 <= y_threshold <= y1):
            intersections.append((data['Distance_(pixels)'][i], data['Distance_(pixels)'][i + 1]))

    # Process to count instances
    intersection_count = len(intersections)
    result = intersection_count // 2  # Divide by 2 as per the pseudocode

    # Display result
    print(f"Number of instances: {result}")
    return result

# Example usage
if __name__ == "__main__":
    csv_path = r"C:\Users\ethan\OneDrive\Desktop\barnacle lab\csv data\trial 2 - mex hat.csv"  # Replace with your CSV file path
    y_threshold = 180  # Replace with your desired threshold value

    mex_hat_counter(csv_path, y_threshold)