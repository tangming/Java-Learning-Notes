---
title: Spring Boot实战-入门
date: 
updated:
tags: [Spring Boot, 学习路线]
categories: 编程语言
comments: true
---
Spring框架已经成文Java后端开发事实上的行业标准，如何用好Spring成为Java程序员的必修课之一。随着Spring Boot和Spring Cloud的出现，可以更好的帮助工程师基于Spring框架及各种基础设施来快速搭建系统。
<!-- more -->
## 认识Spring Boot
![Spring Boot知识框架](/resources/images/redis_RedisClient.png)
Spring Boot在Spring的基础上引入了很多机制，其中最重要的是以下四个：
- **自动配置**：针对Spring应用程序常见的应用功能，Spring Boot能够自动提供相关配置。
- **起步依赖**：告诉Spring Boot需要什么功能，它就能引入需要的库。
- **命令行界面**：这是Spring Booot的可选特性。
- **Actuator**：

## 初始化Spring Boot项目
如果我们要开始构建一个Spring Boot项目，创建项目文件并在其中加入各种依赖，我们需要用到Spring Initializr。Spring Initializr本质上来说是一个Web应用程序，它能够帮我们生成一个基本的Spring Boot项目结构。Spring Initializr有如下几种用法：
- 通过[Web界面](https://start.spring.io)使用。
- 通过IntelliJ IDEA使用。
- 通过Spring Boot CLI使用。
- 通过Spring Tool Suit使用。

### 使用Spring Initializr的Web界面
使用Spring Initializr最直接的办法就是用浏览器打开[https://start.spring.io](https://start.spring.io)，就能够看到项目表单，
![Spring Initializr配置表单](/resources/images/redis_RedisClient.png)

Spring Initializr生成的项目会以ZIP文件的形式保存下来，解压后的项目结构如图所示：
![Spring Initializr创建的项目结构](/resources/images/redis_RedisClient.png)
项目中包含的东西包括：
- `Application.java`：一个带有`main()`方法的类，用于引导启动应用程序。
- `ApplicationTest.java`：一个空的JUnit测试类，它加载了一个使用Spring Boot自动配置功能的Spring应用程序上下文。
- application.properties：配置文件，根据需要添加配置属性，也可以设置为yaml格式。
- pom.xml：

## 参考文章 & 资源链接
- [Java程序员的Spring学习指南](https://wwww.infoq.cn/article/Ad-8ghcGGCNU572U6oEX)