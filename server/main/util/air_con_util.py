import json
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pigpio

class air_con_util():
    
    
    # OUT_PIN = 17
    
    def __init__(self,freq:float = 38.0, gap:int=100) :
        self.FREQ = freq
        self.GAP_MS = gap
        self.GAP_S = self.GAP_MS  / 1000.0
        self.OUT_PIN = 17
        self.FILE = "codes"
    
    def _carrier(self , gpio, frequency, micros):
        """
            Generate carrier square wave.
        """
        wf = []
        cycle = 1000.0 / frequency
        cycles = int(round(micros/cycle))
        on = int(round(cycle / 2.0))
        sofar = 0
        for c in range(cycles):
           target = int(round((c+1)*cycle))
           sofar += on
           off = target - sofar
           sofar += off
           wf.append(pigpio.pulse(1<<gpio, 0, on))
           wf.append(pigpio.pulse(0, 1<<gpio, off))
        return wf

    def send_signal(self,signal_name:str):
        pi = pigpio.pi() # Connect to Pi.

        if not pi.connected:
            exit(0)
            
        try:
            f = open(self.FILE, "r")
            
        except:
            print("Can't open: {}".format(self.FILE))
            return {"msg":"設定ファイルがないため読み込めませんでした" }
        
        records = json.load(f)
        f.close()

        pi.set_mode(self.OUT_PIN, pigpio.OUTPUT) # IR TX connected to this GPIO.
        pi.wave_add_new()
        emit_time = time.time()
        if signal_name not in records:
            print("signal_name {} not found".format(signal_name))
        if signal_name in records:
            
            code = records[signal_name]
            # Create wave
            marks_wid = {}
            spaces_wid = {}
            
            wave = [0]*len(code)
            for i in range(0, len(code)):
                ci = code[i]
                if i & 1: # Space
                    if ci not in spaces_wid:
                        pi.wave_add_generic([pigpio.pulse(0, 0, ci)])
                        spaces_wid[ci] = pi.wave_create()
                    wave[i] = spaces_wid[ci]
                else: # Mark
                    if ci not in marks_wid:
                        wf = self._carrier(self.OUT_PIN, self.FREQ, ci)
                        pi.wave_add_generic(wf)
                        marks_wid[ci] = pi.wave_create()
                    wave[i] = marks_wid[ci]
                        
            delay = emit_time - time.time()
            
            if delay > 0.0:
                time.sleep(delay)
                
            pi.wave_chain(wave)
            
            while pi.wave_tx_busy():
                time.sleep(0.002)
            
            emit_time = time.time() + self.GAP_S
            
            
            for i in marks_wid:
                pi.wave_delete(marks_wid[i])
                
            marks_wid = {}
            
            for i in spaces_wid:
                pi.wave_delete(spaces_wid[i])
            
            spaces_wid = {}  
        pi.stop() # Disconnect from Pi.
        
                        
            