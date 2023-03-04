'''
F01 Team 1D
Team Members:
- Sng Wei Qi Amos (1005952)
- Soh Zhi Ying (1006359)
- Edwin Wongso (1006200)
- Zaina Aafreen (1006145)
- Tan Yu Quan (1006355)
'''

import random
import turtle
import time
import timeit
import winsound 

#make font uniform for most text outputs
font_parameter = ('Arial',16,'normal')
 #initial score
score = [1000]
#no_of_cells, essentially the size of maze
size = [5]
#deduct score for every qn answered, whether correctly or wrongly
#starting coordinates
START_X = -250
START_Y = 185
#length of side
side_length = 36
#assign numbers to directions
left = 1
right = 2
up = 3
down = 4
#create a 2d grid
grid = [[]]
#create a 2d matrix to keep track of visited squares
visited_sq = [[]]
#making 3 turtles, one for the maze, one for the player character,and one for the writing text on turtle zscreen
maze = turtle.Turtle()
maze.hideturtle()
sprite = turtle.Turtle()
sprite.hideturtle()
textpen = turtle.Turtle()
textpen.hideturtle()
scorepen = turtle.Turtle()
scorepen.hideturtle()


'-----------------------------------------'
###########################################
###########################################
###########################################
# Sound Modules
###########################################
###########################################
###########################################
'-----------------------------------------'
# Music is from the Scratch Sound Files: https://scratch.mit.edu/projects/editor/?tutorial=getStarted
# Code is modified from the sample code found in:
# https://www.geeksforgeeks.org/python-winsound-module/
# https://stackoverflow.com/questions/52769618/how-can-i-play-a-sound-while-other-lines-of-code-execute-simultaneously

def sound_effect(mode):
    if mode == "win":
        winsound.PlaySound(None,winsound.SND_ASYNC)
        winsound.PlaySound('Win (Correct).wav',winsound.SND_ASYNC)
        time.sleep(3)
        sound_effect("background")
    elif mode == "lose":
        winsound.PlaySound(None,winsound.SND_ASYNC)
        winsound.PlaySound('Lose (Wrong).wav',winsound.SND_ASYNC)
        time.sleep(3)
        sound_effect("background")
    elif mode == "move":
        winsound.PlaySound(None,winsound.SND_ASYNC)
        winsound.PlaySound('Pop (Move).wav',winsound.SND_ASYNC)
        time.sleep(2)
        sound_effect("background")
    elif mode == "thanks":
        winsound.PlaySound(None,winsound.SND_ALIAS|winsound.SND_ASYNC)
        winsound.PlaySound('Triumph (Thanks).wav',winsound.SND_ALIAS|winsound.SND_ASYNC)
        time.sleep(5)
        winsound.PlaySound(None,winsound.SND_ALIAS|winsound.SND_ASYNC)
    elif mode == "background":
        winsound.PlaySound('Guitar Chords2 (Background).wav',winsound.SND_ALIAS | winsound.SND_ASYNC|winsound.SND_LOOP)


'-----------------------------------------'
###########################################
###########################################
###########################################
# math game
###########################################
###########################################
###########################################
'-----------------------------------------'
def clear_maze_and_sprite():
    maze.clear()
    sprite.clear()
def update_score_and_steps():
    scorepen.clear()
    scorepen.penup()
    scorepen.goto(300,230)    
    scorepen.write("score: "+str(score[0]),font = font_parameter)
    scorepen.penup()
    scorepen.goto(300,250)
    scorepen.pendown()
    scorepen.write("number of steps: "+str(no_of_steps[0]),font =font_parameter)

def ask_for_difficulty():
    level = turtle.textinput("","Choose a level of difficulty (1-3)")
    invalid_input = True
    while invalid_input==True:
        while level == None  or level.isnumeric()==False:
            level = turtle.textinput("","Invalid difficulty. Choose a level of difficulty (1-3)")
        while int(level)>3 or int(level)<1:
            level = turtle.textinput("","Invalid difficulty. Choose a level of difficulty (1-3)")
        if level.isnumeric() == True and 1<=int(level)<=3:
            level = int(level)
            invalid_input = False
    return level
def math_minigame(diff):
    textpen.clear()
    textpen.penup()
    textpen.goto(-300,50)    
    textpen.pendown
    textpen.write ("You have chosen Difficulty level {}.\nThere will be 2 math questions.\nYou have to answer correctly to pass this stage.\n".format(diff),font= font_parameter)
    time.sleep(3.5)
    textpen.clear()
    clear_stage=[None,None,False]
    tries = 1
    clear_stage[0] = question_generator(diff,tries) #1st Qns
    if clear_stage[0][0]:
        tries = 2
    else:
        tries = 3 # Means they get the first qns wrong
    
    clear_stage[1] = question_generator(diff,tries) #2nd Qns
    
    if clear_stage[0][0] and clear_stage[1][0]:
        return True,diff
    else:
        return False,diff
