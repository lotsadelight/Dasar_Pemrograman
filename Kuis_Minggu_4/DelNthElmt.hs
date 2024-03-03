module DelNthElmt where

delNthElmt :: Int -> [Int] -> [Int]
delNthElmt n li
 | null li = []
 | n == 1 = tail li
 | otherwise = [head li] ++ delNthElmt (n-1) (tail li)