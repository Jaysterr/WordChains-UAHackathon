# gamemanager.py
# A manager for... the game :O
# handles game logic

import time
import random as rand
from WordRules import *


# TODO: Implement GameManager
class GameManager:

    def __init__(self) -> None:
        self._req_letters = ["", "", "", "", ""]  # list of letters that must be present in word (?)
        self._req_word_length = 5  # can be changed for potential gamemodes with longer/shorter words
        self._time = time.monotonic_ns() # keeping track of time (in ns to avoid floating point errors), init to current time
        self._word_rules = WordRules(self._req_word_length)
        self._gamemode = [True, False, False, False, False]
        self._indexes = []

    def set_user_word(self, word: list[str]) -> None:
        '''
        Setter method for the GUI to update the users word for this round of the
        game
        '''
        for i in range(len(self._req_letters)):
            self._req_letters[i] = word[i]

    def run_game(self):
<<<<<<< Updated upstream
        
        if self._gamemode[1]:
            return self.game_first_last_match()
        elif self._gamemode[2]:
            return self.game_random_letter_match()
        elif self._gamemode[3]:
            return self.game_no_duplicate_letters()
        elif self._gamemode[4]:
            return self.game_multi_letter_match()
        else:
            return self.game_letter_match()
=======
        fixed_indexes = ["", "", "", "", ""] # Could get rid of and change all to self._req_letters
        # If we want this to work for other word lengths the line above should be tweaked all else works I think
        valid = [0, 1, 2, 3, 4]

        if self._gamemode[1]: # fist_last match enabled
            fixed_indexes[0] = WordRules.get_prev_word()[-1]
            valid.pop(0)

        if self._gamemode[4]: # multi letter match enabled
            amount = rand.randint(2, 4)
            i = 0
            while i < amount:
                found = valid.pop(rand.randint(0, len(valid)-1))
                if self._gamemode[3] and True: # no duplicate letters      ## no dup and valid
                    if WordRules.get_prev_word()[found] not in fixed_indexes: # Would cause auto loss
                        fixed_indexes[found] = WordRules.get_prev_word()[found]
                        i += 1
                elif True: # check valid here this will need to change with Jakobs
                    fixed_indexes[found] = WordRules.get_prev_word()[found]
                    i += 1 
                else:
                    valid.append(found) # purposely do not increment loop 
                    valid.sort()
            
        if self._gamemode[0] and not self._gamemode[4]: # letter match enabled
            # Ensures letter match will not run if multi letter match is enabled
            placed = False
            while not placed:
                found = valid.pop(rand.randint(0, len(valid)-1))
                if self._gamemode[3] and True: # no duplicate letters      ## no dup and valid
                    if WordRules.get_prev_word()[found] not in fixed_indexes: # Would cause auto loss
                        fixed_indexes[found] = WordRules.get_prev_word()[found]
                        placed = True
                elif True: # check valid here this will need to change with Jakobs
                    fixed_indexes[found] = WordRules.get_prev_word()[found]
                    placed = True
                else:
                    valid.append(found) # purposely do not increment loop
                    valid.sort()

        if self._gamemode[2]: 
            letter = rand.choice("abcdefghijklmnopqrstuvwxyz")
            index = rand.randint(0, len(valid)-1)
            while index not in valid: # Valid should never be empty at this point
                index = rand.randint(0, len(valid)-1)
            #
            # Check collisions with duplicate letter
            #
            fixed_indexes[index] = letter

        # all are checked and done need to return which indexes are fixed (could instead of true false fix with letter here too and check =="")
        # Game 
>>>>>>> Stashed changes

    def toggle_gamemode(self, control: int) -> None:
        '''
        Setter method for GUI to update the control variables that determine
        which game rules should be active 
        '''
        self._gamemode[control] = not self._gamemode[control]

    
    def game_letter_match(self) -> bool:
        index = rand.randint(0, self._req_word_length-1)
        
        if self._word_rules.letter_match(self._req_letters, [index]):
            return True
        return False
        
    def game_first_last_match(self) -> bool:        
        if self._word_rules.first_last_match(self._req_letters):
            return True
        return False
        
    def game_random_letter_match(self) -> bool:
        index = rand.randint(0, self._req_word_length-1)
        letter = rand.choice("abcdefghijklmnopqrstuvwxyz")
        
        if self._word_rules.random_letter_match(self._req_letters, (index, letter)):
            return True
        return False
        
    def game_no_duplicate_letters(self) -> bool:        
        if self._word_rules.no_duplicate_letters(self._req_letters):
            return True
        return False
    
    def game_multi_letter_match(self) -> bool:
        amount = rand.randint(2, 4)
        indexes = [0,1,2,3,4]
        for i in range(amount):
            indexes.pop(rand.randint(0, len(indexes)-1))
        
        if self._word_rules.letter_match(self._req_letters, [indexes]):
            return True
        return False
        
    def is_valid(self) -> bool:
        return self._word_rules.check_word_len() and self._word_rules.contains_valid_word()


    def get_time_elapsed(self):
        return time.monotonic_ns() - self._time # count up timer
        # return (10**10) - (time.monotonic_ns() - self._time) # alt countdown timer

    def reset_time(self):
        self._time = time.monotonic_ns()
