import struct
import sys

def convert_sub_to_c16(sub_file_path, c16_file_path):
    # Open the .sub file and read the raw samples
    with open(sub_file_path, 'rb') as sub_file:
        sub_data = sub_file.read()
    
    # Calculate the number of IQ samples from the number of raw samples
    num_samples = len(sub_data) // 2
    
    # Convert the raw samples to IQ data
    iq_data = []
    for i in range(num_samples):
        sample = struct.unpack('<B', sub_data[i*2:i*2+1])[0]
        i_value = (sample & 0x0F) - 8
        q_value = ((sample >> 4) & 0x0F) - 8
        iq_data.append((i_value, q_value))
    
    # Open the .c16 file and write the IQ data
    with open(c16_file_path, 'wb') as c16_file:
        for i, q in iq_data:
            c16_data = struct.pack('>BB', (i + 128), (q + 128))
            c16_file.write(c16_data)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python convert_sub_to_c16.py <sub_file_path> <c16_file_path>')
        sys.exit(1)
    
    sub_file_path = sys.argv[1]
    c16_file_path = sys.argv[2]
    
    convert_sub_to_c16(sub_file_path, c16_file_path)
