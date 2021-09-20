from engi1020.arduino import *
import time
import matplotlib.pyplot as plt
import random 
from time import sleep
from builtins import input
#The required modules were imported, engi1020.arduino to work with the sensors and Arduino, time to calculate reaction time and use the sleep function. The random module to make random number for question and color selection and the matplotlib.pyplot to plot the graph.
def makegraph(xlist,ylist,xlabel,ylabel,title):
    plt.plot(xlist, ylist)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis([1, max(xlist), 0, max(ylist)+1])
    plt.suptitle(title)
    plt.show()
    #This makegraph function was made to plot the graph at the end of game.it uses the number of questions and the list containing the reaction time, the labels for the x and y axis and the title of the graph as inputs. 

buttonpin=4
touchpin=2
#The pin number for the button and touch sensor is set in a variable.
questions =[["Green",0.25],["Blue",0.5],["Red",0]]
#This list is used to store the three questions used in the game, the first values are the text to be displayed in the lcd screen while the second values are the hue values for the corresponding colors. I got these values of hue from my experience with lab 6 where I implemented the changing of lcd screen color depending on the value from the temperature sensor.
print("If you think the color of the lcd screen and the color name in text match press the button else press the touch sensor")
difficulty=float(input ("please enter the difficulty from 0.5, 1 and 2. The lower the number the harder it is: "))
#this difficulty variable is used in the sleep function later on, basically it is used to set how quickly each question comes on the screen after answering.
amount=int(input("please enter the number of questions you want to play for: "))
#this amount variable stores the number of questions for which the user wants to play the game.
correct=0
#this stores the number of times the user got the correct answer
timelist=[]
index=[]
#The timelist list stores the reaction times of the user and the index list is a list that has the number of questions for the graph.
for i in range(amount):
    #a loop to keep looping until all question have been asked.
    question=random.randint(0,2) 
    color=random.randint(0,2) 
    sleep(difficulty)
    #Random number between 0 to 2 is set to question and color. The sleep function is used to set how quickly the question is asked.
    index.append(i+1)
    lcd_print(questions[question][0])
    lcd_hsv(questions[color][1],1,100)
    then=time.time()
    now=0
    #The questions and color are given in the lcd screen and the time is stored
    touch=0
    button=0
    #These variables are set to zero, they will store the input values from button and touch sensor.
    input=False
    #Variable storing a Boolean value of if input is received from any of the inputs.
    while input==False:
        touch=digital_read(touchpin)
        button=digital_read(buttonpin)
        if touch!=0 or button!=0:
            input=True
            #A loop that keeps running until an input is received from the button or touch sensor
    if ((questions[question][0]=="Green" and questions[color][1]==0.25) or (questions[question][0]=="Blue" and questions[color][1]==0.5) or (questions[question][0]=="Red" and questions[color][1]==0)) and button==1:
        correct+=1
        now=time.time()
        #Conditional statement to check if the color and the text match and if the user thinks it is correct by pressing the button. The time is stored in a variable.
    elif ((questions[question][0]=="Green" and questions[color][1]==0.25) or (questions[question][0]=="Blue" and questions[color][1]==0.5) or (questions[question][0]=="Red" and questions[color][1]==0)) and touch==1:
        now=time.time()
        #Conditional statement to check if the color and the text match and if the user thinks it is wrong by pressing the touch sensor. The time is stored in a variable.
    elif ((questions[question][0]=="Green" and questions[color][1]!=0.25) or (questions[question][0]=="Blue" and questions[color][1]!=0.5) or (questions[question][0]=="Red" and questions[color][1]!=0)) and button==1:
        now=time.time()   
        #Conditional statement to check if the color and the text do not match and if the user thinks it is correct by pressing the button. The time is stored in a variable. 
    elif ((questions[question][0]=="Green" and questions[color][1]!=0.25) or (questions[question][0]=="Blue" and questions[color][1]!=0.5) or (questions[question][0]=="Red" and questions[color][1]!=0)) and touch==1:
        correct+=1
        now=time.time()
        #Conditional statement to check if the color and the text do not match and if the user thinks it is wrong by pressing the touch. The time is stored in a variable.
    lcd_clear()   
    reactiontime=now-then
    timelist.append(reactiontime)
    #The reaction time is calculated and stored in the list.
    then=0
print(correct)
makegraph(index,timelist,'question','reaction time','Performance')
#the graph is made.
