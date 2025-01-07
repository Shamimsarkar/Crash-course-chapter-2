name = " md shamim reza.\n\t I love python. "

name_without_left_whitespace = name.lstrip()
name_without_right_whitespace = name.rstrip()
name_without_whitespace = name.strip()

print(name_without_left_whitespace)
print(name_without_right_whitespace)
print(name_without_whitespace)

# Full code in one line

print(f"{name.lstrip()}\n {name.rstrip()} \n{name.strip()}")