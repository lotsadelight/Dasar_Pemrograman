{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use odd" #-}
isAllGanjil :: [Int] -> Bool
isAllGanjil l
    | null l = True
    | head l `mod` 2 /= 0 = isAllGanjil (tail l)
    | otherwise = False