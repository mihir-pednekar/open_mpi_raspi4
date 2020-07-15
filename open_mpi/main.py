from ScapyUtil import ScapyUtil

class FileList:
    
    def list_of_file(self, size, pcap_file_name):
        scapy = ScapyUtil()
        packets = scapy.read_pcap(pcap_file_name)
        p_len = len(packets)
        n = int(p_len/size)
        inner_lst = []
        size_diff = ((size*n)-n)
        
        for j in range(0, p_len, n):
            if j == size_diff:
                local_lst = []
                local_lst.append(str(j)+":"+str(p_len-1))
                inner_lst.append(local_lst)
                break
            else:
                local_lst = []
                local_lst.append(str(j)+":"+str(j+(n-1)))
                inner_lst.append(local_lst)
            
        print(inner_lst)
        print("<================ BREAK INTO DATASETS ================>")
        
        return inner_lst, packets
    
    def read_rule(self, rule_file_name):
        #read all rules
        rule_file = open(rule_file_name, 'r')
        rules = rule_file.readlines()
        return rules