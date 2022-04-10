--single line comment
--[[
multi line comment
write anything here
--]]--




---- printing something

print("hello world!")
print([[i am printing
multiple lines]])
io.write("another way to print\n")
print(string.format("sum of 1 and 2 is %d",1+2))




---- variables

-- declaring variables
text = "example"
local text2 = "another text"
num = 21
bool = true

-- printing variables
print(text, text2)


---- tables
table = {"example", 10, text} -- creating table
-- adding item
-- removing item
-- accessing item


---- dictionary

-- creating dictionary
dict = {
	['text'] = "hello",
	['num'] = 10,
	['var'] = table,
}
-- adding item
-- removing item
-- accessing item




---- functions

-- creating
function add(n1, n2)
	print()
end

-- calling functions
add(5, 7)

print(add)
