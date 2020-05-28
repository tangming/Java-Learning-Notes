---
title: Java基本语言特性-字符串
date: 
updated:
tags: [Java, 字符串]
categories: Java
comments: true
---
字符串操作是编程中最常见的行为。在Java中，字符串不是基本数据类型而是对象，其主要是通过`String`，`StringBuilder`和`StringBuffer`三个类来完成的。三者的继承体系如下：

![](/resources/images/java-string-inheritance-system.png)
<!-- more -->
********************************************************************************
## 1. String
`String`类声明在`java.lang`包中，是最长用的字符串处理类，其实现源码为：
```
public final class String extends Object
    implements java.io.Serializable, Comparable<String>, CharSequence
{
    /** the value is use for character storage. */
    private final char value[];
    /** the offset is the first index of the storage that is used */
    private final int offset;
    ...

}
```
从源码我们可以看出：
- String类是final类，不能被继承，其成员方法也都默认是final方法；
- 实现了`Serializable`接口，可被序列化；
- String类是通过char数组来保存字符串的。

### 1.1 String对象的初始化
代码中我们常见的初始化String的用法有如下几种：
```
String str1; // 只是声明了一个String类型的引用变量，并未做初始化
String str2 = null; // 声明一个String类型的引用变量，并初始化为空
String str3 = "abc"; // 字面量初始化
String str4 = new String("abc"); // 构造函数初始化
```
在上述代码中，`str3`和`str4`都创建了一个内容为`"abc"`的字符串，但是其原理上存在很大差异：
- **字面量初始化**：所谓的字面量，就是通过`""`创建的字符串。JVM首先会在栈中创建一个引用变量`str3`，然后查看字符串常量池中是否存在`"abc"`。如果没有，就将字符串`"abc"`放进常量池，并让`str3`指向它；如果已经有`"abc"`，就直接让`str3`指向它。
- **构造函数初始化**：这是java中标准的创建对象的方式，每次调用都会在堆上创建一个新的对象。

### 1.2 String类的常用API
```
/** 字符串长度 **/
public int length();

/** 字符串拼接 **/
public String concat(String str);

/** 字符串截取 **/
public String subString(int beginIndex);
public String subString(int beginIndex, int endIndex);

/** 字符串查找 **/
public char charAt(int index); // 返回指定索引位置的字符

public int indexOf(String str); // 检索str在字符串中第一次出现的位置，未出现返回-1
public int indexOf(String str, int fromIndex); // 从fromIndex位置开始检索str在字符串中第一次出现的位置，未出现返回-1
public int lastIndexOf(String str); // 检索str在字符串中最后一次出现的位置，未出现返回-1
public int lastIndexOf(String str, int fromIndex); 

public boolean startsWith(String prefix); // 检测字符串是否以指定前缀开始
public boolean startsWith(String prefix, int toOffset); // 检测字符串从指定位置开始是否以指定前缀开始
public boolean endsWith(String suffix); // 检测字符串是否以指定后缀开始

/** 字符串替换 **/
public String replace(char oldChar, char newChar); // 用newChar替换字符串中所有oldChar字符，并返回一个新字符串
public String replaceFirst(String regex, String replacement); // 用replacement替换字符串中遇到的第一个和regex匹配的子串
public String replaceAll(String regex, String replacement);

/** 字符串比较 **/
public int compareTo(String anotherStr); // 对字符串中的内容按字典顺序比较大小，当前字符串比参数大返回正数，小则返回负数，相等返回0
public int compareToIgnoreCase(String anotherStr); // 同compareTo，但是忽略字符大小情况

public boolean equals(String anotherStr); // 比较当前字符串和参数字符串，相等返回true，不相等返回false
public boolean equalsIgnoreCase(String anotherStr); // 同equals，但是忽略字符大小情况

/** 字符串与基本类型转换 **/
public static T parseT(String s); // 字符串转基本类型，T可以是byte, short, int, long, float, double
public static String valueOf(T value); // 基本类型转字符串，T可以是char[], char, boolean, int, long, float, double

/** 字符串大小写转换 **/
public String toLowerCase(String str);
public String toUpperCase(String str);

/** 其他操作 **/
public String trim(); // 去除字符串两端空格
public String[] split(String str); // 将str作为分隔符进行字符串分解，如'\\s+'代表空格
public boolean contains(String str); // 判断参数str是否包含在字符串中
```

