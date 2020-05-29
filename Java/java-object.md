---
title: Java基本语言特性-Object详解
date: 
updated:
tags: [接口]
categories: Java
comments: true
---
在Java中，默认所有的类都直接或间接的继承了`java.lang.Object`类。由于所有类都继承了Object类，所以省略了`extends Object`关键字。Object是所有类的父类，这就意味着所有的类都继承了Object类中的public方法。
<!-- more -->
Object类中主要有以下方法：
```
public final native Class<?> getClass();
public native int hashCode();
public boolean equals(Object obj);
protected native Object clone() throws CloneNotSupportedException;
public String toString();
public final native void notify();
public final native void notifyAll();
public final native void wait(long timeout) throws InterruptedException;
public final void wait(long timeout, int nanos) throws InterruptedException;
public final void wait() throws InterruptedException;
protected void finalize() throws Throwable;
```

