from fake_math import divide as fake_dvde
from true_math import divide as true_divd

result1 = fake_dvde(69, 3)
result2 = fake_dvde(3, 0)
result3 = true_divd(49, 7)
result4 = true_divd(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)