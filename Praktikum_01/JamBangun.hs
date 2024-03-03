module JamBangun where

-- JAM BANGUN 
-- DEFINISI DAN SPESIFIKASI
jamBangun :: Int -> Int -> Int -> (Bool, Int, Int, Int)

-- REALISASI
jamBangun j m d 
    | (j == 23) && (m > 45) && (d > 00) = (True, 0, m - 45, d)
    | j < 7 = (True, 7 - j, (44 - m) + 15, 59 - d)
    | j == 7 && m < 44 = (True, 0, (44 - m), 59 - d)
    | j == 7 && m == 44 && d <= 59 = (True, 0, 0, 59 - d)
    | j == 7 && m == 45 && d == 0 = (True, 0, 0, 0)
    | otherwise = (False, 0, 0, 0)