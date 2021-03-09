package main

/*
	SOME ENGLISH WORLDS
	The tour is interactive
	/ˌin(t)ərˈaktiv/
	形容词: 互动
	These example programs demonstrate different aspects of Go
	这些示例程序演示了Go的不同方面

	be meant to be starting points for your own experimentation
	旨在作为您自己实验的起点

	determining the significance of this date is an exercise for the reader
	确定此日期的重要性是读者的一项练习

	By convention
	按照惯例
	The environment in which these programs are executed is deterministic
	/dəˌtərməˈnistik/
	确定性的

	This code groups the imports into a parenthesized
	将……加上括弧（parenthesize的过去式和过去分词）
*/
import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

// HelloWorld is a func of test.
func HelloWorld() {
	fmt.Println("Hello, World!")

}

// TimePrint is a time print test.
func TimePrint() {
	fmt.Println("Welcome to the playground!")
	fmt.Println("The time is", time.Now())
	t, err := time.Parse(time.UnixDate, "Wed Feb 25 11:06:39 PST 2015")
	// Always check errors enven if they should not happen.
	if err != nil {
		panic(err)
	}
	do := func(name, layout, want string) {
		got := t.Format(layout)
		if want != got {
			fmt.Printf("error: for %q got %q; expected %q\n", layout, got, want)
			return
		}
		fmt.Println(got)
		fmt.Printf("%-16s %q gives %q\n", name, layout, got)
	}
	fmt.Println(t, err)
	fmt.Println("Unix format:", t.Format(time.UnixDate))        // Unix format: Wed Feb 25 11:06:39 PST 2015
	fmt.Println("Same, in UTC:", t.UTC().Format(time.UnixDate)) // Same, in UTC: Wed Feb 25 11:06:39 UTC 2015
	fmt.Printf("\nFormats:\n\n")
	do("Basic short date", "2006/01/02", "2015/02/25")
	do("Basic full date", "Mon Jan 2 15:04:05 MST 2006", "Wed Feb 25 11:06:39 PST 2015")
	do("No fraction", time.UnixDate, "Wed Feb 25 11:06:39 PST 2015")
	tt := time.Now()
	text := []byte("Time: ")

	text = tt.AppendFormat(text, time.RFC822)
	fmt.Println(string(text))

}

// RandPrint is a test.
func RandPrint() {
	fmt.Printf("\nFormats:\n\n")
	// var balance = [5]float32{1000.0, 2.0, 3.4, 7.0, 50.0}
	for i := 0; i < 4; i++ {
		fmt.Println(rand.Intn(100))
	}
	// for _, v := range balance {
	// 	fmt.Println(rand.Intn(100))
	// 	fmt.Println(v)

	// }
	/*
		seed的值相同若rand.Intn(xx)若Intn传参一样则会导致返回的随机值一样
	*/
	rand.Seed(1)
	println(rand.Intn(10))
	rand.Seed(2)
	println(rand.Intn(10))
	rand.Seed(1)
	println(rand.Intn(10))
	for i := 0; i < 4; i++ {
		rand.Seed(1)
		println(1)
		fmt.Println(rand.Intn(100))
	}

}
func add(x int, y int) int {
	return x + y

}
func addShortDeclare(x, y int, msg string) (int, string) {
	return x + y, msg

}
func split(sum int) (x, y int) {
	var a int
	a = sum * 4 / 9
	y = sum - 4
	return a, y

}

var globalC, globalPython, globalJava bool
var globalA int
var globalAS string
var globalB, globalD int = 1, 2

func main() {
	/*
		在C语言中局部变量没有初始化存储的是垃圾数据, 在Go语言中局部变量没有初始化, 会默认初始化为0
		在C语言中全局变量没有初始化存储的是0, Go语言和C语言一样
		在Go语言中, 如果定义了一个局部变量, 但是没有使用这个局部变量, 编译会报错
		在Go语言中, 如果定义了一个全局变量, 但是没有使用这个全局变量, 编译不会报错

		作者：箩篼
		链接：https://www.jianshu.com/p/78f10bdbac73
		来源：简书
		著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
	*/
	var c, python, java = true, false, "no!"
	fmt.Println(globalB, globalD, c, python, java)
	var i int
	println(i, globalC, globalPython, globalJava, globalA, globalAS)
	println(split(10))
	TimePrint()
	HelloWorld()
	RandPrint()
	println(math.Sqrt(7))
	println(add(1, 2))
	println(addShortDeclare(1, 2, "test"))

	/*
		go 的声明语法
		https://blog.golang.org/declaration-syntax
		words
		Although it's a separate point
		虽然这是一个单独的点

		illustrative language
		说明性语言

		in the interests of brevity
		为了简洁起见

		One merit of this left-to-right style
		这种从左到右的风格的优点

		because that postfix * would conflate with multiplication
		n. [语] 后缀, 词尾
		vt. 加字尾于
	*/
	sum := func(a, b int) int { return a + b }(3, 4)
	println(sum)
	// one must parenthesize the type if it starts with a *:
	// (*int)(nil)

}
