# AT_CODE_BEGINNER_SELECTION

本章介绍Atcoder Context *的解题思路。
***
※AtCoder是一家日本的代码竞技平台，目前支持日文和英文。


AtCoder Context ABC 156 D - Bouquet(花束)

本文章为原创文章，未经过允许不得转载
**运行要求**  
**运行时间限制:** 2sec  
**内存限制:** 1024MB  
[原题链接](https://atcoder.jp/contests/abc156/tasks/abc156_d)

**题目**
小明手上有n种花，每一种花都有一束。
从这些花种选择一束以上的花做花束。
但是，小明讨厌a和b两个数字。花束数量和a或b这两个数字相同的花束不能制作。
求小明能够制作多少花束。
结果取和10^9+7相除取mod的结果
在这里，如果有两个花束。花束A,花束B。花束A里用到的花在花束B里不存在的花，花束A和花束B算作不同的花束。

**输入前提条件**
* 所有的输入均为整数
* 2 <=n <= 10^9
* 1 <=a <= b <= min(n,2*10^5)

**输入**  
输入按照以下形式标准输入
```
n a b
```

**输出**
输出小明可以制作的花束的种类。结果取(10^9+7)的mod。

* * *
例1  
**输入**
```
4 1 3
```

**输出**
```
7
```
小明讨厌数字1，3。在这种情况下，小明可以制作2朵花，或者4朵花的花束
在4朵花中选择2多花的选择方法有6种
在4朵花中选择4朵花的选择方法有1种
总共加起来有6+1=7种


例2
**输入**
```
1000000000 141421 173205
```

**输出**
```
34076506
```

**读懂题目**

**解题思路**

**代码**

**总结**


※　另外，我会在我的微信个人订阅号上推出一些文章，欢迎关注
![二维码.jpg](/img/bVbDtut)    
***