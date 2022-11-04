# log
会输出自这条命令开始到下一条log命令之间的信息
# thermo
输出热力学信息
- 此命令要在run前面或者minimize前面
## 关于多少步输出一次的问题
```lammps
print                          .
print =====================================
print "NVT dynamics to heat system"
print =====================================
print                          .

reset_timestep  0
log             heat.eng
timestep        1.0
velocity        all create 1.0 12345678 dist uniform
thermo          100
thermo_style    multi
dump            1 all custom 1000 heat.lammpstrj id type xu yu zu vx vy vz
fix             4 all nvt temp 1.0 ${temperature} 100.0
run             10000
unfix           4
undump          1
write_restart   heat.rst

print                          .
print =====================================
print "NVT dynamics"
print =====================================
print                          .

reset_timestep  0
log             nvt.eng
dump            1 all custom 1000 nvt1.lammpstrj id type xu yu zu vx vy vz
fix             4 all nvt temp ${temperature} ${temperature} 100.0
run             10000
unfix           4
undump          1
write_restart   nvt.rst
```
此代码的第一个thermo为`thermo 100` 第一个为`thermo 10`,会在第一个thermo至第二个100步输出一次,从第二个thermo到遇见下一个thermo或者结束 10步输出一次
