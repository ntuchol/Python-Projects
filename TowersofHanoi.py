def move_disk(source, destination):
    print(f"Move disk from {source} to {destination}")

def hanoi(num_disks, source, auxiliary, destination):
    if num_disks == 1:
        move_disk(source, destination)
    else:
        hanoi(num_disks - 1, source, destination, auxiliary)
        move_disk(source, destination)
        hanoi(num_disks - 1, auxiliary, source, destination)

def solve_hanoi(num_disks):
    hanoi(num_disks, 'A', 'B', 'C')

# Example usage:
num_disks = 3
solve_hanoi(num_disks)