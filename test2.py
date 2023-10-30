#boncuğumla yaptıiğim çalişma  Isırık alcam <3 seni seviyorummm
# BBenn daha cook seviyorummm .. 
class PLC ():
   def __init__(self,ip_adresi,markasi,protokolü):
      self.ip_adresi = ip_adresi
      self.markasi =markasi 
      self.protokolü = protokolü

   def plc_ac(self):
      if self.markasi == "siemens":
         print (self.ip_adresi + " olan "+self.markasi +" markali cihaz açiliyor....")
      elif self.markasi == "beckhoff":
         print(self.ip_adresi + " olan "+self.markasi +" markali cihaz açiliyor....")
      else:
         print("cihaz bulunamadi....")

plc1=PLC("192.466.464.54","vago","ads")
plc1.plc_ac()

plc2=PLC("192.466.464.54","beckhoff","ua")
plc2.plc_ac()