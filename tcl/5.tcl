set a 4

proc sample {x} {
	global a 
	return [expr $a + $x]
}

puts [sample 3]
