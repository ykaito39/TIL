#encoding: UTF-8
for i in 1..ARGV[0].to_i do
	if i%5 == 0 && i%2 == 0
		puts "#{i}: fizzbuzz"
	elsif i%5 == 0
		puts "#{i}: buzz"
	elsif i%3 == 0
		puts "#{i}: fizz"
	else
		puts i
	end
end

