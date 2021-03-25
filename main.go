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
