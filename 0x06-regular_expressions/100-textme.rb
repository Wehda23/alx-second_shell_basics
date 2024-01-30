#!/usr/bin/env ruby
# A Regular expressiong to find pattern using ruby
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
