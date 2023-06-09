class CountPlayer:
    def players_count():
        print()
        while True:
            try:
                number_of_players=int(input("HOW MANY PLAYERS YOU WANT PLAY:"))
                if number_of_players==0:
                    print("enter number of players minimum1")
                else:
                    return number_of_players
                    
            except ValueError:
                print("Invalid input.please enter a number.")
                continue 
    


            