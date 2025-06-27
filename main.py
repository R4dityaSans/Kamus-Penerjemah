meme_dict = {
    "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
    "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
    "ROFL": "Tanggapan terhadap lelucon",
    "SHEESH": "Sedikit ketidaksetujuan",
    "CREEPY": "Menakutkan, tidak menyenangkan",
    "AGGRO": "Untuk menjadi agresif/marah",
    "POV": "Point of View – digunakan untuk menunjukkan sudut pandang seseorang",
    "GOAT": "Greatest Of All Time – yang terbaik sepanjang masa",
    "YEET": "Melempar sesuatu dengan kuat (atau ekspresi semangat)",
    "NOOB": "Pemula atau orang yang belum berpengalaman",
    "SUS": "Curiga, mencurigakan (dari kata 'suspicious')",
    "BASED": "Mengatakan sesuatu yang jujur dan tidak peduli pendapat orang lain",
    "SLAY": "Melakukan sesuatu dengan sangat baik atau tampil sangat keren",
    "LIT": "Sangat seru, keren, atau menyenangkan",
    "BOP": "Lagu yang sangat enak untuk didengar",
    "WOKE": "Sadar akan isu sosial atau keadilan",
    "RIZZ": "Kemampuan untuk menggoda atau memikat seseorang",
    "NPC": "Orang yang terlihat seperti 'karakter latar' dan tidak punya pendapat sendiri",
    "DEAD": "Ekspresi saat sesuatu sangat lucu sampai 'mati ketawa'",
    "GYATT": "Ekspresi kekaguman terhadap penampilan fisik seseorang, sering dipakai bercanda",
}

print("Halo! Selamat datang ke dalam dictionary tentang kata - kata meme!")
time.sleep(1)
print("Anda dapat mencari 5 kata meme dari dictionary ini.")
time.sleep(1)

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!):\n")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Kata ini tidak ditemukan")
