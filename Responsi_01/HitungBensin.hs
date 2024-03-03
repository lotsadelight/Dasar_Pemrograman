module HitungBensin where

-- HITUNG BENSIN
-- DEFINISI DAN SPESIFIKASI
hitungBensin :: Int -> Int -> Int

-- REALISASI
hitungBensin a b
    | a == b = 0
    | a `mod` 2 == 0 = 1 + hitungBensin (a `div` 2) b
    | a `mod` 2 == 1 = 1 + hitungBensin ((a * 3) + 1) b