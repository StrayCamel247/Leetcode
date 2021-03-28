package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func handler(a *TreeNode) {
	// fmt.Print(a)
	queue := []*TreeNode{a}
	fmt.Printf("%+v", queue[0])
}
func main() {
	test := TreeNode{}
	handler(&test)
}
