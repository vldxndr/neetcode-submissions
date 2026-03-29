class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] = 0
            for j in range(i + 1, len(arr)):
                if (arr[j] > arr[i]):
                    arr[i] = arr[j]
            if i == len(arr) - 1:
                arr[i] = -1
        return arr