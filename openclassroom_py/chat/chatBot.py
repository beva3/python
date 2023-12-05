health = {
    "hello" : "hello how are you",
    "how are you":"he i'm fine thanks",
}

def assistant():
    while True:
        q = input("He my friends, can i assiste you now : ")
        if q in health:
            print(health[q])
        else :
            print("sory i'm just IA lests move on")

assistant()