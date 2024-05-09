module DelNthElmt where

delNthElmt :: Int -> [Int] -> [Int]
delNthElmt n li =
 if (null li) then []
 else if (n == 1) then tail li
 else head li : delNthElmt (n-1) (tail li)
