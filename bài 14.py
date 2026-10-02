x = int(input())
to_500 = x//500
x=x%500
to_200 = x//200
x=x%200
to_100 = x//100
print("Số tờ 500", to_500)
print("Số tờ 200", to_200)
print("Số tờ 100", to_100)
