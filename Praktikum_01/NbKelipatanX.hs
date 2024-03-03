module NbKelipatanX where

-- FUNGSI KELIPATAN X
-- DEFINISI DAN SPESIFIKASI
nbKelipatanX :: Int -> Int -> Int -> Int
-- REALISASI
nbKelipatanX m n x 
    | n `mod` x /= 0 = nbKelipatanX m (n-1) x
    | otherwise = kelipatanUtama m n x

-- FUNGSI ANTARA UTNUK MENGHITUNG KELIPATAN X
kelipatanUtama :: Int -> Int -> Int -> Int 
-- REALISASI
kelipatanUtama m n x
    | m <= n = 1 + nbKelipatanX m (n - x) x
    | otherwise = 0