# 1 HTML语法规范
## 1.1 基本语法概述
1. HTML标签是由**尖括号**包围的关键字 例如`<html>`
2. HTML标签是成对出现的，例如`<html>`和`</html>`,我们称为**双标签**。标签中的第一个标签是是开始标签，第二个标签是结束标签
3. 有些特殊的标签必须是单个标签(极少情况),例如`<br/>`，我们称之为**单标签**
## 1.2标签关系 
双标签可以分为两类，**包含关系**和**并列关系**
### 包含关系
```html
<head>
	<title> </title>
</head>
```
### 并列关系
``` html
<head> </head>
<body> </body>
```
# 2 HTML基本结构标签
## 2.1第一个HTML网页
每个网页都会有一个基本的结构标签(也称骨架标签),页面内容也是在这些基本标签上书写。

HTML页面也称HTML文档。
| 标签名             | 定义       | 说明                                                    |
|--------------------|------------|---------------------------------------------------------|
| `<html> </html>`   | HTML标签   | 页面中最大的标签，我们称为**根标签**                    |
| `<head> </head>`   | 文档的头部 | 注意在head标签中我们必须要设置的标签是title             |
| `<title> </title>` | 文档的标题 | 让页面拥有一个属于自己的网页标题                        |
| `<body> </body>`   | 文档的主体 | 元素包含文档的所有内容，页面内容 基本都是放到body里面的 |

例如
```html
<html>
	<head>
		<title>我的第一个页面</title>
	</head>
	<body>
	hello,world!
	</body>
</html>
```
# 3 网页开发工具
## 3.1 文档类型声明标签
`<!DOCTYPE>` 文档类型说明，作用是告诉浏览器使用哪种HTML版本来显示网页
```html
<!DOCTYPE html>
```
这句代码的意思是:当前页面采取的是HTML5版本显示网页

**注意** 
1. `<!DOCTYPE>`声明位于文档中的最前面的位置，处于`<html>`标签之前。
2. `<!DOCTYPE>`不是一个HTML标签，它就是文档类型声明标签。 
## 3.2 lang语言种类
用来定义当前文档显示的语言。
1. en定义语言为英语
2. zh-CN定义语言为中文
简单来说，定义为en就是英文网页，定义为zh-CN就是中文网页
## 3.3 字符集
字符集是多个字符的集合，以便计算机能够识别和存储各种文字。
在`<head>`标签内，可以通过`<metal>`标签的charset属性来规定HTML文档应该使用哪种字符编码
```html
<meta charset="UTF-8" />
```
charset常用的值有：GB2312,BIG5,GBK和UTF-8

# 4 HTML常用标签
## 4.1 标题标签 `<h1>`-`<h6>`
为了使网页更具有语义化，我们经常会在页面中用到标题标签。HTML提供了6个等级的网页标题，即`<h1>`-`<h6>`
```html
<h1>我是1级标题</h1>
<h2>我是2级标题</h2>
```
**特点** 
1. 加了标题的文字会变得更粗，字号也会依次变大。
2. 一个标题独占一行。 

## 4.2段落和换行标签(重要) 
在网页中，要把文字有条理的显示出来，就需要把这些文字分段显示。在HTML标签中，`<p>`标签用于定义**段落** ,它可以将整个网页分为若干段落
```html
<p> 我是一个段落标签</p>
<p> 我是另一个段落标签</p>
```
在html中，一个段落中的文字会从左到右依次排列，直到浏览器窗口的右端，然后才自动换行。如果希望某段文本强制换行显示，就需要使用**换行标签** `<br />`
```html
<br/>
```
单词break的缩写，意为打断，换行

**特点** 
1. `<br>` 是一个单标签
2. `<br>` 标签只是简单的开始新的一行，跟段落不一样，段落之间会插入一些垂直的间距
## 4.3文本格式化标签
在网页中，有时需要为文字设置粗体,斜体和下划线效果，这是就需要用到HTML的文本格式化标签，使文字以特殊的方式显示。

