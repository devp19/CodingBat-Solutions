def string_splosion(str):
  full = ""
  for i in range(len(str) + 1):
    full += str[0:i]

  return full
