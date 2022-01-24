# This is treasure hunt game
import random
# Open new text file"
path= r"C:\Users\eviyt\OneDrive\Desktop\treasure hunt\Treasure Hunt game.txt"
path_2=r"C:\Users\eviyt\OneDrive\Desktop\treasure hunt\Treasure Hunt results.txt"

# Writing the first group of  numbers:
with open(path,"w") as game_File:
    number_0=str(0)* random.randint(1,20)
    number_1=str(1)* random.randint(1,20)
    number_2=str(2)* random.randint(1,20)
    number_3=str(3)* random.randint(1,20)
    number_4=str(4)* random.randint(1,20)
    number_5=str(5)* random.randint(1,20)
    number_6=str(6)* random.randint(1,20)
    number_7=str(7)* random.randint(1,20)
    number_8=str(8)* random.randint(1,20)
    number_9=str(9)* random.randint(1,20)
    sentence=str('Treasure')
# Writing to the file:
    list_Of_Numbers= number_0+number_1+number_2+number_3+number_4+number_5+number_6+number_7+number_8+number_9+sentence
    game_File.writelines(str(list_Of_Numbers))
#writing the second group of numbers:
with open(path,"a") as game_File:
    number_92 = str(9) * random.randint(1, 20)
    number_82 = str(8) * random.randint(1, 20)
    number_72 = str(7) * random.randint(1, 20)
    number_62 = str(6) * random.randint(1, 20)
    number_52 = str(5) * random.randint(1, 20)
    number_42 = str(4) * random.randint(1, 20)
    number_32 = str(3) * random.randint(1, 20)
    number_22 = str(2) * random.randint(1, 20)
    number_12 = str(1) * random.randint(1, 20)
    number_02 = str(0) * random.randint(1, 20)
# writing to the file:
    list_Of_Numbers2= number_92+number_82+number_72+number_62+number_52+number_42+number_32+number_22+number_12+number_02
    game_File.writelines(str(list_Of_Numbers2))

# lets start the game:
counter_steps= 0
how_many_tries= 0


with open(path,"r") as file_handler:
    print("your task is to find the word: Treasure")
    print("you can do it by moving to pointer foward or backward")
    print("press 1 to move foward or press 2 to move backward")
    name_of_player= input('Please enter your name:')
    print('Hey',name_of_player.upper(),"hope you are ready for the hunt!")
    print("_______________________")
    while True:
        moving_foward=1
        moving_backward=2
        pointer_positon=file_handler.seek(0)
        user_select=int(input("please enter 1 or 2:"))
        if user_select == 1:
            steps_foward=int(input("how many steps would you like to take foward:"))
            counter_steps= counter_steps+steps_foward
            pointer_positon=file_handler.read(file_handler.seek(counter_steps))[1]
            if pointer_positon.isdigit():
                how_many_tries= how_many_tries+1
                print(int(pointer_positon))
                pointer_positon ==  file_handler.seek(counter_steps -1)
                print('try again')
                print('______________________')
                continue
        if user_select == 2:
                steps_backward= int(input('how many steps would you like to take backward:'))
                counter_steps=counter_steps-steps_backward
                pointer_positon=file_handler.read(file_handler.seek(counter_steps))[1]
                if pointer_positon.isdigit():
                    how_many_tries = how_many_tries + 1
                    print(int(pointer_positon))
                    pointer_positon ==file_handler.seek(counter_steps-1)
                    print('try again')
                    print('______________________')
                    continue
                else:
                    pointer_positon.isalpha()
                    how_many_tries=how_many_tries+1
                    print(pointer_positon)
                    print('_____________________')
                    print('You have won!')
                    print("TREASURE HAVE BEEN FOUND")
                    print(name_of_player.upper(),"it took you",how_many_tries,"Tries")
                    break
        game_File.close()
        
#challenge:
with open(path_2,"a") as result_file:
    result_file.writelines(str(name_of_player.upper()))
    result_file.writelines("--")
    result_file.writelines(str(how_many_tries))
    result_file.writelines("_____")
    
    result_file.close()


        














































