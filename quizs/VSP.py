from quizs.defaultQuiz import defaultQuiz as Parent

class VSP (Parent):

    def __init__(self):
        self._font = "Times"
        self._bgColor = "#325665"
        self._fgColor = "#86CBDF"
        self._quizName = "VSP Trivia"
        self._titleColor = "white"
        self._secondaryColor = "#A2C534"

        # question, choice1, choice2, chioce3, choice4, correct answer, difficulty [difficulty][selection][data]
        # EASY

        self._quiz = [[["Which is not a branch of VSP", "VSP Vision Care", "Marchon", "Ultair", "Eyefinity", 3],
                    ["How many members do we have?", "1,000-99,999", "100,000-999,999", "1-80 Million", "80 Million+", 4],
                    ["Where did VSP originate?", "Oakland", "New York", "Los Angeles", "San Francisco", 1],
                    ["When was VSP founded?", "1940's", "1950's", "1960's", "2020's", 2],
                    ["How many buildings are in the Rancho campus?", "1", "3", "5", "8", 3],
                    ["What does VSP stand for?", "Vision Service Planet", "Very Strong Pupils", "Vision Service People", "Vision Service Plan", 4]
                    ],  # end Easy

                  # MEDIUM
                  [["Roughly how many doctors are in our network?", "4,000", "18,000", "39,000", "88,000", 3],
                   ["When was VSP founded?", "1952", "1953", "1954", "1955", 4],
                   ["When did VSP change its name from CVS?", "1960's", "1970's", "1980's", "1990's", 2],
                   ["How many employees did VSP have in 1994?", "300", "1,000", "4,000", "over 9,000", 2],
                   ["When did HQ5 open?", "2008", "2010", "2012", "2014", 4]
                   ],  # end Medium

                  # HARD
                  [["When did VSP move to Sacramento?", " 1962 ", " 1965 ", " 1968 ", " 1970 ", 2],
                   ["What was VSP's original name?", "Golden State Vision", "California Vision Services", "California Vision Company", "Oakland Vision", 2],
                   ["Who was the first president and CEO of VSP?", "John O'Donnell", "Jim McGrann", "Roger Valine", "Michael Guyette", 1],
                   ["In the 1980s, how many members did VSP have?", "87,000", "450,000", "1.2 Million", "2.4 million", 4],
                   ["When did VSP launch Altair-Eyewear?", "1981", "1988", "1992", "1997", 3],
                   ["What year did VSP loaunch Eyefinity?", "1998", "1999", "2000", "2001", 3],
                   ["Where did VSP launch its second high-tech optical lab?", "Columbus, OH", "Sacramento, CA", "Lewisville, TX", "Folsom, Ca", 1],
                   ["Where did VSP launch its third high-tech optical lab?", "Columbus, OH", "Sacramento, CA", "Lewisville, TX", "Folsom, Ca", 3]
                   ]  # end Hard
                  ]  # end quiz[]