| 语义   | 标签                          | 说明                                     |
|--------|-------------------------------|------------------------------------------|
| 加粗   | `<strong></strong>` `<b></b>` | 更推荐使用`<strong>` 标签加粗 语义更强烈 |
| 倾斜   | `<em></em>`  `<i></i>`        | 更推荐使用`<em>` 标签加粗 语义更强烈     |
| 删除线 | `<del></del>`  `<s></s>`      | 更推荐使用`<del>` 标签加粗 语义更强烈    |
| 下划线 | `<ins></ins>`  `<u></u>`      | 更推荐使用`<ins>` 标签加粗 语义更强烈    |
## 4.4 `<div>`和 `<span>` 标签
`<div>`和`<span>` 标签是没有语义的，它们只是一个盒子，用来装内容的
```html
<div>这是头部</div>
<span>今日价格</span>
```
div是division的缩写，表示分割，分区。

span意为跨度，跨距.

**特点** 
1. `<div>` 标签用来布局。但是现在一行只能放一个`<div>` 大盒子
2. `<span>` 标签用来布局，一行上可以多个`<span>` ，小盒子
## 4.5 图像标签和路径(重点)
### 1 标签
在HTML中，`<img>` 标签用于定义HTML页面中的图像
```html
<img src="图像URL"/>
```
单词image的缩写，意为图像。

src是`<img>` 标签的**必须属性**，它用于指定图像文件的**路径和文件名**。
| 属性   | 属性值   | 说  明                                                     |
|--------|----------|------------------------------------------------------------|
| src    | 图片路径 | 必须属性                                                   |
| alt    | 文本     | 替换文本，图像不能显示的文字(图片无法显示的时候显示的文字) |
| title  | 文本     | 提示文本，鼠标放到图像上，显示的文字                       |
| width  | 像素     | 设置图像的宽度                                             |
| height | 像素     | 设置图像的高度                                             |
| border | 像素     | 设置图像的边框粗细                                         |
**注意事项** 
1. 一般来说，宽度和高度修改其中一个就可以，另一个等比例缩放	
2. 图像标签可以设置多个属性，必须写在标签名的后面
3. 属性之间不分先后顺序，标签名和属性，属性与属性之间用**空格** 分开。
4. 属性采取键值对的格式，即key="value"的格式，属性=“属性值”
### 2 路径
- 目录文件夹和根目录

实际工作中，我们的文件夹不能随便乱放，否则用起来很难快速的找到他们，因此我们需要一个文件夹来管理他们。

**目录文件夹** 就是普通文件夹,里面只不过存放了我们做页面所需的相关素材，比如html文件，图片等

**根目录** 打开文件夹的第一层就是根目录
## 4.5 超链接标签(重点)
在HTML中，`<a>` 标签用于定义超链接，作用是从一个页面链接到另一个页面。
### 1 链接的语法格式
```html
<a href="跳转目标" target="目标窗口的弹出方式">文本或图像</a>
```
单词anchor的缩写，意为:锚

两个属性的作用如下:
| 属性   | 作用                                                                                        |
|--------|---------------------------------------------------------------------------------------------|
| href   | 用于指定链接目标的url地址，(必须属性)当为标签应用href属性时，它就有了超链接的功能           |
| target | 用于指定链接页面的打开方式，其中_self为默认值(在当前页面打开)，_blank为在新窗口中打开方式。 |

### 2 连接分类
1. 外部链接，例如`<a href="http:www.baidu`.com" target="_blank">百度</a>
2. 内部链接，网站内部页面之间的相互连接，直接链接内部页面名称即可，例如`<a href="index.html">首页</a>`  
3. 空连接，如果没有确定链接目标时，`<a href="#">首页</a>` .
4. 下载链接，如果href里面地址是一个文件或者压缩包，会下载这个文件。
5. 网页元素链接，在网页中的各种网页元素，如文本，图像，表格，音频，视频等都可以添加到超链接 。`<a href="index.html"><img src="img.jpg">首页</a>`
6. 锚点链接，点我们可以链接，可以快速定位到页面中的某个位置。
- 在链接文本的href属性中，设置属性值为**#名字**的形式，如`<a href="#two">第二集</a>` 
- 找到目标位置标签，里面添加一个id属性=刚才的名字，如：`<h3 id="two">第二集介绍</h3>` 

