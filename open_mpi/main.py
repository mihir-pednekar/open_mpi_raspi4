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
        
        return inner_lst, packets, p_len
    
    def read_rule(self, rule_file_name):
        #read all rules
        rule_file = open(rule_file_name, 'r')
        rules = rule_file.readlines()
        return rules
    
    def map_of_rules(self, rules):
        #list_rule_map = []
        final_map = {'Ethernet' : [], 'IP' : [], 'ICMP' : []}
        for rule in rules:
            rule_map = {}
            x = rule.split(" ", 7)
            rule_map['task'] = x[0]
            #rule_map['proto'] = x[1]
            rule_map['direc'] = x[4]
            if x[4] == '->':
                rule_map['src_ip'] = x[2]
                rule_map['src_port'] = x[3]
                rule_map['dst_ip'] = x[5]
                rule_map['dst_port'] = x[6]
                
            else:
                rule_map['src_ip'] = x[5]
                rule_map['src_port'] = x[6]
                rule_map['dst_ip'] = x[2]
                rule_map['dst_port'] = x[3]
            
            trim_str = x[7].strip('(').strip(')')
            trim_list = trim_str.split("; ")
            temp_map = {}
            
            for trim in trim_list:
                temp_list = trim.strip(';').split(":")
                print(temp_list)
                temp_map[temp_list[0]] = temp_list[1]
            
            rule_map['para'] = temp_map
            final_map[x[1]].append(rule_map)
            #list_rule_map.append(rule_map)
        
        return final_map
    
#obj = FileList()
#rules = obj.read_rule("local.rules")
#print(obj.map_of_rules(rules))