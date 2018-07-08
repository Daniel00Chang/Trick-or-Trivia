from quizs.defaultQuiz import defaultQuiz as Parent

class halloween(Parent):

    def __init__(self):
        self._font = "Helvetica"
        self._bgColor = "black"
        self._fgColor = "green"
        self._quizName = "Trick or Trivia"
        self._titleColor = "white"
        self._secondaryColor = "red"

        # question, choice1, choice2, chioce3, choice4, correct answer, difficulty [difficulty][selection][data]
        # EASY
        self._quiz = [[["Casper is a friendly ____!", "Ghost", "Ghast", "Ghoul", "Gremlin", 1],
                       ["Dracula is a _______.", "Snake", "Zombie", "Vampire", "pokemon", 3],
                       ["Put a light in the _______ \nto light up its face.", "window", "pumpkin", "doorway", "refrigerator", 2],
                       ["Witches love to fly around \non a _____.", "vacuum cleaner", "jet plane", "dragon", "broomstick", 4],
                       ["Halloween is on which day?", "Oct 13", "Oct 31", "Nov 1", "Abc 45", 2],
                       ["A _______ costume is scary \nbecause he wears fangs.", "robot", "mighty mouse", "vampire", "turkey", 3],
                       ["To make a Jack o'Lantern  \nyou carve a ______.", "pumpkin", "birthday cake", "carrot", "watermellon", 1],
                       ["Kids love to get _____ when \nthey go trick or treating!", "Fruit", "Cereal", "Kittens", "Candy", 4],
                       ["What room do ghosts avoid?", "bathroom", "kitchen", "living room", "closet", 3]],  # end Easy

                      # MEDIUM
                      [["Pumpkins are a: ", "fruit", "vegetable", "mineral", "arthropod", 1],
                       ["Who is the avid believer \nin the great pumpkin?", "Lucy", "Linus", "Charlie Brown", "John Cena!", 2],
                       ["Which Disney princess rode \nto the ball in a pumpkin?", "Tianna", "Cinderella", "Snow White", "Shrek", 2],
                       ["Every Halloween, Charlie Brown helps his \nfriend Linus wait for what character to appear?", "The Great Pumpkin", "Dracula", "Snoopy", "Pikachu", 1],
                       ["How do pumpkins grow?", "on vines", "under ground", "in a bush", "in a tree", 1],
                       ["Which country celebrates the Day of the \nDead starting at midnight on Oct. 31?", "China", "Canada", "America", "Mexico", 4],
                       ["Pumpkins can be orange, white, green, or what other color?", "Purple", "Lavendar", "Black", "Blue", 4],
                       ["Complete the following chant, normally said \nby witches: double, double, toil and …?", "Rubble", "Bubble", "Stubble", "Trouble", 4],
                       ["What type of vegetable is disliked by \nvampires and is used to frighten them away?", "Carrots", "Ginger", "Garlic", "Salt", 3]],  # end Medium

                      # HARD
                      [["Pumpkins are made up of \nhow much water?", " 30% ", " 50% ", " 90% ", " OVER 9000% ", 3],
                       ["The largest pumpkin ever \ngrown weighed how much?", "844 lbs", "1,140 lbs", "2,091 lbs", "3,000,000 lbs ", 3],
                       ["Pumpkins contain \nsignificant amounts of: ", "potassium and Vit A", "magnesium and Vit C", "folate and Vit D", "free shavacado", 1],
                       ["What variety is the \ntraditional Halloween pumpkin?", "Autumn Gold", "Conneticut Field", "Baby Boo", "Orange", 2],
                       ["Pumpkins are grown on \nhow many continents?", "2", "5", "6", "9", 3],
                       ["The first Jack-o-Lanterns \nwere made out of what?", "Watermelons", "Cantaloupe", "Turnips", "Pumpkins", 3],
                       ["The average American household \nspends how much on Halloween candy?", "$28", "$35", "$44", "$52", 3],
                       ["Where did Halloween originate?", "England", "America", "Scotland", "Ireland", 4],
                       ["Which is the top-selling \ncandy for Halloween?", "Snickers", "Candy Corn", "M&Ms", "Reese's", 2],
                       ["Which day of the year \nhas the highest candy sales?", "Oct 28th", "Oct 29th", "Oct 30th", "Oct 31st", 1],
                       ["Of the $1.9 billion in candy sales, how \nmuch of it is from chocolate candy?", "$1 billion", "$1.2 billion", "$1.5 billion", "$1.7 billion", 2],
                       ["The days leading up to Halloween account \nfor what % of the year's candy sales?", " 10% ", " 15% ", " 20% ", " 23% ", 1],
                       ["What does the English \nword HALLOW mean?", "Sin", "Spirit", "Saint", "Spook", 3],
                       ["What phobia do you suffer from if you \nhave an intense fear of Halloween?", "Phasmophobia", "Samhainophobia", "Wiccaphobia", "Halloweenphobia", 2],
                       ["Halloween, the movie was \nmade in 1978 on a low \nbudget in how many days?", "12 days", "21 days", "30 days", "35 days", 2],
                       ["According to legend, a unibrow, tattoos, \nand a long middle finger, are signs \nof which Halloween creature?", "Werewolf", "Witch", "Vampire", "Golem", 1],
                       ["Which celebrity does not \nhave a Halloween Birthday?", "Vanilla Ice", "Dan Rather", "Peter Jackson", "Kevin Bacon", 4]]  # end Hard
                      ]  # end quiz[]
