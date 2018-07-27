# Check what platform it is running on.
try:
    import RPi.GPIO as GPIO
    import os

    cwd = os.getcwd()
    audio_folder = os.path.join(cwd, "audio")

    correct_audio_path = os.path.join(audio_folder, "correct.mp3")
    incorrect_audio_path = os.path.join(audio_folder, "incorrect.mp3")
    game_open = os.path.join(audio_folder, "What is my purpose.mp3")

    onPi = True

except:  # Either developing on a pc or OS doesn't support GPIO, replace libraries with fake ones
    print("You are either not on a Raspberry Pi, or on an OS that doesn't support GPIO. fake_rpi will be used")

    import sys
    import fake_rpi
    import os

    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi (GPIO)
    sys.modules['smbus'] = fake_rpi.smbus  # Fake smbus (I2C)
    GPIO = fake_rpi.RPi.GPIO

    cwd = os.getcwd()
    audio_folder = os.path.join(cwd, "audio")


    correct_audio_path = os.path.join(audio_folder, "correct.mp3")
    incorrect_audio_path = os.path.join(audio_folder, "wrong.mp3")
    game_open = os.path.join(audio_folder, "correct.mp3")
    print(game_open)

    onPi = False

from tkinter import *  # import tkinter library for GUI, from shortens function calls
import time  # used for sleep commands
import sys  # if you used an exit option, you would need this
import pygame  # used to play audio
from random import randint  # a random number is used to select a random quiz
# GPIO.setwarnings(False)       # I don't think this is necessary if GPIO is cleaned upon exit/crash

# import quizs.defaultQuiz as defaultQuiz
# import quizs.halloween as halloween


#from quizs import __init__
from quizs import defaultQuiz as dTest
from quizs import halloween as hTest
from quizs import VSP as vspTest

# test2 = "test.defaultQuiz"
# defaultQ =  __import__(test2)

#theme = dTest.defaultQuiz()
#quiz = theme.getQuiz()
import numpy as np
SCREEN_SIZE = "800x480"

