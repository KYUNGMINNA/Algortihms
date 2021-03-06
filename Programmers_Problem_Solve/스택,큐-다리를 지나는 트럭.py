from collections import deque

# Stack Solution
def solution(bridge_length, weight, truck_weights):

    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    return print(answer)

solution(2,10,[7,4,5,6])

#deque Solution
def solution2(bridge_length, weight, truck_weights):
    answer = 0
    bridges = deque([0] * bridge_length)
    truck=deque(truck_weights)
    while bridges:
        answer += 1
        bridges.popleft()
        if truck:
            if sum(bridges) + truck[0] <= weight:
                bridges.append(truck.popleft())
            else:
                bridges.append(0)

    return print(answer)

solution2(2,10,[7,4,5,6])