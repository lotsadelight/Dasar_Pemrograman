module GetSmallest where

getSmallest :: [Int] -> Int
getSmallest l
    | length l == 1 = head l
    | head l < getSmallest (tail l) = head l
    | otherwise = getSmallest (tail l)