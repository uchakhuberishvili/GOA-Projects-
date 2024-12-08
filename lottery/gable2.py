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
    "ვანო მოთიაშვილი 50",
    "ზუკა აბაშიძე 50",
    "გურამ პაპუნაშვილი 50",
    "დათა დიასამიძე 50",
    "გიორგი გვრიტიშვილი 50",
    "გურამ ვახტანგაშვილი 50",
    "ნიკოლოზ ჭიტაძე 50",
    "სანდრო ზაბახიძე 50",
    "ილია ძინძიბაძე 50",
    "უჩა ხუბერიშვილი 50"
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