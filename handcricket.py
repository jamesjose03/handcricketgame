#Hand Cricket Game
import random,time
list=["Hand","Cricket","Game!!!"]
def bowl():
        print ("The game starts now! You are bowling! All the best!")
        print("Enter the number of overs to play: ")
        over=int(input())
        balls=over*6
        comptotal=0
        thrownballs=0
        while thrownballs<balls:
                print("Enter the number you guess: ")
                guess=int(input())
                if guess<=6:
                        comprun=random.randint(0,6)
                        if guess==comprun:
                                print("Out! Computer scored: ",comptotal," runs.")
                                break
                        else:
                                print("You guessed wrong! Computer scores: ",comprun," runs.")
                                comptotal=comptotal+comprun
                                thrownballs=thrownballs+1
        print("End of ",over," overs.")
        print("Time to bat! Target is: ",comptotal+1," runs. All the best!")
        scorebat=0
        thrownballs=0
        while thrownballs<balls:
                run=int(input("Enter the run you want to score in this ball: "))
                if run<=6:
                        compguess=random.randint(0,6)
                        if run==compguess:
                                print("Out! You scored: ",scorebat," runs.")
                                break
                        else:
                                scorebat=scorebat+run
                                print("Computer guessed: ",compguess, "You score: ",run,"runs! ",(comptotal+1)-scorebat," more runs needed to win!")
                                
                                if scorebat>comptotal+1:
                                        print ("You win! Congratulations!!!")
                                        break
                                else:
                                        thrownballs=thrownballs+1
                else:
                        print("Invalid input! Disqualified!!!")
                        break
        if scorebat<comptotal+1:
                print ("Computer wins! Sorry, try again next time....")
        

def bat():
    print ("The game starts now! You are batting! All the best!")
    print ("Enter the number of overs to play: ")
    over=int(input())
    balls=6*over
    thrownballs=0
    scorebat=0
    while thrownballs<balls:
        print ("Enter the run you want to score in this ball: ")
        run=int(input())
        if run<=6:
            compguess=random.randint(0,6)
            if run==compguess:
                print ("Out! You scored: ",scorebat," runs.")
                break
            else:
                print ("Computer guessed: ",compguess, "You score: ",run," runs!")
                scorebat=scorebat+run
                thrownballs=thrownballs+1
        else:
            print("Invalid input! Disqualified")
            break
    print ("End of ",over," overs.", "You scored: ",scorebat,"Target: ",scorebat+1)
                        
    print ("Time to bowl!") 
    print("You are bowling now! All the best!")
    compbat=0
    thrownballs1=0
    while thrownballs1<balls:
        print("Enter the number you guess: ")
        guess=int(input())
        if guess<=6:                		
            comprun=random.randint(0,6)
            if guess==comprun: 
                print ("Out!, Computer scored: ", compbat, "runs.")
                if compbat>=scorebat+1:
                    print("Computer wins!! Sorry, try again later...")
                    break
                else:
                    print("You win! Congratulations!!!")
                    break
            else:
                print("You guessed wrong! Computer scores: ",comprun," runs.")
                compbat=compbat+comprun
				
                if compbat>=scorebat+1:
                    print ("Computer wins! Sorry, try again next time...")
                    break
                else:
                    thrownballs1=thrownballs1+1


#print ("Hand Cricket Game!!!")
for i in list:
         print(i,end=" ")
         time.sleep(0.7)
print()
print (" Toss: Heads or Tails? \n Choice: ")
while True:
	try:
		choice=input()
		if choice == "Heads" or choice == "heads":
		    toss_called = "Heads"
		    break
		elif choice == "Tails" or choice == "tails":
		    toss_called = "Tails"
		    break
		else:
            		print("You entered invalid choice: ", choice)
            		continue
	except ValueError:
        	print("You entered invalid key")
        	continue
myList=["Heads","Tails"]

tossch=random.choice(myList)
if(tossch=="Heads"):
        toss="Head"
else:
        toss="Tail"
if(choice==tossch):
                userchoice=input("You won the toss! Bat or Bowl? \n Choice: ")
                userchoice=userchoice.lower()
                if(userchoice=="bat"):
                        bat()
                elif userchoice=="bowl":
                        bowl()
                else:
                        print ("Wrong input")
else:
        print("Sorry, you lost the toss!")
        compchoice=["Bat","Bowl"]
        tosscomp=random.choice(compchoice)
        if(tosscomp=="Bat"):
                print("Computer chose to Bat, you bowl!")
                bowl()
        else:
                print("Computer chose to Bowl, you bat!")
                bat()
        
						
	
					
				
