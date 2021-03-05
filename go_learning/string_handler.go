// -*- coding: utf-8 -*-
//  __author__ : stray_camel
// __description__ :
// __REFERENCES__: golang中的字符串操作
// __date__: 2021-03-05
package main

import (
	"strings"
	"unicode/utf8"
)

// 字符串-定义，golang中-字符串string（默认使⽤utf-8编码，且必须使⽤双引号包裹）
func main() {
	// 字符串的声明
	var str string
	str1 := "hello world"
	var str2 = "hello 世界"
	// 中文字符在unicode下占2个字节，在utf-8编码下占3个字节
	println(len(str2))         //12
	println(len([]rune(str2))) // 8
	// unicode和utf-8编码格式的不同
	// why?中文字符在unicode下占2个字节，在utf-8编码下占3个字节
	// what? unicode 是什么
	// https://zh.wikipedia.org/wiki/Unicode
	println(len(str))
	println(len(str1))
	println("222", utf8.RuneCountInString(str2))
	println("test")
	println(strings.ContainsRune("中文", 20013))
	println("test")
}
