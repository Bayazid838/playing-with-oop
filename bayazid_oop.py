class Person:

    def __init__(self, name, gender, age, isStudent, birthday, likes, goals, hobbies, struggles, subjects, strengths, weakness, ambitions, routine, languages, interests):
        self.name = name
        self.gender = gender
        self.age = age
        self.isStudent = isStudent
        self.birthday = birthday
        self.likes = likes
        self.goals = goals
        self.hobbies = hobbies
        self.struggles = struggles
        self.subjects = subjects
        self.strengths = strengths
        self.weakness = weakness
        self.ambitions = ambitions
        self.routine = routine
        self.languages = languages
        self.interests = interests

    def wakeup(self):
        print("Madara: WAKE UP TO REALITY! \n" + self.name +  " woke up from sleep")
    
    def sleep(self):
        print(self.name + " is sleeping ...AS USUAL LMFAO")
    
    def eat(self):
        print(self.name + " is eating. This guy will always be skinny smh")
    
    def bath(self):
        print(self.name + " is bathing")
    
    def walk(self):
        print(self.name + " is walking")
    
    def run(self):
        print(self.name + " is running")
    
    def talk(self):
        print(self.name + " is talking")
    
    def work(self):
        print(self.name + " is doing work")
    
    def study(self):
        print(self.name + " is studying " + ', '.join(self.subjects))
    
    def do_hobbies(self):
        print(self.name + " is doing hobbies like " + ', '.join(self.hobbies))
    
    def pursue_ambitions(self):
        print(self.name + " is pursuing ambitions in " + ', '.join(self.ambitions))
    
    def language_skills(self):
        print(self.name + " knows " + ', '.join(self.languages))

    def reflect_on_struggles(self):
        print(self.name + " is working on overcoming struggles like " + ', '.join(self.struggles))
    
    def routine_summary(self):
        print(self.name + " follows a routine of " + ', '.join(self.routine))


# Adding all your details to the Bayazid object
Bayazid = Person(
    name="Bayazid Bostami Sinha", 
    gender="Male", 
    age=16, 
    isStudent=True, 
    birthday="26,5,2008", 
    likes=["Coding", "Web Development", "Anime", "Gaming", "Physics", "Astronomy", "Leadership", "Improvement"], 
    goals=["Achieve A* in all subjects", "Master programming", "Pursue astronomy"], 
    hobbies=["Learning new skills", "Singing", "Playing games", "Watching anime"], 
    struggles=["Procrastination", "Distractions (social media, etc.)", "Self-doubt", "Managing time during Ramadan"], 
    subjects=["English 0500", "Maths D 0850", "Bangla 3204", "Physics 0625", "Chemistry 0620", "Biology 0610", "Computer Science 0478", "Add Math 0606"], 
    strengths=["Strong at physics and chemistry", "Coding skills", "Leadership qualities", "Determination to improve"], 
    weakness=["Attention span in Bangla", "Maths D struggles", "Lack of confidence at times"], 
    ambitions=["Pursue a career in astronomy", "Excel in physics and computer science", "Help others through leadership"], 
    routine=["Waking up at 3 AM", "Fasting during Ramadan", "Study sessions", "Prayer and Taraweeh", "Physical exercise", "Quran reflection", "Restoring singing skills", "Working on coding projects"], 
    languages=["English", "Bangla", "Japanese (learning)"], 
    interests=["Astrophysics", "Computer science", "Anime", "Gaming", "Web development", "Blockchain"]
)


print("This is just a bs I made cause I was bored don't take it seriously guys")