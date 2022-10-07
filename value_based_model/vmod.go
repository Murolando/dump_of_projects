package main

import "fmt"

func main(){
	labirint := [][]float32{
		{0.0,0.0,0.0,1.0},
		{0.0,-500.0,0.0,-1.0},
		{0.0,0.0,0.0,0.0},
	}
	for i := 0; i<5;i++{
		labirint = oneMove(labirint)
		fmt.Println(labirint[0])
		fmt.Println(labirint[1])
		fmt.Println(labirint[2])
		fmt.Println()
	}
}
func oneMove(oldLab [][]float32)[][]float32{
	var newLab [][]float32
	newLab = copy(oldLab,newLab)
	// fmt.Println(oldLab,newLab)
	for i,line := range oldLab{
		for j,elems := range line{
			// fmt.Println(i,j,oldLab[i][j])
			if elems == -500{
				continue
			}
			if (i == 0) && (j == 3){
				continue
			}
			if (i == 1) && (j == 3){
				continue
			}
			newLab[i][j] = vValue(oldLab,i,j)
		}
		// fmt.Println()
	}
	return newLab
}
func vValue(lab [][]float32 , y int,x int )float32{
	// left right up down
	var gamma  float32 = 0.5
	moves := [4]float32{-100,-100,-100,-100}
	
	if (x > 0){
		moves[0] = gamma*lab[y][x-1]
	}
	if(x < 3){
		moves[1] = gamma*lab[y][x+1]
	}
	if(y > 0){
		moves[2] = gamma*lab[y-1][x]
	}
	if(y < 2){
		moves[3] = gamma*lab[y+1][x]
	}
	// `fmt.Println(moves)
	return max(moves)
}

func max(a [4]float32)float32{
	var maxx float32 = -500
	for _,i := range a{
		if i>maxx{
			maxx=i
		}
	}
	return maxx
}

func copy(oldLab [][]float32,newLab [][]float32)[][]float32{
	newLab = [][]float32{
		{0.0,0.0,0.0,1.0},
		{0.0,-500.0,0.0,-1.0},
		{0.0,0.0,0.0,0.0},
	}
	for i, line := range oldLab{
		for j, elem := range line {
			newLab[i][j] = elem
		}
	}
	return newLab
}