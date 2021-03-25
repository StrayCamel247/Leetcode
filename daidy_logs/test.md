olang 查看各个协程使用的线程id

代码
```
package main

import (
	"fmt"
	"golang.org/x/sys/windows"
	"sync"
	"time"
)

func phase(n int, wg *sync.WaitGroup) {
	_subId := windows.GetCurrentThreadId()
	println(fmt.Sprintf("协程%d使用的%+v", n, _subId))
	println(fmt.Sprintf("in phase %d, waiteing %d s", n, 5*n))
	time.Sleep(time.Duration(5*n) * time.Second)
	println(fmt.Sprintf("phase %d result", n))
	wg.Done()
}
func main() {
	_mainId := windows.GetCurrentThreadId()
	println(fmt.Sprintf("主线程的%+v", _mainId))
	_num := 3
	a := time.Now()
	var wg = sync.WaitGroup{}
	wg.Add(_num)
	for i := 0; i < _num; i++ {
		go phase(i, &wg)
	}
	time.Sleep(10 * time.Second)
	fmt.Println("mexiting main")
	b := time.Now()
	println(fmt.Sprintf("cost %+v", b.Sub(a)))
}

```

输出
```
主线程的25396
协程2使用的25396
in phase 2, waiteing 10 s
协程1使用的23664
in phase 1, waiteing 5 s
协程0使用的13632
in phase 0, waiteing 0 s
phase 0 result
phase 1 result
phase 2 result
mexiting main
cost 10.0000759s
```
