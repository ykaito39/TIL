#!/usr/bin/ruby
#encoding: UTF-8

puts "times+++++++++++++++++++++++++++++++++++++++"
7.times do |i|
	puts "猫が#{i}匹原っぱはしる"
end

puts "for1++++++++++++++++++++++++++++++++++++++++"
sum = 0
for i in 1..5
	sum += i
end

puts sum

puts "for2++++++++++++++++++++++++++++++++++++++++"
sum	 = 0
from = 1
to	 = 100
for i in from..to
	sum += i
end

puts sum

puts "while++++++++++++++++++++++++++++++++++++++++"
i = 1
while i <= 5
	puts i
	i += 1
end

puts "until+++++++++++++++++++++++++++++++++++++++"
puts "until文は、条件判定がwhile文とは反対になります。"
i = 1
until i >= 10 do
	puts i
	i += 1
end

puts "each1+++++++++++++++++++++++++++++++++++++++"
names = ["awk", "Perl", "C++", "Python"]
names.each do |name|
	puts name
end

puts "each2+++++++++++++++++++++++++++++++++++++++"
sum = 0
(1..5).each do |i|
	sum += i
end
puts sum

puts "loop++++++++++++++++++++++++++++++++++++++++"
i = 0
loop do
	print "Ruby"
	if i > 20
		break
	end
	i += 1
end

puts "break and something+++++++++++++++++++++++++"
i = 0
["D", "Pearl", "Ruby", "Scheme"].each do |lang|
	i += 1
	if i == 3
		break
	end
	p [i, lang]
end

i = 0
["D", "Pearl", "Ruby", "Scheme"].each do |lang|
	i += 1
	if i == 3
		next #3回目のLoopだった場合、これ以降の処理は飛ばされ、次のループに
	end
	p [i, lang]
end



