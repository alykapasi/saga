choices = "Please select one of the following stories to modify:\n\
        1. Alice in Wonderland\n\
        2. Beauty and the Beast\n\
        3. A Christmas Carol\n\
        4. Cinderella\n\
        5. Snow White and the Seven Dwarfs\n\
        6. Little Red Riding Hood\n\
        7. Sleeping Beauty\n\
        8. Rapunzel\n\
        9. Rumpelstiltskin\n\
        10. Jack and the Beanstalk\n\
        11. The Legend of the Sleepy Hollow\n\
        12. Peter Pan\n\
        13. Phantom of the Opera\n\
        14. Winnie the Pooh\n\
        15. The Wizard of Oz\n\
        16. Treasure Island\n\
        17. The Little Mermaid\n\
        18. The Ugly Duckling\n\
        19. Thumbelina\n\
        20. Hansel and Gretel\n\
        21. The Emporer\'s New Suit\n\
        22. Puss in Boots\n\
        23. Goldilocks\n"

choice_list = ["Alice in Wonderland",
                "Beauty and the Beast",
               "A Christmas Carol",
               "Cinderella",
               "Snow White and the Seven Dwarfs",
               "Little Red Riding Hood",
                "Sleeping Beauty",
               "Rapunzel",
               "Rumpelstiltskin",
               "Jack and the Beanstalk",
               "The Legend of the Sleepy Hollow",
                "Peter Pan",
               "Phantom of the Opera",
               "Winnie the Pooh",
               "The Wizard of Oz",
               "Treasure Island",
                "The Little Mermaid",
               "The Ugly Duckling",
               "Thumbelina",
               "Hansel and Gretel",
               "The Emporer\'s New Suit",
                "Puss in Boots",
               "Goldilocks"]

role_list = ['Narrator', 'Existing Character', 'New Character']

def choose_story() -> int:
    while True:
        choice = input('Which story would you like to choose?: ')
        try:
            choice = int(choice)
            if choice in range(1,24):
                print(f'\nYou chose: {choice_list[choice-1]}\n')
                return choice
            else:
                print('Please input a number between 1-23...\n')
        except:
            print('Please input a number between 1-23...\n')

def choose_role() -> int:
    while True:
        choice = input('Which role would you like?:\n1. Narrator\n\
                       2. Existing Character\n3. New Character')
        try:
            choice = int(choice)
            if choice in range(1,3):
                print(f'\nYou chose the')