#!/usr/bin/python3
import pdb
f = open('test').read().splitlines()


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


def decode_literal(packet):
    print(f'Literal version is {int(packet[0:3], 2)} in packet {packet}')
    ended = False
    i = 6
    value = ''
    while not ended:
        if packet[i] == '1':
            i += 1
            value += packet[i:i+4]
            i += 4
        else:
            i += 1
            value += packet[i:i+4]
            ended = True
    print(f'Literal value is {int(value, 2)}')
    return int(packet[0:3], 2)


def decode_operator(packet):
    version_count = int(packet[0:3], 2)
    print(f'Decode version is {version_count}')
    # print(f'Decode packet is {packet}')
    if packet[6] == '0': # 15
        subpacket_length = int(packet[7:22], 2)
        # print(f'Decode subpacket length is {subpacket_length}')
        packets = split_packets(packet[22:22+subpacket_length])
    else: # 11
        subpacket_number = int(packet[7:18], 2)
        if subpacket_number ==  1:
            packets = [packet[18:len(packet)]]
        else:
            packets = split_packets(packet[18:])
    # print(f'Decoded packets are {packets}')
    for packet in packets:
        if packet[3:6] == '100':
            version_count += decode_literal(packet)
        else:
            version_count += decode_operator(packet)
    return version_count
    

def split_packets(binary_input):
    packets = []
    packets_remaining = True
    i = 0
    print(f'Binary input is {binary_input}')
    while packets_remaining:
        packet = '' 
        if binary_input[i+3:i+6] == '100':
            packet += binary_input[i:i+6]
            i += 6
            ended = False
            while not ended:
                if binary_input[i] == '1':
                    packet += binary_input[i:i+5]
                    i += 5
                else:
                    packet += binary_input[i:i+5]
                    i += 4 
                    ended = True
            packets.append(packet)
        elif binary_input[i+3:i+6] != '100':
            packet += binary_input[i:i+6]
            i += 6
            packet += binary_input[i]
            if binary_input[i] == '0': # 15
                print(f'With {binary_input} at {i} I know this is a 0')
                i += 1
                packet += binary_input[i:i+15]
                subpackets = int(binary_input[i:i+15], 2)
                i += 15
                packet += binary_input[i:i+subpackets]
                i += subpackets 
            else: # 11
                i += 1
                # print(f'Else 11 packet is {binary_input} and i is {i}')
                packet += binary_input[i:i+11]
                subpackets = int(binary_input[i:i+11], 2)
                i += 11
                print(f'Here subpackets is {subpackets}')
                if subpackets == 1:
                    packet += binary_input[i:]
                else:
                    print(f'In the else I am up to i {i}')
                    if binary_input[i+6] == '0'
                        
                    for x in range(i+6, len(binary_input)):
                        test_packet = binary_input[i:x]
                        try:
                            test_packets = split_packets(test_packet)
                            if len(test_packets) == subpackets:
                                try:
                                    for packet in test_packets:
                                        if packet[3:6] == '100':
                                            decode_literal(packet)
                                        else:
                                            decode_operator(packet)
                                except:
                                    continue
                                packet += binary_input[i:x]
                                i = x
                                break
                        except:
                            pass
            # print(f'About to append {packet}')
            packets.append(packet)
            packets_remaining = False
            for x in range(i, len(binary_input)):
                if binary_input[x] != '0':
                    packets_remaining = True
                else:
                    packets_remaining = False
            
        if i == len(binary_input)-1:
            packets_remaining = False
        i+= 1
    print(f'Exiting with {packets}')
    return packets


complete_input = ''
for line in f:
    complete_input += line
binary_input = decode_input(complete_input)
print(f'Starting with binary {binary_input}')
packets = split_packets(binary_input)
print(f'Entry packets are {packets}')

final_count = 0
for packet in packets:
    if packet[3:6] == '100':
        final_count += decode_literal(packet)
    else:
        final_count += decode_operator(packet)

print(final_count)
