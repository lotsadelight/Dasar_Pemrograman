{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use odd" #-}
{-# HLINT ignore "Use even" #-}
module FilterGanjil where

filterGanjil :: [Int] -> [Int]
filterGanjil li
    | null li = []
    | head li `mod` 2 /= 0 = head li : filterGanjil (tail li)
    | head li `mod` 2 == 0 = filterGanjil (tail li)