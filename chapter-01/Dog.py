
class Dog:

    def __init__(self, name, month, day, year, speak_text):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speak_text = speak_text

    def speak(self):
        return self.speak_text

    def get_name(self):
        return self.name

    def birth_date(self):
        return "%s/%s/%s" % (str(self.month), str(self.day), str(self.year))

    def change_bark(self, bark):
        self.speak_text = bark

    def __add__(self, other_dog):
        name = "Puppy of %s and %s" % (self.name, other_dog.name)
        speak_text = self.speak_text + other_dog.speak_text
        return Dog(name, self.month, self.day, self.year + 1, speak_text)

def main():
    boy_dog = Dog("Mesa", 5, 15, 2004, "WOOF")
    girl_dog = Dog("Sequoia", 5, 6, 2004, "Bark")

    print(boy_dog.speak())
    print(girl_dog.speak())
    print(boy_dog.birth_date())
    print(girl_dog.birth_date())
    boy_dog.change_bark("woofywoofy")
    print(boy_dog.speak())

    puppy = boy_dog + girl_dog
    print(puppy.speak())
    print(puppy.get_name())
    print(puppy.birth_date())

if __name__ == "__main__":
    main()
