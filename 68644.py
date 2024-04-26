def solution(numbers):
    answer = [numbers[i]+numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))]
    answer = sorted(list(set(answer)))
    
    return answer
