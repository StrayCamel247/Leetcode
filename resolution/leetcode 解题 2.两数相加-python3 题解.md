- 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
- 如果，我们将这两个数相liang加起来，则会返回一个新的链表来表示它们的和。
- 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

## 仿leetcode官方类ListNode定义
**解决调试代码报错：** 
```
name 'ListNode' is not defined//ListNode' object has no attribute 'val'.
```
> 原因：估计leetcode上面平台调试代码的时候启用了自己的一些库文件。 在本地ied调试的时候要加上ListNode的类定义（模仿官方的功能写的）。



类的代码添加：
```
class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"

```
不过就算我们定义了这个类，在本地调试的过程中，我们传参的形式还是list。但是在leetcode提交代码并不是，而是应该官方通过接口将我们传入的[1,2,3]list形式参数转化成了ListNode了。
所以我们还要在本地测试之前添加判断参数形式的代码

```
if isinstance(l1,list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)
```


我们来看看vscode调试打印的效果：
```
if __name__ == "__main__":
    test = Solution()
    print(test.addTwoNumbers([1,3],[2,1,3]))
```
调试结果：（和官方定义得那个输出是一样的）
```
 f:/Leetcode/2.两数相加.py
ListNode {val: 3, next: ListNode {val: 4, next: ListNode {val: 3, next: None}}}
```
[源码储存在github上，欢迎来提bug哦！-点击访问](https://github.com/Freen247/leetcode)
如果觉得不错请给我一个star谢谢了Stray_Camel(＾Ｕ＾)ノ~ＹＯ