import quize
import rockpapercessor

art = """
._ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _.
|                                 |
|     WELCOM TO MY python game    |
|        BY TEJAS AHIRRAO         |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
"""

print(art)

menu= """
select option from below

1. quize game
2. rock-paper-cessor

"""

print(menu)

menusel=int(input("please select calulator by index number: "))

if menusel == 1:
    quize.quizefunc()
if menusel== 2:
    rockpapercessor.code_not_available()
