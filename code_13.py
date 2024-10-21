arquivo = open("palavras.txt", "w")

arquivo.write("banana")
arquivo.write("melancia")

arquivo.close()

arquivo = open("palavras.txt", "a")

arquivo.write("morango\n")
arquivo.write("manga\n")

arquivo.close()