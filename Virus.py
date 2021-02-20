"""Created on Fri Feb 19 10:56:18 2021@author: marek_nowak"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
P_tp=((0.98*0.04)/(2*0.98*0.04+1-0.98-0.04))*100
P_tn=(((1-0.98)*0.04)/(-2*0.98*0.04+0.98+0.04))*100
C = pd.DataFrame({'Obecność wirusa': ["%", np.round(P_tp,3)],'Brak obecności wirusa': ["%", np.round(P_tn,3)]})
A = 0.04 #"Wirus"
B = 0.98 #"Wiarygodność"
C = 0.85 #"Objawy"
R_P = A*B*C #"Pozytywny-wirus"
R_N = (1-B)*(1-C)*(1-A) #"Pozytywny-bez wirusa"
W_P=(R_P/(R_P+R_N))*100
print("Pacjent z objawami jest nosicielem wirusa V:",np.round(W_P,2),'%')


