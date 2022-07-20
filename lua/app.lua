--single line comment
--[[
multi line comment
write anything here
--]]




--[[ printing something ]]--

print("hello world!")
print([[i am printing
multiple lines]])
io.write("another way to print\n")
print(string.format("sum of 1 and 2 is %d",1+2))




--[[ variables ]]--

-- declaring variables
text = "example text"
local text2 = "another text"
num = 21
bool = true
nothing = nil

-- printing variables
print(text, text2)


--[[ tables ]]--

-- simple table
table = {"example", 10, text}

print(table[1])  --> "example"
print(table[2])  --> 10

-- table with key-value pair
pair = {
   ['text'] = "hello",
   ['num'] = 10,
}

print(pair.text)  --> hello
print(pair.num)   --> 10

-- adding item
pair.new_item = true
-- removing item
-- accessing item




--[[ functions ]]--

-- creating
function add(n1, n2)
	print(n1+n2)
end

-- calling functions
add(5, 7)



--[[ loops ]]--

-- for loop
for key, value in ipairs(pair) do
	print(key, value)
end

print("#########")

function cmpfile(name, src)
	tab = {}

	for n = 1, #src do
		tab[n] = { name = src[n] }
	end
end

cmpfile("hulu", {"julu","polo", "milo"})
