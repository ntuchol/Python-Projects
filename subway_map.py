import tkinter as tk

def create_subway_map(root):
    canvas = tk.Canvas(root, width=600, height=400, bg="white")
    canvas.pack()

    station_a = (100, 100)
    station_b = (200, 100)
    station_c = (200, 200)
    station_d = (300, 200)

    canvas.create_line(station_a, station_b, fill="blue", width=5)
    canvas.create_line(station_b, station_c, fill="red", width=5)
    canvas.create_line(station_c, station_d, fill="blue", width=5)

    radius = 5
    canvas.create_oval(station_a[0]-radius, station_a[1]-radius, station_a[0]+radius, station_a[1]+radius, fill="black")
    canvas.create_oval(station_b[0]-radius, station_b[1]-radius, station_b[0]+radius, station_b[1]+radius, fill="black")
    canvas.create_oval(station_c[0]-radius, station_c[1]-radius, station_c[0]+radius, station_c[1]+radius, fill="black")
    canvas.create_oval(station_d[0]-radius, station_d[1]-radius, station_d[0]+radius, station_d[1]+radius, fill="black")

    canvas.create_text(station_a[0], station_a[1]-15, text="Station A")
    canvas.create_text(station_b[0], station_b[1]-15, text="Station B")
    canvas.create_text(station_c[0], station_c[1]+15, text="Station C")
    canvas.create_text(station_d[0], station_d[1]-15, text="Station D")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simple Subway Map")
    create_subway_map(root)
    root.mainloop()
