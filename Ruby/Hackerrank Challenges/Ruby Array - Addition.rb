# https://www.hackerrank.com/challenges/ruby-array-addition/problem

def end_arr_add(arr, element)
        end_arr_add = arr.push(element)
        end_arr_add
end

def begin_arr_add(arr, element)
        begin_arr_add = arr.unshift(element)
        begin_arr_add
end

def index_arr_add(arr, index, element)
        index_arr_add = arr.insert(index, element)
        index_arr_add
end

def index_arr_multiple_add(arr, index)
        index_arr_multiple_add = arr.insert(index, 11, 22)
        index_arr_multiple_add
end
