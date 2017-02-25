import nmap
nm = nmap.PortScanner()
print(nm.nmap_version())
nm.scan('103.12.135.186', '1-1024', '-v')
print(nm.scaninfo())
print(nm.csv())
