class defaultQuiz():

    def __init__(self):
        self._font = "Times"
        self._bgColor = "black"
        self._fgColor = "red"
        self._quizName = "defaultQuiz"
        self._titleColor = "white"
        self._secondaryColor = "green"

        # question, choice1, choice2, chioce3, choice4, correct answer, difficulty [difficulty][selection][data]
        # EASY

        self._quiz = [[["Is this question easy", "No", "Heck no", "Yup", "Naaaa", 3],
                   ["This is a test question", "Don't choose me", "Click here", "Do not touch", "...", 2]],  # end Easy

                  # MEDIUM
                  [["Medium? ", "Yes", "No", "noo", "NOOOOOOOOOO", 1]],  # end Medium

                  # HARD
                  [["You chose hard right?", " I don't remember ", " No ", " nope ", " Yes ", 4]]  # end Hard
                  ]  # end quiz[]

    def getQuiz(self):
        return (self._quiz)

    def getFont(self):
        return (self._font)

    def getBGColor(self):
        return (self._bgColor)

    def getFGColor(self):
        return (self._fgColor)

    def getQuizName(self):
        return (self._quizName)

    def getTitleColor(self):
        return (self._titleColor)

    def getSecondaryColor(self):
        return (self._secondaryColor)
