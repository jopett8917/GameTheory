def definePlayer(player, id):
    
    # Pseudo-definitions
    opponent_history = []
    history = []
    score = []
    opponent_score = []
    getting_team_name = True
    
    #if statement from Prisoner's Dilemma Code
    if player != id:
        return 'INVALID SELECTION'
#=======================================================
    elif player == id: #Copy code from here down
        if getting_team_name:
            return 'skynet'
        else:
            # set Nice/Mean
            NICE = False
            
            # if opponent is safe for first round
            if len(opponent_history) == 0:
                if NICE == True: # If the opponent's personality is nice, collude @ t=0
                    return 'c'
                else:
                    return 'b'
            else:
                if opponent_history[len(opponent_history) - 1] == history[len(history) - 1]: # if both you and opponent give the same answer last round, continue pattern
                    return opponent_history[len(opponent_history) - 1]
                else:
                    if (opponent_history[len(opponent_history) - 1] == 'b') and (history[len(history) - 1] == 'c'): # Screw them
                        return 'b'
                    else: #use the Nice/Mean test
                        if NICE == True:
                            return 'c'
                        else:
                            return 'b'
            
                #FAILSAFE FOR LOSS
                #history[len(history) - 1] = 'c'
                
                #if opponent_score >= score:
                    #opponent_score[len(history)] = (score[len(history)] - 100)