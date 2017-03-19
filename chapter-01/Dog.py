
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
