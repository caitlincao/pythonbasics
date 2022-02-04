#P2_Cao.py
#Caitlin Cao
#March 16, 2020
import random
import time

def adv_game():
    delay = 2
    user_name = input("Please enter your name: ")
    print("Welcome, "+user_name+", to the adventure game Pambie – Island of Zombies and Dragons!\n")
    gender = input("Do you want your character to be a male or a female?\n")
    char_name = input("What do you want to name your character?\n")

    friends = input("You can first name some of your friends on this island:\n")
    friends_list = friends.split()
    for i in range(len(friends_list)):
        if friends_list[i] == char_name or friends_list[i] == user_name:
            print("You can't have friend who has the same name as you!")
            friends_list.remove(friends_list[i])
            new_one = input("Please add another friend: ")
            friends_list.append(new_one)

    print("Your updated friend list is: ", friends_list)

    if gender == "male":
        print("You, "+char_name+", have been chosen to be the dragon's leader!\n")
        original_soldiers = random.randint(3000, 4000)
        print("You have "+str(original_soldiers)+" soldiers in your troop.")
        message = "Your rival tribal chief offers the marriage of you and his daughter, "
        message += "do you want to marry her?\n"
        marry = input(message)

        if marry == "yes":
            print()
            print("You are married to the daughter of the chief!")
            new_soldiers = random.randint(100, 1000)
            print("Your troops's size just increases "+str(new_soldiers)+ "!")
            soldiers = original_soldiers + new_soldiers
            print("You now have", str(soldiers), "soldiers.")
            print("You decide to fight the zombies now!")
            print()

            weathers = ["windy", "rainy", "sunny", "snowy", "cloudy"]
            print("There are five kinds of weather on which you can choose to launch the attack against the zombies:")
            print(weathers)
            print()
            for weatherday in weathers:
                answer = input("Do you want to fight the zombies on a "+weatherday+" day?\n")
                if weatherday != "cloudy" and answer == "yes":
                    time.sleep(delay)
                    print()
                    print("The zombies are agitated to EAT your soldiers' brains!")
                    print("You are defeated by the zombies on a "+weatherday+" day!")
                    break
                elif weatherday == "cloudy" and answer == "yes":
                    zombies = random.randint(3000, 4500)
                    if soldiers > zombies:
                        time.sleep(delay)
                        print()
                        print("You successfully defeat "+str(zombies)+" zombies with "+str(soldiers)+" soldiers! Congratulations!")
                        break
                    else:
                        time.sleep(delay)
                        print()
                        print(str(zombies), "zombies are agitated to EAT your soldiers' brains!")
                        print("YOU AND YOUR", str(soldiers), "SOLDIERS ARE ALL DEAD!")
                        print("All your friends", friends_list, "are very sad.")
                        break
                elif answer == "no" and weatherday != "cloudy":
                    continue
                else:
                    print("You decide not to fight the zombies on any days. Bye-bye!")
                    break

        elif marry == "no":
            print()
            print("So you don't want to marry her. Your troop size remains the same.")
            print("You still have", str(original_soldiers), "soldiers in your troop.")
            print()
            zombies = random.randint(3000, 4000)
            if original_soldiers > zombies:
                time.sleep(delay)
                print("You successfully defeat "+str(zombies)+" zombies with "+str(original_soldiers)+ " soldiers! Congratulations!")
            else:
                time.sleep(delay)
                print(str(zombies), "zombies are agitated to EAT your soldiers' brains")
                print("YOUR AND YOUR", str(original_soldiers), "SOLDIERS ARE ALL DEAD!")
                print("All your friends", friends_list, "are very sad.")

    else:   #female character
        print()
        print("You, "+char_name+", are the princess of the dragons!")
        fight = "yes"
        count = 0
        while fight != "no":
            print("The zombies are going to attack your dragons!")
            dragons = random.randint(100, 500)
            print("You now have", str(dragons), "dragons. One dragon can kill 3 zombies.")
            print()
            zombies = random.randint(300, 1500)
            count += 1
            if 3*dragons > zombies:
                time.sleep(delay)
                print("Your "+str(dragons)+" kill all "+str(zombies)+" zombies!!! Congratulations!")
                break
            else:
                time.sleep(delay)
                print("OH NOOOOO")
                print("All your "+str(dragons)+" dragons are eaten by "+str(zombies)+ " zombies.")

                time.sleep(delay)
                print("BUT the prince of another tribe asks to marry you and help you...")
                marriage = input("Do you want to marry him?\n")
                if marriage == "yes":
                    time.sleep(delay)
                    print("With your husband's help, your troop are able to recover a little bit...")
                    another = input("Do you want to fight the zombies again?\n")
                    if another == "yes":
                        continue
                    else:   #do not want to fight the zombies
                        print("You lose everything. Let's start over. T_T")
                        print("All your friends", friends_list, "are very sad.")
                        fight = "no"    #changing the variable to "no" will make it quit the while loop
                else:   #not choose to marry
                    print("You lose everything. Let's start over. T_T")
                    print("All your friends", friends_list, "are very sad.")
                    fight = "no"

        print()
        print("You have fought the zombies", count, "times in total.")

def main():
    adv_game()

main()
