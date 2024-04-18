def solution(N, stages):
    '''
    stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
    - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
    - N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 의미한다.
    실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    '''
    
    answer = []
    for stage in range(1, N+1):
        failure = stages.count(stage)
        if stages:
            ratio = failure / len(stages)
            stages = [x for x in stages if x!=stage]
        else:
            ratio = 0.0
        answer.append((stage, ratio))
    
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    answer = [x[0] for x in answer]
    
    return answer
