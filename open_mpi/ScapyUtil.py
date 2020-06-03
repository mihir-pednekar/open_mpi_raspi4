'''
Created on 03-Jun-2020

@author: mihir
'''

from scapy.all import *

class ScapyUtil:
    '''
    Too read pcap files
    '''
    pcap_file_name = ""

    def __init__(self, path):
        '''
        Constructor
        '''
        self.pcap_file_name = path
        
    def read_pcap(self):
        # rdpcap comes from scapy and loads in our pcap file
        packets = rdpcap('example.pcap')
        
        # Let's iterate through every packet
        for packet in packets:
            # We're only interested packets with a DNS Round Robin layer
            if packet.haslayer(DNSRR):
                # If the an(swer) is a DNSRR, print the name it replied with.
                if isinstance(packet.an, DNSRR):
                    print(packet.an.rrname)
        