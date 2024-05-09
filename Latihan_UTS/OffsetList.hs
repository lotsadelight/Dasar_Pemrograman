module OffsetList where

id :: Float -> Float
id x = x

p1 :: Float -> Float
p1 x = x + 1

p2 :: Float -> Float
p2 x = x + 2

offsetList :: (Float -> Float) -> (Float -> Float) -> Float -> Float -> [Float]
offsetList f g a b
    | a > b = []
    | otherwise = f a : offsetList f g (g a) b

-- APLIKASI UNTUK LAMBDA
-- offsetList (\x->x) (\x->x+2) 1.2 7.1
-- offsetList (\x->if x < 0 then -999 else (x + 3.2)) (\x->x+0.5) (-1.0) 1.0