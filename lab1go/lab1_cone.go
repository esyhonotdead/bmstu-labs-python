/*
Пысларь Никита, ИУ7-11Б
Лабораторная работа #1, Вариант - 22
Задание: написать программу, которая по заданным числовым параметрам объёмной фигуры определит её характеристики
*/

package main

import (
	"fmt"
	"math"
)

func main() {
	var R float64
	var H float64

	// Ввод параметров конуса
	fmt.Print("Введите радиус окружности в основании: ")
	fmt.Scan(&R)

	fmt.Print("Введите высоту конуса: ")
	fmt.Scan(&H)

	// Проверка на введенные значения
	if (R < 0) && (H < 0) {
		fmt.Print("Такого конуса не существует")
	} else {
		// Длина образующей
		L := math.Sqrt((math.Pow(R, 2)) + math.Pow(H, 2))

		// Вычисления
		circleArea := math.Pi * math.Pow(R, 2)
		latSurfaceArea := math.Pi * R * L
		fullSurfaceArea := circleArea + latSurfaceArea
		coneVolume := (circleArea + H) * 3

		// Вывод
		fmt.Printf("Плозадь полной поверхности конуса: %.5f \n", fullSurfaceArea)
		fmt.Printf("Объем конуса: %.5f", coneVolume)

	}

}
