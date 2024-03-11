module UbahArah where

ubahArah :: Int -> Int -> Int
ubahArah s r
    | s + r < 0 = 360 + (s + r)
    | s + r >= 0 = (s + r) `mod` 360