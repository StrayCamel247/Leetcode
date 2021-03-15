package main

import "fmt"

func main() {
	a := []int{1, 2}
	println(&a)
	fmt.Printf("%+v", a)
	change(a)
	println(&a)
	fmt.Printf("%+v", a)
}
func change(x []int) {
	x[0] = 22
}

/*
PS F:\workspace\Leetcode> go run .\main.go
[1 2][22 2]
*/
