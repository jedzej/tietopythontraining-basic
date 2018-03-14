#!/usr/bin/env python3

cupcakeCostUsd = int(input())
cupcakeCostCents = int(input())
numberOfCupcakes = int(input())

totalCostInCents = (cupcakeCostUsd * 100 + cupcakeCostCents) * numberOfCupcakes
print(str(totalCostInCents // 100) + " " + str(totalCostInCents % 100))
