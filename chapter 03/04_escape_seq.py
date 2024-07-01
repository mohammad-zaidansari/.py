a = "Zaid is a good boy \n but not a bad boy"

print(a)

b = "this is \"good\" boy"
print(b)

c = "this is \\bad\\ boy"
print(c)

text = "Hello\rWorld"
print(text)
# Output: World

text = "Hello\bWorld"
print(text)
# Output: HellWorld

text = "Hello\fWorld"
print(text)
# Output: Hello
#        World

text = "Unicode: \u03A9"  # Greek capital letter Omega (Ω)
print(text)
# Output: Unicode: Ω

text = r"This is a raw string: \n \t \\"
print(text)
# Output: This is a raw string: \n \t \\
