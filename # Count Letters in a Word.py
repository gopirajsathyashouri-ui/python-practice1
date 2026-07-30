# Count Letters in a Word
input_message= input().lower()
freq = {}
for ch in input_message:
  if ch in freq:
    freq[ch] += 1
  else :
    freq[ch] = 1

print(freq)
     
     

