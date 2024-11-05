#!/usr/bin/env ruby
#Match a repetitive token pattern
puts ARGV[0].scan(/hbt{2,5}n/).join
