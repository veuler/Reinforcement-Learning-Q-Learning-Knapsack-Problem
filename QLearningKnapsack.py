import random, time, sys
import numpy as np

q_table = np.zeros((11,11), dtype="int")

values = []
for x in range(10):
    values.append(random.choice(range(1,10)))

weights = []
for x in range(10):
    weights.append(random.choice(range(1,10)))

all_valwei = []
for x,y in zip(values,weights):
    all_valwei.append([x,y])

main_states = {}
states = main_states

for x in range(1,11):
    main_states[x] = all_valwei[x-1]

for x in main_states.items():
    print(x)
print("#"*30)


################# parameters
bag_limit = 14
total_limit = 0
total_value = 0

alpha = 0.75
gamma = 0.6
reward = 0.1
new_max_reward = 0
epsilon = 0.9

level = 0
cur_state = 0

#q_table[state_index][new_state_index] = (1-alpha) * q_table[state_index][new_state_index] + alpha * (reward * gamma * new_max_reward)
gmax = 0

sol2 = []
sayac = 0

check12 = []
while True:
    if level == 350:
        break

    max_tries = 0
    sol1 = []
    while total_limit < bag_limit:

        check = random.choice(range(1,10)) / 10

        if epsilon > check or cur_state == 0:
            sayac +=1
            print("RANDOM ATILIYOR")
            action = random.choice(list(states))

            print(action, states[action])

            total_limit += states[action][1]
            total_value += states[action][0]

            print("total limit", total_limit)
            print("total value", total_value)

            if total_limit > 14:
                reward = -0.1
                reward = reward + total_value

                find_max_val = []
                for x in states.items():
                    if x[0] != action:
                        find_max_val.append(x[0])
                print(find_max_val)
                print("max: ", max(find_max_val))

                new_max_reward = max(find_max_val)

                q_table[cur_state][action] = (1 - alpha) * q_table[cur_state][action] + alpha * (reward + gamma * new_max_reward)

                if gmax == 0 or total_value > gmax:
                    gmax = total_value
                    sol2 = sol1
                break

            else:
                reward = 0.1

                reward = reward + total_value

                find_max_val = []
                for x in states.items():
                    if x[0] != action:
                        find_max_val.append(x[0])
                print(find_max_val)
                print("max: ", max(find_max_val))

                new_max_reward = max(find_max_val)

                q_table[cur_state][action] = (1-alpha) * q_table[cur_state][action] + alpha * (reward + gamma * new_max_reward)

                if (action,states[action]) not in sol1:
                    sol1.append((action,states[action]))
                cur_state = action

        else:
            find_max_val = []
            satir = q_table[cur_state]

            for ind,x in enumerate(satir):
                if ind != cur_state:
                    find_max_val.append(x)

            new_max_reward = max(find_max_val)
            action = find_max_val.index(new_max_reward) +1

            print(action, states[action])

            total_limit += states[action][1]
            total_value += states[action][0]

            print("total limit", total_limit)
            print("total value", total_value)

            if total_limit > 14:
                reward = -0.1

                reward = reward + total_value

                q_table[cur_state][action] = (1 - alpha) * q_table[cur_state][action] + alpha * (reward + gamma * new_max_reward)

                if gmax == 0 or total_value > gmax:
                    gmax = total_value
                    sol2 = sol1
                break
            else:
                reward = 0.1

                reward = reward + total_value

                q_table[cur_state][action] = (1 - alpha) * q_table[cur_state][action] + alpha * (reward + gamma * new_max_reward)

                if (action,states[action]) not in sol1:
                    sol1.append((action,states[action]))
                cur_state = action

                max_tries += 1

        print("#" * 100)
        print(q_table)
        print("#" * 100)

    print("##########################NEW LEVEL STARTS ##################")
    level += 1

    total_limit = 0
    total_value = 0

    if epsilon > 0.7:
        epsilon = epsilon - 0.005
    elif epsilon > 0.2:
        epsilon = epsilon - 0.01

    states = main_states
    cur_state = 0

    print("SOLUTION SOLUTION SOLUTION SOLUTION")
    print(sol2)
    print("SOLUTION SOLUTION SOLUTION SOLUTION")
    print("EPSILON: ", epsilon)




print(q_table)
print("#"*30)
for x in main_states.items():
    print(x)
print("#"*30)
print("SOLUTION SOLUTION SOLUTION SOLUTION") ########NOT THE OPTIMAL ONE
print(sol2)
print("SOLUTION SOLUTION SOLUTION SOLUTION")

