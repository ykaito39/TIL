# 更新履歴
# v0.1 2016/03/17
# 	・tweetできるようになったよ(´・ω・`)
# 	・複数行ツイートに対応
# v0.2 2016/03/18
#	・TL取得できるようになったよ	

require 'rubygems'
require 'pp'
require 'twitter'

CK = ''
CS = ''
AT = ''
AS = ''

client = Twitter::REST::Client.new do |config|
    config.consumer_key        = CK
    config.consumer_secret     = CS
    config.access_token        = AT
    config.access_token_secret = AS
end

iam = client.user

case ARGV[0]
	when 'tweet' then
		argv_cp = ARGV
		argv_cp.delete_at(0)	#1つ目の要素(command指定文字)を消す
		str = ""

		#入力文字列を複数行化
		argv_cp.each do |c|
			str += c + "\n"
		end

		#tweetする
		client.update(str)
		puts "\n--------tweet内容--------"
		puts str
		puts "-------------------------"

	when 'gettl' then
		#TLより20件取得
		client.home_timeline(:count => 20).each do |tweet|
			puts "#{tweet.user.name}@#{tweet.user.id}"
			puts "#{tweet.text}"
			puts
		end

	else
		print "Option: tweet or gettl"
end
