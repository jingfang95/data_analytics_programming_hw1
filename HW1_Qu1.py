#!/usr/bin/env python
# coding: utf-8

# In[2]:


def h_choices_counter():

    if human_choice == 'Rock':
        human_choices['Rock'] +=1

    elif human_choice == 'Paper':
        human_choices['Paper'] += 1
    
    else: 
        human_choices['Scissors'] += 1


# In[1]:


def computer_brain():

    inverted_beats = {value: key for key, value in beats.items()}
        
    key_max = max(human_choices.keys(),key=(lambda k: human_choices[k]))
    
    computer_choice = inverted_beats[key_max]
    
    return computer_choice
    
    
    


# In[3]:


import random



choices = ['Rock','Paper','Scissors']

beats = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

human_stats = {'games_played':0, 'wins': 0}

computer_choice = random.choice(choices)

human_choices={'Rock':0, 'Paper':0,'Scissors':0}

human_choice = input('To play choose between: Rock, Paper and Scissors or you can choose to quit: ')


def Human_turn(human_choice,choices,computer_choice,beats,human_choices):
    
        while True:

            if human_choice in choices:
                
                human_choices[human_choice] +=1
                human_stats['games_played'] +=1
                
                if human_choice == computer_choice:
                    print("It's a tie!")
                    computer_brain()
                    human_choice = input('To play choose between: Rock, Paper and Scissors or you can choose to quit: ')
                    
                elif beats[human_choice] == computer_choice:
                    print("You win!")
                    human_stats['wins'] += 1
                    computer_brain()
                    human_choice = input('To play choose between: Rock, Paper and Scissors or you can choose to quit: ')
                    
                else:
                    print("You lose!")
                    computer_brain()
                    human_choice = input('To play choose between: Rock, Paper and Scissors or you can choose to quit: ')
                    
            else:
                if human_choice == 'quit':
                    print("You won", human_stats['wins'],"games out of",human_stats['games_played'])
                    print("Have a good day!")
                    break
                            
                else:
                    print("Enter a valid choice")
                    human_choice = input('To play choose between: Rock, Paper and Scissors or you can choose to quit: ')

Human_turn(human_choice,choices,computer_choice,beats,human_choices)


# In[ ]:




