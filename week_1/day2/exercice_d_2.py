#exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dics= dict(zip(keys,values))
print(dics)

#exercice 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total =0
for name,age in family.items():
    if age <3:
        price=0
    elif 3 <= age <= 12:
        price =10
    else:
        price=15
    print(f"{name} has to pay ${price}")
    total +=price
print(f"the total price for the family is ${total}")

#exercice 3
brand ={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"]=2
print(brand["number_stores"])

print(f"zara's client are {brand['type_of_clothes']}")
brand["contry_creation"]= "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

del brand["creation_date"]
print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

more_on_zara={
    "creation_date": 1975,
    "number_stores": 10000

}
brand.update(more_on_zara)
print(brand["number_stores"])

#exercice 4
def describe_city(city, contry='belize'):
    print(f"{city} is in {contry}")

describe_city('belmopan')
describe_city('belize city')
describe_city('orange walk town')

#exercice 5
import random
def khtar_num(user_num):
    random_n=random.randint(1,100)
    if user_num == random_n:
        print(f"success!  both are {user_num}")
    else:
        print(f"failed! you chose {user_num} but the number is {random_n}")
inp=int(input("enter a number between 1 and 100:"))
khtar_num(inp)

#exercice 6
def make_shirt(size,style):
    print(f"you have ordered a {style} shirt of size {size}")
make_shirt("large","call me MARYAMA")

def make_shirt(size="large",style="I love Python"):
    print(f"the size of the shirt is {size} and the syle is '{style}'")
make_shirt()
make_shirt(style="I love chocolate")
make_shirt(size="medium")
make_shirt("small", "don' give up")
make_shirt( style="your weight doesn't define you",size="XXL")

#exercice 7
import random
def get_random_temp():
    return random.randint(-10,40)
def main():
    temp=get_random_temp()
    print(f"the temperature today is {temp}°C")
    if temp<0:
        print("Brrr, it's freezing! Wear some extra layers today!!!")
    elif 0<= temp <16:
        print("Quite chilly! Don't forget your coat")
    elif 16<= temp <23:
        print("Perfect wheather")
    elif 23<= temp <32:
        print("It's sunny, enjoy your day")
    elif 32<= temp <40:
        print("It’s really hot! drink plenty of water today")
    
def get_random_temp(season):
    if season == "winter":
        return random.uniform(-10,16)
    elif season == "spring":
        return random.uniform(10,23)
    elif season == "summer":
        return random.uniform(24,40)
    elif season == "autumn":
        return random.uniform(5,20)
    else:
        return random.uniform(-10,40)

def main():
    season= input("enter a season (winter, spring, summer, autumn): ").lower()
    temp = get_random_temp(season)
    
    print(f"the temperature right now is {temp:.1f}°C")
    if temp <0:
        print("Brrr, it's freezing! Wear some extra layers today!!!")
    elif 0<= temp <16:
        print("Quite chilly! Don't forget your coat")
    elif 16<= temp <23:
        print("Perfect wheather")
    elif 23<= temp <32:
        print("It's sunny, enjoy your day")
    elif 32<= temp <40:
        print("It’s really hot! drink plenty of water today")

def m_season(mounth):
    if mounth in [12,1,2]:
        return "winter"
    elif mounth in [3,4,5]:
        return "spring"
    elif mounth in [6,7,8]:
        return "summer"
    else:
        return "autumn"
mounth= int(input("enter the mounth as a number (1-12):"))
season= m_season(mounth)
temp =get_random_temp(season)
main()

#exercice 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def question_game(data):
    correct = 0
    wrong = 0
    w_answer = []
    for item in data:
        user_ans = input(f"{item['question']} ")
        if user_ans.lower() == item["answer"].lower():
            print("✅ Correct!\n")
            correct += 1
        else:
            print("❌ Wrong!\n")
            wrong += 1
            w_answer.append({
                "question": item["question"],
                "your_answer": user_ans,
                "correct_answer": item["answer"]
            })
    return correct, wrong, w_answer


def result(correct, wrong, w_answer):
    print(f"\nYou got {correct} correct and {wrong} wrong")
    if wrong > 0:
        print("\nHere are the questions you got wrong:")
        for item in w_answer:
            print(f"Q: {item['question']}")
            print(f"   Your answer: {item['your_answer']}")
            print(f"   Correct answer: {item['correct_answer']}\n")


def main():
    while True:
        correct, wrong, w_answer = question_game(data)
        result(correct, wrong, w_answer)

        if wrong > 3:
            print("You got more than 3 wrong, you lose :( Try again!!\n")
            rply = input("Do you want to play again? (yes/no): ").lower()
            if rply != "yes":
                print("Thank you for playing, bye!")
                break
            else:
                print("Great! Let's play again\n")
        else:
            print("🎉 Well done!")
            break


main()