import subprocess
import os

class Programas():

    def Volume(self):
        diretorio_atual = os.path.abspath(os.path.dirname(__file__))
        volume = os.path.splitdrive(diretorio_atual)[0]
        return volume
    def open_cam(self):
     powershell_path = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
     subprocess.call('start ms-settings:camera', shell=True, executable=powershell_path)
    def open_mic(self):
        volume = self.Volume()
        subprocess.call([f'{volume}\\AutomacaoCheklist\\TestesAC\\Teste de mic.html'], shell=True)
    def open_monitor(self):
        volume = self.Volume()
        subprocess.call([f'{volume}\\AutomacaoCheklist\\TestesAC\\TesteMonitor.html'], shell=True)
    def open_speaker(self):
        volume = self.Volume()
        subprocess.call([f'{volume}\\AutomacaoCheklist\\TestesAC\\TesteSpeaker.mp3'], shell=True)
    def open_teclado(self):
        volume = self.Volume()
        subprocess.call([f'{volume}\\AutomacaoCheklist\\TestesAC\\TesteTeclado.html'], shell=True)
    def open_disco(self):
        volume = self.Volume()
        subprocess.call([f'{volume}\\AutomacaoCheklist\\TestesAC\\TesteDisco\\DiskInfo64.exe'], shell=True)
    def open_cpuInfo(self):
        volume = self.Volume()
        subprocess.run([f'{volume}\\AutomacaoCheklist\\TestesAC\\Sensor de CPU\\HWiNFO64.exe'], shell=True)
    def open_gpuStress(self):
        volume = self.Volume()
        subprocess.run([f'{volume}\\AutomacaoCheklist\\TestesAC\\GPU Stress\\FurMark_win64\\FurMark_GUI.exe'], shell=True)
    def open_cpuMEM(self):
        volume = self.Volume()
        subprocess.run([f'{volume}\\AutomacaoCheklist\\TestesAC\\CPU + Memoeria Stress 1\\OCCT.exe'], shell=True)
    def open_battery(self):
        volume = self.Volume()
        subprocess.run([f'{volume}\\AutomacaoCheklist\\TestesAC\\batteryinfoview\\BatteryInfoView.exe'], shell=True)
