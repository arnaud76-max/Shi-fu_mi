#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


user_score = 0
cp_score = 0

user_nbr_round = int(input('Combien de manche ?'))
nbr_round = 0
while (nbr_round < user_nbr_round):
    
    user_choice = input('Choisis entre pierre, feuille ,ciseaux, lézard , spock  :')
    if(user_choice =='pierre' or user_choice == 'feuille' or user_choice == 'ciseaux' or user_choice =="lézard"
       or user_choice=="spock"):
        
        
        print('-------------------------------')
        
        can_use = ['pierre', 'feuille', 'ciseaux','lézard','spock']
        cp_choice = random.choice(can_use)
        
        print('L\ordinateur à choisi; ', cp_choice)
        if(user_choice == cp_choice ):
                print('Egalitée ')
                
        elif(user_choice == 'pierre' and cp_choice == 'feuille'):
                print("L'ordi gagne !")
                cp_score = cp_score + 1
                
        elif(user_choice == 'pierre' and cp_choice == 'ciseaux'):
                print('Bravo vous avez gagné !')
                user_score = user_score + 1
                
        elif(user_choice == 'feuille' and cp_choice == 'pierre'):
                print('Bravo vous avez gagné !')
                user_score = user_score + 1
                
        elif(user_choice == 'feuille' and cp_choice == 'ciseaux'):
                print('L\'ordi gagne !')
                cp_score = cp_score + 1
                   
        elif(user_choice =='ciseaux' and cp_choice =='pierre'):
                print('L\'ordi gagne !')
                cp_score = cp_score + 1
                  
        elif(user_choice == 'ciseaux' and cp_choice == 'feuille'):
                print('Bravo vous avez gagné !')
                user_score = user_score + 1   
                
        elif(user_choice =='lézard' and cp_choice == "spock"):
                 print("Vous avez empoisonné l'ordi")
                 user_score = user_score + 1 
                    
        elif(cp_choice =='lézard' and user_choice == "spock"):
                 print('L\'ordi vous avez empoisonné ')
                 user_score = user_score + 1 
                    
        elif(user_choice =='pierre' and cp_choice == "lézard"):
                 print("Bravo vous avez écraser l'ordi")
                 user_score = user_score + 1 
                    
        elif(cp_choice =='pierre' and user_choice == "lézard"):
                 print("L'ordi vous a écraser")
                 cp_score = cp_score + 1 
                    
        elif(user_choice =='spock' and cp_choice == "ciseaux"):
                 print("Bravo vous avez écraser l'ordi")
                 user_score = user_score + 1 
                    
        elif(cp_choice =='spock' and user_choice == "ciseaux"):
                 print("L'ordi vous a écraser")
                 cp_score = cp_score + 1   
                    
        elif(user_choice =='lézard' and cp_choice == "feuille"):
                 print("Vous avez mangé l'ordi")
                 user_score = user_score + 1 
                    
        elif(cp_choice =='lézard' and user_choice == "feuille"):
                 print("L'ordi vous a mangé")
                 cp_score = cp_score + 1   
                      
        elif(user_choice =='ciseaux' and cp_choice =='lézard'):
                print("Vous avez décapiter l'otrdi")
                user_score = user_score + 1   
             
        elif(cp_choice =='ciseaux' and user_choice =='lézard'):
                print("L'Ordi vous a décapiter")
                cp_score = cp_score + 1  
             
        elif(user_choice =='spock' and cp_choice =='pierre'):
                print("Vous avez détruit l'ordi ")
                user_score = user_score + 1  
                      
        elif(cp_choice =='spock' and user_choice =='pierre'):
                print("L'ordi vous avez détruit ")
                user_score = user_score + 1        
                      
        nbr_round = nbr_round + 1
        print('Manche numéro', nbr_round, 'sur' ,user_nbr_round)

        print("Tu as" , user_score, "points")
        print("L'ordi a" , cp_score, "points")


# In[ ]:





# In[ ]:




