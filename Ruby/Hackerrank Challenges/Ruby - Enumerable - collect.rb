# https://www.hackerrank.com/challenges/ruby-enumerable-collect/problem

def rot13(secret_messages)
  # your code here
    
    secret_messages.collect do |message|
        message.tr!("abcdefghijklmnopqrstuvwxyz",
        "nopqrstuvwxyzabcdefghijklm")
    end
    
    return secret_messages
end
