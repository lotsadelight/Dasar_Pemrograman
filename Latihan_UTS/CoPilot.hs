sumIntegers :: Int -> Int
sumIntegers n = sumHelper 0 n

sumHelper :: Int -> Int -> Int
sumHelper acc 0 = acc
sumHelper acc n = sumHelper (acc + n) (n - 1)