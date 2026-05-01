import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Thangaraj - AIML Profile GUI")
root.geometry("520x380")
root.configure(bg="#EAF6FF")

# Main Title
title = tk.Label(
    root,
    text="👨‍💻 My AIML Profile",
    font=("Arial", 20, "bold"),
    bg="#EAF6FF",
    fg="#003366"
)
title.pack(pady=15)

# Name
tk.Label(
    root,
    text="Name: Thangaraj",
    font=("Arial", 13, "bold"),
    bg="#EAF6FF"
).pack(pady=4)

# Role
tk.Label(
    root,
    text="Role: Aspiring AI/ML Engineer | Python Developer",
    font=("Arial", 12),
    bg="#EAF6FF"
).pack(pady=4)

# Learning
tk.Label(
    root,
    text="Learning: Python | SQL | AI/ML | DL | NLP | LLM | German 🇩🇪",
    font=("Arial", 11),
    bg="#EAF6FF"
).pack(pady=4)

# Journey
tk.Label(
    root,
    text="Journey: Building skills step by step with consistency",
    font=("Arial", 11),
    bg="#EAF6FF"
).pack(pady=4)

# Function for button click
def show_goal():
    goal_label.config(
        text="🚀 Goal: AI Engineer | ML Engineer | Python Developer"
    )

# Button
goal_button = tk.Button(
    root,
    text="My Career Goal",
    font=("Arial", 12, "bold"),
    command=show_goal,
    bg="#003366",
    fg="white",
    padx=15,
    pady=6
)
goal_button.pack(pady=18)

# Output Label
goal_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#EAF6FF",
    fg="#006400"
)
goal_label.pack(pady=10)

# Footer
tk.Label(
    root,
    text="Python Tkinter Mini Project",
    font=("Arial", 10, "italic"),
    bg="#EAF6FF",
    fg="#555555"
).pack(side="bottom", pady=10)

# Run app
root.mainloop()