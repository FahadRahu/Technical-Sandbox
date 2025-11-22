import random

number_friends = int(input("Enter the number of friends joining (including you): "))

friends = {}
print("")

if number_friends > 0:
    print("Enter the name of every friend (including you) each on a new line: ")
    for n in range(number_friends):
        name = input()
        friends[name] = friends.get(name, 0)

    print('Enter the total bill value:')
    bill = int(input())
    split_bill = round((bill / number_friends), 2)
    for split in friends:
        friends[split] = friends[split] + split_bill

    print(friends)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    luck_choice = input()

    if luck_choice == 'Yes':
        keys_list = list(friends.keys())
        lucky_person = random.choice(keys_list)
        print(f'{lucky_person} is the lucky one!')

        friends[lucky_person] = 0
        new_split_bill = round((bill / (number_friends - 1)), 2)

        for new_split in friends:
            if new_split == lucky_person:
                friends[lucky_person] = 0
            else:
                friends[new_split] = new_split_bill

        print(friends)

    else:
        print('No one is going to be lucky')
        print(friends)
else:
    print("No one is joining for the party")