fib :: (Integral a) => a -> a
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

firstKEntriesOfSequence k = [ fib a | a <- [0..k] ]
kthPartialSum k = sum (firstKEntriesOfSequence k)
termsToAddInMetaSum n = [ kthPartialSum (fib k) | k <- [0..n] ]
metaSum n = sum (termsToAddInMetaSum n)

main = print (metaSum 6)