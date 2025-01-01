import random
import tkinter as tk
from tkinter import scrolledtext

# Dictionary for chatbot responses
dic = {
    "father": "Our father of nation is Mahatma Gandhi",
    "population": "India is the most populated country in the world, with a population of 1,409,128,296 as of July 1, 2024.",
    "colors": "Primary colors are the fundamental colors that cannot be made by mixing other colors, and are the basis for all other colors: Red, yellow, and blue.",
    "fun": [
        "It is physically impossible for pigs to look up into the sky.",
        "Cat urine glows under a black-light.",
        "A crocodile can't stick its tongue out.",
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't!"
    ]
}

# Chatbot logic function
def bot(user_input):
    a = user_input.lower()
    b = a.split()

    if any(word in {"hi", "hello", "hey"} for word in b):
        return "Hi, How can I help you?"
    elif any(word in {"bye", "goodbye", "tata"} for word in b):
        return "Tata, goodbye!"
    elif any(word in {"fun", "facts", "fact"} for word in b):
        return f"Here's a fun fact: {random.choice(dic['fun'])}"
    elif any(i in dic for i in b):
        for i in b:
            if i in dic:
                return dic[i]
    else:
        return "I'm sorry, I didn't understand that."

# Function to handle sending messages
def user():
    user_input = user_entry.get()
    if user_input.strip():
        chat_area.insert(tk.END, f"You: {user_input}\n")  # Display user input
        response = bot(user_input)
        chat_area.insert(tk.END, f"Chatbot: {response}\n\n")  # Display chatbot response
        user_entry.delete(0, tk.END)  # Clear the input field
        if "goodbye" in user_input.lower() or "bye" in user_input.lower():
            root.after(1000, root.quit)  # Close the app after goodbye

# Create the main Tkinter window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("400x500")

# Chat area (Scrollable text box)
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.NORMAL)

# Frame to hold the user input field and send button
input_frame = tk.Frame(root)
input_frame.pack(pady=5, padx=10, fill=tk.X)

# User input field
user_entry = tk.Entry(input_frame, font=("Arial", 14))
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

# Send button
send_button = tk.Button(input_frame, text="Send", font=("Arial", 12), command=user)
send_button.pack(side=tk.RIGHT, padx=5)

# Start the Tkinter main loop
root.mainloop()
