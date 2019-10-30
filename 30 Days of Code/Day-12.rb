# https://www.hackerrank.com/challenges/30-inheritance/problem



class Student < Person
    def initialize(firstName, lastName, id, scores)
        super(firstName, lastName, id)
        @scores = scores
    end

    def calculate
        sum = 0 
        @scores.each do |score|
        sum = sum + score
    end

    average = sum / @scores.length

    if(average >= 90)
        return 'O' # Outstanding
    elsif(average >= 80)
        return 'E' # Exceeds Expectations
    elsif(average >= 70)
        return 'A' # Acceptable
    elsif(average >= 55)
        return 'P' # Poor
    elsif(average >= 40)
        return 'D' # Dreadful
    else
        return 'T' # Troll
    end
  end   
end

