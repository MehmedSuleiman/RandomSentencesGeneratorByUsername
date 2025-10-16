import random

def grt_rondom_wors(words):
    return  random.choice(words)

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbes = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbes = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

print("Hi, this is your first sentence :")

while True:
    rondom_names = grt_rondom_wors(names)
    rondom_places = grt_rondom_wors(places)
    rondom_verbes = grt_rondom_wors(verbes)
    rondom_nouns = grt_rondom_wors(nouns)
    rondom_adverbes = grt_rondom_wors(adverbes)
    rondom_details = grt_rondom_wors(details)
    print(f"{rondom_names} from {rondom_places} {rondom_adverbes} {rondom_verbes} {rondom_nouns}")
    break