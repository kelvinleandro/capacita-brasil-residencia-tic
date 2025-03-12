for i in range(1,6):
  print(i, end=" ")
print()

#####

arr = [10, 20, 30, 40, 50]
print(arr[0])

#####

res = 0
for i in range(1,11):
  res += i
print(f"Soma: {res}")

#####

dici = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
print(dici["nome"])

#####

text = "Python"
for i in reversed(range(len(text))):
  print(text[i], end="")
print()

#####

count = {}
text = "banana"
for l in text:
  if l in count:
    count[l] += 1
  else:
    count[l] = 1

print(count)