module SumIsiList where

sumIsiList :: [Int] -> Int 
sumIsiList l 
    | null l = 0
    | otherwise = head l + sumIsiList (tail l)