## 如何初始化一个结构


```c
// 这种做法只能在函数体外面,如果是在函数体里面，编译会不通过
struct st {
  int i;
  int j;
};

struct st st1;

struct st st1 = {   //注意这里的struct st 不可省略
  3,
  4
}
```

```c
struct st {
  int i;
  int j;
};

struct st st1 = {
  3,
  4
};

```
