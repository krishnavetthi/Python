Given_string = "OQYWFClFhFGAvIWYwGKpmZhnJiyzTslSIhSwvOsqJMEphzmifTkyqOMNpnOtXZxmCfgDYqbaBHAUvIWhMnvwZnEMVDvmEfLrDoQnAZgQEgXQVnmSYkfedpAdhrtpOgORpYLRZYGWdhWYuqQssCUXtTzKRDAhpjUheOzUroZNzWFtZOVwIapzUYtbSbjYNErzQ"
print(len(Given_string))

print(Given_string.count('a'))

print(Given_string.startswith('if'))

print(Given_string[63:89])

# Print 46th character
print(Given_string[45])

word = ['1','2','3','4']
word[ : ] = [ ] 
print(word)

L = ['one','two','three', 'four', 'five', 'six']
print(sorted(L))
print (L)

input_str = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
# string_1 = input_str[0] + ' & ' + input_str[1]#Type your answer here
string_1 = ' & '.join(input_str)
print(string_1)

list_1 = [1,2]
list_2 = [3,4]
#Type your answer here
list_1.extend(list_2)
print(list_1)

my_list = ['geeks', 'for', 'geeks']
another_list = [6, 0, 4, 1]
my_list.append(another_list)
print(my_list)

# List of order ID’s which are processed 
processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]

# List of order ID’s which are returned
returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]

print(len(processed_orders)+len(returned_orders))

total_orders = processed_orders+returned_orders
total_orders.sort()
print(total_orders[49])

print(1099 in processed_orders)
print(total_orders[128])

print(total_orders[0:5])

# employee data with key as id of the employee and values as age of the employee
Employee_data ={101: 43, 102: 25, 103: 43, 104: 31, 105: 26, 106: 28, 107: 29, 108: 43, 109: 25, 110: 22, 111: 22, 112: 25, 113: 30, 115: 45, 116: 23, 117: 29, 118: 28, 119: 30, 120: 28, 121: 42, 122: 39, 123: 29, 124: 42, 125: 43, 126: 42, 127: 40, 128: 27, 129: 23, 130: 30, 131: 37, 132: 20, 133: 36, 134: 27, 135: 27, 136: 22, 137: 28, 138: 23, 139: 45, 140: 39, 141: 29, 142: 33, 143: 39, 145: 34, 146: 26, 147: 30, 148: 38, 149: 29, 150: 24, 151: 28, 152: 34, 153: 42, 154: 29, 155: 23, 156: 31, 158: 25, 160: 45, 161: 42, 162: 27, 163: 24, 164: 20, 166: 24, 167: 28, 168: 20, 169: 33, 170: 34, 171: 37, 172: 45, 173: 35, 174: 23, 175: 44, 176: 27, 177: 30, 178: 26, 179: 27} 
val = sorted(Employee_data.values())
print(val[-1])
# or
print(max(Employee_data.values()))

print(len(Employee_data.keys()))

mean = (sum(Employee_data.values()))/(len(Employee_data.keys()))
print(mean)

Employee_data.update({104: 27, 140:27,164:27})
del Employee_data[143]

mean = (sum(Employee_data.values()))/(len(Employee_data.keys()))
print(mean)