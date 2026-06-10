<?php
$conn = new mysqli("localhost", "root", "Ganjarpantek123", "perpustakaan");

// Create
$conn->query("INSERT INTO buku (judul, pengarang, penerbit, stok) VALUES ('Struktur Data', 'Sanjaya', 'Informatika', 3)");

// Read
$result = $conn->query("SELECT * FROM buku");
while($row = $result->fetch_assoc()) { 
    print_r($row); 
    echo "<br>";
}

// Update
$conn->query("UPDATE buku SET stok = 5 WHERE id_buku = 2");

// Delete
// $conn->query("DELETE FROM buku WHERE id_buku = 2"); // Diberi komentar agar datanya bisa terlihat saat di-refresh
?>