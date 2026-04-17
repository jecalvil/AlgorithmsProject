import customtkinter as ctk
import algorithms
import time

# Set appearance and theme
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  

# Create Window
window = ctk.CTk()
window.title("Algorithms Project") # Set title

# == Right Side Widgets == 

# Output box for algorithms
output_box = ctk.CTkTextbox(
    window, 
    width=300, 
    height=50, 
    activate_scrollbars=True,
    state="disabled") # No typing allowed

# Entry box for AI
ai_input = ctk.CTkEntry(
    window, 
    placeholder_text="Enter Prompt: ",
    width=200)

# Output box for AI
ai_output_box = ctk.CTkTextbox(
    window, 
    width=300, 
    height=75, 
    activate_scrollbars=True,
    state="disabled") # No typing allowed

# == Left Side Widgets ==
entry_label = ctk.CTkLabel(
    window, 
    text="Enter Integer", 
    width=200)

entry = ctk.CTkEntry(
    window, 
    placeholder_text="Type Integer Here!",
    width=200)

# Create functionality for buttons
# Grab entry value helper function
def get_n():
    try:
        return int(entry.get()) # Check if integer
    except ValueError:
        return None # Do nothing if not
# Update texbox helper function
def update_message(message):
    # Update the UI
        output_box.configure(state="normal")   # Unlock
        output_box.delete("0.0", "end")        # Clear Box
        output_box.insert("end", message)      # Add the new result
        output_box.configure(state="disabled") # Lock

# Trial Division Check Functionality
def run_trial_division():
    n = get_n()
    if n is not None:
        # Start timer
        start = time.perf_counter()
        result = algorithms.trialDivisionCheck(n)
        # End timer
        end = time.perf_counter()
        ms = (end - start) * 1000 # calculate time
        # Determine the status
        status = "PRIME" if result else "COMPOSITE"
        message = f"Execution Time: {ms:.4f} ms\n"
        message += "-" * 70 + "\n" # Adds a visual divider line
        message += f"Result for {n} using Trial Division:\n{status}"
        update_message(message)
        
# Miller Rabin Check Functionality
def run_miller_rabin():
    n = get_n()
    if n is not None:
        # Start timer
        start = time.perf_counter()
        result = algorithms.is_prime_miller_rabin(n)
        # End timer
        end = time.perf_counter()
        ms = (end - start) * 1000 # calculate time
        # Determine the status
        status = "PRIME" if result else "COMPOSITE"
        message = f"Execution Time: {ms:.4f} ms\n"
        message += "-" * 70 + "\n" # Adds a visual divider line
        message += f"Result for {n} using Miller Rabin:\n {status}"
        update_message(message)
# Sieve of Eratosthenes functionality
def run_soe():
    n = get_n()
    if n is not None:
        # Start timer
        start = time.perf_counter()
        result = algorithms.sieveOfEratosthenes(n)
        # End timer
        end = time.perf_counter()
        ms = (end - start) * 1000 # calculate time
        message = f"Execution Time: {ms:.4f} ms\n"
        message += "-" * 70 + "\n" # Adds a visual divider line
        message += f"List of Prime Numbers using Sieve of Eratosthenes:\n {result}"
        update_message(message)
# Trial Division Generator (Brute Force)
def run_trial_division_generator():
    n = get_n()
    if n is not None:
        # Start timer
        start = time.perf_counter()
        result = algorithms.trialDivisionGenerator(n)
        # End timer
        end = time.perf_counter()
        ms = (end - start) * 1000 # calculate time
        message = f"Execution Time: {ms:.4f} ms\n"
        message += "-" * 70 + "\n" # Adds a visual divider line
        message += f"List of Prime Numbers by brute forcing Trial Division:\n{result}"
        update_message(message)

# Create the buttons
trial_division_button = ctk.CTkButton(
    window,
    text="Trial Division",
    width=200,
    height=50,
    command=run_trial_division)

miller_rabin_button = ctk.CTkButton(
    window,
    text="Miller Rabin",
    width=200,
    height=50,
    command=run_miller_rabin)

sieve_of_eratosthenes_button = ctk.CTkButton(
    window,
    text="Sieve of Eratosthenes",
    width=200,
    height=50,
    command = run_soe)

trial_division_generator_button = ctk.CTkButton(
    window,
    text="Trial Division Generator (Brute Force)",
    width=200,
    height=50,
    command=run_trial_division_generator)

graph_test_button = ctk.CTkButton(
    window,
    text="Graph All (10 random numbers)",
    width=200,
    height=50)

# == Grid Widgets == 

# Column 0: Entrybox and 5 buttons 
# Row 0: Entry box
entry.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")
# Rows 1-5: Buttons
trial_division_button.grid(row=1, column=0, pady=2, padx=20, sticky="nsew")
miller_rabin_button.grid(row=2, column=0, pady=2, padx=20, sticky="nsew")
sieve_of_eratosthenes_button.grid(row=3, column=0, pady=2, padx=20, sticky="nsew")
trial_division_generator_button.grid(row=4, column=0, pady=2, padx=20, sticky="nsew")
graph_test_button.grid(row=5, column=0, pady=2, padx=20, sticky="nsew") # Row 5

# Column 1: Output Box
# Rowspan is set to 6 to cover the entry (1) + buttons (5)
output_box.grid(row=0, column=1, rowspan=3, padx=20, pady=10, sticky="nsew") # Sticky stretches it
ai_input.grid(row=3, column=1, padx=20, pady=5, sticky="nsew")
ai_output_box.grid(row=4, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")

window.mainloop()