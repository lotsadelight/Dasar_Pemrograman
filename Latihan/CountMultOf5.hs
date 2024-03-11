module Latihan.CountMultOf5 where

-- DEFINISI DAN SPESIFIKASI
{- Menerima sebuah list of integer dan mengembalikan banyaknya elemen list yang merupakan kelipatan dari 5. -}

-- REALISASI 
countMultOf5 :: [Int] -> Int
countMultOf5 li
    | null li = 0 
    | head li `mod` 5 == 0 = 1 + countMultOf5 (tail li)
    | otherwise = 0