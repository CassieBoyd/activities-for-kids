"""
Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

For example, Jay ran like a fool! or Chantelle slid down the slide!.
"""

def run(kid):
    print(f"Run, {kid}, run!")


def swing(kid):
    print(f"{kid} is swingin' in the rain, just swingin' in the rain")

def slide(kid):
    print(f"{kid} broke on through to the other slide!")

def hide_and_seek(kid):
    print(f"Ready or not, {kid} will find you and they will kill you!")

"""
The following lists of children should be iterated, and the names sent to the appropriate functions.
"""

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

kid = "Will"

if kid in running_kids:
    run(kid)
elif kid in swinging_kids:
    swing(kid)
elif kid in sliding_kids:
    slide(kid)
elif kid in hiding_kids:
    hide_and_seek(kid)
