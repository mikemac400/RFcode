#Group tutorial 4: Tuned Resonance crcuit with autotransformer 
'''Goals
- impedance matching on input side
- impedance matching on output side 
- calculate the center frequency voltage gain v2/Eg 
- calculate the operating power gain Pout / Pin
'''

import math 

#design criteria
f0 = 110e6      #center frequency 
BW = 8e6        #3db bandwidth in synchronous tuning 
Rg = 50         #generator resistance
RL = 50         #load impedance 
Cpi = 15e-12    #pi model parasitic capacitance
Rpi = 330       #pi model resistance 
gm = 210e-3     #transconductance 
Co = 0.8e-12    #output capacitance 
Rcc = 80        #total collector load. Not to be confused with the actual load which is attached to center tap.
Ro = 1/0.3e-3   #transistor output resistance based on g0 conductance given  
GBF2 = 0.6436   #gain bandwidth factor 2.

#SOLUTION
#input side
BWres = BW / GBF2    #bandwidth for a signle side of the circuit, since the total bandwidth will be smaller than the one sides bandwidth in a tuned circuit
Qres = f0 / BWres   #Q factor for single sided circuit 
Ct = (2 * Qres) / (2 * math.pi * Rpi * f0)   #solve for intermediary variable Ctotal. The 2 comes from the fact that Rg' must equal Rpi, so the impedance of Rtotal is halved. Remember the important equation Q = R * C * w0
C1 = Ct - Cpi
L1 = 1 / (Ct *  (2*math.pi*f0)**2)
N1 = (330/50)**0.5
#output side
Rp = (Rcc*Ro*2) / (Ro-Rcc)      #Had to solve a long system of equations to get here. Important to remember that Rcc is equal to the parralel competition of RL-transformed and Rp, and RL-transformed is equal to the parralel combination of Rp and Ro. The last equation makes sense, since RL-transformed should impedance match the rest of the circuit, but the first equation makes less sense. I asked the professor and he said you "throw out" the output resistance of the transistor to get the collector resistance. I guess this makes sense, since if you measured from the collector, you would not see the transistor resistance, but according to the circuit diagram you would... I'm not really sure but I'll take it on faith for now. I think you can calculate Ro based on the output I-V characteristics. 
N2 = ((RL*(Rp+Ro)) / (Rp*Ro))**0.5  #it's easy to get RL' and thus N once Rp is calculated. Next we have to design the circuit to operate in our frquency of interest. It seems like these problems boil down to a) impedance matching by changing N values which affect resistance and b) ensuring that the circuit is operating at the right area, which mainly dependson C and L. At resonance though, the impedance only depends on R values which is why the transformer is important. 
Rt2 = (Ro*Rcc)/(Ro+Rcc)         #capacitance calc 
Ct2 = (Qres / (Rt2 *2*math.pi*f0))
C2 = Ct2-Co
L2 = 1 / ((2*math.pi*f0)**2*Ct2)    #inductance calc

#the above is for impedance matching and BW/f0 creation. Next the question wants us to calculate the voltage gain.#If impedance matching is correct, v1 should be half of the input voltage. v1 controls the gain. 


gain = (-gm*Rt2/2)


#prints
print()
print('============Input Side================')
print('C1 = ', C1)
print('L1 = ', L1)
print('N1 = ', N1)
print('===========Output Side===============')
print('Rp = ', Rp)
print('N2 = ', N2)
print('C2 = ', C2)
print('L2 = ', L2)
print('Rt2 = ', Rt2)

print()
