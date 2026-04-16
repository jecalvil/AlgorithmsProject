import math
import random
import customtkinter as ctk

# Trial Division Prime Generator
def generate_primes_trial_division(limit):
    """
    Generate all prime numbers up to 'limit' using trial division.

    Precondition:
        limit is an integer >= 2
    Postcondition:
        returns a list of all primes <= limit
    """
    if limit < 2:
        return []

    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for divisor in range(2, int(math.sqrt(num)) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# Miller-Rabin Primality Tester
def is_prime_miller_rabin(n, k=10):
    """
    Probabilistic primality test using Miller-Rabin.

    Precondition:
        n is an integer
        k is the number of test rounds
    Postcondition:
        returns True if n is probably prime, otherwise False

    Note:
        More rounds (k) means higher confidence.
    """
    if n < 2:
        return False

    # Small prime checks
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0 and n != p:
            return False

    # Write n - 1 as d * 2^r
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        passed_round = False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                passed_round = True
                break

        if not passed_round:
            return False

    return True

# GUI Application
class PrimeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Prime Generator & Tester")
        self.geometry("600x500")

        # Generate Primes Section
        self.gen_label = ctk.CTkLabel(self, text="Generate Primes Up To:")
        self.gen_label.pack(pady=10)

        self.gen_entry = ctk.CTkEntry(self, placeholder_text="Enter limit (e.g., 100)")
        self.gen_entry.pack(pady=5)

        self.gen_button = ctk.CTkButton(self, text="Generate Primes", command=self.generate_primes)
        self.gen_button.pack(pady=10)

        # Test Primality Section
        self.test_label = ctk.CTkLabel(self, text="Test Number for Primality:")
        self.test_label.pack(pady=10)

        self.test_entry = ctk.CTkEntry(self, placeholder_text="Enter number (e.g., 97)")
        self.test_entry.pack(pady=5)

        self.test_button = ctk.CTkButton(self, text="Test with Miller-Rabin", command=self.test_prime)
        self.test_button.pack(pady=10)

        # Results Textbox
        self.result_text = ctk.CTkTextbox(self, wrap="word")
        self.result_text.pack(pady=20, padx=20, fill="both", expand=True)

    def generate_primes(self):
        try:
            limit = int(self.gen_entry.get())
            primes = generate_primes_trial_division(limit)
            result = f"Primes up to {limit}:\n" + ", ".join(map(str, primes))
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", result)
        except ValueError:
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Invalid input. Please enter a number.")

    def test_prime(self):
        try:
            num = int(self.test_entry.get())
            is_prime = is_prime_miller_rabin(num)
            result = f"{num} is {'probably prime' if is_prime else 'composite'} (Miller-Rabin test)"
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", result)
        except ValueError:
            self.result_text.delete("1.0", "end")
            self.result_text.insert("1.0", "Invalid input. Please enter a number.")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = PrimeApp()
    app.mainloop()
