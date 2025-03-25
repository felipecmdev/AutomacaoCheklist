import subprocess

class Programas():
    def open_cam(self):
     powershell_path = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
     subprocess.call('start ms-settings:camera', shell=True, executable=powershell_path)
    def open_mic(self):
        subprocess.call(['C:\\AutomacaoCheklist\\TestesAC\\Teste de mic.html'], shell=True)
    def open_monitor(self):
        subprocess.call(['C:\\AutomacaoCheklist\\TestesAC\\TesteMonitor.html'], shell=True)
    def open_speaker(self):
        subprocess.call(['C:\\AutomacaoCheklist\\TestesAC\\TesteSpeaker.mp3'], shell=True)
    def open_teclado(self):
        subprocess.call(['C:\\AutomacaoCheklist\\TestesAC\\TesteTeclado.html'], shell=True)
    def open_disco(self):
        subprocess.call(['C:\\AutomacaoCheklist\\TestesAC\\TesteDisco\\DiskInfo64.exe'], shell=True)
    def open_cpuInfo(self):
        subprocess.run(['C:\\AutomacaoCheklist\\TestesAC\\Sensor de CPU\\HWiNFO64.exe'], shell=True)
    def open_gpuStress(self):
        subprocess.run(['C:\\AutomacaoCheklist\\TestesAC\\GPU Stress\\FurMark_win64\\FurMark_GUI.exe'], shell=True)
    def open_cpuMEM(self):
        subprocess.run(['C:\\AutomacaoCheklist\\TestesAC\\CPU + Memoeria Stress 1\\OCCT.exe'], shell=True)
    def open_battery(self):
        subprocess.run(['C:\\AutomacaoCheklist\\TestesAC\\batteryinfoview\\BatteryInfoView.exe'], shell=True)
