set INPUTFILE [open 1.txt r]
puts $INPUTFILE
while {[gets $INPUTFILE line] >= 0} {
	puts "$line"
}
close $INPUTFILE
