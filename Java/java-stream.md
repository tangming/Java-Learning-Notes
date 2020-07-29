---
title: Java语言特性-Stream
date:
tags: [数据结构]
categories: Java
---
流式编程是Java8的新增特性之一，主要用来提升对集合进行操作的的效率。区别于IO流的概念，Stream是一个数据渠道，用于操作数据源(如数组、集合等)的元素序列。
<!-- more -->
## 流
**什么是流**  
所谓的流，就是把对数据的操作拼接成一个pipeline(管道)，让数据像水流通过管道一样依次完成相应的计算。流可以看作对集合的一次升级，
**集合专注于数据本身，流专注于对数据的计算**。Stream API提供了一种高效且易于使用的数据处理方式，能够让我们对集合进行非常复杂的
查找、过滤和映射等操作。
```Java
 /* 
 * 获取所有年龄大于18的学生
 */

 // 传统方法
 List<Student> result = new ArrayList<>();
 for (Student student:studentList) {
     if (student.getAge() > 18) {
         result.add(student);
     }
 }

 // Stream方法
 result = studentList.stream().filter(s->s.getAge()>18).collect(Collectors.toList());

```
**流的特征**  
流是对数据进行计算的操作链，具有以下特征：
- Stream不会存储元素，因为其本身是一系列操作；
- Stream会返回一个新的结果对象，不会改变源对象；
- Stream是延迟执行的，类似于ITK，只有当有需求时才会执行。

******

## 流的使用
使用Stream操作有三个步骤：
- **创建Stream**：从一个数据源中获取一个流
- **中间操作**：一个或多个中间操作，对数据源进行处理
- **终止操作**：执行中间操作链，并产生结果

### 流的创建
**集合创建流**  
Java8中的Collection接口中提供了两个获取流的default方法，也就是说所有实现Collection接口的实现类可以不用实现这两个方法就可以使用。
- `default Stream stream()`：返回一个顺序流；
- `default Stream parallelStream()`：返回一个并行流。

**数组创建流**  
Java8中Arrays提供了一个静态方法`static Stream stream(T[] array)`可以获取数组流。例如：
```Java
Integer[] nums = new Integer[8];
Stream<Integer> stream = Arrays.stream(nums);
```

**Stream的静态方法创建流**  
Stream类创建流主要有两种类型：
- 通过`publid static Stream of(T... values)`传入参数值创建一个流，它可以接收任意数量的参数。
```Java
Stream<Integer> stream = Stream.of(1,2,3,4,5);
```
- 可以通过给`Stream.iterate()`和`Stream.generate()`中传入函数创建无限流。
```Java
/*
*@param seed 表示一个起始值
*@param f UnaryOperator类型的实例，是一个函数式接口
*/
public static Stream iterate(final T seed, final UnaryOperator f)

/*
*@param s Supplier类型的参数
*/
public static Stream generate(Supplier s)
```
具体使用例子：
```Java
// 从1开始打印该参数加2的值
public void test1() {
    Stream.iterate(1, (x)->x+2)).forEach(System.out::println);
}

// 生成并打印一个随机数
public void test2() {
    Stream.generate(()->Math.random().forEach(System.out::println));
}
```
**Note：**
> 使用无限流一定要使用`limit()`进行截断，否则流会无限制的创建下去。上述代码会一直运行输出。

### 流的中间操作
在流创建完成后，我们就可以进行中间操作。多个中间操作可以连接起来形成一个pipeline。中间操作可以分为**四类**：筛选、截取、映射以及排序。

**筛选操作**  
筛选操作主要有两个方法：`filter()`和`distinct()`。
- `Stream <T> filter(Predicate<? super T> predicate)`：接收一个和Predicate函数对应Lambda表达式，返回一个布尔值，从流中过滤某些元素。
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(2,3,4,5,6,7,8);
    list.stream().filter(e->e>5).forEach(System.out::println); // 输出大于5的元素
}
```
- `Stream <T> distinct()`：去掉流中的重复元素。根据流所生成的元素的`hashCode()`和`equals()`去除重复元素。
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(2,3,4,4,5,6,6);
    list.stream().distinct().forEach(System.out::println); // 输出2,3,4,5,6
}
```

**截取操作**  
截取操作也有两个方法：`limit()`和`skip()`。
- `Stream <T> limit(long maxSize)`：截断流，使其元素不超过给定数量（去尾）。
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(2,3,4,5,6,7,8);
    list.stream().limit(4).forEach(System.out::println); // 输出2,3,4,5
}
```
- `Stream <T> skip(long n)`：跳过元素，返回一个去掉前n个元素的流（掐头）。
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(2,3,4,5,6,7,8);
    list.stream().skip(4).forEach(System.out::println); // 输出6,7,8
}
```
`limit()`和`skip()`两个函数结合使用可以有效实现对集合中数据的截取。

