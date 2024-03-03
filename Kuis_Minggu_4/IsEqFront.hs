module IsEqFront where

-- T1 dan T2 dan menghasilkan true jika potongan awal list T2 
-- mengandung T1 (dengan panjang dan urutan karakter yang sama). Banyaknya elemen T2 selalu lebih dari atau sama dengan T1.​

isEqFront :: [Char] -> [Char] -> Bool
isEqFront li1 li2 
    | (null li1) = True
    | (null li2) = False 
    | (head li1) == (head li2) = isEqFront (tail li1) (tail li2)
    | (head li1) /= (head li2) = False

-- T1: [’a’, ’b’, ’c’] T2: [’a’, ’b’, ’c’, ’d’, ’e’]              Hasil: true​
-- T1: [’a’, ’b’, ’c’] T2: [’a’, ’b’, ’c’]                         Hasil: true​
-- T1: [’a’, ’b’, ’c’] T2: [’a’, ’b’, ’a’, ’b’, ’c’, ’d’]        Hasil: false​
-- T1: [’a’, ’b’, ’c’] T2: [’a’, ’b’, ’d’, ’a’, ’b’, ’c’]        Hasil: false 