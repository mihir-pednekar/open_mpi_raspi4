from scapy.all import *
from datetime import datetime

class ScapyUtil:

	def read_pcap(self, path):
		packets = rdpcap(path)
		return packets
		#print(packets[0].show())
		
	def write_pcap(self, pkt, file_name):
		wrpcap(file_name, pkt)
		
	def get_timestamp(self):
		# current date and time
		now = datetime.now()
		timestamp = now.strftime("%Y%d%m%H%M%S")
		return timestamp