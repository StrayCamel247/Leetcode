package main

import (
	"encoding/ascii85"
	"testing"
)

func Test_ascii85(t *testing.T) {
	src := "hello world"
	srcbyte := []byte(src)
	var dst []byte = make([]byte, ascii85.MaxEncodedLen(len(srcbyte)))
	ascii85.Encode(dst, []byte(src))
	t.Log(string(dst))
	// output:
	// BOu!rD]j7BEbo7d
}
