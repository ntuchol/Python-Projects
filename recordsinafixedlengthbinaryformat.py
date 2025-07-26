import struct

with open('records.bin', 'wb') as file:
    records = [
        (b'John', 25, 72.5),
        (b'Alice', 30, 65.0),
        (b'Bob', 22, 80.3),
    ]
    for record in records:
        packed_data = struct.pack(record_format, record[0].ljust(10, b'\x00'), record[1], record[2])
        file.write(packed_data)

with open('records.bin', 'rb') as file:
    while chunk := file.read(record_size):
        unpacked_data = struct.unpack(record_format, chunk)
        name = unpacked_data[0].decode('utf-8').strip('\x00')
        age = unpacked_data[1]
        weight = unpacked_data[2]
        print(f'Name: {name}, Age: {age}, Weight: {weight}')
