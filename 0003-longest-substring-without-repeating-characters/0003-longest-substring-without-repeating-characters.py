class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftpointer = 0  # 왼쪽 포인터
        max_length = 0  # 가장 긴 부분 문자열의 길이
        char_set = set()  # 현재 윈도우에서의 문자 집합
        for rightpointer in range(len(s)):
            # 중복된 문자가 발견되면 left 포인터를 오른쪽으로 이동
            while s[rightpointer] in char_set:
                char_set.remove(s[leftpointer])
                leftpointer += 1
            # 현재 문자를 집합에 추가
            char_set.add(s[rightpointer])
            # 최대 길이를 갱신
            max_length = max(max_length, rightpointer - leftpointer + 1)
        return max_length