import tkinter as tk

# Function that runs when the button is clicked
def greet_user():
    name = entry.get()  # Get text from the input box
    if name:
        label_output.config(text=f"Hello, {name}! Welcome to Python UIs.", fg="green")
    else:
        label_output.config(text="Please type a name first!", fg="red")

# Create the main application window
root = tk.Tk()
root.title("My First Python UI")
root.geometry("400x250")

# Add a title label
label_title = tk.Label(root, text="ESP32 Interface Builder", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Add a text prompt
label_prompt = tk.Label(root, text="Enter your name to connect:", font=("Arial", 10))
label_prompt.pack(pady=5)

# Add a text input box
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

# Add a button
button = tk.Button(root, text="Connect & Greet", font=("Arial", 10, "bold"), command=greet_user)
button.pack(pady=10)

# Add a blank label to display the output message later
label_output = tk.Label(root, text="", font=("Arial", 12, "italic"))
label_output.pack(pady=10)

# Start the application loop
root.mainloop()

