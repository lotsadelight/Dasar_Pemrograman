module ListOfInteger where

nbElmt :: [Int] -> Int
-- Menghasilkan banyaknya elemen dalam list.
nbElmt li 
    | null li = 0
    | otherwise = 1 + nbElmt (tail li)

elmtKeN :: [Int] -> Int -> Int 
-- Menghasilkan elemen ke-n dari sebuah list.
elmtKeN li n 
    | n /= 1 = elmtKeN (tail li) (n - 1)
    | otherwise = head li

nbOcc :: [Int] -> Int -> Int
-- Menghitung kemunculan x pada sebuah list. 
nbOcc li x
    | null li = 0
    | head li == x = 1 + nbOcc (tail li) x
    | otherwise = 0 + nbOcc (tail li) x