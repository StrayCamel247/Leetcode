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
*/
import (
	"fmt"
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
func main() {
	TimePrint()
	HelloWorld()
	RandPrint()

}
