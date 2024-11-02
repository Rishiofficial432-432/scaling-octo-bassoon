import tkinter as tk

def send_message():
    user_input = entry_box.get()
    chat_box.insert(tk.END, f"You: {user_input}\n")
    entry_box.delete(0, tk.END)

    # Simple response based on keywords
    if "hello" in user_input.lower():
        response = "Hello! How can I help you?"
    elif "how are you" in user_input.lower():
        response = "I'm doing well, thank you. How are you?"
    else:
        response = "I'm not sure how to respond to that. Please try asking something else."

    chat_box.insert(tk.END, f"Bot: {response}\n")

# Create the main window
window = tk.Tk()
window.title("Chatbot")

# Create the chat box
chat_box = tk.Text(window, height=20, width=50)
chat_box.pack()

# Create the entry box
entry_box = tk.Entry(window, width=50)
entry_box.pack()

# Create the send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

window.mainloop()