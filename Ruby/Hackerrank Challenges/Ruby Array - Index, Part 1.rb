# https://www.hackerrank.com/challenges/ruby-array-index-i/problem

# return the element of the Array variable `arr` at the position `index`
# arr.at(index) # or
# arr[index]
def element_at(arr, index)
    arr[index]
end
# return the elements of the Array variable `arr` between the start_pos and end_pos (both inclusive)
def inclusive_range(arr, start_pos, end_pos)
    arr[start_pos..end_pos]    
end
# return the elements of the Array variable `arr`, start_pos inclusive and end_pos exclusive
def non_inclusive_range(arr, start_pos, end_pos)
    arr[start_pos...end_pos]
end
# return `length` elements of the Array variable `arr` starting from `start_pos`
def start_and_length(arr, start_pos, length)
    if arr.length > start_pos+length
        arr[start_pos...(start_pos+length)]
    end
end
