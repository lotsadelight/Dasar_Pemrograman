module FilterGanjil where

filterGanjil :: [Int] -> [Int]
filterGanjil li
    | null li = []
    | (head li) mod 2 /= 0 = [head li] ++ 