**映射操作**  
映射操作的主要方法有两个：`map()`和`flatMap()`。
- `Stream <R> map(Function<? super T, ? super R> mapper)`：接收一个Function作为参数，该函数会被应用到每个元素上，并将其映射成一个新的元素，也就是转换操作。
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(2,3,4);
    list.stream().map(x->x*x).forEach(System.out::println); // 计算元素的平方，输出4,9,16
}
```
- `Stream <R> flatMap(Function<? super T, ? extends Stream<? extends R>> mapper)`：接收一个Function函数作为参数，将流中的每一个值都转换成另一个流，然后把所有流连接成一个流。
例如：
```Java
public class TestStreamAPI {
    public void test() {
        List<String> list = Arrays.asList("abc","def","xyz");
        list.stream().flatMap(TestStreamAPI::string2Stream).forEach(System.out::println); // a,b,c,d,e,f,x,y,z
    }

    public static Stream<Character> string2Stream(String string) {
        List<Character> list = new ArrayList<>();
        char[] charArray = str.toCharArray();
        for (char c:charArray) {
        list.add(c);
        }
        return list.stream();
    }
}
```
除此之外，还有其他映射函数，如`mapToDouble(ToDoubleFunction f)`，`mapToInt(ToIntFunction f)`，`mapToLong(ToLongFunction f)`等。

**排序操作**  
排序操作接口只有一个，即`sorted()`
- `Stream <T> sorted(Comparator<? super T> comparator)`：指定比较规则进行排序。
例如：
```Java
public void test1() {
    List<Integer> list = Arrays.asList("d","c","a");
    list.stream().sorted() // 默认排序
        .forEach(System.out::println); // 输出a,c,d
}

public void test2() {
    List<Integer> list = Arrays.asList("d","c","a");
    list.stream().sorted((x,y)->x.compareTo(y)) // 指定降序排序
        .forEach(System.out::println); // 输出d,c,a
}
```

### 终止操作
终止操作会从流的中间操作pipeline生成结果，其结果可以是任何不是流的值，如`List`、`Integer`，甚至是`void`。终止操作有**三类**：查找与匹配、归纳以及收集。

**收集操作**  
- `<R,A> R collect(Collector<? super T, A, R> collector)`：收集、将流转换为其他形式，比如List、Set、Map等。
例如：
```Java
public void test() {
    List<Integer> source = Arrays.asList(2,3,4);
    
    // 将流中元素收集到List中
    List<Integer> list = source.stream().collect(Collectors.toList());
    // 将流中的元素收集到Set中
    Set<Integer> set = source.stream().collect(Collectors.toSet()); // 有重复元素会自动过滤
}
```

**归纳操作**  
归纳操作主要是将流中的各个元素结合起来，它需要提供一个起始值，然后按照一定规则进行运算，它接收一个二元操作的函数式接口。有以下三个重载：
```Java
T reduce(T identity, BinaryOperator<T> accumulator); // identity为提供的起始值，返回一个确定值
Optional<T> reduce(BinaryOperator<T> accumulator); // 没有提供起始值，返回Optional防止流中没有足够的元素
<U> U reduce(U identify, BiFunction<U,? super T,U> accumulator, BinaryOperator<U> combiner);
```
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(10，5,3,4);
    Integer result = list.stream().reduce(2,Integer::sum); // 输出：2+10+5+3+4=24
    Optional<Integer> optional = list.stream().reduce(Integer::sum);
    Integer result = optional.get(); // 输出22=10+5+3+4
}
```

**查找与匹配操作**
查找与匹配的方法有：
- `boolean allMatch(Predicate p)`：检查是否匹配所有元素
- `boolean anyMatch(Predicate p)`：检查是否匹配至少一个元素
- `boolean noneMatch(Predicate p)`：检查是否没有匹配元素
- `Optional<T> findFirst()`：返回第一个元素
- `Optional<T> findEnd()`：返回当前流中的任意元素
- `long count()`：返回流中元素的总数
- `Optional<T> max(Comparator c)`：返回流中最大值
- `Optional<T> min(Comparator c)`：返回流中最小值
- `void forEach(Consumer c)`：内部迭代
例如：
```Java
public void test() {
    List<Integer> list = Arrays.asList(10，5,3,4);
    boolean allMatch = list.stream().allMatch(x->x>2); // 是否所有元素都大于2

    Optional<Integer> first = list.stream().findFirst();
    Integer val = first.get();

    Integer maxVal = list.stream().max(Integer::compareTo).get();
}
```
**Note：**
> 从某种意义上来说，`min,max,sum,average`都是特殊的`reduce`。


## 参考文章&资源链接
- [详解Java8特性之Stream API](https://juejin.im/entry/5b595bfc5188257bcc167251)
- [Java 8 Streams API 详解](https://juejin.im/post/5dccc589f265da79245c81b3#heading-6)
- [Java8 流式编程Stream](https://juejin.im/post/5d37bbd451882551c37fbc04)
