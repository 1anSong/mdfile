## 不要忘记初始化
```	
#include <stdio.h>
int sum(int *a, int n) {
  int sum = 0;//这里必须初始化sum,如果不初始化，会输出一个垃圾值
 // int sum; 
  for (int i = 0; i < n; i++)
    sum += a[i];
  return sum;
}

int main(void) {
  int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
  printf("%d", sum(arr, 10));
  return 0;
}
```
## int 与 #define
### 在一个程序中，如果定义名字相同的两个变量，编译器会提示warning
```
int i = 5;
int i = 5;
```
这种会提示warning

### 在一个程序中，如果定义名字相同的两个宏，要分情况
#### 如果宏的值一样，则没有问题
```
#define I 5
#define I 5  
```
#### 如果宏的值不一样，则没有问题
```
#define I 4
#define I 5  
```

## Why am I getting "undefined reference to sqrt" error even though i include math.h header?
解决办法：gcc test.c -o test -lm

## size_t 
在C语言中，数组长度，索引值最好使用size_t类型，而不是int 或者 unsigned 

## typedef 在struct中的使用
```
typedef struct complex{
  float real;
  float imag;
}COMPLEX;
```
-用typedef命名一个结构类型时，可以*省略该结构的的标记*:
```
typedef struct{
  float real;
  float imag;
}COMPLEX;
```
## enum 
enum 常量是int类型，因此只要能使用到int类型的地方就可以使用枚举类型。
```
enum specturm {red,yellow};
```
这里 enum specturm 就类似于 int，可以当成int使用。

例如：
```
#include <stdio.h>
enum test { hello, world };
enum test val(void);

int main(void) {
  printf("%d\n", val());
  return 0;
}
```
## 断言库的使用
assert接受一个整形表达式作为参数，如果表达式求值为***假***,assert()宏
就在标准错误流（stderr)中写入一条错误消息，并调用abort()函数终止程序。

例如
```
#include <assert.h>

int main(void) {
  int x = 4;
  assert(x < 0);
  return 0;
}
```
程序编译运行，会输出一下东西
a.out: 2.c:5: main: Assertion `x < 0' failed.

## 优先级
1. *c.type == *(c.type)
2. *c->type == *(c->type)
3. *p++ == *(p++) 
4. *++p == *(++p) 

```
#include <stdio.h>
int main(int argc, char *argv[]) {
  static char *var = "xcsong";
  static char *var1 = "xcsong";
  char *p = var;
  char *p1 = var1;

  char ch = *p++;
  char ch1 = *++p1;

  printf("%c\n", ch); /* x */
  printf("%c\n", ch1); /* c */

  return 0;
}
```
## 如何声明&定义一个结构
有三种方式
### 第一种方式

```
struct point {
  int x;
  int y;
};
struct point p1,p2;
```
p1和p2都是point，里面有x和y的值。

### 第二种方式
```
struct {
  int x;
  int y;
} p1,p2;
```
p1和p2都是一种无名结构，里面有x和y,这种方式只是想要两个变量，变量里包含x和y，用这种方法以后可能再使用这种变量.

### 第三种形式
```
struct point {
  int x;
  int y;
} p1,p2;
```
p1和p2都是point，里面有x和y的值。

## struture 和 指针
也可以取struct变量的地址进行初始化
```
#include<stdio.h>

struct test_type{
 int i;
 int j;
};

int main(void)
{
  struct test_type test;
  (&test)->i=3; /* 这里就是使用test的地址进行初始化 */
  test.j = 4;
  printf("%d\n",test.i);
  printf("%d\n",(&test)->j);
  return 0;
}

```
## gdb调试
### 启动调试
对于C程序来说，需要再编译时加上-g参数，保留调试信息，否则不能使用GDB进行调试。

## const 限定符
以const关键字声明的对象，其值不能通过*赋值 递增 递减 * 来修改
```
const int nochange; /* 限定 nochange的值不能被修改 */
nochange 12; /* 不允许 */

const int nochange = 12; /* 允许，可以初始化const变量 */

const char *var = "hello";
char *p = var; /*不允许*/

```


