# Write your code here.

# Task 1: Hello
def hello():
    return "Hello!"

# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"

# Task 3: Calculator
def calc( a, b, operation = "multiply"):
    try:
        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a - b
        elif operation == "divide":
            try:
                return a/b
            except ZeroDivisionError:
                return("You can't divide by 0!")
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            return a * b
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4: Data Type Conversion
def data_type_conversion(value, type):

    # name = ''
    # if type == "int":
    #     name = int
    # elif type == "str":
    #     name = str
    # else:
    #     name = float

    # Cleaner
    type_dict = {
        "int": int,
        "str": str,
        "float": float
    }

    try:
        name = type_dict.get(type)
        return name(value)
    except (ValueError,TypeError):
        return f"You can't convert {value} into a {type}."
    
# Task 5: Grading System, Using *args
def grade(*args):
    # We get args. --> args is a tuple
    # 1. Calc avg
    # 2. Compare avg in A-F grade scale 
    # 3. retun str "A" - "F"

    #ERROR HANDLING
    try:
        # Calculate avg
        avg = sum(args)/len(args)
        # Compare grade scale
        if avg >= 90:
            return "A"
        elif avg < 90 and avg >= 80:
            return "B"
        elif avg < 80 and avg >= 70:
            return "C"
        elif avg < 70 and avg >= 60:
            return "D"
        else:
            return "F"
    except (ValueError, TypeError): 
        return "Invalid data was provided."

# Task 6: Use a For Loop with a Range
def repeat(string, count):
    # use for loop and range
    # thinking of a for loop with range(count) then just adding the string at the end... have answer string to return
    ans = ''
    for i in range(count):
        ans += string
    return ans

# Task 7: Student Scores, Using **kwargs
def student_scores(positional_arg, **kwargs):
    # print(kwargs[max(kwargs.values())])

    if positional_arg == "best":
        highest_score = 0
        top_name = ''
        for key, value in kwargs.items(): 
            if value > highest_score: #if current value is greater than the highest score we've accessed, then we write down that person and make the new highest_score that person's score
                highest_score = max(highest_score, value) 
                top_name = key
        return top_name
    else:
        return sum(kwargs.values())/len(kwargs.values())
# print(student_scores("best", Tom=75, Dick=89, Angela=91, Frank=50 ))

# Task 8:Titleize, with String and List Operations
def titleize(string):
    #split() method returns list
    #words = ['war', 'and' , 'peace']
    #little words list? so if word is in that list, dont capitalize
    #join() to join them back and capitalize() to capitalize the word

    #initialize answer string
    ans = ""
    #initialized little_words list
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    #take in the string then split them into a list
    words = string.split()
    last_i = len(words)-1

    for i, word in enumerate(words):
        if i != 0 and i != last_i and word in little_words:
            continue
        words[i] = word.capitalize()
    ans = ' '.join(words)
    return ans

# print(titleize("war and peace"))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    #input: str, str
    #output: str

    #if user inputs some letters, the return value is a string that only shows the letters of user's guess, while "_" for letters not in the guess
    #strings are immutable = can't change in place/ after it was created

   #intialize secret list with [_,_,...] length og secret
   #then loop into secret list and ask if that letter in secret is in the guess
   #then just change that spot in the list into the letter in that same spot from secret

    secret_list = ["_"] * len(secret)
    for i, letter in enumerate(secret_list):
        if secret[i] in guess:
            secret_list[i] = secret[i]
    return "".join(secret_list)

# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(string):
    # (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. \\
    # (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. \\
    # (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
    # could do cleaner code
    words = string.split()
    vowels = "aeiou"
    ans = ""

    for i, word in enumerate(words):
        #CASE 1: pig_latin("apple") == "appleay"
        if word[0] in vowels:
            ans = word + "ay"
            words[i] = ans
            continue

        #CASE 2: a1.pig_latin("banana") == "ananabay"
        j = 0
        consonants = ""
        while j < len(word) and word[j] not in vowels:
            if word[j] == "q" and j + 1 < len(word) and word[j+1] == "u": #CASE 3: "qu"
                j+=2
                consonants += "qu"
                break
            else:
                consonants += word[j]
                j+=1
        ans = word[j:]+ consonants +"ay"
        words[i] = ans
    return " ".join(words)

# print(pig_latin("banana"))
# print(pig_latin("the quick brown fox"))