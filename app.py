import customtkinter as ctk
import algorithms
import time
import matplotlib.pyplot as plt
import random
from ai import get_ai_response
import threading

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
    height=150, 
    activate_scrollbars=True,
    state="disabled") # No typing allowed

# Handle AI input/output
def run_ai(prompt):
    # Get response from ai
    response = get_ai_response(prompt)
    # Update UI with answer
    ai_output_box.configure(state="normal")
    ai_output_box.insert("end", f"AI Math Wizard: {response}\n\n")
    ai_output_box.configure(state="disabled")
    ai_output_box.see("end")


def handle_input(event=None):
    # Get input from entry box
    user_input = ai_input.get()
    # Do nothing if empty
    if not user_input.strip():
        return
    # Show message in output box
    ai_output_box.configure(state="normal") # enable it
    ai_output_box.insert("end", f"Algorithm Learner: {user_input}\n")
    # Clear entry box
    ai_input.delete(0, 'end')
    ai_output_box.configure(state="disabled")
    ai_output_box.see("end")
    # Start AI in background
    threading.Thread(target=run_ai, args=(user_input,), daemon=True).start()

ai_input.bind("<Return>", handle_input)

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
# Create Plot
def run_performance_test():
    # 50 FIXED PRIMES (Checkers: 5M to 50M)
    # Worst-case for Trial Division
    n_checkers = [
        5000011, 5918417, 6836819, 7755293, 8673737, 9592189, 10510607, 11429063,
        12347489, 13265933, 14184379, 15102821, 16021271, 16939723, 17858173, 18776611,
        19695067, 20613511, 21531971, 22450417, 23368861, 24287311, 25205759, 26124217,
        27042659, 27961121, 28879571, 29798027, 30716471, 31634927, 32553373, 33471821,
        34390271, 35308723, 36227177, 37145621, 38064077, 38982523, 39900971, 40819427,
        41737873, 42656321, 43574771, 44493223, 45411677, 46330121, 47248577, 48167023,
        49085471, 50000017
    ]
    # Random ranges (Generators: 1k to 30k)
    n_generators = sorted([random.randint(1000, 30000) for i in range(30)]) # sort so the plot is nice
    # Time containers
    check_times, miller_times = [], []
    sieve_times, gen_times = [], []
    # Checkers from 5 million to 50 million
    for n in n_checkers:
        t0 = time.perf_counter() # Trial division time
        algorithms.trialDivisionCheck(n)
        check_times.append((time.perf_counter() - t0) * 1000)
        t1 = time.perf_counter() # Miller Rabin
        algorithms.is_prime_miller_rabin(n, k=10)
        miller_times.append((time.perf_counter() - t1) * 1000)
    # Generators: 1000 to 30000
    for n in n_generators:
        t2 = time.perf_counter() # Time the Sieve
        algorithms.sieveOfEratosthenes(n)
        sieve_times.append((time.perf_counter() - t2) * 1000)  
        t3 = time.perf_counter() # Time the Trial Div Generator
        algorithms.trialDivisionGenerator(n)
        gen_times.append((time.perf_counter() - t3) * 1000)
    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    # Left: Checkers (Worst-case performance)
    ax1.plot(n_checkers[2:], check_times[2:], label=r"Trial Div (Worst Case $n^{1/2}$)", color="blue", marker='o', markersize=4)
    ax1.plot(n_checkers[2:], miller_times[2:], label=r"Miller-Rabin (Worst Case $n^{1/3}$)", color="green", marker='o', markersize=4)
    ax1.set_title("Checkers: Fixed Primes (5M - 50M)")
    ax1.set_xlabel("Value of n")
    ax1.set_ylabel("Time (ms)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Right: Generators (Random Ranges)
    ax2.plot(n_generators, sieve_times, label="Sieve (O(n log log n))", color="purple")
    ax2.plot(n_generators, gen_times, label="Trial Div Gen", color="red")
    ax2.set_title("Generators: Random Ranges (1k - 30k)")
    ax2.set_xlabel("Range up to n")
    ax2.set_ylabel("Time (ms)")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


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
    text="Graph All",
    width=200,
    height=50,
    command=run_performance_test)

# == Grid Widgets == 

# Column 0: 1 Entrybox and 5 buttons 
# Row 0: Entry box
entry.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")
# Rows 1-5: Buttons
trial_division_button.grid(row=1, column=0, pady=2, padx=20, sticky="nsew")
miller_rabin_button.grid(row=2, column=0, pady=2, padx=20, sticky="nsew")
sieve_of_eratosthenes_button.grid(row=3, column=0, pady=2, padx=20, sticky="nsew")
trial_division_generator_button.grid(row=4, column=0, pady=2, padx=20, sticky="nsew")
graph_test_button.grid(row=5, column=0, pady=2, padx=20, sticky="nsew") # Row 5

# Column 1: Output Box, Ai input, ai output
output_box.grid(row=0, column=1, rowspan=3, padx=20, pady=10, sticky="nsew") # Sticky stretches it
ai_input.grid(row=3, column=1, padx=20, pady=5, sticky="nsew")
ai_output_box.grid(row=4, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")

window.mainloop()