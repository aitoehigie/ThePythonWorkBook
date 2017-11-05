#!/usr/bin/env

widgets = int(input("Enter the number of widgets:"))
gizmos = int(input("Enter the number of gizmos:"))

weight_of_widget = 75
weight_of_gizmos = 112

total_weight_of_widgets = widgets * weight_of_widget
total_weight_of_gizmos = gizmos * weight_of_gizmos

total_weight_of_order = total_weight_of_widgets + total_weight_of_gizmos

print(f"""
Total weight of order: {total_weight_of_order}
""")
