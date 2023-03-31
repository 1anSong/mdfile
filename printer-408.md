# 打印机使用手册
使用课题组
## 先决条件
- 确保自己的电脑连接**ct-408**网络
> wifi name: ct-408

> passwd: ct0912408
- 确保打印机所连接的电脑开机
Note:只要打印机电脑开机，将自动连接到ct-408网络

## 打印流程

step 1: ssh连接打印机电脑

 >ip : 192.168.31.100
> 端口：22
>用户名：public
>密码：public

step 2: 确保打印机正确连接（可省略）

在终端输入以下内容
```
lpq
```
如一切正常，输出
HP_LaserJet_M1005 is ready
 no entries

3. 开始打印

```
lpr <filename>
```
**Warning**:无法打印office文件（word，excel,ppt),但可以先将他们转成pdf，再打印。

## 问题&解决办法
若第二步出现问题，则可以用以下步骤解决
1. 找到可用的打印机


```
lpstat -p -d
```
正常情况下输出：
printer HP_LaserJet_M1005 is idle.  enabled since <日期>
其中  HP_LaserJet_M1005 为闲置状态下的打印机

2. 将上一步输出的打印机名称 如：HP_LaserJet_M1005 设置为默认打印机
```
lpoptions -d HP_LaserJet_M1005
```
3. 再次检查打印机是否成功连接
```
lpq 
```
