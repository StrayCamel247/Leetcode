## heapArena 
https://draveness.me/golang/docs/part3-runtime/ch07-memory/golang-memory-allocator/#%e7%a8%80%e7%96%8f%e5%86%85%e5%ad%98

稀疏内存中 的每个 heapArena
```
type heapArena struct {
	bitmap       [heapArenaBitmapBytes]byte
	spans        [pagesPerArena]*mspan
	pageInUse    [pagesPerArena / 8]uint8
	pageMarks    [pagesPerArena / 8]uint8
	pageSpecials [pagesPerArena / 8]uint8
	checkmarks   *checkmarksMap
	zeroedBase   uintptr
}
```
不同平台和架构的二维数组大小可能完全不同，如果我们的 Go 语言服务在 Linux 的 x86-64 架构上运行，二维数组的一维大小会是 1，而二维大小是 4,194,304，因为每一个指针占用 8 字节的内存空间，所以元信息的总大小为 32MB。由于每个 runtime.heapArena 都会管理 64MB 的内存，整个堆区最多可以管理 256TB 的内存，这比之前的 512GB 多好几个数量级。

问题1 信息元不是heapArena吗。为何说信息元总大小为32mb，而heapArena管理64mb呢

问题2 整个堆区最多可以管理 256TB，这个数字哪里来的呀？

## 跨度类
https://draveness.me/golang/docs/part3-runtime/ch07-memory/golang-memory-allocator/#%e8%b7%a8%e5%ba%a6%e7%b1%bb

在跨度类5中

5	48	8192	170	32	31.52%

上表展示了对象大小从 8B 到 32KB，总共 67 种跨度类的大小、存储的对象数以及浪费的内存空间，以表中的第四个跨度类为例，跨度类为 5 的 runtime.mspan 中对象的大小上限为 48 字节、管理 1 个页、最多可以存储 170 个对象。因为内存需要按照页进行管理，所以在尾部会浪费 32 字节的内存，当页中存储的对象都是 33 字节时，最多会浪费 31.52% 的资源：

((48−33)∗170+32)/8192=0.31518

问题 这个33字节是哪来的？