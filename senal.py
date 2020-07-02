import RPi.GPIO as GPIO
import time
import subprocess

LEDRPI=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDRPI, GPIO.OUT) ## GPIO 17 como salida
#GPIO.setup(18, GPIO.OUT) ## GPIO 27 como salida
def blink():
   #print "Ejecucion iniciada..."
   k=0
   while k<60:
      GPIO.output(LEDRPI, True) ## Enciendo el 17
      time.sleep(0.2) ## Esperamos 1 segundo
      GPIO.output(LEDRPI, False) ## Apago el 17
      time.sleep(0.7)
      k=k+1
   #print "Ejecucion finalizada"
   #GPIO.cleanup() ## Hago una limpieza de los GPIO
def alarma():
   #print "Ejecucion iniciada..."
   j=0
   while j<60:
      GPIO.output(LEDRPI, True) ## Enciendo el 17
      time.sleep(0.05) ## Esperamos 1 segundo
      GPIO.output(LEDRPI, False) ## Apago el 17
      time.sleep(0.05)
      j=j+1
   #print "Ejecucion finalizada"
   #GPIO.cleanup() ## Hago una limpieza de los GPIO

i=1
while i>0:
   address = "8.8.8.8"
   res = subprocess.call(['ping', '-c', '1', address])
   if res == 0:
      #print "ping to", address, "OK"
      blink()
   elif res == 2:
      #print "no response from", address
      alarma()
   else:
      #print "ping to", address, "failed!"
      alarma()
   time.sleep(1)
