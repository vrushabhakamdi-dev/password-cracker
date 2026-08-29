"""
FORGE WITH CODE
Password Cracking Simulator
Educational / Local Simulation Only

Requirements:
    Python 3.x

Run:
    python password_simulator.py
"""

import itertools
import string
import time


# ============================================================
# CONFIGURATION
# ============================================================

MAX_ATTEMPTS = 2_000_000

# Keep the demo intentionally small.
CHARSET = string.ascii_lowercase + string.digits


# ============================================================
# PASSWORD STRENGTH ANALYZER
# ============================================================

def analyze_password(password):
    length = len(password)
    score = 0

    if length >= 8:
        score += 25

    if length >= 12:
        score += 25

    if any(c.islower() for c in password):
        score += 10

    if any(c.isupper() for c in password):
        score += 10

    if any(c.isdigit() for c in password):
        score += 10

    if any(c in string.punctuation for c in password):
        score += 20

    if score < 30:
        level = "VERY WEAK"
    elif score < 50:
        level = "WEAK"
    elif score < 70:
        level = "MODERATE"
    elif score < 90:
        level = "STRONG"
    else:
        level = "VERY STRONG"

    return score, level


# ============================================================
# FORMAT LARGE NUMBERS
# ============================================================

def format_number(number):
    return f"{number:,}"


# ============================================================
# SIMULATED BRUTE-FORCE ENGINE
# ============================================================

def simulate_crack(target):

    print("\n" + "=" * 60)
    print("        FORGE WITH CODE — PASSWORD SIMULATOR")
    print("=" * 60)

    score, level = analyze_password(target)

    print(f"\nTarget Length : {len(target)}")
    print(f"Strength      : {level}")
    print(f"Score         : {score}/100")
    print("Charset       : lowercase + numbers")
    print("\nSTATUS        : SIMULATION RUNNING...\n")

    attempts = 0
    start_time = time.perf_counter()

    # Try combinations from length 1 upward.
    for length in range(1, len(target) + 1):

        for combination in itertools.product(CHARSET, repeat=length):

            attempts += 1

            # Safety limit for the educational demo.
            if attempts > MAX_ATTEMPTS:
                elapsed = time.perf_counter() - start_time

                print("\n[!] Simulation limit reached.")
                print(f"Attempts : {format_number(attempts)}")
                print(f"Time     : {elapsed:.2f} seconds")
                print("\nThis demo intentionally stops before")
                print("performing a large-scale brute-force search.")

                return

            guess = "".join(combination)

            # Display progress occasionally.
            if attempts % 10_000 == 0:

                elapsed = time.perf_counter() - start_time
                speed = attempts / elapsed if elapsed > 0 else 0

                print(
                    f"\rAttempts: {format_number(attempts):>12} | "
                    f"Speed: {speed:,.0f}/sec | "
                    f"Current: {guess:<10}",
                    end=""
                )

            # Target found.
            if guess == target:

                elapsed = time.perf_counter() - start_time
                speed = attempts / elapsed if elapsed > 0 else 0

                print("\n\n" + "=" * 60)
                print("                 RESULT FOUND")
                print("=" * 60)

                print(f"\nPassword : {guess}")
                print(f"Attempts : {format_number(attempts)}")
                print(f"Speed    : {speed:,.0f} attempts/sec")
                print(f"Time     : {elapsed:.2f} seconds")

                print("\nSTATUS   : PASSWORD FOUND")
                print("=" * 60)

                return

    print("\nSimulation completed.")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n╔════════════════════════════════════════════════════╗")
    print("║       PYTHON PASSWORD CRACKING SIMULATOR          ║")
    print("║              EDUCATIONAL DEMO                     ║")
    print("╚════════════════════════════════════════════════════╝")

    print("\nUse a small demo password.")
    print("Recommended examples: a1, ab1, test1")

    target = input("\nEnter demo password: ").strip()

    if not target:
        print("Password cannot be empty.")
        return

    # Restrict the demonstration to the local demo charset.
    if any(character not in CHARSET for character in target):
        print("\nPlease use only:")
        print("lowercase letters (a-z) and numbers (0-9)")
        return

    if len(target) > 6:
        print("\nFor this educational demo,")
        print("use a password of 6 characters or fewer.")
        return

    simulate_crack(target)


if __name__ == "__main__":
    main()