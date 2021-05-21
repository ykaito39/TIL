#!/usr/bin/ruby
#encoding: UTF-8

tags = [ "A", "IMG", "PRE" ]
tags.each do |tagname|
	case tagname
	when "P", "A", "D", "HOGE"
		puts "its a small world."
	when "IMG", "THE"
		puts "its a big world."
	else
		puts "HOGE HOGE"
	end
end

array = [ "A", 1, nil]
array.each do |item|
	case item
	when String
		puts "#{item} is String."
	when Numeric
		puts "#{item} is Numeric."
	else
		puts "#{item} is not ほげほげ."
	end
end
