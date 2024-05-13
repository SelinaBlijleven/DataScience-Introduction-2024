alphabet = {
    'a':  1,
    'b':  2,
    'c':  3
}

# Print alle elementjes (keys en values) uit de dictionary
for k, v in alphabet.items():
    print(f"{k}: {v}")

print(alphabet.keys())
print(alphabet.values())
print('d' in alphabet.keys())