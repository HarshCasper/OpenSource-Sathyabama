# https://www.hackerrank.com/challenges/ruby-enumerable-group-by/problem

def group_by_marks(marks, pass_marks)
  # your code here
  marks.group_by do |key, value|
    if key.empty? == false
      if value <= pass_marks
          "Failed"
      else
          "Passed"
      end
    end
  end       
end
