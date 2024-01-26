# 2/13/23 Glossary:

glossary = {
				'else' : 'conditional function' ,
				'elif' : 'works as else_if condition' ,
				'del' : 'used to delete something from the code' ,
				'.title()' : 'used to capitalize a word' ,
				'.get()' : 'used to add a value into a key' ,
				}
"""
print(f"Else: {glossary['else'].title()}.")
print(f"\nElif: {glossary['elif'].title()}.")
print(f"\nDel: {glossary['del'].title()}.")
print(f"\n.title(): {glossary['.title()'].title()}.")
print(f"\n.get(): {glossary['.get()'].title()}.")
"""

# 2/15/23 looping into the dict. to avoid multiple print() calls:

for terms, definition in glossary.items():
	print(f"{terms.title()}:\n\t-->{definition.title()}.\n")