def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]  
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  
        triangle.append(row)
    return triangle

rows = 5
triangle = generate_pascals_triangle(rows)
for row in triangle:
    print(row)
