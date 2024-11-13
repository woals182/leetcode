class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 음수 및 마지막자리 0인애들 처리
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # 뒤에서 자리 뒤집어서 찾기
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x //= 10

        # x가 리버스거나 리버스 마지막자리 제외하고 비교하기
        return x == reversed or x == reversed // 10
