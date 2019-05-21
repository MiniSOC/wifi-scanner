import nmap
from netaddr import IPNetwork
import _thread

def get_ips_from_cidr(cidr_range):
    ips = []
    for ip in IPNetwork(cidr_range):
        ips.append(str(ip))
    return ips

def scan_ip(nm, ip):
    data = nm.scan(hosts=ip, arguments="-sP")
    print(data["scan"])


nm = nmap.PortScanner()
ips = get_ips_from_cidr("192.168.0.1/30")
for ip in ips:
    # try:
    #     _thread.start_new_thread(scan_ip, (nm, ip))
    # except:
    #     print("Unable to start thread")
    scan_ip(nm,ip)



