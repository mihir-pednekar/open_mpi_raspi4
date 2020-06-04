from scapy.all import *

class ScapyUtil:

	def read_pcap(self, path):
		packets = rdpcap(path)
		print(packets[0].show())
