def solution(number, k):
    answer = []

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return print(''.join(answer[:len(answer) - k]))
number="4177252841"
k=4
solution(number,k)