import re

lexems = {"Var": "20", "Begin": "30", "End": "40", ";": "4", ",": "5", "+": "6", "-": "6", "*": "7", "/": "8", "(": "9",
        ")": "10", ":": "11", "=": "12", ".":"13", "~": "14"}

lexem = ""
letter = False
digit = False
nline = 1

input = open("input.txt", "r", encoding="utf8")
file_out = open("result_lexem.txt", "w", encoding="utf8")
while char := input.read(1):
      if re.match(r"[a-zA-Z]", char):
        lexem += char
        letter = True
      elif re.match(r"[0-9]", char):
        lexem += char
        digit = True
      else:
        if letter and not digit:
          if lexem in lexems:
            file_out.write(f"{lexem} {lexems[lexem]} {nline}\n")
          else:
            file_out.write(f"{lexem} ident {nline}\n")
        elif not letter and digit:
          file_out.write(f"{lexem} digit {nline}\n")
        else:
          if lexem:
            file_out.write(f"{lexem} digit {nline}\n")

        lexem = ""
        letter = digit = False

        if char == "\n":
          nline += 1
          continue
        if char != " ":
          if char in lexems:
            file_out.write(f"{char} {lexems[char]} {nline}\n")
          else:
            file_out.write(f"{char} 0 {nline}\n")


input.close()
file_out.close()