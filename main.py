import random 
import time

print("Some men receive a feminine spirit whose invisible beauty stimulates their imagination, and whose power of seduction ignites the fire of creativity. They are muses of darkness, for they are always near like a shadow, but of light, for they bring inspiration.")
time.sleep(5)
print("The hidden lovers of great poets, painters, and artisans, those who manipulate the sexual energy of the mind, that is, the energy for creating beauty, not children of flesh.")
time.sleep(5)
print("Could you be one of those blessed with a guardian succubus? Answer the 5 questions from the 5 stars and discover what the secret alchemy will reveal about you.")
time.sleep(5)
# define the personality and message
month = int(input("\nThe mystic Moon asks for your month of birth (1-12): "))
day = int(input("The mystic Moon asks for your day of birth (1-31): "))

# define the body type
first_letter = input ("The wise Mercury asks for the initial letter of your first name: ").upper() 

# define the appendix
last_letter = input ("The beautiful Venus asks for the initial letter of your last name: ").upper()

# define the face shape
age = input ("The glorious Sun asks for the second digit of your age (0-9): ") 

# define the color of her skin
eyes = input ("The passionate Mars asks for the color of your eyes (red, blue, turquoise, green, brown or black): ").lower()

personality = ""
appendix = ""
color = ""
face = ""
body = ""

# COLOR
if eyes == "red":
    color = random.choice(["blood red", "flaming orange", "electric pink"])
elif eyes == "blue":
    color = random.choice(["late afternoon sky blue", "saltwater blue", "blue like veins under pale skin"])
elif eyes == "turquoise":
    color = random.choice(["freshwater blue", "green like grass at dawn", "cyan like a rare jewel"])
elif eyes == "green":
    color = random.choice(["shimmering emerald green", "nocturnal forest green", "futuristic neon green"])
elif eyes == "brown":
    color = random.choice(["brown like milk chocolate", "brown like noble wood", "brown like polished bronze"])
elif eyes == "black":
    color = random.choice(["starless sky color", "dragon's throat color", "lustrous black leather"])

# BODY
if first_letter in "ABCDE":
    body = "hourglass-shaped"
elif first_letter in "FGHIJ":
    body = "inverted triangular"
elif first_letter in "KLMNO":
    body = "pear-shaped"
elif first_letter in "PQRST":
    body = "triangular"
elif first_letter in "UVWXYZ":
    body = "rectangular"


# FACE
faces = [
    "rounded face with long, straight hair",         
    "rounded face with short, curly hair and bangs",          
    "heart-shaped face with braided hair",             
    "heart-shaped face with long hair",         
    "inverted triangle-shaped face with short hair",         
    "inverted triangle-shaped face with dreadlocks",          
    "rectangular face with braided hair",         
    "elliptical face with wavy hair",
    "heart-shaped face with wavy hair",       
    "heart-shaped face with dreadlocks"        
]

face = faces[int(age)]


# APPENDIX
if last_letter in "ABCD":
    appendix = "long wings and thin, vertical horns"
elif last_letter in "EFGH":
    appendix = "several soft tails and two short horns, long pointed ears"
elif last_letter in "IJKL":
    appendix = "four elegant wings, curved horns leaning to the sides"
elif last_letter in "MNOP":
    appendix = "6 crown-like horns and four majestic wings"
elif last_letter in "QRST":
    appendix = "four thick horns, a long, thick tail"
elif last_letter in "UVW":
    appendix = "a long serpent tail instead of legs, and two horizontal horns"
elif last_letter in "XYZ":
    appendix = "elfin ears and small delicate wings"

# PERSONALITY
def get_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

sign = get_sign(day, month)

personalities = {
    "Aries": "impulsive, fiery and passionate about creation — a creative force that burns without asking for permission.",
    "Taurus": "sensual, patient and devoted, with an almost sacred pleasure for every detail of the creative work.",
    "Gemini": "versatile and curious, changing form and idea with the same lightness of an inspiring breeze.",
    "Cancer": "protective, emotional and intuitive, nurturing each idea like a mother cares for a child of dreams.",
    "Leo": "confident and radiant, a muse who demands to be seen, leading you to greatness with her royal flame.",
    "Virgo": "meticulous, critical and analytical, transforms chaos into perfection with fingers of divine precision.",
    "Libra": "elegant and harmonious, sees beauty even in imbalance and guides you through the aesthetics of the heart.",
    "Scorpio": "intense and magnetic, dives deep into the creator's soul, where desire and power intertwine.",
    "Sagittarius": "free and visionary, laughs at limits and transforms art into transcendental adventure.",
    "Capricorn": "disciplined and ambitious, builds empires of beauty with firm hands and an implacable gaze.",
    "Aquarius": "rebellious and innovative, channels the future, where art and science dance in perfect dissonance.",
    "Pisces": "dreamy and empathetic, made from the very substance of dreams — inspirations in liquid form."
}

personality = personalities[sign]


messages = {
    1: "Let curiosity be your compass and passion your fuel.",
    2: "Create for the joy of it, not just the outcome.",
    3: "Your unique perspective is your greatest creative asset.",
    4: "Don't let the fear of a blank page stop you from writing your story.",
    5: "Passion is the engine; consistency is the key that starts it.",
    6: "The world needs the art that only you can make.",
    7: "Follow the work that makes you lose track of time.",
    8: "A masterpiece is just a series of small, passionate acts.",
    9: "Your passion is a quiet whisper; learn to listen for it.",
    10: "Create bravely, even if your voice shakes.",
    11: "Done is better than perfect when you're starting out.",
    12: "Nurture your passions, for they are the seeds of your future."
}

time.sleep(3)
print("\nThe ancestral wisdom whispers to you the secrets of creation...\n")
time.sleep(3)
print(f"Your guardian succubus has beautiful {color} skin, tinting her sculptural {body} body, "
      f"crowned by a beautiful {face}, with {appendix}. Although she is a creature made from the substance of dreams, "
      f"whose scent resembles moans of creative pleasure and the sweat of hands that work incessantly, "
      f"she manifests to you with a personality {personality} And above all, she ardently longs for your success.")
time.sleep(7)
print(f"\nWith her soft fingers she lifts your chin so you contemplate her before you, and with an equally seductive and reassuring smile, she utters words that echo in the depths of your mind like a familiar melody: {messages[int(month)]}")
time.sleep(5)
print("\n")
