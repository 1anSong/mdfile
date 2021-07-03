## 什么是递归
### 函数的嵌套调用
```cpp
#include <iostream>
#include <cmath>
using namespace std;
bool checkPrime(int);
int main()
{
	int a;
	cout << "请输入一个整数" << endl;
	while (cin >> a)
	{
		if (checkPrime(a))
			cout << "是质数"<<endl;
		else
			cout << "不是质数"<< endl;
	}
	return 0;
}

bool checkPrime(int number)
{
	int i,k;
	k=sqrt(number);
	for (i=2;i<=k;i++)
	{
		if(number%i==0)
			return 0;
	}
	return 1;
}

```
### 思路整理
函数不能嵌套定义
- 所有函数一律平等

函数可以嵌套调用
- 无论嵌套多少层 原理都一样
### 问个问题
一个函数能够调用"它自己"吗?
### 已知n,求n!
```cpp
#include <iostream>
using namespace std;
int fact(int n)
{
	if (n==1)
		return 1;
	else 
		return n*fact(n-1);

}
int main()
{
	cout << fact(4) <<endl;
	return 0;
}
```
### 什么是递归?(定义)
#### 他说
一个函数在其定义中直接或者间接调用其自身的一种方法
![循环]() <++>
#### 


## 深入理解递归的过程

## 递归的作用
### 用递归来完成递推
### 模拟连续发生的动作
### 进行"自动的分析"

