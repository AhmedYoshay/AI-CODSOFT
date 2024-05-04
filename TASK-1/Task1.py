import tkinter as tk

data = {
    "hi": "Hi there! I'm a friendly chatbot here to assist you.",
    "hello": "Hello! How can I help you today?",
    "what is your name": "I'm just a chatbot, so I don't have a name, but you can call me ChatBot.",
    "where are you from": "I'm from the digital world, always ready to chat!",
    "how are you": "I'm just a chatbot, but I'm here to assist you.",
    "do you have any hobbies or interests?": "I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?": "I don't eat, but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?": "I'm a chatbot, so I don't have personal preferences for colors.",
    "do you enjoy listening to music?": "I can't listen to music, but I'm here to chat about it!",
    "bye": "Goodbye! Take care and have a great day!",
}

def get_response(user_input):
    for pattern, response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentence?"

def send_message(event=None):
    user_input = entry.get()
    if user_input == 'bye':
        messages.config(state=tk.NORMAL)
        messages.insert(tk.END, "You: " + user_input + '\n')
        messages.insert(tk.END, "Chatbot: " + get_response(user_input) + '\n')
        messages.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        entry.config(state=tk.DISABLED)
    else:
        messages.config(state=tk.NORMAL)
        messages.insert(tk.END, "You: " + user_input + '\n')
        messages.insert(tk.END, "Chatbot: " + get_response(user_input) + '\n')
        messages.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

# Create GUI window
root = tk.Tk()
root.title("My Chatbot")

# Configure colors
root.configure(bg="#6A5ACD")
messages_bg = "#6A5ACD"
entry_bg = "white"

# Create chat display
messages = tk.Text(root, width=50, height=20, bg=messages_bg, fg="white")
messages.config(state=tk.DISABLED)
messages.pack()

# Create entry field
entry_frame = tk.Frame(root, bg=root.cget("bg"))
entry_frame.pack(pady=(10, 0))
entry = tk.Entry(entry_frame, width=50, bg=entry_bg)
entry.pack(side=tk.LEFT, padx=(10, 5))
entry.focus_set()

# Create send button
send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="#8A2BE2", fg="white")
send_button.pack(side=tk.RIGHT, padx=(0, 10))

# Bind enter key to send message
entry.bind("<Return>", send_message)

# Run the GUI
root.mainloop()
