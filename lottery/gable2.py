import random
import time

def lottery():
    for _ in range(30):
        selected = random.choice(wheel)
        print(f"🎡 {selected}",)#end="\r")
        time.sleep(0.1)

    print(" " * 50, end="\r")

    winner1 = random.choice(wheel)
    wheel.remove(winner1)
    winner2 = random.choice(wheel)
    wheel.remove(winner2)
    winner3 = random.choice(wheel)

    print(f"\nThe 3 winners of the lottery are:")
    print(f"🎉 1st Place: {winner1} won {first_prize:.2f} GEL 🎉")
    print(f"🎉 2nd Place: {winner2} won {second_prize:.2f} GEL 🎉")
    print(f"🎉 3rd Place: {winner3} won {third_prize:.2f} GEL 🎉")

bet = [
    "ucha khuberishvili 1000000", "nikoloz qimeridze 10", "ilia dzindzibadze 1000000", 
    "cotne gujabidze 10", "shalva shubitidze 10", "zuka abashidze 10", 
    "giga khutsishvili 10", "berdia beqauri 10", "sandro zabakhidze 10", 
    "vano motiashvili 10", "guram vakhtangashvili 10", "daniel abramiani 10", 
    "nika edisherashvili 10", "giorgi xmaladze 10", "data fofxadze 10", 
    "alex pitava 10", "gobron witlauri 10", "erekle kilasonia 10", 
    "andria alavidze 10", "nika nutsubidze 10", "guram papunashvili 10", 
    "nikoloz whitadze 10", "giorgi varadashvili 10", "nika kvaratshelia 10", 
    "george gvritishvili 10", "saba isakadze 10", "ani razmadze 10", 
    "luka lortqifanidze 10", "davit narimanidze 10", "giorgi shavadze 10",
]


overall = sum(int(entry.split()[-1]) for entry in bet)


res = overall * 15 / 100
remaining = overall - res


ticket_counts = {}
for entry in bet:
    name, amount = " ".join(entry.split()[:-1]), int(entry.split()[-1])
    tickets = amount // 5
    ticket_counts[name] = tickets


wheel = []
for name, tickets in ticket_counts.items():
    wheel.extend([name] * tickets)


first_prize = remaining * 50 / 100
second_prize = remaining * 30 / 100
third_prize = remaining * 20 / 100


print("\nTicket Count per Player:")
for name, tickets in ticket_counts.items():
    print(f"{name}: {tickets} tickets")

print("\nTotal Bet Amount:", overall)
# print("15% of Total Bet Amount (excluded):", res)
# print("Remaining Total for Prizes:", remaining)
print("\nPrize Distribution:")
print(f"1st Place: {first_prize:.2f} GEL (50%)")
print(f"2nd Place: {second_prize:.2f} GEL (30%)")
print(f"3rd Place: {third_prize:.2f} GEL (20%)")


ask = input("\nDO YOU WANT TO SPIN THE WHEEL? (yes/no): ")
if ask.lower() == "yes":
    lottery()