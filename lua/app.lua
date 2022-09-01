#!/usr/bin/env lua

--single line comment

--[[
    multi line comment
    write anything here
--]]

--[=[
]][[]]][]]
--]=]



--[[ printing something ]]--
print("hello world!")
print([[
    i am printing
    multiple lines
]])
io.write("another way to print\n")
print(string.format("sum of 1 and 2 is %d",1+2))




--[[data types]]
print(type("Hello world")) --> string
print(type(10.4*3))        --> number
print(type({}))            --> table
print(type(print))         --> function
print(type(true))          --> boolean
print(type(nil))           --> nil

-- converting string to number
print(tonumber("10"))
print("10" + 2) --> 12
-- converting number to string
print(tostring(17))
print(10 .. "5") --> 105


--[[ variables ]]--
--[[ The following words are reserved
we cannot use them as identifiers:
    and       break  end    in      if  do
    while     false  local  return  repeat
    for       nil    then   else    elseif
    function  until  not    or      true
--]]

-- declaring variables

a = 1
b = a*2

a = 1 b = a*2

local text = "example text"  -- local variable
TEXT = "another text"  -- global variable

_ = nil -- dummy variable

local word = "lorem"
local num = 21  -- number
local bool = true
local nothing = nil



-- printing variables
print(text, TEXT)
print(_VERSION)  -- predefined variable

-- deleting variable
text = nil
TEXT = nil


--[[ tables ]]--

-- creating table
array = {
    "example",
    10,
    text,
    ['key'] = 'value'
}

print(array[1])     --> "example"
print(array[2])     --> 10
print(array['key']) --> "value"
print(array.key)    --> value

-- adding item
array['user'] = "user_name"
array.new_item = true

-- removing item
-- accessing item




--[[ functions ]]--

-- creating
function add(n1, n2)
	print(n1+n2)
end
function factorial(n)
    if n == 0 then
        return 1
    else
        return n * factorial(n-1)
    end
end

-- calling functions
add(5, 7)
print(factorial(4))



--[[ loops ]]--
