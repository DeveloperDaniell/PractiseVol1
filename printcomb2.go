package piscine

import "github.com/01-edu/z01"

func PrintComb2() {

	for i := '0'; i <= '9'; i++ {
		for j := '0'; j <= '9'; j++ {
			for x := '0'; x <= '9'; x++ {
				for z := '0'; z <= '9'; z++ {
					if i < x || j < z && i == x {
						z01.PrintRune(i)
						z01.PrintRune(j)
						z01.PrintRune(' ')
						z01.PrintRune(x)
						z01.PrintRune(z)
						if i == '9' && j == '8' && x == '9' && z == '9' {
							z01.PrintRune('\n')
						} else {
							z01.PrintRune(',')
							z01.PrintRune(' ')
						}
					}
				}
			}
		}
	}
}
