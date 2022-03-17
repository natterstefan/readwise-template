from setup import env

def loadTemplate(template, dt):
    return env.get_template(template).render(dt)

# https://www.adamsmith.haus/python/answers/how-to-remove-empty-lines-from-a-string-in-python
def removeEmptyLines(s):
    return '\n'.join([line for line in s.split('\n') if line.strip()])

def outputToFileAndConsole(outputPath, template, data):
  content = removeEmptyLines(loadTemplate(template, data))

  with open(outputPath, "w") as file:
    file.write(content)
    file.close()

  print(content)
  print('\n')