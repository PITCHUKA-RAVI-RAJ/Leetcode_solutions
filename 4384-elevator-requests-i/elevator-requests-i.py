class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        t=0
        for i in range(len(requests)-1):
            t+=abs(requests[i]-requests[i+1])
        return t+requests[0]