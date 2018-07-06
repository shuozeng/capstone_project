import json

with open('sensorswww_data.txt', 'r') as f:
	data_strings = f.read()

data_strings = ''.join(data_strings.split())

data = []
start = curr = 0
num_braces = 0
while curr < len(data_strings):
	if data_strings[curr] == '{':
		num_braces += 1
	elif data_strings[curr] == '}':
		num_braces -= 1
	
	if num_braces == 0:
		s = data_strings[start:curr + 1]
		p_obj = json.loads(s)
		data.append(p_obj)
		start = curr + 1
	
	curr += 1

with open('new_data.json', 'w') as f:
	json.dump(data, f, sort_keys=True, indent=4)


