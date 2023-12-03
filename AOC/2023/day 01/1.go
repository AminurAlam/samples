package main

import (
	"fmt"
	"os"
)

func main() {
    var nums = [2]int{1, 2}
    fmt.Println(nums)

	text, err := os.ReadFile("input")

	if err != nil {
        print("error!")
	}
    fmt.Println(string(text))
}
