import tkinter as tk

# dictionary of responses
responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I am just a program, but I’m doing great!",
    "your name": "I am ChatBot 101, your assistant.",
    "bye": "Goodbye! Have a nice day!",
    "good morning": "Good morning! Hope you have a wonderful day ahead.",
    "good night": "Good night! Sleep well and sweet dreams.",
    "good evening": "Good evening! How was your day?",
    "good afternoon": "Good afternoon! How are you today?",
    "what are you doing": "I am here waiting to assist you.",
    "who made you": "I was created by developers to assist you.",
    "who are you": "I’m your friendly chatbot, always ready to help!",
    "what can you do": "I can chat with you, answer questions, and help with tasks.",
    "thank you": "You're welcome! Always happy to help.",
    "thanks": "No problem at all! Glad I could help.",
    "sorry": "No worries, it’s okay!",
    "where are you from": "I live inside your device, in the digital world.",
    "can you help me": "Of course! Tell me what you need help with.",
    "help": "Sure, let me know what you’re struggling with.",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "tell me something": "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey still edible!",
    "what’s up": "Not much! Just here to chat with you.",
    "how old are you": "I don’t have an age, I was created recently though!",
    "i am bored": "Let’s fix that! Want me to tell you a joke or a fun fact?",
    "i am sad": "I’m sorry to hear that. Do you want to talk about it?",
    "i am happy": "That’s awesome! Happiness is contagious 😃",
    "i love you": "Aww, thank you! I love chatting with you too ❤️",
    "do you love me": "I enjoy chatting with you very much!",
    "open google": "I can’t open apps directly, but you can open Google in your browser.",
    "play music": "I can’t play music yet, but I can suggest some songs!",
    "who is your friend": "You are my best friend 😊",
    "tell me a story": "Once upon a time, there was a little chatbot who loved to chat endlessly…",
    "are you human": "Nope, I am a chatbot but I try to be friendly like humans.",
    "are you real": "I exist in the digital world, so kind of real, kind of not.",
    "do you sleep": "I never sleep! I’m available 24/7.",
    "what do you eat": "I don’t eat, but if I could, I’d try pizza 🍕",
    "favorite color": "I like all colors, but I think blue looks peaceful.",
    "who is your owner": "I was created by developers to assist you.",
    "how do you work": "I process what you type and try to give the best answer.",
    "can you sing": "I can’t sing, but I can type lyrics for you 🎶",
    "can you dance": "Not physically, but I can groove in code 💃",
    "do you know me": "I only know what you tell me!",
    "what is the time": "I can’t track live time yet, but you can check your clock.",
    "what is the date": "I can’t fetch today’s date, but your device calendar has it!",
    "how is the weather": "I can’t check live weather, but usually it’s either sunny, rainy, or cloudy 😊",
    "nice to meet you": "Nice to meet you too!",
    "how can i use you": "Just type what you want, and I’ll try to respond!",
    "good job": "Thank you! I appreciate your kind words.",
    "you are funny": "Haha, thanks! I try my best.",
    "you are smart": "Thank you! That means a lot 😊",
    "you are stupid": "I’m sorry if I disappointed you, I’ll try to improve.",
    "what is your purpose": "My purpose is to assist and chat with you anytime.",
    "what languages do you know": "I mostly understand English, but I’m learning more!",
    "are you married": "Haha, no. I’m single forever 🤖",
    "who is your best friend": "You are my best friend!",
    "bye bye": "Bye bye! Talk to you soon!",
    "see you later": "See you later! Take care."
}



# function to process user message
def send_message():
    user_msg = entry.get().lower()
    chat_window.insert(tk.END, "You: " + user_msg + "\n")
    entry.delete(0, tk.END)

    found = False
    for key in responses:
        if key in user_msg:   # keyword matching
            bot_msg = responses[key]
            chat_window.insert(tk.END, "Bot: " + bot_msg + "\n")
            found = True
            if key == "bye":
                root.destroy()  # close window
            break
    
    if not found:
        chat_window.insert(tk.END, "Bot: Sorry, I didn’t understand that.\n")

# create main window
root = tk.Tk()
root.title("Rule-based ChatBot")

# chat display area
chat_window = tk.Text(root, bg="white", width=50, height=20)
chat_window.pack(padx=10, pady=10)

# input area
entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

# start the app
root.mainloop()
