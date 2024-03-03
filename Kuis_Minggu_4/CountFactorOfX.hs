module CountFactorOfX where

countFactorOfX :: Int -> [Int] -> Int 
countFactorOfX n l
    | null l = 0
    | (n `mod` head l) /= 0 = 0 + countFactorOfX n (tail l)
    | ((n `mod` head l) == 0) && (n >= head l) = 1 + countFactorOfX n (tail l)
