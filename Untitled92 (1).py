#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np

trials = 100000  
successes = 0    

for i in range(trials):
    random_score = np.random.randint(0, 1000)    # Случайное количество очков от 1 до 6
    if random_score == 777:
        successes += 200
    elif random_score == 999:
        successes += 100  
    elif random_score == 555:
        successes += 50 
    elif random_score == 333:
        successes += 15
    elif random_score == 111:
        successes += 10 
    elif random_score != 777 and random_score %100 == 77:
        successes += 5
    elif random_score != 777 and random_score %10 == 7:
        successes += 3
    elif random_score %100 == 0:
        successes += 2
    elif random_score %10 == 0:
        successes += 1
    vygoda = successes - trials
    p_monte_carlo_lozer  =  trials/trials  - successes/trials 
    p_monte_carlo_win = successes/trials -trials/trials
if vygoda > 0:
    print("Игра выгодна игроку")
    print("Игрок приобретает",p_monte_carlo_win)
else:
    print("Игра невыгодна игроку")
    print("Игрок теряет",p_monte_carlo_lozer)

    p = 204 / 1000
print("Теоретическая вероятность",p)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




