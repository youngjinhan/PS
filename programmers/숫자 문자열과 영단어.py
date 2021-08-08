def solution(s):
    answer = 0
    digits={'zero': 0, 'one':1, 'two':2, 'three': 3, 'four': 4 , 'five': 5,
           'six': 6 , 'seven': 7, 'eight': 8, 'nine': 9 , 'ten': 10}
    for digit in digits:
        s=s.replace(digit, str(digits[digit]))
    answer=int(s)
    return answer
