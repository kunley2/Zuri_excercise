import random

choices = ['R','P','S']
random_choices = random.choices(choices)
choice_dict = {'R':'Rock','P':'Paper','S':'Scissors'}


class RockPaperScissors():
    """ this game is the rock, paper, scissors game """
    def __init__(self,random_choices):
        self.choice = random_choices[0]
        
    def welcome(self):
        print('Welcome to kunle rock paper game.\n')
        self.name = str(input('please put in your name: '))    
        self.choose()
    
    def choose(self,):
        chosen = str(input(f'please choose an option. \n R: rock, P: Paper, S: scissors: ' )).capitalize()
        print(f'{self.name}: {choice_dict[chosen]}')
        if chosen not in choices:
            print('please read the instructions carefully')
            self.choose()
        if self.choice == chosen:
            print(f'CPU: {choice_dict[self.choice]}')
            print('its a draw')
            x = 1
            while x != 0:
                restart = int(input('Press 1: to restart or press 0: to exit: '))
                if restart == 1:
                    self.welcome()
                elif restart == 0:
                    exit()
                else:
                    print('please pick between 1 or 0')
                    x = 1
        elif self.choice == 'R':
            if chosen == 'S':
                print(f'CPU: {choice_dict[self.choice]}')
                print('sorry you lose!!!')
            else:
                print(f'CPU: {choice_dict[self.choice]}')
                print('you won!!\n thank you for playing')   
        elif self.choice == 'P':
            if chosen == 'S':
                print(f'CPU: {self.choice}')
                print('sorry you lose!!!')
            else:
                print(f'CPU: {choice_dict[self.choice]}')
                print('you won!!\n thank you for playing') 
        else:
            if chosen == 'R':
                print(f'CPU: {choice_dict[self.choice]}')
                print('sorry you lose!!!')
            else:
                print(f'CPU: {choice_dict[self.choice]}')
                print('you won!!\n thank you for playing') 
            # exit()
if __name__ == '__main__':                  
    RockPaperScissors(random_choices).welcome()        
# RockPaperScissors(random_choices).welcome()  
    
    