def question_generator(diff,tries):
    if tries == 3: #Means 1st Qns wrong, no point showing question
        return (False,diff)
    
    num_list = [] #Place to store num 1 to 4
    operator_list = [" + "," - "," * "] #place to store type of operators
    op = random.choice(operator_list)
    for i in range(4): #Generate num 1 to 4
        number= random.randint(1,10)
        num_list.append(number)
    
    qns_string = str(num_list[0]) + op #51 - 55 is to form the string of the qns
    for i in range(1,diff+1):
        qns_string = qns_string + str(num_list[i])
        
        if i < diff:
                qns_string = qns_string + op
                

    ans = eval(qns_string) # function to calculate the math problem that is in string format
    textpen.clear
    textpen.penup()
    textpen.goto(-300,50)
    textpen.pendown()
    textpen.write ("What is the answer?\n",font= font_parameter)
    textpen.write (qns_string ,font= font_parameter)
    
    try: 
        player_answer = turtle.textinput("Player's answer","\nWhat is your answer? ")
        player_input = float(player_answer) 
    except ValueError: #if user type in a word, it will return as a very big number and thus will get the question wrong
        #print ("Please input an integer. Here is a new question.")
        #question_generator(type,diff,tries) - You can generate a new question or just make it as a wrong answer. Up to you
        player_input = None
        
    if player_input == ans:
        if tries == 1:
            message = "Going onto the next question"
            textpen.clear()
            textpen.penup()
            textpen.goto(-300,50)
            textpen.pendown()
            textpen.write (message,font= font_parameter)
            sound_effect("win")
            textpen.clear()
            
        else:
            message = "Good Job! \nGoing back to the main page."
            textpen.clear()
            textpen.penup()
            textpen.goto(-300,50)
            textpen.pendown()
            textpen.write (message,font= font_parameter)
            sound_effect("win")
            textpen.clear()

        return (True, diff) 

    else:
        textpen.clear() # Clear Screen
        textpen.penup()
        textpen.goto(-300,0)
        textpen.pendown()
        textpen.write ("You are wrong! Try again next time.\nGoing back to the main page.",font= font_parameter)
        sound_effect("lose")

        #time.sleep(1.5) # Hold caption before showing the question again
        textpen.clear()
        return (False,diff)
def start_math_game():
    clear_maze_and_sprite()
    textpen.penup()
    textpen.goto(-100,280)
    textpen.pendown()
    textpen.write("### Math Game ^.^ ###",font = font_parameter)
    difficulty = ask_for_difficulty()
    difficulty = int(difficulty)
    return math_minigame(difficulty)

