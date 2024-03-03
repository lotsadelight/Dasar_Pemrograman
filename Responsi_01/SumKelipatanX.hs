module SumKelipatanX where

-- DEFINISI DAN SPESIFIKASI
sumKelipatanX :: Int -> Int -> Int -> Int

-- REALISASI
sumKelipatanX a b x
    | (mod a x /= 0) && (a <= b) = sumKelipatanX (a+1) b x
    | a > b = 0
    | (a <= b) && (mod a x == 0) = a + sumKelipatanX (a+1) b x

-- APLIKASI
-- sumKelipatanX 1 10 2