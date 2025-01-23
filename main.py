# 1. Adım: file31.txt dosyasını oluştur ve metni yaz
with open("file31.txt", "w") as file:
    file.write("Phytons simple easy to learn syntax emphasizes readability and therefore reduces the cost of program maintanance.")

# 2. Adım: file31.txt dosyasını oku ve içindeki boşlukları alt çizgiyle değiştir
with open("file31.txt", "r") as file:
    content = file.read()

content_with_underscores = content.replace(" ", "_")

# 3. Adım: Sonucu file31_spaces_to_undercores.txt dosyasına kaydet
with open("file31_spaces_to_undercores.txt", "w") as file:
    file.write(content_with_underscores)

