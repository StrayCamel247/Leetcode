package main

import (
	"reflect"
)

type decorator func()

func (this decorator) invoke() {
	println("before")
	this()
	println("after")
}

func myFunc(s string) {
	println(s)
}

func call(func_name interface{}, params ...interface{}) func() {
	f := func() {
		var fc = reflect.ValueOf(func_name)
		in := make([]reflect.Value, len(params))
		for k, param := range params {
			in[k] = reflect.ValueOf(param)
		}
		fc.Call(in)
	}
	return f
}

func main() {
	f := call(myFunc, "hh")
	x := decorator(f)
	x.invoke()
}
