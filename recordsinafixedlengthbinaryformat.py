import struct

# Define the format: '10s' for a 10-byte string, 'i' for a 4-byte integer, 'f' for a 4-byte float
record_format = '10sif'
record_size = struct.calcsize(record_format)

# Writing fixed-length binary records
with open('records.bin', 'wb') as file:
    # Example records
    records = [
        (b'John', 25, 72.5),
        (b'Alice', 30, 65.0),
        (b'Bob', 22, 80.3),
    ]
    for record in records:
        # Pad the string to 10 bytes and pack the data
        packed_data = struct.pack(record_format, record[0].ljust(10, b'\x00'), record[1], record[2])
        file.write(packed_data)

# Reading fixed-length binary records
with open('records.bin', 'rb') as file:
    while chunk := file.read(record_size):
        # Unpack the binary data
        unpacked_data = struct.unpack(record_format, chunk)
        # Decode the string and strip padding
        name = unpacked_data[0].decode('utf-8').strip('\x00')
        age = unpacked_data[1]
        weight = unpacked_data[2]
        print(f'Name: {name}, Age: {age}, Weight: {weight}')