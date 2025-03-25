import platform 
import cpuinfo
import psutil
import wmi
import subprocess

from datetime import date

class PCinfo:

    def DataHoje(self):
     fdate = date.today( ).strftime(' %d/%m/%Y ')
     return fdate
   
    def Disk(self):
        ws = wmi.WMI(namespace='root/Microsoft/Windows/Storage')
        for d in ws.MSFT_PhysicalDisk():
            disco = d.Model
        return disco
    
    def Winver(self):
     return platform.platform() 

    def Mem(self):
        mem = (psutil.virtual_memory().total / 1024 / 1024 / 1024)
        mem = round(mem)
        return mem
        
    def SerialNumber(self):
        return subprocess.check_output('wmic bios get serialnumber').decode("utf-8").split('\n')[1]