class App(Frame):
    theme = dTest.defaultQuiz()
    vsp = vspTest.VSP()
    halloween = hTest.halloween()
    quiz = theme.getQuiz()

    # init is run on object creation
    def __init__(self, master):
        self.master = master
        self.changeTheme(self.vsp)
        Frame.__init__(self, master)
        self.grid()
        self.playSound(game_open)  # This will play as soon as the app is started

    def changeTheme(self, newTheme):
        self.theme = newTheme
        self.quiz = newTheme.getQuiz()
        self.master.configure(background=newTheme.getBGColor())



    # This re-prints the header, it's called before each question is printed
    def header(self):
        self.label_1 = Label(root,
                             text="Welcome to " + self.theme.getQuizName(),
                             font=(self.theme.getFont(), 36),
                             bg=self.theme.getBGColor(),
                             fg=self.theme.getTitleColor())
        self.label_1.grid(columnspan=6,
                          padx=(100, 10))

        self.label_2 = Label(root,
                             text="Answer the question for candy!",
                             font=(self.theme.getFont(), 28),
                             bg=self.theme.getBGColor(),
                             fg=self.theme.getSecondaryColor())
        self.label_2.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

    # I had to add this label, otherwise it would crash when I try to delete label_7 in selectQuestion() on my first run
    def prime(self):
        self.label_7 = Label(root,
                             text="I serve candy.",
                             font=(self.theme.getFont(), 32),
                             bg=self.theme.getBGColor(),
                             fg=self.theme.getFGColor())
        self.label_7.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

    # Prints select difficulty buttons
    def chooseDifficulty(self):
        self.label_8 = Label(root,
                             text="Please choose a difficulty.",
                             font=(self.theme.getFont(), 32),
                             bg=self.theme.getBGColor(),
                             fg=self.theme.getFGColor())
        self.label_8.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

        self.button_8 = Button(root,
                               text="Easy",
                               font=(self.theme.getFont(), 36),
                               command=lambda: self.selectQuestion(0))  # lambda allows you to pass an argument
        self.button_8.grid(row=5,
                           column=1,
                           padx=(100, 10))

        self.button_9 = Button(root,
                               text="Medium",
                               font=(self.theme.getFont(), 36),
                               command=lambda: self.selectQuestion(1))
        self.button_9.grid(row=5,
                           column=3,
                           padx=(100, 10))

        self.button_10 = Button(root,
                                text="Hard",
                                font=(self.theme.getFont(), 36),
                                command=lambda: self.selectQuestion(2))
        self.button_10.grid(row=5,
                            column=5,
                            padx=(100, 10))

        self.label_11 = Label(root,
                              text="Prizes: Easy = 1 candy, Medium = 2 candies, Hard = 3 candies",
                              font=(self.theme.getFont(), 16),
                              bg=self.theme.getBGColor(),
                              fg=self.theme.getFGColor())
        self.label_11.grid(columnspan=6,
                           pady=5,
                           padx=(100, 10))

        self.button_theme = Button(root,
                                   text="Theme",
                                   font=(self.theme.getFont(), 16),
                                   command=lambda: self.selectTheme())
        self.button_theme.grid(row=1,
                               column=6,
                               padx=(100,10))


    def selectTheme(self):
        self.label_7.destroy()  # destroys the label from correct() wrong()
        self.label_8.destroy()  # destroys all the labels and buttons from difficulty()
        self.button_8.destroy()
        self.button_9.destroy()
        self.button_10.destroy()
        self.label_11.destroy()


    # Randomly selects a question in the correct difficulty
    def selectQuestion(self, difficultyLvl):

        self.label_7.destroy()  # destroys the label from correct() wrong()
        self.label_8.destroy()  # destroys all the labels and buttons from difficulty()
        self.button_8.destroy()
        self.button_9.destroy()
        self.button_10.destroy()
        self.label_11.destroy()



        quantity = (int(len(self.quiz[difficultyLvl])) - 1)  # gets the number of questions in selected difficulty, cast int to avoid errors
        randomSelection = int(randint(0, quantity))  # randomly selects a number in a valid range
        randomOrder = int(randint(1, 50))
        np.random.seed(randomOrder)

        # place choices in an array
        choices = [self.quiz[difficultyLvl][randomSelection][1],
                   self.quiz[difficultyLvl][randomSelection][2],
                   self.quiz[difficultyLvl][randomSelection][3],
                   self.quiz[difficultyLvl][randomSelection][4]]
        choices = np.array(choices)

        # get answer
        answerLoc = self.quiz[difficultyLvl][randomSelection][5]
        answer = self.quiz[difficultyLvl][randomSelection][answerLoc]

        # shuffle order
        np.random.shuffle(choices)
        answerLoc = np.where(choices == answer)
        answerLoc = int((answerLoc[0][0]))+1

        # pass values to be printed to screen. [difficulty][selection][data]
        self.quizMe(self.quiz[difficultyLvl][randomSelection][0],  # question
                    choices[0],  # choice1
                    choices[1],  # choice2
                    choices[2],  # choice3
                    choices[3],  # choice4
                    answerLoc,  # answerNum
                    difficultyLvl)  # difficulty

    # This method accepts all quiz info and prints it to the screen
    def quizMe(self, question, choice1, choice2, choice3, choice4, correctChoice, difficultyLvl):

        result = [self.wrong, self.wrong, self.wrong, self.wrong, self.wrong]  # array to hold method names for button commands. Prime array by filling with wrong
        result[correctChoice] = self.correct  # assigns correct answer in correct possition

        choice = [choice1, choice2, choice3, choice4]  # array for font sizing
        # check to see what font size is necessary for buttons
        fontSizeB = 36
        for x in range(0, 4):  # cycles through all the choices to find the longest string.
            if len(choice[x]) > 8:
                fontSizeB = 24

        # check to see what font size is necessary for the question. I'm looking for a more dynamic solution.
        fontSizeL = 32
        if len(question) > 30:
            fontSizeL = 30
            if len(question) > 35:
                fontSizeL = 28
                if len(question) > 45:
                    fontSizeL = 22

        # question
        self.label_3 = Label(root,
                             text=question,
                             font=(self.theme.getFont(), fontSizeL),
                             bg=self.theme.getBGColor(),
                             fg=self.theme.getFGColor())

        self.label_3.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

        # choice1
        self.button_1 = Button(root,
                               text=choice1,
                               font=(self.theme.getFont(), fontSizeB),
                               command=lambda: result[1](difficultyLvl))  # lambda allows you to pass an argument
        self.button_1.grid(row=4,
                           column=1,
                           pady=5,
                           padx=(100, 10))

        # choice2
        self.button_2 = Button(root,
                               text=choice2,
                               font=(self.theme.getFont(), fontSizeB),
                               command=lambda: result[2](difficultyLvl))
        self.button_2.grid(row=4,
                           column=3,
                           sticky=W,
                           padx=(100, 10))

        # choice3
        self.button_3 = Button(root,
                               text=choice3,
                               font=(self.theme.getFont(), fontSizeB),
                               command=lambda: result[3](difficultyLvl))
        self.button_3.grid(row=5,
                           column=1,
                           pady=5,
                           padx=(100, 10))

        # choice4
        self.button_4 = Button(root,
                               text=choice4,
                               font=(self.theme.getFont(), fontSizeB),
                               command=lambda: result[4](difficultyLvl))
        self.button_4.grid(row=5,
                           column=3,
                           sticky=W,
                           padx=(100, 10))

    # Executes all necessary functions for a correct answer
    def correct(self, difficultyLvl):
        self.clearPage()  # Destroys all buttons and lables on screen before displaying results

        self.label_7 = Label(root,
                             text="CORRECT!!!!",
                             font=(self.theme.getFont(), 32),
                             bg=self.theme.getBGColor(),
                             fg="green")

        self.label_7.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

        self.playSound(correct_audio_path)  # Send the filepath of the audio to play for correct answer
        self.pushCandy((difficultyLvl + 1))  # dispenses appropriate number of candies for difficulty

        self.chooseDifficulty()  # asks for difficulty of next question


    # Executes all necessary functions for a wrong answer
    def wrong(self, difficultyLvl):
        self.clearPage()  # Destroys all buttons and lables on screen before displaying results

        self.label_7 = Label(root,
                             text="Wrong, try again.",
                             font=(self.theme.getFont(), 32),
                             bg=self.theme.getBGColor(),
                             fg="red")

        self.label_7.grid(columnspan=6,
                          pady=5,
                          padx=(100, 10))

        self.playSound(incorrect_audio_path)  # Send the filepath of the audio to play for correct answer
        self.pushCandy(1)  # dispenses 1 candy for incorrect guess
        self.chooseDifficulty()  # asks for difficulty of next question

    # Pushes the servo in and out to dispense candy, dispenses as much candy as parameter specifies
    def pushCandy(self, candies):

        GPIO.setmode(GPIO.BOARD)  # refers to the pins by the physical position they appear in
        GPIO.setup(7, GPIO.OUT)  # servo on pin 7
        p = GPIO.PWM(7, 50)  # pin 7 pulse width mod, 50hz
        p.start(2.5)  # duty cycle, nutral position

        while candies > 0:
            p.ChangeDutyCycle(12)  # Pull plunger. This number may need to be altered depending on your servo and orientation.
            time.sleep(.4)  # Gives the servo time to transition
            p.ChangeDutyCycle(2.5)  # Push plunger. This number may also need to be altered.
            time.sleep(.4)
            candies = candies - 1  # Decrements the count of candies that still need to be dispensed.

        p.stop()  # stops servo control
        GPIO.cleanup()  # cleans the GPIO settings. Without this the servo acts irratically between uses.
        print("candy")  # When testing on desktop, comment all other lines in this method and leave the print to avoid error.

    # play sound from whatever file is at parameter dirrectory. I used this to play a sound effect at multiple points.
    def playSound(self, fileName):
        pygame.mixer.init()
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(1)  # change this value if you want to audio to loop.

    # Kills buttons and labels from page after answer is selected
    def clearPage(self):
        self.button_1.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        self.button_4.destroy()
        self.label_3.destroy()


root = Tk()
root.title("Trick or Trivia")  # adds a name to the titlebar of the application
root.overrideredirect(True)  # This takes up the whole screen and removes x to exit
root.geometry(SCREEN_SIZE.format(root.winfo_screenwidth(),root.winfo_screenheight()))  # when I was testing on desktop I replaced {0}x{1}+0+0 with the resolution of my touchscreen
root.focus_set()  # <-- move focus to this widget

if (onPi == True):
    root.configure(background='black',cursor="none")  # removes cursor for a cleaner look, relies on touchscreen. Remove cursor="none" if you need a mouse.
else:
    root.configure(background='black')

app = App(master=root)  # object instantiation
# app.populateQuiz()
app.header()
app.prime()
app.chooseDifficulty()
app.mainloop()  # This is necessary for event programming in tkinter
