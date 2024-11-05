#!/usr/bin/env ruby
#Extract sender, receiver, and flags information
puts ARGV[0].scan(/(?<=from|to|flags):(\+?\w+|[-?[0-1]:?]+)/).join(',')
