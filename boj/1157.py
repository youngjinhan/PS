al=input().upper()
freq_a=''
freq_n=0
for i in range(ord('A'),ord('Z')+1):  # ord(char) : character to ASCII number
    if al.count(chr(i))>freq_n:    # chr(num) : ASCII number to character
        freq_n=al.count(chr(i))
        freq_a=chr(i)
    elif al.count(chr(i))==freq_n:
        freq_a='?'
print(freq_a)
