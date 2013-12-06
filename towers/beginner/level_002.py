#  --------
# |@   s  >|
#  --------

level.description("It is too dark to see anything, but you smell sludge nearby.")
level.tip("Use warrior.feel.empty? to see if there is anything in front of you, and warrior.attack! to fight it. Remember, you can only do one action (ending in !) per turn.")
level.time_bonus(20)
level.ace_score(26)
level.size(8, 1)
level.stairs(7, 0)
def a_func(warrior):
    warrior.add_abilities('walk')
level.warrior(0, 0, 'east', func=a_func)
level.unit('sludge', 4, 0, 'west')