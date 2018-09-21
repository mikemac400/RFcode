import math 

#Inputs 
Cpi = 24e-12
Rpi = 1.22e3
Rg = 50
gm = 155e-3
Co = 0.8e-12
f0 = 50e6
w0 = 2*math.pi*f0
BW = 4e6
R2 = 100
RL = 50

#Find the butterworth poles for the output (s0 and s2) and the input (s1)
s0r = -0.5
s0j = (3)**0.5/2
s1r = -1
s1j = 0
s2r = -0.5
s2j = (3)**0.5/2

#use these poles to calculate Q and w0 for each amplifier stage. 
#the capacitve coupling provides the required frequency staggering. w0 is the same for each stage.
Qin = f0 / BW
k = ((3)**0.5*BW) / (2*f0)
Qout = 2*f0 / BW    #Q is the same in both output circuits 


#calculate component values for input circuit 
Nin = (1.2e3/50)**0.5
Ctin = Qin / (w0*(1.22e3/2))
C1 = Ctin - Cpi
L1 = 1 / (w0**2 * Ctin)
nin = (Rg/Rpi)**0.5
Cplin = Ctin - Cpi  #parralel combination of C11 and C12 
C12 = Cplin / nin
C11 = (C12 * Cplin) / (C12 - Cplin)

#calculate output component values  
k = (3**0.5 * BW) / (2 * f0)
Cs = Qout / (R2 * w0)    #Csigma
Ls = 1/ (w0**2 * Cs)     #Lsigma
Ck = k*Cs                #coupling capacitor 
C2 = Cs - Ck - Co
n2 = (RL/R2)**0.5
Cpl = Cs - Ck            #parralel combination of transformation capacitors 
C22 = Cpl / n2
C21 = (n2 * C22) / (1-n2)

#calculate system properties 
gain = (gm * R2 * 3**0.5 * n2) / (nin * 8)
gaindb = 20*math.log10(gain)
Pg = 4*gain**2  #power gain 
Pgdb = 20*math.log10(Pg)


#prints
print('============input==============')
print('Qin = ', Qin)
print('C1 = ', C1)
print('L1 = ', L1)
print('nin = ', nin)
print('C11 = ', C11)
print('C12 = ', C12)

print('============output=============')
print('k = ', k)
print('Qout = ', Qout)
print('Csigma = ', Cs)
print('Ls = ', Ls)
print('Ck = ', Ck)
print('C2 = ', C2)
print('n2 = ', n2)
print('C21 = ', C21)
print('C22 = ', C22)
print('======System Properties========')
print('voltage gain = ', gain)
print('Voltage Gain (db) = ', gaindb) 
print('Power gain = ', Pg)
print('Power gain (db) = ',Pgdb)
