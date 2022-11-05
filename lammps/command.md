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
# restart
```
print                          .
print ==========================================
print "50 steps CG Minimization"
print ==========================================
print                          .

log             min.eng
dump            1 all atom 1 min.lammpstrj
dump_modify     1 image yes scale yes
thermo          10
thermo_style    multi
min_style       sd
minimize        0.0 1.0e-8 50 500
undump          1


print                          .
print ==========================================
print "1000 steps nvt  simulations"
print ==========================================
print                          .

restart         10 nvt.*.rst
log             nvt.eng
dump            1 all atom 10 nvt.lammpstrj
dump_modify     1 image yes scale yes
thermo          10
thermo_style    multi
fix             4 all nvt temp 183 183 100.0
run             1000
unfix           4
undump          1

```
因为`minimize`以后没有`reset_timestep`,所以步数不会停止,nvt会接着minimize的步数,51-1500
由于`restart`是10步一输出，所以会从60一直输出到1500，即nvt.60.rst nvt.70.rst ... nvt.1040 nvt.1050.rst

