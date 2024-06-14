class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0]*n
        for l, r, s in bookings:
            answer[l-1] += s
            if r < n: answer[r] -= s
        for i in range(1, n):
            answer[i] += answer[i-1]
        return answer