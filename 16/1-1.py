#!/usr/bin/python3
import pdb

def decode_hex(hex_code):
    if hex_code == '0':
            return '0000'
    if hex_code == '1':
        return '0001'
    if hex_code == '2':
        return '0010'
    if hex_code == '3':
        return '0011'
    if hex_code == '4':
        return '0100'
    if hex_code == '5':
        return '0101'
    if hex_code == '6':
        return '0110'
    if hex_code == '7':
        return '0111'
    if hex_code == '8':
        return '1000'
    if hex_code == '9':
        return '1001'
    if hex_code == 'A':
        return '1010'
    if hex_code == 'B':
        return '1011'
    if hex_code == 'C':
        return '1100'
    if hex_code == 'D':
        return '1101'
    if hex_code == 'E':
        return '1110'
    if hex_code == 'F':
        return '1111'


def decode_input(hex_code):
    binary = ''
    for char in hex_code:
        binary += decode_hex(char)
    return binary


def decode_literal(packet, mode):
    ended = False
    version = int(packet[0:3], 2)
    i = 5
    value = ''
    while not ended:
        if packet[i+1] == '1':
            value += packet[i+1:i+5]
            i += 5
        else:
            value += packet[i+1:i+5]
            i += 5
            ended = True
    if mode == 'version':
        return version
    elif mode == 'value':
        return value
    elif mode == 'end':
        return i
    elif mode == 'value&version':
        return value, version
    elif mode == 'version&end':
        return version, end


def determine_type(packet):
    if packet[3:6] == '100':
        return 'literal'
    else:
        if packet[6] == '0':
            return 'op_15'
        else:
            return 'op_11'


def handle_op_15(packet, mode):
    version = int(packet[0:3], 2)
    sub_bit_length = int(packet[7:22], 2)
    packet_end = 22 + sub_bit_length
    sub_bits = packet[22:packet_end]
    if mode == 'subs':
        return sub_bits
    elif mode == 'end':
        return int(packet_end)
    elif mode == 'version':
        return version
    elif mode == 'subs&version':
        return sub_bits, version
    elif mode == 'version&end':
        return version, packet_end


def handle_op_11(packet, mode):
    # pdb.set_trace()
    version = int(packet[0:3], 2)
    sub_number = int(packet[7:18], 2)
    packets = []
    x = 17
    for i in range(0, sub_number):
        x += 1
        packet_type = determine_type(packet[x:])
        if packet_type == 'literal':
            packet_end = x + decode_literal(packet[x:], 'end')
            packets.append(packet[x:packet_end+1])
            x = packet_end
        elif packet_type == 'op_15':
            packet_end = x + handle_op_15(packet[x:], 'end')
            packets.append(packet[x:packet_end])
            x = packet_end
        elif packet_type == 'op_11':
            packet_end = handle_op_11(packet[x:], 'end')
            packets.append(packet[x:packet_end])
            x = packet_end
    if mode == 'subs':
        return packets
    elif mode == 'version':
        return version
    elif mode == 'end':
        return x
    elif mode == 'subs&end':
        return packets, x
    elif mode == 'subs&version':
        return packets, version
    elif mode == 'version&end':
        return version, x


def decode_operator(packet):
    operator_type = determine_type(packet)
    if operator_type == 'op_15':
        z = 22
    else:
        z = 18
    packets = []
    while z < len(packet) and (len(packet) - z) >= 10:
        packet_type = determine_type(packet[z:])
        if packet_type == 'literal':
            packet_end = decode_literal(packet[z:], 'end') + 1
            packets.append(packet[z:z+packet_end])
            z += packet_end
        elif packet_type == 'op_15':
            packet_end = handle_op_15(packet[z:], 'end')
            packets.append(packet[z:z+packet_end])
            z += packet_end
        elif packet_type == 'op_11':
            packet_end = handle_op_11(packet[z:], 'end')
            packets.append(packet[z:z+packet_end])
            z += packet_end
    return packets


# Check how many bits till end, if less then 11 assume last packet + padding
f = open('test').read().splitlines()
complete_input = ''
for line in f:
    complete_input += line
binary_input = decode_input(complete_input)
print(f'Base binary is {binary_input}')
i = 0
version_count = 0
while i < len(binary_input) and (len(binary_input) - i) >= 10:
    packet_type = determine_type(binary_input[i:])
    if packet_type == 'literal':
        version, end = decode_literal(binary_input[i:], 'version&end')
        version_count += version
        print(f'lit v of {version} from {binary_input[i:]}')
        i += end
    else: 
        if packet_type == 'op_15':
            version, end = handle_op_15(binary_input[i:], 'version&end')
        elif packet_type == 'op_11':
            version, end = handle_op_11(binary_input[i:], 'version&end')
        version_count += version
        print(f'v of {version} from {binary_input[i:]}')
        packets = [binary_input[i:i+end]]
        while packets:
            inpr_packet = packets.pop()
            cur_packet_type = determine_type(inpr_packet)
            if cur_packet_type == 'literal':
                version_count += int(inpr_packet[0:3], 2)
                print(f'Nested lit v of {int(inpr_packet[0:3], 2)} for {inpr_packet}')
            else:
                for packet in decode_operator(inpr_packet):
                    packets.append(packet)
                    if determine_type(packet) != 'literal':
                        print(f'Found {packet} with v {int(packet[0:3], 2)}')
                        version_count += int(packet[0:3], 2)
        i += end

print(version_count)
    
    
