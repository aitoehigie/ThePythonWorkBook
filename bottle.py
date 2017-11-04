#!/usr/bin/env python

small_containers: int = int(input("How many <1 litre containers:"))
large_containers: int = int(input("How many >1 litre containers:"))

small_container_deposit = 0.10
large_container_deposit = 0.25

refund = round((small_containers * small_container_deposit) + (large_containers * large_container_deposit), 2)

print(f"Your container deposit refund is ${refund}")


