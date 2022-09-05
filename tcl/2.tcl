set a {1 2 3 4 5}
set length_a [llength $a] 
if {$length_a > 3} {
	puts "The length of a is larger than 3"
} elseif {$length_a ==3} {
	puts "The length of a is equal to 3"
} else {
	puts "The length of a is shorter than 3"
}
