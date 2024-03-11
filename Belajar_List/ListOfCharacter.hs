module ListOfCharacter where 

inverse :: [Char] -> [Char]
inverse lc
    | null lc = []
    | length lc == 1 = lc
    | otherwise = [last lc] ++ (inverse (init lc))

isElmt :: Char -> [Char] -> Bool
isElmt a l 
    | null l = False 
    | a == head l = True 
    | otherwise = isElmt a (tail l)

makeUnique :: [Char] -> [Char]
makeUnique l 
    | null l = []
    | isElmt (last l) (init l) = makeUnique (init l)
    | otherwise = makeUnique (init l) ++ [last l]