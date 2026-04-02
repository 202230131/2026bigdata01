from asyncio import print_call_graph

import ticket

humans = int(input("몇 명"))
ages = list()
age = 0

for 1 in range(humans):
    age = int(input("나이"))
    ages.append(age)

print(f"총 요금 {ticket.entrance_fee(ages)}원 입니다.")
print(ages)


