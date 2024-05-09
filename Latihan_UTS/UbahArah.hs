module UbahArah where

ubahArah :: Int -> Int -> Int
ubahArah s r
    | s + r < 0 = 360 + (s + r)
    | s + r >= 0 = (s + r) `mod` 360

getElTengah :: [Int] -> Int
getElTengah l
   | length l == 1 = head l
   | length l == 2 = head l 
   | otherwise = getElTengah (tail (init l))

fDeretTujuh :: Int -> Int 
fDeretTujuh n 
    | n == 1 = 1 
    | otherwise = fDeretTujuh (n-1) + (6 + 5*(n-2))

getSmallest :: [Int] -> Int
getSmallest li
    | length li == 1 = head li
    | head li <= getSmallest (tail li) = head li
    | otherwise = getSmallest (tail li)