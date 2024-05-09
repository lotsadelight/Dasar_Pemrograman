module Latihan_UTS.SortList where

sortList :: [Int]->[Int]
sortList l
 | length l == 1 = [head l]
 | otherwise =
    [if head l < head (sortList (tail l))
        then head l
    else head (sortList (tail l))] ++ sortList (tail (
        if head l > head (sortList (tail l))
            then (sortList (tail l)) ++ [head l]
        else [head l] ++ (sortList (tail l)) ))

-- 9, 13, 4, 6, 23, 5, 7