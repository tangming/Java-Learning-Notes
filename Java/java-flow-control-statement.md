---
title: Java基本语言特性-流程控制语句
date: 
updated:
tags: [Java, 流程控制]
categories: Java
comments: true
---
流程控制语句包括顺序结构、分支结构和循环结构，Java中流程控制的关键字有`if-else`、`while-do-while`、`for`、`switch-case`、`break`、`continue`、`return`等等。
<!-- more -->

********************************************************************************
## 1.for-each和index-for
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

********************************************************************************
## 2.switch-case语句
### 2.1 switch中支持的数据类型
switch支持的数据类型有六中：byte、char、short、int、String、Enum。其实，真正支持的数据类型只有int，byte、char、short可以自动转换成int类型，enum可以表示为int，string的hashcode也是一个整型的数。
### 2.2 switch中的default和break
- default对应的是缺省情况，没有符合条件的情况下才执行，所以应该将default语句放到最后；
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