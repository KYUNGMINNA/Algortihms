def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    return print(str(int(''.join(numbers))))

solution([6,10,2])