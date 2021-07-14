#### tip
1. 按照计算机的**存储方式** 可分为两大基本类型:整数类型和浮点数类型
2. sizeof 圆括号的使用时机取决于运算对象是**类型** 还是**特定量** ?运算对象是类型时,圆括号必不可少,但是对于特定量,可有可无.也就是说,对于类型,应写成sizeof(char),sizeof(float);对于特定量,可写成sizeof name,size of 6.28.尽管如此,还是建议所有情况下都使圆括号,如sizeof(6.28).
3. 在字符串中,可以使用\n来表示换行字符,不能通过按下Enter或(Return)键产生实际的换行符.
4. C的标准数学库提供了一个pow()函数用于指数运算,例如,pow(3.5,2.2)返回3.5的2.2次幂
5. scanf()函数返回成功读取的项数.
6. 在字符串

#### C标准
- K&R C 
- ANSI C ISO C C89 C90 
- C99
- C11
#### ANSI C
```
int imax(int,int);
int imax(int a,int b);
```
#### C90
c90新增了`const`关键字,用于限定一个变量为**只读**其声明格式如下：
``` c
const int MONTHS =12; //MONTHS在程序中不可更改，值为12
```
#### printf()返回值
printf()返回打印所有字符的个数，包括空格，和不可见的换行符`\n`
```c
// prntval.c --printf()的返回值
#include <stdio.h>
int main(void) {
  int bph2o = 212;
  int rv;

  rv = printf("%d F is water's boiling point.\n", bph2o);
  printf("The printf() function printed %d characters.\n", rv);
  return 0;
}
```
####  




