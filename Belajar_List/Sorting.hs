module Sorting where

isBigger :: Int -> [Int] -> Bool
isBigger a li
    | null li = True
    | head li > a = False
    | otherwise = isBigger a (tail li)

biggest :: [Int] -> Int
biggest li
    | length li == 1 = head li
    | isBigger (last li) (init li) = last li
    | otherwise = biggest (init li)

isSmaller :: Int -> [Int] -> Bool
isSmaller a li
    | null li = True
    | head li < a = False
    | otherwise = isSmaller a (tail li)

smallest :: [Int] -> Int
smallest li
    | length li == 1 = head li
    | isSmaller (last li) (init li) = last li
    | otherwise = smallest (init li)

delElmt :: Int -> [Int] -> [Int]
delElmt a li
    | null li = []
    | head li /= a = head li : delElmt a (tail li)
    | otherwise = tail li

sortBigtoSmall :: [Int] -> [Int]
sortBigtoSmall li
    | null li = []
    | otherwise = biggest li : sortBigtoSmall (delElmt (biggest li) li)

sortSmalltoBig :: [Int] -> [Int]
sortSmalltoBig li
    | null li = []
    | otherwise = smallest li : sortSmalltoBig (delElmt (smallest li) li)