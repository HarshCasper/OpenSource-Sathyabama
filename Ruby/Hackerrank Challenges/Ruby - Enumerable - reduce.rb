# https://www.hackerrank.com/challenges/ruby-enumerable-reduce/problem

def sum_terms(n)
    nth_term = (n**2)+1
  (1..n).reduce(0){|sum, n| sum+(n**2+1)}
 end
