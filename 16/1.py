#!/usr/bin/python3
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


#def decode_literal(packet):



#def decode_binary(binary_input):



complete_input = ''
for line in f:
    complete_input += line

binary_input = decode_input(complete_input)
packets = []
packets_remaining = True
i = 0
while packets_remaining:
    packet = ''
    if binary_input[i+3:i+6] == '100':
        packet += binary_input[i:i+6]
        i += 6
        ended = False
        while not ended:
            print(f'Up to {i} which I think is {binary_input[i]}')
            if binary_input[i] == '1':
                packet += binary_input[i:i+5]
                i += 5
            else:
                packet += binary_input[i:i+5]
                i += 5 
                ended = True
        packets.append(packet)
    elif binary_input[i+3i+6] != '100':
        packet += 
        
    if i == len(binary_input)-1:
        packets_remaining = False
    i+= 1
print(packets)
