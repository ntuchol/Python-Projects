def print_table(data):
    if not data:
        print("No data to display.")
        return

    headers = data[0].keys()
    col_widths = {header: max(len(header), max(len(str(row[header])) for row in data)) for header in headers}

    header_row = " | ".join(f"{header:{col_widths[header]}}" for header in headers)
    print(header_row)
    print("-" * len(header_row))

    for row in data:
        data_row = " | ".join(f"{str(row[header]):{col_widths[header]}}" for header in headers)
        print(data_row)

data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 24, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 29, "City": "Chicago"}
]

print_table(data)
