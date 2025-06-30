
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            if to_vertex not in self.adjacency_list[from_vertex]:
                self.adjacency_list[from_vertex].append(to_vertex)

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list:
            if to_vertex in self.adjacency_list[from_vertex]:
                self.adjacency_list[from_vertex].remove(to_vertex)

    def get_following(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def get_followers(self, vertex):
        followers = []
        for user, connections in self.adjacency_list.items():
            if vertex in connections:
                followers.append(user)
        return followers


class Person:
    def __init__(self, name, gender, bio):
        self.name = name
        self.gender = gender
        self.bio = bio

    def show_profile(self):
        return (
            f"Name: {self.name}\n"
            f"Gender: {self.gender}\n"
            f"Bio: {self.bio}"
        )


def find_user_by_name(name, user_list):
    for user in user_list:
        if user.name.lower() == name.lower():
            return user
    return None


def show_all_usernames(user_list):
    print("\nUser List:")
    for u in user_list:
        print(f"- {u.name}")


def menu():
    print("\n--- BuzzLink: Mini Social Connector ---")
    print("1. View all users")
    print("2. View profile details")
    print("3. View someone's followers")
    print("4. View who someone is following")
    print("5. Follow someone")
    print("6. Unfollow someone")
    print("7. Exit")


def main():
    users = [
        Person("Hana", "Female", "Avid reader and café explorer"),
        Person("Daniel", "Male", "Hiking addict and guitar strummer"),
        Person("Alia", "Female", "Plant mom and part-time illustrator"),
        Person("Faiz", "Male", "Game developer who lives for coding"),
        Person("Jia Wen", "Female", "Cat lover and late-night writer")
    ]

    network = Graph()

    for user in users:
        network.add_vertex(user)

    # Initial followings
    network.add_edge(users[0], users[1])  # Hana -> Daniel
    network.add_edge(users[1], users[2])  # Daniel -> Alia
    network.add_edge(users[2], users[3])  # Alia -> Faiz
    network.add_edge(users[3], users[4])  # Faiz -> Jia Wen
    network.add_edge(users[4], users[0])  # Jia Wen -> Hana

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            show_all_usernames(users)

        elif choice == "2":
            show_all_usernames(users)
            name = input("Enter name to view profile: ")
            user = find_user_by_name(name, users)
            if user:
                print("\nProfile Info:")
                print(user.show_profile())
            else:
                print("User not found.")

        elif choice == "3":
            name = input("Enter name to check followers: ")
            user = find_user_by_name(name, users)
            if user:
                fans = network.get_followers(user)
                if fans:
                    print(f"{user.name}'s Followers:")
                    for f in fans:
                        print(f"- {f.name}")
                else:
                    print(f"{user.name} has no followers.")
            else:
                print("User not found.")

        elif choice == "4":
            name = input("Enter name to see who they follow: ")
            user = find_user_by_name(name, users)
            if user:
                followings = network.get_following(user)
                if followings:
                    print(f"{user.name} is following:")
                    for f in followings:
                        print(f"- {f.name}")
                else:
                    print(f"{user.name} follows no one.")
            else:
                print("User not found.")

        elif choice == "5":
            show_all_usernames(users)
            follower = input("Who wants to follow someone?: ")
            followee = input("Who do they want to follow?: ")
            user1 = find_user_by_name(follower, users)
            user2 = find_user_by_name(followee, users)
            if user1 and user2:
                network.add_edge(user1, user2)
                print(f"{user1.name} now follows {user2.name}.")
            else:
                print("Invalid user(s). Try again.")

        elif choice == "6":
            show_all_usernames(users)
            unfollower = input("Who wants to unfollow someone?: ")
            unfollowee = input("Who do they want to unfollow?: ")
            user1 = find_user_by_name(unfollower, users)
            user2 = find_user_by_name(unfollowee, users)
            if user1 and user2:
                network.remove_edge(user1, user2)
                print(f"{user1.name} has unfollowed {user2.name}.")
            else:
                print("Invalid user(s). Try again.")

        elif choice == "7":
            print("Thanks for using BuzzLink! Goodbye.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
