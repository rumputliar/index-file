import os

def index_files(directory, output_file):
    """
    Mengindeks file dalam directory dan subdirectory serta menyimpan hasilnya ke dalam file output.

    :param directory: Path directory yang akan diindeks
    :param output_file: Path file txt tempat hasil indeks akan disimpan
    """
    index_data = []  # Menyimpan data indeks

    for root, dirs, files in os.walk(directory):
        # Mendapatkan relative path untuk menyimpan hanya bagian yang kita inginkan
        rel_path = os.path.relpath(root, directory)
        for file in files:
            if rel_path != '.':
                # Memisahkan berdasarkan subdirectory jika ada
                index_data.append(f"{rel_path}/{file}")
            else:
                index_data.append(file)

    # Menyimpan hasil indeks ke file output
    with open(output_file, 'w') as f:
        for line in index_data:
            f.write(f"{line}\n")

if __name__ == "__main__":
    # Menggunakan directory tempat kode dijalankan
    main_directory = os.getcwd()  # Mendapatkan path directory saat ini
    output_file_name = "file_index.txt"  # Nama file output
    index_files(main_directory, output_file_name)
    print(f"Indeks file telah disimpan di {output_file_name} di directory {main_directory}")