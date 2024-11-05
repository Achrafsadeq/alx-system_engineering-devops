#!/usr/bin/env ruby
#Match a string that starts with 'h' and ends with 'n' with any single character in between
puts ARGV[0].scan(/^h.n$/).join
