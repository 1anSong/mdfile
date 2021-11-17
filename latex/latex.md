### command
| usage                        | explaination               | example              |
|------------------------------|----------------------------|----------------------|
| kpsewhich {package-name}.sty | check package if installed | kpsewhich mhchem.sty |

### 强调字体
- `\emph` 表示强调
```
\emph{需要强调的字体}
```
### 把公式的斜体变成正体
```
${\rm a+b}+c$
```
其中a+b为正体，+c为斜体
### 插入化学公式
```
引入宏包mhchem \usepackage{mhchem}
\ce{H2O}
```
