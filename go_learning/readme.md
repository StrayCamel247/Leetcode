## golang学习
> 记录golang学习的点滴

### 字符串操作

#### 中文字符在unicode下占2个字节，在utf-8编码下占3个字节
[https://blog.csdn.net/yaomingyang/article/details/79374209]
英文字母和中文汉字在不同字符集编码下的字节数
字节数 : 1;编码：GB2312

字节数 : 1;编码：GBK

字节数 : 1;编码：GB18030

字节数 : 1;编码：ISO-8859-1

字节数 : 1;编码：UTF-8

字节数 : 4;编码：UTF-16

字节数 : 2;编码：UTF-16BE

字节数 : 2;编码：UTF-16LE

> 参考文献：[http://codman.cc/2017/01/golang_encoding/#fn:alecrab-ansi]
网上搜索unicode、utf-8等关键词，都会出现以如下文字描述开头：
很久以前，有一群人，他们决定用8个可以开合的晶体管来组合成不同的状态，以表示世界上的万物。他们看到8个开关状态是好的，于是他们把这称为“字节”。再后来，他们又做了一些可以处理这些字节的机器，机器开动了，可以用字节来组合出很多状态，状态开始变来变去。他们看到这样是好的，于是它们就这机器称为”计算机“。
> [https://www.eet-china.com/mp/a6621.html],[https://blog.csdn.net/whocarea/article/details/87783614], [https://blog.csdn.net/qq_25867649/article/details/75386417?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=1328602.11601.16149291142371347&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control]
**what?**
那么unicode 是什么？

> [wiki搜索](https://zh.wikipedia.org/wiki/Unicode)

记得大学的时候另一种通过数字显示字符的编码格式：ASCII（American Standard Code for Information Interchange，美国信息交换标准代码）
> [wiki搜索](https://zh.wikipedia.org/wiki/Ascii)

ascii第一版地出现在1963，的出现为推动了字节编码集发展打下了根基

其实ANSI并不是某一种特定的字符编码，而是在不同的系统中，ANSI表示不同的编码。你的美国同事Bob的系统中ANSI编码其实是ASCII编码（ASCII编码不能表示汉字，所以汉字为乱码），而你的系统中（“汉字”正常显示）ANSI编码其实是GBK编码，而韩文系统中（“한국어”正常显示）ANSI编码其实是EUC-KR编码。

而unicode地出现从1991年才开始出现第一版

unicode的发展过程中还演变出了一系列的字符集：ISO 8859字符集、GB2312字符集、BIG5字符集、GB18030字符集等等

字符集只是字符的集合，不一定适合作网络传送、处理，有时须经编码(encode)后才能应用。如Unicode可依不同需要以UTF-8、UTF-16、UTF-32等方式编码。字符编码就是以二进制的数字来对应字符集的字符。因此，对字符进行编码，是信息交流的技术基础。

关于window系统的asci编码格式
[https://www.cnblogs.com/malecrab/p/5300486.html]
其实这种编码格式只存在windows系统中，随着系统的变化而变化，上述链接中有例子


utf-8