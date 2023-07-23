
def roll_call_dwarves(names):
    for i in range(len(names)):
        num = str(i+1) + '.'
        print(num, names[i])


def summon_captain_planet(calls):
    return[call.capitalize() + '!' for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheese_types = ['cheddar', 'gouda', 'camenber']
    for string in strings:
        if string in cheese_types:
            return string
    return None
