#!/usr/bin/python3
# Translation from python 2 (blackhatpython)
import socket
import os
import struct
import ctypes

# host to listen on
host = "10.222.107.54"


# our IP header
class IP(ctypes.Structure):
    _fields_ = [
        ("ihl", ctypes.c_ubyte, 4),
        ("version", ctypes.c_ubyte, 4),
        ("tos", ctypes.c_ubyte),
        ("len", ctypes.c_ushort),
        ("id", ctypes.c_ushort),
        ("offset", ctypes.c_ushort),
        ("ttl", ctypes.c_ubyte),
        ("protocol_num", ctypes.c_ubyte),
        ("sum", ctypes.c_ushort),
        ("src", ctypes.c_uint32),   # differ from book (64-bit vs 32-bit OS)
        ("dst", ctypes.c_uint32)    # differ from book (64-bit vs 32-bit OS)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):

        # map protocol constans to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        # human readable IP addresses '@I' differs from book (see above)
        self.src_address = socket.inet_ntoa(struct.pack("@I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("@I", self.dst))

        # human readable protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(ctypes.Structure):

    _fields_ = [
        ("type", ctypes.c_ubyte),
        ("code", ctypes.c_ubyte),
        ("checksum", ctypes.c_ushort),
        ("unused", ctypes.c_ushort),
        ("next_hop_mtu", ctypes.c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass


if os.name == "nt":  # windows special
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                        socket_protocol)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == 'nt':
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

try:
    while True:
        # read in a package
        raw_buffer = sniffer.recvfrom(65565)[0]

        # create an IP header from the first 32 bytes of the buffer
        ip_header = IP(raw_buffer[:32])  # differs from book (20 vs 32 bytes)

        # print out the protocol that was detected and the hosts
        print("Protocol: {} {} -> {}".format(ip_header.protocol,
                                             ip_header.src_address,
                                             ip_header.dst_address))

        # if it is ICMP, we want it
        if ip_header.protocol == "ICMP":
            # calculate where our ICMP packet starts
            offset = ip_header.ihl * 4
            buf = raw_buffer[offset:offset + ctypes.sizeof(ICMP)]

            # create our ICMP structure
            icmp_header = ICMP(buf)

            print("ICMP -> Type: {} Code: {}".format(icmp_header.type,
                                                     icmp_header.code))
except KeyboardInterrupt:
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