# 5 HTML中的注释和特殊字符
## 5.1 注释
如果需要在HTML文档中添加一些便于阅读和理解但又不需要在页面中的注释文字，就需要使用注释标签。 
HTML中的注释以"<!--"开头，以"-->"结束。
```html
<!-- 注释语句 -->
```
一句话：注释标签中的内容是给程序员看的，这个代码是不执行不显示到页面的。
## 5.2 特殊字符
在HTML中，一些特殊的符号很难或者不方便直接使用，此时我们就可以使用下面的字符来替代。
| 特殊字符 | 描述   | 字符的代码 |
|----------|--------|------------|
|          | 空格   | `&nbsp;`   |
| <        | 小于号 | `&lt;`     |
| >        | 大于号 | `&gt;`     |
| &        | 和号   | `&amp;`    |
| ￥       | 人民币 | `&yen;`    |
# 6 表格标签
## 6.1 表格的主要作用
表格主要是用于显示,展示文字，因为它可以让数据显示的十分规整，可读性十分好。特别是后台展示数据的时候，能够熟练运行表格就显得很重要。一个清爽简约的表格能够把数据表现得十分有条理。
## 6.2 表格的基本语法
```html
<table>
 <tr>
	<td>单元格内的文字</td>
	...
 </tr>
...
</table>
```
1. `<table></table>` 是用来定义表格的标签
2. `<tr></tr>` 标签用来定义表格的行，必须嵌套在`<table></table>` 标签中。
3. `<td></td>` 标签用来定义表格的单元格，必须嵌套在`<tr></tr>` 标签中。
4. 字母td是指表格数据(table data),即数据单元格的内容。
 
**例如** 
```html
<body>
    <table>
        <tr><td>姓名</td> <td>性别</td> <td>年龄</td></tr>
        <tr><td>刘德华</td> <td>男</td> <td>56</td></tr>
        <tr><td>张学友</td> <td>男</td> <td>58</td></tr>
        <tr><td>郭富城</td> <td>男</td> <td>51</td></tr>
        <tr><td>黎明</td> <td>男</td> <td>57</td></tr>
    </table>
</body>
```
## 6.3 表头单元格标签`<th></th>` 
一般表头单元格位于表格的第一行，表头单元格里面的文本内容**加粗居中**显示。 
`<th>` 标签表示HTML中表格的表头部分(table head的缩写)
```html
<body>
    <table>
        <tr><th>姓名</th> <th>性别</th> <th>年龄</th></tr>
        <tr><td>刘德华</td> <td>男</td> <td>56</td></tr>
        <tr><td>张学友</td> <td>男</td> <td>58</td></tr>
        <tr><td>郭富城</td> <td>男</td> <td>51</td></tr>
        <tr><td>黎明</td> <td>男</td> <td>57</td></tr>
    </table>
</body>
```
## 6.4 表格属性(了解)
	表格标签这部分属性我们在实际开发中并不常见，后面通过CSS来设置。
| 属性名      | 属性值            | 描述                                          |
|-------------|-------------------|-----------------------------------------------|
| align       | left center right | 规定表格相对周围元素的对齐方式                |
| border      | 1 ""              | 规定表格是否拥有边框，默认为"",表示为没有边框 |
| cellpadding | 像素值            | 规定单元边沿与其内容之间的空白，默认为1像素   |
| cellspacing | 像素值            | 规定单元格之间的空白，默认为2像素             |
| width       | 像素值或百分比    | 规定表格的宽度。                              |
