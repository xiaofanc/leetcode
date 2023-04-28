"""
execute command:
"cd /": return to the root
"cd .": keep in the same dir
"cd ..": return back to the previous dirs
"cd users": go to the folder users under the current dirs
"""

def execute_command(commands):
	stack = []
	for c in commands:
		if c == "cd /":
			stack = []
		elif c == "cd ..":
			if stack:
				stack.pop()
		elif c == "cd .":
			continue
		else:
			folder = c.split(" ")[1]
			stack.append(folder)
	return "/"+"/".join(stack) if stack else "/"

commands = ["cd ..", "cd .", "cd trash", "cd ..", "cd ."]
print(execute_command(commands)) # "/"

commands = ["cd folder1", "cd .", "cd trash", "cd ..", "cd ."]
print(execute_command(commands)) # "/"


