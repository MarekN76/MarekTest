"""Created on Fri Feb 12 10:10:56 2021@author: marek_nowak"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
k1=pd.read_csv('Wzrost.csv')
'--------------Wartości średnie------------------'
s1= np.mean(k1['Wzrost_cm'][0:5])
s2= np.mean(k1['Wzrost_cm'][5:10])
S=[s1,s2]
'------------------------------------------------'
'---------------Wariancja wzrostu----------------'
c1= np.var(k1['Wzrost_cm'][0:5])
c2= np.var(k1['Wzrost_cm'][5:10])
C=[c1,c2] 
'------------------------------------------------'
Pm=np.exp((-(172-s1)*(172-s1))/(2*c1))/np.sqrt(2*c1*np.pi)
Pk=np.exp((-(172-s2)*(172-s2))/(2*c2))/np.sqrt(2*c2*np.pi)
D=[Pm,Pk]
k2=pd.DataFrame({'Płeć':['Mężczyzna','Kobieta'],'Średni_Wzrost':np.round(S,2),'Wariancja_Wzrostu':np.round(C,2),'Prawdopodobieństwo_172':np.round(D,2)})
print(k2)
if Pm > Pk:
    Pc=((Pm*0.5)/(Pm*0.5+Pk*0.5))*100
    print("Wynik dla Mężczyzny przy wzroście 172:",np.round(Pc,1),"%")
else:
    Pc=((Pk*0.5)/(Pk*0.5+Pm*0.5))*100
    print("Wynik dla Kobiety przy wzroście 172:",np.round(Pc,1),"%")