### 1.3 String对象的不可变性
前面提到，String对象是不可变的，它的值在创建后就不能被修改，对String的任何操作都不会影响原对象，所有看起来进行了字符串的修改都是通过重新创建字符串完成的。将String设计成不可变的原因如下：
- **字符串常量池的需要**：字符串常量池可以将一些字符常量放在常量池中重复使用，避免频繁创建和回收对象、节省内存空间。字符串如果可变，当字符串被修改，就会使另一个字符串变量指向错误的值。
- **线程安全考虑**：字符串不可变，则其本身就是线程安全的，可以被多线程共享。
- **支持hash映射和缓存**：字符串不可变性保证了其hash值的不变性，在需要hashcode时不需要重新计算，很适合作为Map中的键。
- **保证类加载的安全性**：字符串常作为网络连接、数据库连接的参数，不可变保证了连接的安全性。

### 1.4 字符串常量池
字符串常量池是Java的常量池之一，用来存放字符串。前面提到通过字面量初始化的字符串会放入字符串常量池中，更准确的说法是编译期能够确定的字符串存储到常量池，通过构造函数创建的字符串在运行期确定，放在堆上。
```
final String str = "Hello"; // 常量池
String str1 = "Hello"; // 常量池
String str2 = "World"; // 常量池
String str3 = "Hello" + "World"; // 常量池
String str4 = "Hello" + str2; // 堆
String str5 = str1 + str2; // 堆
String str6 = str + str2; // 常量池
```
将字符串放入常量池的方法除了通过**使用字面量初始化**外，还可以通过String类的实例方法`intern()`。执行`intern()`方法时，若常量池中存在对应的字符串，有就返回引用；没有则会在常量池中添加一个对此字符串实例的引用，并返回。

********************************************************************************
## 2. StringBuffer和StringBuilder
String对象是不可变的，因此每次在对String类型进行修改的时候都创建了一个新的String对象，然后将指针指向新的String对象。这样不仅效率低，而且浪费了大量的内存空间。对于需要经常性修改字符串的操作，需要使用`StringBuffer`和`StringBuilder`这两个类。和String类不同的是，这两个类的对象能够被多次修改，并且不产生新的未使用的对象。

### 2.1 StringBuffer的原理
StringBuffer是可变类，它的每一对象都有一定的缓冲区容量，当字符串的大小没有超过缓冲区容量时，不会分配新的内存，超过时会自动增加容量。  
// TODO：实现的函数

### 2.1 StringBuffer和StringBuilder支持的API
StringBuffer支持的主要操作是`append`和`insert`方法，`append`方法将新的字符添加到缓冲区的末端，`insert`方法将字符添加到指定位置。
```
public StringBuffer append(String s); // 在字符串结尾拼接
public StringBuffer insert(int index, String str); // 在指定位置插入数据

public StringBuffer delete(int start,int end); // 删除指定范围的字符
public StringBuffer deleteCharAt(int index); // 删除指定位置的字符

public StringBuffer reverse(); // 将字符序列进行反转

```
### 2.2 StringBuffer和StringBuilder的异同
- StringBuffer和StringBuilder都继承自同一个抽象父类`AbstractStringBuilder`；
- StringBuffer对方法加了同步锁或者对调用的方法加了同步锁，所以是线程安全的；StringBuilder是线程不安全的；
- StringBuilder比StringBuffer的速度要快。

********************************************************************************
## 3. Java String的常见问题
- 字符串的比较，是使用`==`还是`equals()`？
  > 简单来说，`==`判断的是两个引用变量中的值是否相等，也就是这两个引用是否指向同一个内存地址；`equals()`则判断的是字符串的值是否相等。除非确实要判断两个String引用是否是同一个对象，否则总该用`equals()`方法。
- 对于敏感信息，为什么使用`char[]`比使用`String`好？
  > String是不可变对象，而char[]是可以被修改的。因此，只要在使用完成后对char[]进行修改，敏感信息不容易在其他地方暴露。
- switch语句能否支持String作为case条件？
  > 从Java7开始，switch支持String类型；在Java6及以前的版本不支持。另外，在Java8中支持的类型包括byte，char，short，int，String，Enum。
- 如何通过空白字符拆分字符串？
  > String的`split(String str)`方法可以将str作为分隔符对字符串进行拆分，返回一个`String[]`。`“\s”`代表空白字符、`“\t”`代表制表符、换行`“\n”`以及回车`“\r”`，编译器对源码解析时需要进行转码，所以传入的字符串需要`“\\s”`。
- `subString()`方法内部是如何工作的？
  > 在JDK6中，共用原来的char[]数组，然后通过偏移和长度构建了一个新的String；JDK7中，则是创建了一个新的char[]。
- 如何将String转化为日期？
  > ```
  > SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd);
  > String str = "2020-05-24";
  > Date date = format.parse(str);
  > ```


## 参考文章 & 资源链接
- [Java不可变类和String不可变特性](https://cloud.tencent.com/developer/article/1378004)
- [Java基础：字符串常量池与intern](https://juejin.im/post/5c160420518825235a05301e)