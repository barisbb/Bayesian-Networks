import numpy as np

def normalize(array):
    tmp=1/(sum(array))
    return np.array([tmp*array[0],tmp*array[1]])

#Variable Elimination

earthquake=False #change here
johncalls=True   #change here

p_ma=np.array([0.70,0.01,0.3,0.99])
p_b=np.array([0.001, 0.999,0.001,0.999])
if(johncalls):
    p_a=np.array([0.9,0.05,0.9,0.05])
else:
    p_a=np.array([0.1,0.95,0.1,0.95])

p_ma_1=p_a*p_ma
p_a_1=np.array([p_ma_1[0]+p_ma_1[2], p_ma_1[1]+p_ma_1[3]])

if(earthquake):
  p_ab=np.array([0.95,0.29,0.05,0.71])
else:
  p_ab=np.array([0.94,0.001,0.06,0.999])

p_a_1_revised=np.array([p_a_1[0], p_a_1[0],p_a_1[1],p_a_1[1]])
p_ab_1=p_a_1_revised*p_ab
p_ab_1=p_ab_1*p_b
p_ab_1_revised=np.array([p_ab_1[0] +p_ab_1[1],p_ab_1[2] + p_ab_1[3]])
p_ab_1_revised=normalize(p_ab_1_revised)

print("Alarm probability:" + str(p_ab_1_revised[0]))

#Filtering

umbrella=[False,False,False,True] #change here
day_r=np.array([0.5,0.5])

for i in range(4): #totally 4 days
    r=np.array([0.7*day_r[0],0.3*day_r[0]])+np.array([0.3*day_r[1],0.7*day_r[1]])
    u_given_r=0
    if(umbrella[i]==True):
        u_given_r=np.array([0.9,0.2])
    else:
        u_given_r=np.array([0.1,0.8])
    
    r_given_u=u_given_r*r
    r_given_u=normalize(r_given_u)
    day_r=r_given_u
print('Probability of rain:'+str(day_r[0]))
    
