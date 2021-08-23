# HTML语法规范
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
# HTML基本结构标签
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
# 网页开发工具
## 3.1文档类型声明标签
`<!DOCTYPE>` 文档类型说明，作用是告诉浏览器使用哪种HTML版本来显示网页
```html
<!DOCTYPE html>
```
这句代码的意思是:当前页面采取的是HTML5版本显示网页

**注意** 
1. `<!DOCTYPE>`声明位于文档中的最前面的位置，处于`<html>`标签之前。
2. `<!DOCTYPE>`不是一个HTML标签，它就是文档类型声明标签。 
## 3.2lang语言种类
用来定义当前文档显示的语言。
1. en定义语言为英语
2. zh-CN定义语言为中文
简单来说，定义为en就是英文网页，定义为zh-CN就是中文网页
## 3.3字符集
字符集是多个字符的集合，以便计算机能够识别和存储各种文字。
在`<head>`标签内，可以通过`<metal>`标签的charset属性来规定HTML文档应该使用哪种字符编码
```html
<meta charset="UTF-8" />
```
charset常用的值有：GB2312,BIG5,GBK和UTF-8

# HTML常用标签
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
## 4.4文本格式化标签
在网页中，有时需要为文字设置粗体,斜体和下划线效果，这是就需要用到HTML的文本格式化标签，使文字以特殊的方式显示。

| 语义   | 标签                          | 说明                                     |
|--------|-------------------------------|------------------------------------------|
| 加粗   | `<strong></strong>` `<b></b>` | 更推荐使用`<strong>` 标签加粗 语义更强烈 |
| 倾斜   | `<em></em>`  `<i></i>`        | 更推荐使用`<em>` 标签加粗 语义更强烈     |
| 删除线 | `<del></del>`  `<s></s>`      | 更推荐使用`<del>` 标签加粗 语义更强烈    |
| 下划线 | `<ins></ins>`  `<u></u>`      | 更推荐使用`<ins>` 标签加粗 语义更强烈    |
## `<div>`和 `<span>` 标签
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
## 4.5图像标签和路径(重点)
### 1图像标签
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