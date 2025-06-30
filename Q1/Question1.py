
import random

def generate_ic_number():
    yy = random.randint(0, 99)
    mm = random.randint(1, 12)

    if mm in {4, 6, 9, 11}:
        dd = random.randint(1, 30)
    elif mm == 2:
        dd = random.randint(1, 28)
    else:
        dd = random.randint(1, 31)

    loc_code = random.randint(0, 9999)
    seq = random.randint(0, 99)

    return f"{yy:02d}{mm:02d}{dd:02d}{loc_code:04d}{seq:02d}"

def hash_function(ic_number, table_size):
    ic_str = str(ic_number).zfill(12)
    folded = sum(int(ic_str[i:i+3]) for i in reversed(range(0, 12, 3)))
    return folded % table_size

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.collisions = 0

    def insert(self, ic_number):
        index = hash_function(ic_number, self.size)
        if self.table[index]:
            self.collisions += 1
        self.table[index].append(ic_number)

    def get_collision_count(self):
        return self.collisions

    def get_collision_rate(self):
        total_items = sum(len(bucket) for bucket in self.table)
        return (self.collisions / total_items) * 100 if total_items > 0 else 0

    def print_sample(self):
        print(f"\nHash Table Sample (size {self.size}):")

        print("\nFirst 15 entries:")
        for i in range(15):
            self._print_entry(i)

        print("\nLast 15 entries:")
        for i in range(self.size - 15, self.size):
            self._print_entry(i)

    def _print_entry(self, index):
        chain = self.table[index]
        if chain:
            formatted = " --> ".join(chain)
            print(f"table[{index}] --> {formatted}")
        else:
            print(f"table[{index}]")

def run_experiment():
    sizes = [1009, 2003]
    rounds = 10
    count_per_round = 1000

    results = {1009: [], 2003: []}

    for r in range(rounds):
        print(f"\n=== Round {r + 1} ===")
        ic_batch = [generate_ic_number() for _ in range(count_per_round)]

        for size in sizes:
            table = HashTable(size)
            for ic in ic_batch:
                table.insert(ic)
            results[size].append(table.get_collision_count())

            print(f"Table size {size}:")
            print(f"Collisions: {table.get_collision_count()} ({table.get_collision_rate():.2f}%)")

            if r == 0:
                table.print_sample()

    print("\n--- Collision Summary by Round ---")
    for r in range(rounds):
        print(f"Round {r + 1}: Table 1009 = {results[1009][r]} collisions, Table 2003 = {results[2003][r]} collisions")

    print("\n--- Final Averages ---")
    for size in sizes:
        avg_coll = sum(results[size]) / rounds
        avg_rate = (avg_coll / count_per_round) * 100
        print(f"Average collisions for Table {size}: {avg_coll:.1f} ({avg_rate:.2f}%)")

if __name__ == "__main__":
    run_experiment()
