---
title: Java基本语言特性-流程控制语句
date: 
updated:
tags: [Java, 流程控制]
categories: Java
comments: true
---
流程控制语句包括顺序结构、分支结构和循环结构。Java中流程控制的语句大致可分为三大类：
- 选择语句
  + if, else if, else
  + switch...case 
- 循环语句
  + while
  + do...while
  + for
  + foreach
- 跳转语句
  + return
  + break
  + continue
<!-- more -->

********************************************************************************
## 1.循环语句
### while循环
只要布尔表达式为true，循环体就会一直执行下去。
```
while(布尔表达式) {
    // 循环体
}
```
### do...while循环
对与while循环语句而言，如果不满足条件则不能进入循环。`do...while`循环至少会执行一次。
```
do {
    // 循环体
}while(布尔表达式);
```
### for-each和index-for
Java中for循环有两种模式：
```
// foreach
for (type var:listVar) {
    ...
}
// index-for
for (exp1;exp2;exp3) {
    ...
}
```
- for-each语法上更加简洁，但是也缺失了索引信息；
- for-each速度较快，只是对元素进行遍历优先用for-each。

**NOTE:**
> 不要在循环遍历容器的时候删除容器中的元素，正确做法是通过迭代器对元素进行修改。

********************************************************************************
## 2.选择语句
对于`if...else`语句来说，当括号中的条件表达式成立，则执行`if`语句中的代码块，否则执行`else`中的代码块。`switch`语句判断一个变量与一系列值中的某一个值是否相等，每一个值称为一个分支。
`switch`语句有如下的规则：
- switch语句中的变量类型只能是byte、char、short、int、String、Enum。其实，真正支持的数据类型只有int，byte、char、short可以自动转换成int类型，enum可以表示为int，string的hashcode也是一个整型的数。
- switch语句中可以有多个case语句，每个case后面跟一个比较变量和冒号。
- case语句中值的类型必须与变量的数据类型相同，且只能是**常量**或**字面常量**。
- switch语句可以包含一个default语句，对应是缺省情况，在没有符合条件的情况下才执行。default语句必须是switch语句的最后一个分支。
- case匹配之后会顺序执行后面的代码，无论后面的case是否匹配，知道遇到break。

********************************************************************************
## 3.跳转语句
跳转语句可以帮助程序员更加准确地控制整个流程，Java提供了与其他语言相通的跳转控制语句，包括`return`、`break`和`continue`。
- return语句用于终止程序的运行或方法退出，并把控制权返回给方法的调用者；
- break语句用在循环语句或条件语句中，用于终止一个循环或判断条件分支，让程序进入下一个流程；
- continue语句表示退出当前循环，适用于循环语句。

### labeled break/continue
除了普通的`break`和`continue`外，Java还支持带标签的`break`和`continue`，用来跳出一些嵌套很深的循环，其作用类似与`goto`。labeled break/continue通用的格式如下：
```
//-----------------------------------------
break label; // 结束带label标签的整个循环
continue label; // 跳过带label标签的当前循环
//-----------------------------------------
public static void main(String[] args) {
    label:
    for(int i=0;i<3;i++) {
        for(int j=3;j>0;j--) {
            if(y==x) {
                continue label; // 输出0,3 0,2 0,1 1,3 1,2 2,3
                //break label; // 输出0,3 0,2 0,1 1,3
            }
            System.out.println(x+","+y);
        }
    }
}
```