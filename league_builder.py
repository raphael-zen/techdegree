# note : I am try to get an "Exceeds Expectations" grade as I managed to complete the bonus task

import csv
import random

if __name__ == '__main__':
    
    dragons = []
    sharks = []
    raptors = []
    final_full_list = []
    
    # function below will randomly allocate players in 3 lists until the list is emptied 
    # we will use it to create 3 random lists of experienced and non experienced players
    # lists can be uneven but in our case study it is fine as 18%3 == 0
    
    
    def random_split_in_3(list): 
        list1 =[]
        list2 =[]
        list3 =[]
    
        while len(list) > 0: 
            
            try:
                list1_ran = random.randint(0,len(list)-1)
                list1 += [list.pop(list1_ran)]
                
                list2_ran = random.randint(0,len(list)-1)
                list2 += [list.pop(list2_ran)]
                
                list3_ran = random.randint(0,len(list)-1)
                list3 += [list.pop(list3_ran)]
                
            except ValueError:
                print("number of players cannot be divided by 3.. uneven teams!")
    
        return(list1, list2, list3)
    
    # csv data is read and players are allocated in 2 different lists : experienced and not
    
    with open('soccer_players.csv', 'r') as players_csv:
        players_list = csv.DictReader(players_csv)
        
        exp_players = []
        noexp_players = []
    
        
        for row in players_list:            
            if row['Soccer Experience'] == 'YES':
                exp_players.append(list(row.values()))
            else:
                noexp_players.append(list(row.values()))
                
    # now let's allocate the randomly split experienced and non exp players
    
    experienced_split_3 = random_split_in_3(exp_players)
    noexperienced_split_3 = random_split_in_3(noexp_players)
    
    dragons.extend(experienced_split_3[0])
    sharks.extend(experienced_split_3[1])
    raptors.extend(experienced_split_3[2])
    
    dragons.extend(noexperienced_split_3[0])
    sharks.extend(noexperienced_split_3[1])
    raptors.extend(noexperienced_split_3[2])

     # let's output our results in a txt file   
     # but first let's create a final full list including the team name for each player 
     # it will be useful for both the teams.txt and the welcome letters
    
    def adding_team_names(team_list, team_name):
        for player in team_list:
            player.append(team_name)
            
    adding_team_names(dragons, "Dragons")
    adding_team_names(sharks, "Sharks")
    adding_team_names(raptors, "Raptors")

    final_full_list += dragons + sharks + raptors

    # now let's create the teams.txt file
    
    teams = open("teams.txt", "w")
    
    
    def writing_txt_teams(team_list, file):
        temp_team = team_list[0][4]

        with open(file, "a") as f: 
            f.write(temp_team+"\n")
            for player in team_list: 
                if temp_team != player[4]:
                    f.write("\n\n"+player[4]+"\n")
                    temp_team = player[4]
                    
                f.write(", ".join(player[0:4])+"\n")
             
        f.close()
    
    # appending the txt file with each team
    
    writing_txt_teams(dragons, "teams.txt")
    writing_txt_teams(sharks, "teams.txt")
    writing_txt_teams(raptors,"teams.txt")
        
 
    
    # now let's use the final full list to conveniently write the welcome letters
    
    def welcome_letter(players_full_list):
        for player in players_full_list:
            letter = open(str(player[0]).replace(" ", "_").lower() +".txt","w")
            letter.write(f"Dear {player[3]},\n\nI have the pleasure to let you know that {player[0]} has been (randomly) allocated to team {player[4]}.\nThe first practice will be on Sunday 9th September.\n\nSee you there!\n\nBest,\nMister League Builder.")
            
    welcome_letter(final_full_list)
    
    # and voila ! 
