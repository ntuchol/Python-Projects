def polygon_area(vertices, n=None, i=0, area=0):
    
    if n is None:
        n = len(vertices)
    
    if i == n:
        x_n, y_n = vertices[-1]
        x_1, y_1 = vertices[0]
        area += x_n * y_1 - y_n * x_1
        return abs(area) / 2
    
    x_i, y_i = vertices[i]
    x_next, y_next = vertices[(i + 1) % n]
    area += x_i * y_next - y_i * x_next
    return polygon_area(vertices, n, i + 1, area)


polygon_vertices = [(2, 3), (5, 11), (12, 8), (9, 5), (5, 6)]
area = polygon_area(polygon_vertices)
print(f"The area of the polygon is: {area}")
