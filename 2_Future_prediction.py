import random 
import datetime

def gen_random_prediction():
    prediction = [
        "You will meet someone who will change your life soon!",
        "A big opportunity is coming your way, stay ready!",
        "Unexpected money will come to you when you least expect it!",
        "You will travel to a place you've always wanted to visit!",
        "A new skill you learn this year will bring success!",
        "Your hard work will pay off in ways you never imagined!",
        "A mysterious massage will change your perspective on life!",
        ]
    return random.choice(prediction)

def gen_lucky_number(birth_year):
    return (birth_year * random.randint(1, 9)) % 100


def gen_personality_trait(name):
    trait = ["Brave", "Creative", "Intelligent", "Kind", "Adventurous", "Focused", "Visionary"]
    return trait[sum(ord(char) for char in name) % len(trait)]

def main ():
    print(f"Welcome to the Python Future predictor! ")
    
    name = input("Enter your name: ")
    
    birth_year = int(input("Enter your birth year (e.g 2004): "))
    
    age = datetime.datetime.now().year - birth_year
    
    lucky_number = gen_lucky_number(birth_year)
    persnolity = gen_personality_trait(name)
    prediction = gen_random_prediction()
    
    print(f'''              Name: {name}
              Age: {age}
              lucky Number: {lucky_number}
              Personality Trait: {persnolity}
              Prediction: {prediction}
              ''')
    
if __name__ == "__main__":
    while True:
        main()
    