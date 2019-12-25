# https://www.hackerrank.com/challenges/ruby-array-selection/problem

def select_arr(arr)
  select_arr = arr.select(&:odd?)
end

def reject_arr(arr)
  reject_arr = arr.reject {|x| x % 3 == 0}
end

def delete_arr(arr)
  delete_arr = arr.delete_if{ |a| a > 0 }.map{ |a| -a }
end

def keep_arr(arr)
  keep_arr = arr.keep_if {|a| a < 4 }
end
