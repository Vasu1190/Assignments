bot_asked_for_name = False
user_name = None

def capture_user_name(user_input, bot_response=None):
    global user_name
    temp_user_name = None  # Temporary variable to hold the extracted name

    if "Before answering your query, may I know your name? Kindly use the format myself followed by your name." in bot_response:
        # Extracting the user's name from the input
        words = user_input.split()
        for i, word in enumerate(words):
            if word.lower() in ["my", "i'm", "i", "is", "am", "name", "my name is", "myself", "my self", "iam", "i am"]:
                # Check for keywords indicating the user's name
                temp_user_name = words[i+1] if i+1 < len(words) else None
                break

    if temp_user_name:
        user_name = temp_user_name  # Update the global user_name variable
    return temp_user_name 


def get_conversation_rules():
    global user_name
    
    
    conversation_rules = {
        'greeting': {
            'condition': lambda user_question: user_question.lower() in ['hi', 'hai', 'hello'],
            'response': "Bot: Hi, I'm Hope AI Assistant. How can I help you?",
            'action': None,
            'next_rule': 'waiting_for_name'
        },
        'waiting_for_name': {
            'condition': lambda user_question: ("course details" in user_question or "course detail" in user_question or "course detail plz" in user_question or "course details plz" in user_question or "course details please" in user_question),
            'response': "Bot: Before answering your query, may I know your name? Kindly use the format myself followed by your name." ,
            'action': capture_user_name,
            'next_rule': 'intro'
        },
        'intro': {
            'condition': lambda user_question: user_name is not None and user_name in user_question,
            'response': lambda user_question: f"Bot: Ok {user_name}, tell  me how did you know about us? Facebook, Instagram, or Youtube.",
            'action': None,
            'next_rule': 'prompt_webinar_attendance'
        },
        'prompt_webinar_attendance': {
            'condition': lambda user_question: any(word in user_question for word in ["facebook", "fb", "insta", "instagram", "YouTube"]),
            'response': "Bot: Did you attend our free webinar?",
            'action': None,
            'next_rule': None
        },
        'prompt_attend_webinar': {
            'condition': lambda user_question: ("no" in user_question or 'no i dint' in user_question or "no i dint attend" in user_question or "no i dint attend the webinar" in user_question or "i dint attend the webinar" in user_question),
            'response': f"Bot: Ok {user_name}, I request you to attend our free webinar. You will know about the syllabus, fee details. We provide support for 3 years, lifetime access and all other information about the course. Please book a call @ 1234",
            'action': None,
            'next_rule': None
        },
        'prompt_book_call': {
            'condition': lambda user_question:("yes" in user_question or "yes attended" in user_question or "s attended " in user_question or "yes attended webinar" in user_question or "Yep" in user_question or "yes i attended" in user_question or "yes i attended the webinar" in user_question),
            'response': f"Bot: Ok {user_name}, during the webinar, I mentioned that you should book a 1:1 call to discuss more about the course. If you encounter any issues while booking the slot, please let me know." ,
            'action': None,
            'next_rule': None
        },        
        'prompt_share_issues': {
            'condition': lambda user_question: ("yes facing issues" in user_question or "facing issue" in user_question or "facing issues " in user_question or "yes facing issue" in user_question or "Yep facing issues" in user_question or "yes facing issues" in user_question or "Yep facing issues" in user_question or "Yes facing issues while booking the slot" in user_question or "s faced issues while booking the slot" in user_question),
            'response': "Bot: Please share the issues you are facing.",
            'action': None,
            'next_rule': None
        },
        'connect_human_representative': {
            'condition': lambda user_question: ("network issue" in user_question or "not able to book" in user_question or "not able to book the slot" in user_question),
            'response': "Bot: I will connect you with a human representative.",
            'action': None,
            'next_rule': None
        
        },
        'ask_any_other_queries': {
            'condition': lambda user_question: any(word in user_question for word in ["ok", "thankyou", "thank you", "thnku", "thnk u", "ok thanku","ok thank you ", "ok thank u" ]),
            'response': "Bot: Feel free to ask any other queries if any.",
            'action': None,
            'next_rule': None
        }
    }
    return conversation_rules

from PIL import Image
from IPython.display import display, Image

def display_company_title_image(user_question):
    title_keywords = ["owner", "ceo", "founder", "creator", "proprietor", "chief executive officer"]
    title = None
    for keyword in title_keywords:
        if keyword in user_question:
            title = keyword.capitalize()
            break

    if title:
        # Display related image
        display(Image(filename='Ramisha Rani K.jpg'))  # Replace 'related_image.jpg' with your image path
        # Provide the answer
        #print(f"Bot: The {title} of the company is Ramisha Rani K")


