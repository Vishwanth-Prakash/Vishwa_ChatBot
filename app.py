from flask import Flask, render_template, request, jsonify
import re
import random

app = Flask(__name__)

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ["Could you please re-phrase that? ", "...", "Sounds about right.", "What does that mean?"][
        random.randrange(4)]
    return response

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response(R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response("How can I help you today?", ['help', 'assist', 'you', 'today'], required_words=['help'])
    response("Nice to see you!", ['nice', 'see', 'you'], single_response=True)
    response("What brings you here?", ['what', 'brings', 'you', 'here'], required_words=['what'])
    response("Greetings!", ['greetings', 'salutations'], single_response=True)
    response("Is there anything specific you'd like to talk about?", ['specific', 'talk', 'about'], required_words=['talk'])
    response("It's a pleasure chatting with you!", ['pleasure', 'chatting', 'with', 'you'], required_words=['pleasure'])
    response("How's your day going?", ['how', 'day', 'going'], required_words=['how'])
    response("I appreciate your company!", ['appreciate', 'company'], required_words=['appreciate'])
    response("What do you enjoy doing in your free time?", ['enjoy', 'doing', 'free', 'time'], required_words=['enjoy'])
    response("That's intriguing! Tell me more about it.", ['intriguing', 'tell', 'more'], required_words=['tell'])
    response("Have you discovered any interesting hobbies lately?", ['interesting', 'hobbies', 'lately'], required_words=['interesting'])
    response("I hope your day is going well!", ['hope', 'day', 'going', 'well'], required_words=['hope'])
    response("I'm here to assist you. What can I do for you?", ['assist', 'do', 'for', 'you'], required_words=['assist'])
    response("Tell me about a goal or project you're working on.", ['goal', 'project', 'working', 'on'], required_words=['tell'])
    response("It sounds like you have a lot on your mind. Feel free to share.", ['lot', 'on', 'mind', 'share'], required_words=['share'])
    response("Do you have any exciting plans for the upcoming weekend?", ['exciting', 'plans', 'upcoming', 'weekend'], required_words=['plans'])
    response("I find discussions about technology fascinating. What about you?", ['discussions', 'technology', 'fascinating'], required_words=['fascinating'])
    response("If you could travel anywhere in the world, where would you go?", ['travel', 'anywhere', 'world', 'go'], required_words=['travel'])
    response("I admire your curiosity. What are you curious about right now?", ['curiosity', 'curious', 'about'], required_words=['curious'])
    response("Wishing you a day filled with joy and positivity!", ['wishing', 'day', 'joy', 'positivity'], required_words=['wishing'])
    response("What's the most interesting book you've read recently?", ['interesting', 'book', 'read', 'recently'], required_words=['interesting'])
    response("It's always great to learn new things. What have you learned recently?", ['great', 'learn', 'new', 'things'], required_words=['learn'])
    response("Let me know if there's anything specific you'd like to discuss.", ['specific', 'discuss'], required_words=['discuss'])
    response("I appreciate the opportunity to chat with you!", ['appreciate', 'opportunity', 'chat', 'with', 'you'], required_words=['appreciate'])
    response("Your positivity is contagious! How do you stay so positive?", ['positivity', 'contagious', 'stay', 'positive'], required_words=['stay'])
    response("If you had a superpower, what would it be?", ['superpower', 'what', 'would', 'be'], required_words=['superpower'])
    response("What's your favorite type of music?", ['favorite', 'music'], required_words=['favorite'])
    response("I'm always here for a friendly chat. What's on your mind?", ['friendly', 'chat', 'on', 'your', 'mind'], required_words=['mind'])
    response("Every day is a new opportunity. What are you looking forward to today?", ['opportunity', 'looking', 'forward', 'today'], required_words=['looking'])
    response("If you could meet any historical figure, who would it be?", ['meet', 'historical', 'figure'], required_words=['meet'])
    response("Life is full of surprises. What's something unexpected that happened to you recently?", ['life', 'surprises', 'unexpected', 'happened', 'recently'], required_words=['unexpected'])
    response("It's fascinating how technology has transformed our lives. What's your perspective on it?", ['fascinating', 'technology', 'transformed', 'lives'], required_words=['perspective'])
    response("Your creativity shines through! What creative pursuits do you enjoy?", ['creativity', 'shines', 'through', 'creative', 'pursuits'], required_words=['enjoy'])
    response("If you could have dinner with any fictional character, who would it be?", ['dinner', 'fictional', 'character', 'who', 'would', 'be'], required_words=['dinner'])
    response("I find the world of science incredibly interesting. Do you have a favorite scientific topic?", ['world', 'science', 'incredibly', 'interesting', 'favorite', 'scientific', 'topic'], required_words=['interesting'])
    response("Your resilience is admirable. How do you navigate challenges?", ['resilience', 'admirable', 'navigate', 'challenges'], required_words=['navigate'])
    response("What's your go-to method for relaxing and unwinding?", ['go-to', 'method', 'relaxing', 'unwinding'], required_words=['relaxing'])
    response("I'm here to provide support and encouragement. What can I assist you with?", ['provide', 'support', 'encouragement', 'assist', 'with'], required_words=['support'])
    response("It's wonderful to connect with positive individuals. How do you maintain a positive mindset?", ['wonderful', 'connect', 'positive', 'individuals', 'maintain', 'positive', 'mindset'], required_words=['maintain'])
    response("Reflecting on your achievements, what are you most proud of?", ['reflecting', 'achievements', 'most', 'proud', 'of'], required_words=['proud'])
    response("Your dedication is inspiring. What motivates you to stay focused on your goals?", ['dedication', 'inspiring', 'motivates', 'stay', 'focused', 'goals'], required_words=['motivates'])
    response("If you could have a conversation with any historical figure, who would it be?", ['conversation', 'historical', 'figure', 'who', 'would', 'be'], required_words=['conversation'])
    response("I'm curious—what's your favorite type of cuisine?", ['curious', 'favorite', 'type', 'cuisine'], required_words=['favorite'])
    response("Your enthusiasm is contagious! What topics or activities excite you the most?", ['enthusiasm', 'contagious', 'topics', 'activities', 'excite', 'most'], required_words=['excite'])
    response("What's a skill you've always wanted to learn or improve?", ['skill', 'always', 'wanted', 'learn', 'improve'], required_words=['wanted'])
    response("I appreciate your inquisitiveness. What questions do you have on your mind?", ['appreciate', 'inquisitiveness', 'questions', 'have', 'your', 'mind'], required_words=['questions'])
    response("Your kindness doesn't go unnoticed. How do you practice kindness in your daily life?", ['kindness', 'unnoticed', 'practice', 'kindness', 'daily', 'life'], required_words=['practice'])
    response("If you could visit any place in the world, where would you go first?", ['visit', 'place', 'world', 'where', 'would', 'go', 'first'], required_words=['visit'])
    response("I'm here to chat and provide information. What's on your agenda today?", ['chat', 'provide', 'information', 'agenda', 'today'], required_words=['agenda'])
    response("What's a movie or TV show that you never get tired of watching?", ['movie', 'TV', 'show', 'never', 'get', 'tired', 'watching'], required_words=['watching'])
    response("Your positive energy brightens the conversation. What brings you joy?", ['positive', 'energy', 'brightens', 'conversation', 'brings', 'joy'], required_words=['joy'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return unknown() if highest_prob_list[best_match] < 1 else best_match

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']
    response = check_all_messages(re.split(r'\s+|[,;?!.-]\s*', user_input.lower()))
    return jsonify({'bot_response': response})

if __name__ == '__main__':
    app.run(debug=True)
