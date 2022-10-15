# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# ¬ - это аналог not
# V - аналог or
# ⋀ - аналог and

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            l_part = not (x or y or z)
            r_part = not x and not y and not z
            print('¬(', x, ' ⋁ ', y, ' ⋁ ', z, ') = ¬', x, ' ⋀ ¬', y, ' ⋀ ¬', z)
            print(l_part, ' = ', r_part)
            print(l_part == r_part)
