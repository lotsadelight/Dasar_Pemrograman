module DeretSegitiga where

-- DERET SEGITIGA 
-- DEFINISI DAN SPESIFIKASI
deretSegitiga :: Int -> Int
    
-- REALISASI
deretSegitiga n
    | n == 1 = 1 
    | otherwise = n + deretSegitiga (n-1)