import customtkinter as ctk

# Set appearance and theme
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  

# Create Window
window = ctk.CTk()
window.title("Algorithms Project")

# == Create Widgets == 

# Left Side Widgets (Top Left Area)
entry_label = ctk.CTkLabel(
    window, 
    text="Enter Integer", 
    width=200)

entry = ctk.CTkEntry(
    window, 
    placeholder_text="Type Integer Here!",
    width=200)

trial_division_button = ctk.CTkButton(
    window,
    text="Trial Division",
    width=200,
    height=50)

miller_rabin_button = ctk.CTkButton(
    window,
    text="Miller Rabin",
    width=200,
    height=50)

sieve_of_eratosthenes_button = ctk.CTkButton(
    window,
    text="Sieve of Eratosthenes",
    width=200,
    height=50)

temp_button = ctk.CTkButton(
    window,
    text="TEMP BUTTON",
    width=200,
    height=50)

graph_test_button = ctk.CTkButton(
    window,
    text="Graph All (10 random numbers)",
    width=200,
    height=50)

# Right Side Widget (Top-Right Area)
# ctk.CTkTextbox is the modern equivalent of tk.Text
output_box = ctk.CTkTextbox(
    window, 
    width=300, 
    height=250, 
    activate_scrollbars=True)

# == Grid Widgets == 

# Column 0: Label, Entrybox, and 5 buttons
entry_label.grid(row=0, column=0, pady=(10, 2), padx=20)
entry.grid(row=1, column=0, pady=(0, 10), padx=20)
trial_division_button.grid(row=2, column=0, pady=5, padx=20)
miller_rabin_button.grid(row=3, column=0, pady=5, padx=20)
sieve_of_eratosthenes_button.grid(row=4, column=0, pady=5, padx=20)
temp_button.grid(row=5, column=0, pady=5, padx=20)
graph_test_button.grid(row=6, column=0, pady=5, padx=20)

# Column 1: Output Box
# We use sticky="nsew" so it fills the height created by the buttons
output_box.grid(row=0, column=1, rowspan=6, padx=20, pady=20, sticky="nsew")

window.mainloop()