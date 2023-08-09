class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if len(flowerbed) == 1 and n == 0 :
            return True

        if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0 :
            return True 

        if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 1 :
            return False



        for i in range(0, len(flowerbed)) :
            if c == n :
                break

            if i != 0 and i != len(flowerbed) - 1 :
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] != 1 :
                    flowerbed[i] = 1
                    c += 1

            if i == 0 :
                if flowerbed[i + 1] == 0 and flowerbed[i] != 1 :
                    flowerbed[i] = 1
                    c += 1

            if i == len(flowerbed) - 1 :
                if flowerbed[i - 1] == 0 and flowerbed[i] != 1 :
                    flowerbed[i] = 1
                    c += 1

        return n == c