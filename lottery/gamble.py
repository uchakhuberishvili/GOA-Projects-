import random
import time
bet = [
    "ucha khuberishvili 5", "nikoloz qimeridze 5", "ilia dzindzibadze 5", 
    "cotne gujabidze 5", "shalva shubitidze 5", "zuka abashidze 5", 
    "giga khutsishvili 5", "berdia beqauri 5", "sandro zabakhidze 5", 
    "vano motiashvili 5", "guram vakhtangashvili 5", "daniel abramiani 5", 
    "nika edisherashvili 5", "giorgi xmaladze 5", "data fofxadze 5", 
    "alex pitava 5", "gobron witlauri 5", "erekle kilasonia 5", 
    "andria alavidze 5", "nika nutsubidze 5", "guram papunashvili 5", 
    "nikoloz whitadze 5", "giorgi varadashvili 5", "nika kvaratshelia 5", 
    "george gvritishvili 5", "saba isakadze 5", "ani razmadze 5", 
    "luka lortqifanidze 5", "davit narimanidze 5", "giorgi shavadze 5"
]

overall = sum(int(entry.split()[-1]) for entry in bet)
res = overall * 15 / 100

ticket_counts = {}
for entry in bet:
    name, amount = " ".join(entry.split()[:-1]), int(entry.split()[-1])
    tickets = amount // 5
    ticket_counts[name] = tickets

print("\nTotal Bet Amount:", overall)
print("15% of Total Bet Amount:", res)
print("\nTicket Count per Player:")
for name, tickets in ticket_counts.items():
    print(f"{name}: {tickets} tickets")

wheel = []
for name, tickets in ticket_counts.items():
    wheel.extend([name] * tickets)

random.shuffle(wheel)

print("\nSpinning the wheel...\n")
for _ in range(150):
    selected = random.choice(wheel)
    print(f"🎡 {selected}",)
    time.sleep(0.1)

print(" " * 50, end="\r")

winner = random.choice(wheel)
print(f"The winner of the lottery is: 🎉 {winner} 🎉")
