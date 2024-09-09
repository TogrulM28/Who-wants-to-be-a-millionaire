import tkinter as tk
import random
import pygame
import json
import os

login = tk.Tk()
login.title("Login")
login.geometry('550x750')
login.config(bg='#000044')
login.attributes('-fullscreen',True)
login.resizable(False,False)
                

image = tk.PhotoImage(file='lesson 20/millionaire.png')
image_lbl = tk.Label(bg="#000044",image=image)
image_lbl.pack()

class Username:
    def __init__(self, name, score=[]):
        self.name = name
        self.score = score

def start():
    user = username_entry.get()
    user1 = Username(user,score=[])
    if username_entry.get() == '' or len(username_entry.get())==2:
        login_result.config(text='Username invalid!!!',fg='white')
    else:
        try:
            with open(f"lesson 20/users/{user}.json","r") as player:
                login.destroy()
                millionaire = tk.Tk()
                millionaire.title("Who wants to be a millionaire?")
                millionaire.config(bg='black')
                millionaire.attributes('-fullscreen',True)
                millionaire.resizable(False,False)
                
                data = json.load(player)
                
                




                user_lbl = tk.Label(millionaire,text=user.capitalize(),bg="black",fg='darkorange',font=("Courier",25,'bold'))
                user_lbl.pack()


                leave_btn = tk.Button(text='Take The Money And Leave',font=('cambria',25,'bold'),bd=0,bg='#0dfbff',fg='black',activebackground='green',command=lambda :take_n_leave(data))
                leave_btn.pack(side='top')

                scoreboard_btn = tk.Button(state='norma',text="Exit",font=('cambria',24,'bold'),bd=0,bg='black',fg='yellow',activebackground='yellow',activeforeground='black',command=lambda :exit())
                scoreboard_btn.pack()
                

                #################################################################################################################################################################################

                #################################################################################################################################################################################
                #                                                                      JOKERS

                jokerframe = tk.LabelFrame(millionaire,foreground='white',bg='black')
                jokerframe.pack(side='top',anchor='w',fill='both',expand='yes')
                
                stageframe = tk.LabelFrame(jokerframe,bg='darkblue')
                stageframe.pack(side='right')

                state_50 = tk.Label(text='not used')
                joker50_img = tk.PhotoImage(file="lesson 20/50-50.png")
                joker50_imgX = tk.PhotoImage(file="lesson 20/50-50-X.png")
                joker_50 = tk.Button(jokerframe,image=joker50_img,bg='black',fg='white',activebackground='black',activeforeground="#d6d6d6",relief='flat',command=lambda :joker50())
                joker_50.pack(side='left',anchor='n',padx=10,pady=10)
                
                call_state = tk.Label(text='not used')
                jokercall_img = tk.PhotoImage(file="lesson 20/phoneAFriend.png")
                jokercall_imgX = tk.PhotoImage(file="lesson 20/phoneAFriendX.png")
                joker_call = tk.Button(jokerframe,image=jokercall_img,bg='black',fg='white',activebackground='black',activeforeground="#d6d6d6",relief='flat',height=64,command=lambda :calljoker())
                joker_call.pack(side='left',anchor='n',padx=10,pady=10)

                imageA = tk.PhotoImage(file='lesson 20/audA.png')
                imageB = tk.PhotoImage(file='lesson 20/audB.png')
                imageC = tk.PhotoImage(file='lesson 20/audC.png')
                imageD = tk.PhotoImage(file='lesson 20/audD.png')
                image_none = tk.PhotoImage(file='lesson 20/audnone.png')
                aud_img = tk.Label(jokerframe,bg='black',image=image_none)
                aud_img.pack(side='right')
                aud_state = tk.Label(text='not used')
                jokeraud_img = tk.PhotoImage(file='lesson 20/audiencePole.png')
                jokeraud_imgX = tk.PhotoImage(file='lesson 20/audiencePoleX.png')
                joker_audience = tk.Button(jokerframe,image=jokeraud_img,bg='black',fg='white',activebackground='black',activeforeground="#d6d6d6",relief='flat',height=64,command=lambda :joker_aud())
                joker_audience.pack(side='left',anchor='n',padx=10,pady=10)

                
                prize_lbl = tk.Label(jokerframe,text="",bg='black',fg='white',font=('cambria', 35))
                prize_lbl.pack(side='left',anchor='center',pady=200)

                def take_n_leave(data):
                    scoreboard_btn.config(state='normal')
                    optionA.config(state='disabled')
                    optionB.config(state='disabled')
                    optionC.config(state='disabled')
                    optionD.config(state='disabled')
                    joker_50.config(state='disabled')
                    joker_call.config(state='disabled')
                    joker_audience.config(state='disabled')
                    next_q.config(state='disabled')
                    leave_btn.config(state='disabled')
                    global stage_n
                    stage_n = 75 - len(list_q)
                    if stage_n == 1:
                        prize_lbl.config(text="You won $100!")
                        data['score'].append(100)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 2:
                        prize_lbl.config(text="You won $200!")
                        data['score'].append(200)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 3:
                        prize_lbl.config(text="You won $300!")
                        data['score'].append(300)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 4:
                        prize_lbl.config(text="You won $500!")
                        data['score'].append(500)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 5:
                        prize_lbl.config(text="You won $1000!")
                        data['score'].append(1000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 6:
                        prize_lbl.config(text="You won $2000!")
                        data['score'].append(2000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 7:
                        prize_lbl.config(text="You won $4000!")
                        data['score'].append(4000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 8:
                        prize_lbl.config(text="You won $8000!")
                        data['score'].append(8000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 9:
                        prize_lbl.config(text="You won $16000!")
                        data['score'].append(16000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 10:
                        prize_lbl.config(text="You won $32000!")
                        data['score'].append(32000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 11:
                        prize_lbl.config(text="You won $64000!")
                        data['score'].append(64000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 12:
                        prize_lbl.config(text="You won $125000!")
                        data['score'].append(125000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 13:
                        prize_lbl.config(text="You won $250000!")
                        data['score'].append(250000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif stage_n == 14:
                        prize_lbl.config(text="You won $500000!")
                        data['score'].append(500000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)


                def joker50():
                    joker_50.config(image=joker50_imgX,state='disabled')
                    state_50.config(text='used')
                    pygame.mixer.init()
                    sound_file = os.path.join('lesson 20', '50_50 sound.mp3')
                    sound5050 = pygame.mixer.Sound(sound_file)
                    sound5050.play()
                    joker_50.config(image=joker50_imgX,state='disabled')
                    choice[1].remove(choice[2])
                    remove1 = random.choice(choice[1])
                    choice[1].remove(remove1)
                    remove2 = random.choice(choice[1])
                    if optionA['text'] == remove1:
                        optionA['text'] = ' '
                        optionA.config(state='disabled')
                    elif optionB['text'] == remove1:
                        optionB['text'] = ' '
                        optionB.config(state='disabled')
                    elif optionC['text'] == remove1:
                        optionC['text'] = ' '
                        optionC.config(state='disabled')
                    elif optionD['text'] == remove1:
                        optionD['text'] = ' '
                        optionD.config(state='disabled')
                    
                    if optionA['text'] == remove2:
                        optionA['text'] = ' '
                        optionA.config(state='disabled')
                    elif optionB['text'] == remove2:
                        optionB['text'] = ' '
                        optionB.config(state='disabled')
                    elif optionC['text'] == remove2:
                        optionC['text'] = ' '
                        optionC.config(state='disabled')
                    elif optionD['text'] == remove2:
                        optionD['text'] = ' '
                        optionD.config(state='disabled')
                
                def calljoker():
                    joker_audience.config(state='disabled')
                    joker_50.config(state='disabled')
                    call_state.config(text='used')
                    joker_call.config(image=jokercall_imgX,state='disabled')
                    pygame.mixer.init()
                    sound_a = os.path.join('lesson 20', 'answer A.mp3')
                    sound_b = os.path.join('lesson 20', 'answer B.mp3')
                    sound_c = os.path.join('lesson 20', 'answer C.mp3')
                    sound_d = os.path.join('lesson 20', 'answer D.mp3')
                    ansA = pygame.mixer.Sound(sound_a)
                    ansB = pygame.mixer.Sound(sound_b)
                    ansC = pygame.mixer.Sound(sound_c)
                    ansD = pygame.mixer.Sound(sound_d)
                    if choice[2] == optionA["text"]:
                        ansA.play()
                    elif choice[2] == optionB["text"]:
                        ansB.play()
                    elif choice[2] == optionC["text"]:
                        ansC.play()
                    elif choice[2] == optionD["text"]:
                        ansD.play()

                def joker_aud():
                    joker_audience.config(image=jokeraud_imgX,state='disabled')
                    joker_call.config(state='disabled')
                    joker_50.config(state='disabled')
                    aud_state.config(text='used')
                    aud_state.config(text='used')
                    pygame.mixer.init()
                    sound_aud = os.path.join('lesson 20', 'audience.mp3')
                    sound = pygame.mixer.Sound(sound_aud)
                    sound.play()

                    def aud_joker():
                        if choice[2] == optionA["text"]:
                            aud_img.config(image=imageA,bg='white')
                            aud_img.pack(side='right',padx=7)
                        elif choice[2] == optionB["text"]:
                            aud_img.config(image=imageB,bg='white')
                            aud_img.pack(side='right',padx=7)
                        elif choice[2] == optionC["text"]:
                            aud_img.config(image=imageC,bg='white')
                            aud_img.pack(side='right',padx=7)
                        elif choice[2] == optionD["text"]:
                            aud_img.config(image=imageD,bg='white')
                            aud_img.pack(side='right',padx=7)
                    
                    millionaire.after(31500,aud_joker())


                #################################################################################################################################################################################
                #                                                                               Questions

                nextqframe = tk.LabelFrame(millionaire,foreground='white',bg='black')
                nextqframe.pack()

                qaframe = tk.Frame(millionaire,bg='black')
                qaframe.pack(side='bottom',padx=10,pady=10,fill='x',expand='yes')


                qframe = tk.LabelFrame(qaframe,text='',fg='white',bg='black',font=('cambria',21))
                qframe.pack(padx=10,pady=10,fill='x',expand='yes',anchor='s')

                q_lbl = tk.Label(qframe, text='Press start',font=('helvetica',20,"bold"),bg='black',fg='white')
                q_lbl.pack(fill='both',pady=10)


                list_q = [
                    ['Which football club has won the most Champions League Titles?',['Real Madrid','Liverpool','AC Milan','Bayern Munich'],'Real Madrid'],
                    ['What is the capital of France?',['Paris','Madrid','Berlin','Rome'],'Paris'],
                    ['Which country won the FIFA World Cup in 2018?',['France','Croatia','Brazil','Argentina'],'France'],
                    ['Which footballer is known as "The King" and has won three FIFA World Cups?',['Pelé','Diego Maradona','Zinedine Zidane','Ronaldo'],'Pelé'],
                    ['Which club won the UEFA Champions League in 2005 after a famous comeback against AC Milan?',['Liverpool','Barcelona','Real Madrid','Bayern Munich'],'Liverpool'],
                    ['In what year did the Premier League officially begin?',['1992','1998','1996','2000'],'1992'],
                    ['Who is the top scorer in Champions League history?',['Cristiano Ronaldo','Lionel Messi','Lewandowski','Benzema'],'Cristiano Ronaldo'],
                    ['Which club was defeated 8-2 by FC Bayern Munich in 2020?',['Barcelona','AC Milan','Real Madrid','Liverpool'],'Barcelona'],
                    ['Which team was defeated by Bayern Munich in the 1974-1975 champions league final?',['Leeds United','Real Madrid','Barcelona','AC Milan'],'Leeds United'],
                    ['Which player holds the record for the most appearances in World Cup history?',['Lothar Matthäus','Paolo Maldini','Cafu','Miroslav Klose'],'Lothar Matthäus'],
                    ['Which African country was the first to reach the quarter-finals of the FIFA World Cup?',['Cameroon','Nigeria','Ghana','Senegal'],'Cameroon'],
                    ['Who holds the record for the most goals scored in a single Premier League season?',['Mohamed Salah','Thierry Henry','Erling Haaland','Cristiano Ronaldo'],'Erling Haaland'],
                    ['Which country has won the most FIFA World Cup titles?',['Brazil','Germany','Italy','Argentina'],'Brazil'],
                    ['Which club did David Beckham join after leaving Manchester United in 2003?',['Real Madrid','AC Milan','LA Galaxy','Paris Saint-Germain'],'Real Madrid'],
                    ['Which manager has won the most UEFA Champions League titles?',['Carlo Ancelotti','Pep Guardiola','Jose Mourinho','Sir Alex Ferguson'],'Carlo Ancelotti'],
                    ['Who invented the lightbulb?',['Thomas Edison','Alexander Graham Bell','Nikola Tesla','Benjamin Franklin'],'Thomas Edison'],
                    ['Which planet is known as the Red Planet?',['Earth','Mars','Venus','Jupiter'],'Mars'],
                    ['Who wrote the play "Romeo and Juliet"?',['William Shakespeare','Charles Dickens','Leo Tolstoy','Mark Twain'],'William Shakespeare'],
                    ['What is the chemical symbol for gold?',['Ag','Au','Pb','Fe'],'Au'],
                    ['Who painted the Mona Lisa?',['Vincent van Gogh','Pablo Picasso','Leonardo da Vinci','Claude Monet'],'Leonardo da Vinci'],
                    ['How many continents are there on Earth?',['5','6','7','8'],'7'],
                    ['What is the largest ocean on Earth?',['Atlantic','Indian','Southern','Pacific'],'Pacific'],
                    ['In which year did World War II end?',['1942','1945','1950','1960'],'1945'],
                    ['Who is the author of the "Harry Potter" series?',['J.K. Rowling','J.R.R. Tolkien','George R.R. Martin','Stephen King'],'J.K. Rowling'],
                    ['What is the smallest prime number?',['1','2','3','5'],'2'],
                    ['Who was the first person to walk on the Moon?',['Yuri Gagarin','Neil Armstrong','Buzz Aldrin','Michael Collins'],'Neil Armstrong'],
                    ['Which country is home to the kangaroo?',['India','South Africa','Australia','Brazil'],'Australia'],
                    ['Who invented the telephone?',['Nikola Tesla','Alexander Graham Bell','Thomas Edison','Guglielmo Marconi'],'Alexander Graham Bell'],
                    ['What is the hardest natural substance on Earth?',['Iron','Quartz','Diamond','Titanium'],'Diamond'],
                    ['In what year did the Titanic sink?',['1910','1912','1914','1920'],'1912'],
                    ['Who is known as the "Father of Computers"?',['Alan Turing','Charles Babbage','Steve Jobs','Bill Gates'],'Charles Babbage'],
                    ['Which element is necessary for respiration?',['Nitrogen','Hydrogen','Carbon Dioxide','Oxygen'],'Oxygen'],
                    ['What is the largest land animal?',['Elephant','Rhinoceros','Hippopotamus','Giraffe'],'Elephant'],
                    ['What is the longest river in the world?',['Amazon','Nile','Yangtze','Mississippi'],'Nile'],
                    ['Who was the first President of the United States?',['John Adams','Abraham Lincoln','George Washington','Thomas Jefferson'],'George Washington'],
                    ['What is the square root of 144?',['10','11','12','13'],'12'],
                    ['Who wrote the novel "1984"?',['Aldous Huxley','George Orwell','F. Scott Fitzgerald','Ernest Hemingway'],'George Orwell'],
                    ['What is the powerhouse of the cell?',['Nucleus','Mitochondria','Ribosome','Chloroplast'],'Mitochondria'],
                    ['How many strings does a standard guitar have?',['4','5','6','7'],'6'],
                    ['What is the main ingredient in guacamole?',['Tomato','Avocado','Onion','Lettuce'],'Avocado'],
                    ['What is the capital of Japan?',['Kyoto','Tokyo','Osaka','Hiroshima'],'Tokyo'],
                    ['Which planet is closest to the sun?',['Venus','Mars','Mercury','Earth'],'Mercury'],
                    ['What is the largest mammal in the world?',['Elephant','Blue Whale','Great White Shark','Giraffe'],'Blue Whale'],
                    ['Who developed the theory of relativity?',['Isaac Newton','Albert Einstein','Galileo Galilei','Niels Bohr'],'Albert Einstein'],
                    ['What is the most abundant gas in the Earth\'s atmosphere?',['Oxygen','Carbon Dioxide','Hydrogen','Nitrogen'],'Nitrogen'],
                    ['Who wrote the novel "Moby Dick"?',['Mark Twain','Jules Verne','Herman Melville','F. Scott Fitzgerald'],'Herman Melville'],
                    ['Which is the smallest country in the world by area?',['Monaco','Liechtenstein','Vatican City','San Marino'],'Vatican City'],
                    ['What is the largest planet in the solar system?',['Earth','Saturn','Neptune','Jupiter'],'Jupiter'],
                    ['Who was the first woman to win a Nobel Prize?',['Marie Curie','Jane Austen','Ada Lovelace','Florence Nightingale'],'Marie Curie'],
                    ['What is the currency of the United Kingdom?',['Dollar','Euro','Pound Sterling','Franc'],'Pound Sterling'],
                    ['Which element is represented by the symbol "O"?',['Osmium','Oxygen','Gold','Iron'],'Oxygen'],
                    ['Which artist painted "Starry Night"?',['Leonardo da Vinci','Pablo Picasso','Claude Monet','Vincent van Gogh'],'Vincent van Gogh'],
                    ['What is the tallest mountain in the world?',['Mount Kilimanjaro','Mount Everest','K2','Mount McKinley'],'Mount Everest'],
                    ['Who discovered penicillin?',['Marie Curie','Alexander Fleming','Isaac Newton','Louis Pasteur'],'Alexander Fleming'],
                    ['Which continent is the Sahara Desert located on?',['Asia','South America','Africa','Australia'],'Africa'],
                    ['How many bones are in the adult human body?',['206','205','207','209'],'206'],
                    ['Which country is the origin of the famous car brand "Ferrari"?',['France','Germany','Japan','Italy'],'Italy'],
                    ['Which city hosted the 2008 Summer Olympics?',['London','Tokyo','Beijing','Athens'],'Beijing'],
                    ['Who was the first African American president of the United States?',['Martin Luther King Jr.','Barack Obama','George Washington Carver','Malcolm X'],'Barack Obama'],
                    ['What is the chemical symbol for water?',['H2O','CO2','O2','NaCl'],'H2O'],
                    ['Which country is famous for the Eiffel Tower?',['Germany','Italy','France','Spain'],'France'],
                    ['Who is the founder of Microsoft?',['Steve Jobs','Mark Zuckerberg','Bill Gates','Elon Musk'],'Bill Gates'],
                    ['What is the smallest unit of matter?',['Molecule','Atom','Electron','Proton'],'Atom'],
                    ['Which country is home to the Great Barrier Reef?',['Brazil','Australia','India','South Africa'],'Australia'],
                    ['How many hearts does an octopus have?',['1','2','3','4'],'3'],
                    ['Which planet has the most moons?',['Mars','Jupiter','Saturn','Neptune'],'Saturn'],
                    ['What is the capital of Canada?',['Toronto','Vancouver','Montreal','Ottawa'],'Ottawa'],
                    ['Who painted the ceiling of the Sistine Chapel?',['Michelangelo','Leonardo da Vinci','Raphael','Donatello'],'Michelangelo'],
                    ['Which element has the atomic number 1?',['Helium','Oxygen','Hydrogen','Carbon'],'Hydrogen'],
                    ['In which year did humans first land on the Moon?',['1965','1969','1971','1975'],'1969'],
                    ['Which organ is responsible for pumping blood through the body?',['Liver','Lungs','Brain','Heart'],'Heart'],
                    ['What is the national language of Brazil?',['Spanish','Portuguese','French','English'],'Portuguese'],
                    ['Who wrote "Pride and Prejudice"?',['Emily Brontë','Charles Dickens','Jane Austen','Mary Shelley'],'Jane Austen'],
                    ['Which continent is the largest by land area?',['Asia','Africa','North America','Europe'],'Asia'],
                    ['How many players are on a soccer team on the field at the start of a match?',['9','10','11','12'],'11']
                ]
                #################################################################################################################################################################################
                #                                                                  Question order

                def next_question():
                    aud_img.config(image=image_none,bg='black')
                    leave_btn.config(state='normal')
                    if state_50['text'] == 'not used':
                        joker_50.config(state='normal')
                    else:
                        joker_audience.config(state='disabled')
                    if call_state['text'] == 'not used':
                        joker_call.config(state='normal')
                    else:
                        joker_call.config(state='disabled')
                    if aud_state['text'] == 'not used':
                        joker_audience.config(state='normal')
                    else:
                        joker_audience.config(state='disabled')
                    global choice
                    choice = random.choice(list_q)
                    q_lbl.config(text=(choice[0].replace("{",'').replace("}",'')))
                    random.shuffle(choice[1])
                    optionA.config(text=choice[1][0])
                    optionB.config(text=choice[1][1])
                    optionC.config(text=choice[1][2])
                    optionD.config(text=choice[1][3])
                    list_q.remove(choice)
                    qframe.config(text=(f"Question {75 - len(list_q)}"))
                    if qframe['text'] == "Question 75":
                        next_q.config(state='disabled')
                    optionA.config(state='normal',bg='blue')
                    optionB.config(state='normal',bg='blue')
                    optionC.config(state='normal',bg='blue')
                    optionD.config(state='normal',bg='blue')
                    next_q.config(text='Next question')
                    next_q.config(state='disabled')
                    for i in range(1,16):
                        stagenum = eval(f"stage{i}")
                        stagenum.config(bg='darkblue')
                    stage_num = eval(f"stage{75 - len(list_q)}")
                    stage_num.config(bg='orange')
                    pygame.mixer.init()
                    sound_file = os.path.join('lesson 20', 'qstart.mp3')
                    qstart_answer_sound = pygame.mixer.Sound(sound_file)
                    qstart_answer_sound.play()



                next_q = tk.Button(nextqframe, text='',font=('sanserif',20,'bold'),bg='#2310bf',fg='white',activebackground='#0023ff',activeforeground="#d6d6d6",relief='ridge',command=lambda :next_question())
                next_q.pack(anchor='center',side='top')


                #################################################################################################################################################################################

                #################################################################################################################################################################################
                #                                                                  ANSWER OPTIONS
                def colorblue():
                    optionA.config(background='blue')
                    optionB.config(background='blue')
                    optionC.config(background='blue')
                    optionD.config(background='blue')

                def anscorrect(button1):
                    button1.config(background='green')

                def answrong(button1):
                    button1.config(background='red')

                def ans_correct(button1,button2,button3,button4):
                    button1.config(state='disabled',background='#d8a418')
                    button2.config(state='disabled')
                    button3.config(state='disabled')
                    button4.config(state='disabled')
                    pygame.mixer.init()
                    sound_file = os.path.join('lesson 20', 'correct answer.mp3')
                    correct_answer_sound = pygame.mixer.Sound(sound_file)
                    correct_answer_sound.play()
                    millionaire.after(10100,anscorrect(button1))
                    next_q.config(state='normal')
                    stage_num = eval(f"stage{75 - len(list_q)}")
                    stage_num.config(bg='green')
                    leave_btn.config(state='normal')
                    

                def ans_wrong(button1,button2,button3,button4):
                    button1.config(state='disabled',background='#ea241b')
                    button2.config(state='disabled')
                    button3.config(state='disabled')
                    button4.config(state='disabled')
                    pygame.mixer.init()
                    sound_file = os.path.join('lesson 20', 'wrong answer.mp3')
                    wrong_answer_sound = pygame.mixer.Sound(sound_file)
                    wrong_answer_sound.play()
                    millionaire.after(10100,answrong(button1))
                    next_q.config(text='Wrong answer',state='disabled')
                    stage_num = eval(f"stage{75 - len(list_q)}")
                    stage_num.config(bg='red')
                    
                    

                    if 10>75 - len(list_q)-1>=5:
                        prize_lbl.config(text="You won $1000!")
                        data['score'].append(1000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    elif 15>=75 - len(list_q)-1>=10:
                        prize_lbl.config(text="You won $32000!")
                        data['score'].append(32000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    else:
                        prize_lbl.config(text="You lost...")
                        
                    

                def ans_submit(button1,button2,button3,button4):
                    joker_50.config(state='disabled')
                    joker_call.config(state='disabled')
                    joker_audience.config(state='disabled')
                    stage_n = 75 - len(list_q)
                    if choice[2] == button1["text"]:
                        ans_correct(button1,button2,button3,button4)
                    else:
                        if button2["text"] == choice[2]:
                            button2.config(bg='green')
                        elif button3["text"] == choice[2]:
                            button3.config(bg='green')
                        elif button4["text"] == choice[2]:
                            button4.config(bg='green')
                        ans_wrong(button1,button2,button3,button4)
                    if stage_n == 15:
                        prize_lbl.config(text=f"{user.capitalize()} is officially a MILLIONAIRE!!!")
                        next_q.config(state='disabled')
                        scoreboard_btn.config(state='normal')
                        data['score'].append(1000000)
                        with open(f'lesson 20/users/{user}.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        with open('lesson 20/scoreboard.json','w') as millionaires:
                            data_score = json.load(millionaires)
                            data_score.append(user)
                        optionA.config(text="$1000000")
                        optionB.config(text="$1000000")
                        optionC.config(text="$1000000")
                        optionD.config(text="$1000000")
                        leave_btn.config(text='MILLIONAIRE')


                answerframe = tk.Frame(qaframe,bg='black')
                answerframe.pack(side='bottom',fill='x')

                topframe = tk.Frame(answerframe,bg='black')
                topframe.pack(side='top',pady=5)

                frameA = tk.Frame(topframe,bg='blue')
                frameA.pack(side='left',padx=22)
                label_a = tk.Label(frameA,text='A:',fg='#e9aa00',bg='blue',font=('cambria',15))
                label_a.pack(side='left')
                optionA = tk.Button(frameA,state='disabled',text=' ',height=3,width=28,bg='black',font=('helvetica',15),fg='white',bd=0,activebackground='#d8a418',command=lambda :ans_submit(optionA,optionB,optionC,optionD))
                optionA.pack()

                frameB = tk.Frame(topframe,bg='blue')
                frameB.pack(padx=22)
                label_b = tk.Label(frameB,text='B:',fg='#e9aa00',bg='blue',font=('cambria',15))
                label_b.pack(side='left')
                optionB = tk.Button(frameB,state='disabled',text=' ',height=3,width=28,bg='black',font=('helvetica',15),fg='white',bd=0,activebackground='#d8a418',command=lambda :ans_submit(optionB,optionA,optionC,optionD))
                optionB.pack()



                bottomframe = tk.Frame(answerframe,bg='black')
                bottomframe.pack(side='bottom',pady=5)

                frameC = tk.Frame(bottomframe,bg='blue')
                frameC.pack(side='left',padx=22)
                label_c = tk.Label(frameC,text='C:',fg='#e9aa00',bg='blue',font=('cambria',15))
                label_c.pack(side='left')
                optionC = tk.Button(frameC,state='disabled',text=' ',height=3,width=28,bg='black',font=('helvetica',15),fg='white',bd=0,activebackground='#d8a418',command=lambda :ans_submit(optionC,optionB,optionA,optionD))
                optionC.pack()


                frameD = tk.Frame(bottomframe,bg='blue')
                frameD.pack(padx=22)
                label_d = tk.Label(frameD,text='D:',fg='#e9aa00',bg='blue',font=('cambria',15))
                label_d.pack(side='left')
                optionD = tk.Button(frameD,state='disabled',text=' ',height=3,width=28,bg='black',font=('helvetica',15),fg='white',bd=0,activebackground='#d8a418',command=lambda :ans_submit(optionD,optionB,optionC,optionA))
                optionD.pack()

                #################################################################################################################################################################################
                #                                                                               Stages

                global stage1,stage2,stage3,stage4,stage5,stage6,stage7,stage8,stage9,stage10,stage11,stage12,stage13,stage14,stage15
                
                stage15 = tk.Label(stageframe,text='15    $1 MILLION',bg='darkblue',font=('helvetica',17),fg='white')
                stage15.pack(anchor='w')
                stage14 = tk.Label(stageframe,text='14    $500,000 ',bg='darkblue',font=('helvetica',17))
                stage14.pack(anchor='w')
                stage13 = tk.Label(stageframe,text='13    $250,000 ',bg='darkblue',font=('helvetica',17))
                stage13.pack(anchor='w')
                stage12 = tk.Label(stageframe,text='12    $125,000 ',bg='darkblue',font=('helvetica',17))
                stage12.pack(anchor='w')
                stage11 = tk.Label(stageframe,text='11    $64,000 ',bg='darkblue',font=('helvetica',17))
                stage11.pack(anchor='w')
                stage10 = tk.Label(stageframe,text='10    $32,000 ',bg='darkblue',font=('helvetica',17),fg='white')
                stage10.pack(anchor='w')
                stage9 = tk.Label(stageframe,text=' 9    $16,000 ',bg='darkblue',font=('helvetica',17))
                stage9.pack(anchor='w')
                stage8 = tk.Label(stageframe,text=' 8    $8,000 ',bg='darkblue',font=('helvetica',17))
                stage8.pack(anchor='w')
                stage7 = tk.Label(stageframe,text=' 7    $4,000 ',bg='darkblue',font=('helvetica',17))
                stage7.pack(anchor='w')
                stage6 = tk.Label(stageframe,text=' 6    $2,000 ',bg='darkblue',font=('helvetica',17))
                stage6.pack(anchor='w')
                stage5 = tk.Label(stageframe,text=' 5    $1,000 ',bg='darkblue',font=('helvetica',17),fg='white')
                stage5.pack(anchor='w')
                stage4 = tk.Label(stageframe,text=' 4    $500 ',bg='darkblue',font=('helvetica',17))
                stage4.pack(anchor='w')
                stage3 = tk.Label(stageframe,text=' 3    $300 ',bg='darkblue',font=('helvetica',17))
                stage3.pack(anchor='w')
                stage2 = tk.Label(stageframe,text=' 2    $200 ',bg='darkblue',font=('helvetica',17))
                stage2.pack(anchor='w')
                stage1 = tk.Label(stageframe,text=' 1    $100 ',bg='darkblue',font=('helvetica',17))
                stage1.pack(anchor='w')


                #################################################################################################################################################################################
                
                next_question()

                colorblue()

                millionaire.mainloop()
    
        except FileNotFoundError:
            with open(f"lesson 20/users/{user}.json","w") as f:
                user2 = json.dumps(user1.__dict__)
                f.write(user2 )
                login_result.config(text='Account created!',fg='#00ffff')
            




username_lbl = tk.Label(text="Username:", font=('cambria',35),bg="#000044",fg='white')
username_lbl.pack(pady=10)

username_entry = tk.Entry(textvariable=tk.StringVar(), font=('cambria',23))
username_entry.pack()

start_button = tk.Button(text="Start", font=("Helvetica", 27, "bold"),bg="green", fg="#ffffff", activebackground="#ffcc00",activeforeground="#000000", bd=0, relief="flat",command=start)
start_button.pack(pady=20)

login_result = tk.Label(text="", font=("helvetica",25),bg="#000044")
login_result.pack(pady=10)

back1 = tk.Button(text='Exit',font=('cambria',35,'bold'),bg='white',fg='black',bd=0,command=lambda :exit())
back1.pack(anchor='center',pady=10)

pygame.mixer.init()
sound_file = os.path.join('lesson 20', 'welcome.mp3')
soundwelcome = pygame.mixer.Sound(sound_file)
soundwelcome.play()

login.mainloop()