'-----------------------------------------'
###########################################
###########################################
###########################################
# geography game
###########################################
###########################################
###########################################
'-----------------------------------------'
country_dict = {'A': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan'], 'B': ['Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi'], 'C': ["Côte d'Ivoire", 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czechia'], 'D': ['Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic'], 'E': ['Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia'], 'F': ['Fiji', 'Finland', 'France'], 'G': ['Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana'], 'H': ['Haiti', 'Holy See', 'Honduras', 'Hungary'], 'I': ['Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy'], 'J': ['Jamaica', 'Japan', 'Jordan'], 'K': ['Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan'], 'L': ['Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg'], 'M': ['Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar'], 'N': ['Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway'],'O': ['Oman'], 'P': ['Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal'], 'Q': ['Qatar'], 'R': ['Romania', 'Russia', 'Rwanda'], 'S': ['Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria'], 'T': ['Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu'], 'U': ['Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan'], 'V': ['Vanuatu', 'Venezuela', 'Vietnam'], 'Y': ['Yemen'], 'Z': ['Zambia', 'Zimbabwe']}
class geographygame:
    def __init__(self):
        self.correct_answer = True
        self.pass_test = True
        self.level = 0
        self.countries_answered = 0
        self.no_countries_required = 0
        self.alphabets = []
        self.country_list = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',"Côte d'Ivoire",'Cabo Verde','Cambodia','Cameroon','Canada','Central African Republic','Chad','Chile','China','Colombia','Comoros','Congo','Costa Rica','Croatia','Cuba','Cyprus','Czechia','Democratic Republic of the Congo','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Eswatini','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Holy See','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States of America','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']

    def game_intro(self):
        textpen.clear()
        textpen.penup()
        textpen.goto(-260,0)
        textpen.pendown()
        textpen.write("______________________________________________\nWelcome to the Geography Game \nThis is where your knowledge about countries will be tested\n______________________________________________\nPress Enter to continue...",font= ('Arial',16,'normal'))   
        turtle.textinput("Press Enter", "Press Enter to continue")

    def control(self):
        self.set_difficulty()
        self.get_alphabets()
        self.game_intro()
        self.maingame()
        return self.pass_test,self.level

    def set_difficulty(self):
        self.no_countries_required = self.level*2 + 3

    def get_alphabets(self):
        alphabet_list = []
        for keys in country_dict.keys():
            alphabet_list += [keys]
        for i in range(5):
            letter = random.choice(alphabet_list)
            self.alphabets += [letter]
            alphabet_list.remove(letter)
        return self.alphabets

    def eliminate_country(self,player_input):
        if player_input == None:
            return False
        elif player_input.isalpha() == False:
            return False
        country_uppered = player_input.capitalize()
        if country_uppered in self.country_list:
            self.country_list.remove(country_uppered)
            return True
        else:
            return False

    def maingame(self):
        self.display_board()
        while self.countries_answered<self.no_countries_required and self.pass_test == True:
            country = self.ask_player()
            if country == "I give up":
                self.pass_test = False
                break
            if self.eliminate_country(country) == True:
                self.correct_answer = True
                self.countries_answered +=1
                self.display_board()
            elif self.eliminate_country(country) == False:
                self.correct_answer = False
        if self.pass_test == True:
            return self.display_passed()
        else:
            return self.display_fail()    
    def display_alphabet(self):
        textpen.penup()
        textpen.goto(-300,0)
        textpen.pendown()
        textpen.write("{}   {}   {}   {}   {}".format(self.alphabets[0],self.alphabets[1],self.alphabets[2],self.alphabets[3],self.alphabets[4]),font= ('Arial',30,'bold'))
        
    def ask_player(self):
        if self.correct_answer ==True:
            player_input = turtle.textinput("Name a country","Press Enter after every country to check")
            return player_input
        else:
            player_input = turtle.textinput("Name a country","Incorrect, try again\nPress Enter after every country to check\nType 'I give up' if you want to give up")
            return player_input
    def display_board(self):
        textpen.clear()
        textpen.penup()
        remainding_count = self.no_countries_required-self.countries_answered
        textpen.setpos(-300,200)
        textpen.write("Name {} countries with names beginning with:".format(remainding_count,),font= ('Arial',16,'normal'))
        self.display_alphabet()
    def display_passed(self):
        textpen.clear()
        textpen.write("Congratulations! You have passed!",font= ('Arial',16,'normal'))
        sound_effect("win")
        textpen.clear()
        turtle.textinput(None,"Press Enter to continue...")
    def display_fail(self):
        textpen.clear()
        textpen.write("Too bad! You have failed!",font= ('Arial',16,'normal'))
        sound_effect("lose")
        textpen.clear()
        turtle.textinput("Good luck next time","Press Enter to continue...")
    def start_geo_game(self):
        clear_maze_and_sprite()
        textpen.penup()
        textpen.goto(-100,280)
        textpen.write("### Geography Game ^.^ ###",font = font_parameter)
        self.level = ask_for_difficulty()
        return self.control()
'-----------------------------------------'
###########################################
###########################################
###########################################
#typing game
###########################################
###########################################
###########################################
'-----------------------------------------'
sentence_bank = ['navigation', 'Ometo', 'Eve', 'endogenous', 'biota', 'fleshy', 'Bura Group 2 Cluster', 'Nepal-Tharu cluster', 'Republic of Ireland', 'Aiome', 'newton', 'adjustment','Corsu-C Spoken', 'Guernica', 'composer', 'streaming media', 'tree ear', 'Cao Lan', 'Mister', 'Jbel-Bani', 'Lorang', 'terminal', "Ge'ez alphabet", 'water protection', 'Ukrainska-SW', 'skipper', 'Kayapa Kallahan', 'mesa', 'team', 'filament', 'elderberry juice', 'horizontal', 'Tuat Spoken', 'Takua', 'pamphlet', 'crankcase', 'graphite', 'fleet', 'Chiroro- Kursi', 'Daur Spoken', 'astral', 'pinkish', 'computer-assisted translation', 'larger than life', 'envious', 'common vampire bat', 'South Kerela', 'interstitial fluid', 'carbonic acid gas', 'Jeiani', 'betterment', "Kajire-'Dulo", 'French Guiana', 'Vise-grips', 'door frame', 'revegetation', 'clothes-peg', 'wood pulp', 'entomologist', 'anoretic', 'Babango', 'dependent', 'incestuous', 'sexology', 'Gbati-ri', 'endemism', 'Oban-Lorn', 'scorzonera', 'Talasa', 'expansionist', 'Jaipur', 'understudy', 'Barei', 'raft', 'vulcanological', 'accreditation', 'Chicano Spoken', 'station bookstall', 'dermatologist', 'tourist', 'Cibemba', "Pa'o Karen", 'epoch', 'type', 'Mawasi', 'lavish', 'xenobiotic', 'yottagram', 'blank out', 'Arctic Circle', 'cynophobia', 'waistcoat', 'IVF', 'quality', 'Pan-Arabic', 'Cree', 'Vallage', 'Guba Spoken', 'Wello Spoken', 'causal adverb', 'truce', 'Bitolia', 'Northern Ohlone', 'post-industrial', 'M-Baram', 'Kalimantan', 'Cisalpine Celtic', 'endophyte', 'gnotobiont', 'Bognak Spoken', 'Doi Spoken', 'polyglot', 'bromance', 'Skolt Sami', 'candlestick', 'reflectometry', 'selfie', 'English', 'hazardous', 'river blindness', 'crucifixion', 'juridical', 'Tocharian A (Latin script)', 'Amazonian', 'Antiguan Creole', 'refinement', 'unhindered birth', 'alarm clock', 'at first go', 'VoIP', 'fetid', 'earth leakage circuit breaker', 'paint shop', 'exhort', 'handicapped', 'dysphemistic', 'Kambaata Spoken', 'referral', 'Bauzi', 'corn lice', 'Bissa', 'Mal Paharia Written', 'congruence', 'antisocial', 'liquid petroleum', 'Italiano-G', 'barf bag', 'sociological', 'SQLite', 'norovirus', 'Ames test', 'Molise', 'irremediably', 'unrecorded', 'news', 'cry out', 'Onna-N', 'marrying-out', 'intermammary cleft', 'Maslam- Sao', 'already', 'ern', 'Nongtung', 'Great Andamanese', 'zero balance account', 'hcf', 'pashmina scarf', 'crusade', 'multilocation', 'sad', 'Mintil', 'Parkwa', 'Central Kurdish', 'Singli', 'Criollo-De-Bobures', 'so long', 'coachwork', 'counter-culture', 'stupa', 'unexhaustible', 'bottleneck', 'counterpoison', 'Terres-Froides', 'cello', 'Bongili', 'Beludj', 'podiatry', 'Manche', 'permissible exposure limit', 'twenty-cent piece', 'Badrian', 'miserliness', 'Remontado Agta', 'firefighter', 'crane', 'settling tank', 'Kovee-N-Tsho-Ri']
class typinggame:
    def __init__(self):
        self.playername = "" #set player name for scoreboard
        self.time = 0 #base timer 
        self.level = 5 #update with level selected
        self.cont = True #contidition for continuing to the next sentence
        self.sentence = ""
        self.required_sentence = 0
        self.remainding_sentence = 0
        self.timeleft = 0
        self.sentence_bank = []
        self.completed_sentences =[]
        self.pass_test = False 
    def ask_user_for_level(self):
        self.level = turtle.textinput("","Choose a level of difficulty (1-3)")
        invalid_input = True
        while invalid_input==True:
            while self.level.isnumeric()==False:
                self.level = turtle.textinput("","Invalid difficulty. Choose a level of difficulty (1-3)")
            while int(self.level)>3 or int(self.level)<1:
                self.level = turtle.textinput("","Invalid difficulty. Choose a level of difficulty (1-3)")
            if self.level.isnumeric() == True and 1<=int(self.level)<=3:
                self.level = int(self.level)
                invalid_input = False
            
    def reset_canvas(self,x,y):
        textpen.clear()
        textpen.ht()
        textpen.penup() 
        textpen.setpos(x,y)   
    def start_typing_game(self):
        clear_maze_and_sprite()
        self.game_instructions()
        self.ask_user_for_level()
        self.select_level()
        self.timetostart()
        self.maingame()
        textpen.clear()
        return self.pass_test,self.level
    def game_instructions(self):
        textpen.clear()
        textpen.ht()
        textpen.penup()
        textpen.setpos(-260,0)
        textpen.write("___________________________________________\nWelcome to the typing game \nThis is where your typing speed is put to the test \nYou will be allowed to choose 3 levels \nLevel 1: 60 seconds 2 sentences\nLevel 2: 30 seconds 2 sentences \nLevel 3: 20 seconds 3 sentences \n___________________________________________",font= ('Arial',16,'normal'))  
        time.sleep(3) 
        turtle.textinput("Press Enter", "Press Enter to continue")
    def timetostart(self): #3 sec countdown to game starting
        ready = turtle.textinput("Player ready", "Are You Ready?\n(y/n)")
        if ready == 'y':
            self.reset_canvas(-260,120)
            textpen.write("___________________________________________\nGame starts in\n___________________________________________",font= ('Arial',16,'normal'))
            time.sleep(1.5)
            self.reset_canvas(-260,120)
            textpen.write("___________________________________________\n\n___________________________________________",font= ('Arial',16,'normal'))
            textpen.setpos(-25,-25)
            textpen.write("3",font= ('Arial',50,'bold'))
            time.sleep(0.8)
            self.reset_canvas(-260,120)
            textpen.write("___________________________________________\n\n___________________________________________",font= ('Arial',16,'normal'))
            textpen.setpos(-25,-25)
            textpen.write("2",font= ('Arial',50,'bold'))
            time.sleep(0.8)
            self.reset_canvas(-260,120)
            textpen.write("___________________________________________\n\n___________________________________________",font= ('Arial',16,'normal'))
            textpen.setpos(-25,-25)
            textpen.write("1",font= ('Arial',50,'bold'))
            time.sleep(0.8)
        else:
            turtle.textinput("Player not ready","Press enter when ready")
            return self.timetostart()
    def get_sentence(self): # loads a sentence from sentence bank
        sentence = ""
        while len(sentence)<20:
            word = random.choice(sentence_bank) + " "
            sentence += word
        sentence = sentence[:-1]
        self.sentence = sentence
    def select_level(self): # select level of difficulty
        level = self.level
        if level == 1 or level ==2:
            self.required_sentence = 2
        elif level ==3:
            self.required_sentence = 3
        level_time = (1/level)*60
        self.time = level_time
        self.reset_canvas(-260,120)
        textpen.write("___________________________________________\nYou have selected Level {}\n___________________________________________".format(self.level),font= ('Arial',16,'normal'))
        time.sleep(1.5)
        self.reset_canvas(-260,120)
        textpen.write('___________________________________________\nYou have {} seconds to type {} sentences\n___________________________________________'.format(level_time,self.required_sentence),font= ('Arial',16,'normal'))
        time.sleep(3)
        self.reset_canvas(-260,120)
        textpen.write('___________________________________________\nThe sentences will appear between these 2 lines\n___________________________________________',font= ('Arial',16,'normal'))
        time.sleep(3)
    def display_sentence(self):
        self.reset_canvas(-260,120)
        textpen.write('___________________________________________\n{}\n___________________________________________'.format(self.sentence),font= ('Arial',16,'normal'))
    def maingame(self): #main function of game
        self.pass_test = False
        no_completed_sentences = 0
        completed_sentences = []
        required_sentences = self.required_sentence
        time_left = (1/self.level)*60
        switch_sentence = True
        self.timeleft = time_left
        self.game_mechanics(no_completed_sentences,completed_sentences,required_sentences,time_left,switch_sentence)
    def game_mechanics(self,no_completed_sentences,completed_sentences,required_sentences,time_left,switch_sentence):
        while time_left>0:
            if switch_sentence == True:
                self.get_sentence()
            else:
                pass
            self.display_sentence()
            self.display_info(time_left,no_completed_sentences)
            starttime = timeit.default_timer()
            if switch_sentence == True:
                user_input = turtle.textinput("Copy the sentence",None)
            elif switch_sentence == False:
                user_input = turtle.textinput("Copy the sentence","Incorrect try again")
            if user_input == self.sentence:
                endtime = timeit.default_timer()
                time_taken = endtime-starttime
                time_left -=time_taken
                no_completed_sentences +=1
                switch_sentence = True
                remainding_sentences = required_sentences- no_completed_sentences
                self.timeleft = time_left
                completed_sentences += [self.sentence]
                if remainding_sentences ==0 and time_left>0:
                    self.completed_sentences = completed_sentences
                    self.pass_test = True
                    self.display_pass()
                    return self.get_player_stats()
                else:
                    return self.game_mechanics(no_completed_sentences,completed_sentences,required_sentences,time_left,switch_sentence)                   
            else: 
                switch_sentence =False
                endtime = timeit.default_timer()
                time_taken = endtime-starttime
                time_left -=time_taken
                if time_left >=0:
                    return self.game_mechanics(no_completed_sentences,completed_sentences,required_sentences,time_left,switch_sentence)
                else:
                    break
        return self.display_fail() 
    def get_player_stats(self):
        time_remainding = self.timeleft
        level = self.level
        completed_sentences = self.completed_sentences
        words = []
        wordslst = []
        no_chars = 0
        for i in completed_sentences:
            word = i.split(" ") 
            words += [word]
        for i in words:
            wordslst += i
        no_words = len(wordslst)
        for i in wordslst:
            no_char = len(i)
            no_chars += no_char
        see_data = turtle.textinput(None,"Do you want to see your WPM and CPM?\n(y/n)")
        if see_data == "y":
            wpm  =round(no_words/((1/level)*60 - time_remainding)*60,1)
            cpm  =round(no_chars/((1/level)*60 - time_remainding)*60,1)
            self.reset_canvas(-260,120)
            textpen.write("Words per Minute: {}\nCharacters per Minute: {}".format(wpm,cpm),font= ('Arial',16,'normal'))
            turtle.textinput(None,"Press Enter to continue")
            return 
        elif see_data =="n":
            return True
        else:
            turtle.textinput(None,"Please choose only y/n\nPress Enter to try again")
            typinggame.get_player_stats(self)
    def display_info(self,timeleft,no_completed_sen):
        textpen.setpos(70,-120)
        textpen.write("Time left: {}\nSentence Completed: {}".format(round(timeleft,1),no_completed_sen),font= ('Arial',16,'normal'))
    def display_pass(self):
        time_left = self.timeleft
        level = self.level
        self.reset_canvas(-175,0)
        textpen.write("Congratulations! You have passed!\nYou took {} seconds".format(round((1/level)*60 - time_left),1),font= ('Arial',16,'normal'))
        sound_effect("win")
    def display_fail(self):
        self.reset_canvas(-175,0)
        textpen.write("Times Up!\nYou took more than {} seconds".format(self.time),font= ('Arial',16,'normal'))
        turtle.textinput("Good luck next time","Press Enter to continue...")
        sound_effect("lose")

'-----------------------------------------'
###########################################
###########################################
###########################################
#number_pattern
###########################################
###########################################
###########################################
'-----------------------------------------'
no_of_steps = [0] #use a single-element list because we will alter no_of_steps throughout the duration of the game, lists are far 
#easier to change compared to global variables in python
# # Link (for geo_seq, arithmetric_seq and f_seq):
# https://www.geeksforgeeks.org/what-are-the-4-types-of-sequences/#:~:text=Four%20types%20of%20Sequence,Harmonic%20Sequence%2C%20and%20Fibonacci%20Sequence.
def geo_seq():
    n=5
    common_ratio = random.randint(2,12)
    a = random.randint(1,5)
    correct_ans = []

    for i in range(n):
        number_generated = a*(common_ratio**((i+1)-1))
        correct_ans.append(number_generated)
    
    if correct_ans[1] == correct_ans[0] and correct_ans[1]==correct_ans[2]: #To prevent number pattern with all same no
        geo_seq()
    
    qns_w_blank = correct_ans.copy()
    qns_w_blank[4] = "_______"
    return correct_ans, qns_w_blank

def arithmetic_seq():
    n=5 
    common_diff = random.randint(2,20)
    diff_sign = -1**(random.randint(1,2))
    a = random.randint(1,20)
    correct_ans = []

    for i in range(n):
        number_generated = a+((i+1)*common_diff*diff_sign)
        correct_ans.append(number_generated)
    
    if correct_ans[1] == correct_ans[0] and correct_ans[1]==correct_ans[2]:
        arithmetic_seq()

    qns_w_blank = correct_ans.copy()
    qns_w_blank[4] = "_______"
    return correct_ans, qns_w_blank

def f_seq():
    
   n=5 
   correct_ans = []
   num_1 = random.randint(0,20)
   num_2 = random.randint(num_1+3,num_1*2)
   correct_ans.append(num_1)
   correct_ans.append(num_2)
   
   for i in range(2,n):
        number_generated = correct_ans[i-2]+correct_ans[i-1]
        correct_ans.append(number_generated)
    
   if correct_ans[1] == correct_ans[0] and correct_ans[1]==correct_ans[2]:
        f_seq()
    
   qns_w_blank = correct_ans.copy()
   qns_w_blank[4] = "_______"
   return correct_ans, qns_w_blank 

def tri_num():
    #Link: https://en.wikipedia.org/wiki/Triangular_number
    n=5 
    a = random.randint(1,20)
    correct_ans = []

    for i in range(a,a+5):
        number_generated = (i*(i-1))/2
        correct_ans.append(number_generated)
    
    if correct_ans[1] == correct_ans[0] and correct_ans[1]==correct_ans[2]:
        tri_num()
    qns_w_blank = correct_ans.copy()
    qns_w_blank[4] = "_______"
    return correct_ans, qns_w_blank

def figurate_num(): 
    #Link: http://oeis.org/wiki/Figurate_numbers
    n=5
    sides = random.randint(5,7) #Penta-, Hexa- or Heptagonal Figurate Number
    a = random.randint(0,5)
    correct_ans = []

    if sides ==5:
        for i in range(a,a+5): 
            number_generated = (3*(i**2)-i)/2
            number_generated = int(number_generated)
            correct_ans.append(number_generated)
    
    elif sides ==6:
        for i in range(a,a+5): 
            number_generated = 2*(i**2) - i
            number_generated = int(number_generated)
            correct_ans.append(number_generated)
    
    else:
        for i in range(a,a+5): 
            number_generated = (5*(i**2)-(3*i))/2
            number_generated = int(number_generated)
            correct_ans.append(number_generated)

    
    if correct_ans[1] == correct_ans[0] and correct_ans[1]==correct_ans[2]:
        figurate_num()

    qns_w_blank = correct_ans.copy()
    qns_w_blank[4] = "_______"
    return correct_ans, qns_w_blank

def setup(x,y):
    textpen.penup()
    textpen.goto(x,y)
    textpen.pendown()
def pattern_minigame(difficulty):
    level = int(difficulty)
    chance_list = [3,2,1] #No of chances for beginner, intermmediate and advanced
    chance = chance_list[level-1] 
    pass_level = False

    if level == 1: # Beginner 
       eqn_type = random.randint(0,1)
       if eqn_type == 0:
            qns_ans = geo_seq() #Geometric Progression
       else:
            qns_ans = arithmetic_seq() #Arithmetric Progression
    elif level == 2:  #Intermmediate
       eqn_type = random.randint(0,1)
       if eqn_type ==0:
           qns_ans = f_seq()
       else:
           qns_ans = tri_num()
    else: 
        qns_ans = figurate_num()

    while (chance > 0 and pass_level == False):
        qns_paper = qns_ans[1].copy()
        qns_string = ""
        setup(-300,150)
        for element in qns_paper: #Generate string from list for turtle.write
            qns_string = qns_string + str(element) + " "
        textpen.write ("Level:{}\nChance: {}\nFill up the missing number:\n".format(level,chance),font= font_parameter )
        textpen.write (qns_string ,font= font_parameter)
        user_answer = None
        while user_answer==None:
            user_answer = turtle.textinput("Let's see if you are right...","\nWhat is your answer? ") #User's answer
        try:
            qns_paper[4] = int(user_answer)
        except: 
            setup(-300,50)
            textpen.write("Invalid input. Integer only!",font= font_parameter)
            time.sleep(0.8)
            textpen.clear()
            qns_paper[4] = None
        if (qns_paper==qns_ans[0]):
            textpen.clear()
            setup(-150,0)
            textpen.write ("You are correct!",font= font_parameter)
            sound_effect("win")
            textpen.clear()
            pass_level = True
        else:
            chance -= 1
            setup(-300,0)
            textpen.clear()
            textpen.write ("You are wrong! {} chance(s) left!".format(chance),font= font_parameter)
            sound_effect("lose") # Play the sound and act as hold
            textpen.clear()
    return pass_level
#call this function to start the number pattern game
def start_number_pattern(): 
    clear_maze_and_sprite()
    setup(-100,280)
    textpen.write("### Number Sequence Game ^.^ ###",font = font_parameter)
    difficulty =ask_for_difficulty()
    passed = pattern_minigame(difficulty)
    difficulty = int(difficulty)
    if passed == True:
        return (True,difficulty)
    else:
        return (False,difficulty)
###########################################
##########################################
###########################################
#Maze control
###########################################
###########################################
###########################################

screen = turtle.Screen()
screen.screensize(800, 800)
screen = turtle.Screen()
screen.screensize(800, 800)
class Maze_control:
    # we initialize the Square object by setting all the walls to be closed
    def __init__(self, center_coord):
        self.center = center_coord
        self.leftwall = True
        self.rightwall = True
        self.downwall = True
        self.upwall = True
    def draw_walls(self):
        maze.penup()
        maze.pensize(8)
        maze.goto(self.center[0] - 0.5 * side_length, self.center[1] + 0.5 * side_length)
        if self.upwall == True:  # if the wall is closed, we use pendown( to draw it, else we leavee penup
            maze.pendown()
        maze.forward(side_length)
        maze.right(90)
        maze.penup()
        if self.rightwall == True:
            maze.pendown()
        maze.forward(side_length)
        maze.right(90)
        maze.penup()
        if self.downwall == True:
            maze.pendown()
        maze.forward(side_length)
        maze.right(90)
        maze.penup()
        if self.leftwall == True:
            maze.pendown()
        maze.forward(side_length)
        maze.right(90)
        maze.penup()
    def refill_possible_choices(self,row, col):
        choices = [up, down, left, right]
        if row == size[0] or visited_sq[row+1][col] == 1:
            choices.remove(down)
        if row == 0 or visited_sq[row-1][col] == 1:
            choices.remove(up)
        if col == 0 or visited_sq[row][col-1] == 1:
            choices.remove(left)
        if col == size[0] or visited_sq[row][col+1] == 1:
            choices.remove(right)
        return choices
    def find_initial_cell(self):
        for row in range(size[0]+1):
            for col in range(size[0]+1):
                if visited_sq[row][col] == 0:
                    if col > 0 or row > 0:
                        choices_of_last_visited = self.refill_last_visited_choices(row, col)
                        previous_square = random.choice(choices_of_last_visited)
                        if previous_square == up:
                            grid[row][col].upwall = False
                            grid[row-1][col].downwall = False
                        if previous_square == right:
                            grid[row][col].rightwall = False
                            grid[row][col+1].leftwall = False
                        if previous_square == down:
                            grid[row][col].downwall = False
                            grid[row+1][col].upwall = False
                        if previous_square == left:
                            grid[row][col].leftwall = False
                            grid[row][col-1].rightwall = False
                    self.find_adjacent(row, col)
    def find_adjacent(self,row, col):   
        visited_sq[row][col] = 1
        choices = self.refill_possible_choices(row, col)
        if len(choices) == 0:
            return None
        #choose a random direction
        direction = random.choice(choices)
        if direction == left:
            grid[row][col].leftwall = False
            grid[row][col-1].rightwall = False
            return self.find_adjacent(row, col-1)
        if direction == right:
            grid[row][col].rightwall = False
            grid[row][col+1].leftwall = False
            return self.find_adjacent(row, col+1)
        if direction == up:
            grid[row][col].upwall = False
            grid[row-1][col].downwall = False
            return self.find_adjacent(row-1, col)
        if direction == down:
            grid[row][col].downwall = False
            grid[row+1][col].upwall = False
            return self.find_adjacent(row+1, col)
        return None
    def refill_last_visited_choices(self,row, col):
        choices = [up, right, down, left]
        if row == 0 or visited_sq[row-1][col] == 0:
            choices.remove(up)
        if row == size or visited_sq[row+1][col] == 0:
            choices.remove(down)
        if col == 0 or visited_sq[row][col-1] == 0:
            choices.remove(left)
        if col == size or visited_sq[row][col+1] == 0:
            choices.remove(right)
        return choices
    def redraw_maze(self):
        for row in range(size[0]+1):
            for col in range(size[0]+1):
                grid[row][col].draw_walls()
class Sprite:
    def __init__(self, center_coord, p_row, p_col):
        self.sprite_length = 0.5*side_length 
        self.row = p_row
        self.col = p_col
        self.center = grid[p_row][p_col].center
    def draw_sprite(self):
        sprite.clear()
        sprite.penup()
        sprite.pencolor("red")
        sprite.pensize(5)
        sprite.goto(self.center[0]-0.5*self.sprite_length, self.center[1]+0.5*self.sprite_length)
        for count in range(4):
            sprite.pendown()
            sprite.forward(self.sprite_length)
            sprite.right(90)
        sprite.penup()
    def up_possible(self):
        if grid[self.row][self.col].upwall == False:
            return True
        return False
    def left_possible(self):
        if grid[self.row][self.col].leftwall == False:
            return True
        return False
    def down_possible(self):
        if grid[self.row][self.col].downwall == False:
            return True
        return False
    def right_possible(self):
        if grid[self.row][self.col].rightwall == False:
            return True
        return False
    def moveup(self):
        self.row -= 1
        self.center = grid[self.row][self.col].center
    def moveleft(self):
        self.col -= 1
        self.center = grid[self.row][self.col].center
    def movedown(self):
        self.row += 1
        self.center = grid[self.row][self.col].center
    def moveright(self):
        self.col += 1
        self.center = grid[self.row][self.col].center
    def follow_instructions(self,instructions):
        original_row = self.row
        original_col = self.col
        for i in range(len(instructions)):
            if instructions[i] == 'u':
                if self.up_possible() == False:
                    textpen.clear()
                    self.row = original_row
                    self.col = original_col
                    return False
                self.moveup()
            elif instructions[i] == 'd':
                if self.down_possible() == False:
                    textpen.clear()
                    self.row = original_row
                    self.col = original_col
                    return False
                self.movedown()
            elif instructions[i] == 'r':
                if self.right_possible() == False:
                    textpen.clear()
                    self.row = original_row
                    self.col = original_col
                    return False
                self.moveright()
            elif instructions[i] == 'l':
                if self.left_possible() == False:
                    textpen.clear()
                    self.row = original_row
                    self.col = original_col
                    return False
                self.moveleft()
        self.draw_sprite()
        return True
cur_x = START_X
cur_y = START_Y
for row in range(size[0]+4):
    sound_effect("background")
    grid.append(list())
    visited_sq.append(list())
    if row > 0:
        cur_y -= side_length
    cur_x = START_X
    for col in range(size[0]+4):
        visited_sq[row].append(0)
        cur_x += side_length
        center_of_current_square = (cur_x, cur_y)
        current_square_object = Maze_control(center_of_current_square)
        grid[row].append(current_square_object)
        if row>size[0] or col>size[0]:
            grid[row][col].upwall = False
            grid[row][col].rightwall = False
            grid[row][col].downwall = False
            grid[row][col].leftwall = False
maze_methods = Maze_control((0,0)) #this variable was created for the sole purpose of accessing Maze_control class methods
maze_methods.refill_possible_choices(0, 0)
maze_methods.find_initial_cell()
#randomise the location of the entrance and exit of the maze
grid[0][0].leftwall = False
grid[size[0]][size[0]].rightwall = False
player_start_point = (grid[0][0].center[0]-0.1*side_length, grid[0][0].center[1])
player = Sprite(player_start_point, 0, 0)
update_score_and_steps()
turtle.setup(width=1.0,height=1.0)
turtle.textinput("","We suggest that you enable fullscreen, to be able to see the whole maze and any text that appears.\nPress enter to continue")
turtle.textinput("","in this game, you have to answer questions\nto gain steps to get through the maze.\nYou currently have 0 steps, so answer this next question to gain steps\nthe number of steps gained is equal to the difficulty you choose for each question.\nPress enter to continue")
turtle.textinput("","Whenever you answer a question, your score displayed on the top right decreases,\nregardless of whether you answered the question correctly. \nThe harder the question answered, the lower the deduction in score.\nPress enter to start your first minigame!")
turtle.textinput("","Maximise your score.\nPress enter to continue")
textpen.clear()
#this loop keeps running while the player is in the maze, and hasn't completed
while player.col < size[0]+1: 
    screen.tracer(0)
    player.draw_sprite()
    maze_methods.redraw_maze()
    screen.update()
    time.sleep(3)
    #initialise correct_ans and difficulty
    correct_ans,difficulty = False, 0
    current_game = random.randint(0,3)
    if current_game == 0:
        game = typinggame()
        correct_ans, difficulty = game.start_typing_game()
    elif current_game == 1:
        game = start_number_pattern()
        correct_ans, difficulty = game
    elif current_game == 2:
        game = start_math_game()
        correct_ans, difficulty = game
    else:
        game = geographygame()
        correct_ans, difficulty = game.start_geo_game()
    if correct_ans==True:
        no_of_steps[0] += difficulty
    else:
        turtle.textinput("","It's ok if you failed the last question, We have another question for you to try!\nPress enter to continue")
        continue
    score[0] -= (30/difficulty)
    score[0] = round(score[0],0)
    update_score_and_steps()
    maze_methods.redraw_maze()
    player.draw_sprite()
    prompt= "Type the directions you want to go (u/r/d/l). You can only type "+str(no_of_steps[0])+" directions.\nExample: ""urr"" means up, right, right.\nThe red square will follow these directions only if you answer the next question correctly!"
    instructions = turtle.textinput("",prompt)
    valid_instructions = False
    while valid_instructions == False:
        char_counter = 0
        if instructions != None:
            instructions.strip()
        if len(instructions)!=no_of_steps[0]:
            instructions = turtle.textinput("","invalid input, you can only type "+str(no_of_steps[0])+" directions of the type (u/r/d/l)")
            continue
        for i in range(len(instructions)):
            if instructions[i]!='u' and instructions[i]!='d' and instructions[i]!='r' and instructions[i]!='l':
                break
            char_counter+=1
        if char_counter == len(instructions):
            valid_instructions = player.follow_instructions(instructions)
        if valid_instructions == False:
            instructions =  turtle.textinput("","invalid input, Your player ran into a wall.")
            continue
    if valid_instructions == True:
        no_of_steps[0] = 0 #reset no_of_steps[0] to 0 after player is moved
    update_score_and_steps()
    textpen.clear()
    screen.tracer(0)
    maze_methods.redraw_maze()
    player.draw_sprite()
    sound_effect("move")
    screen.update()
time.sleep(1.5)
clear_maze_and_sprite()
prompt = "Good job on finishing the quiz with " + str(score[0]) + " points!\nHope you enjoyed our game!"
sound_effect("thanks")
turtle.textinput("",prompt)
turtle.clearscreen()
turtle.write("Click anywhere to exit ... ",font = font_parameter)
turtle.exitonclick()