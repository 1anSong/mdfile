set a {1 2 3}
set b {4 5 6}
set c [concat $a $b]
puts $c
puts [concat $a $b]
set t1 "hello"
set t2 "world"
puts [concat $t1 $t2]

set list1 {a b c d e f}
puts [lindex $list1 1]
set b [expr [llength $list1] - 1]
puts $b
puts [lindex $list1 $b]

lappend list1 c
puts $list1


set list3 {b c a a}
set var [lsort $list3]
puts $var
set var1  [lsort -unique $list3]
puts $var

set a [expr 1 + 2]
puts $a 


set a {0 1 2}
set v {1 2}
set c  [expr [llength $a ]+[llength $v]]
puts $c


set a 1 
set b 2

if {$a > $b} {
	puts $a } else {
puts $b }


