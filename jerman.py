# kamus_streamlit.py

import streamlit as st

st.set_page_config(page_title="Kamus Jerman - Indonesia", layout="centered")

# Kamus data
kamus_jerman = {
    "hallo": "halo",
    "tschüss": "selamat tinggal",
    "bitte": "tolong / silakan",
    "danke": "terima kasih",
    "ja": "ya",
    "nein": "tidak",
    "freund": "teman (laki-laki)",
    "freundin": "teman (perempuan)",
    "mann": "pria / suami",
    "frau": "wanita / istri",
    "kind": "anak",
    "schule": "sekolah",
    "universität": "universitas",
    "lehrer": "guru (laki-laki)",
    "lehrerin": "guru (perempuan)",
    "student": "mahasiswa",
    "buch": "buku",
    "heft": "buku tulis",
    "stift": "pulpen/pensil",
    "tisch": "meja",
    "stuhl": "kursi",
    "haus": "rumah",
    "wohnung": "apartemen",
    "fenster": "jendela",
    "tür": "pintu",
    "auto": "mobil",
    "fahrrad": "sepeda",
    "zug": "kereta",
    "flugzeug": "pesawat",
    "schiff": "kapal",
    "bahn": "rel/kereta api",
    "stadt": "kota",
    "dorf": "desa",
    "land": "negara",
    "berg": "gunung",
    "fluss": "sungai",
    "see": "danau",
    "meer": "laut",
    "himmel": "langit",
    "sonne": "matahari",
    "mond": "bulan",
    "stern": "bintang",
    "baum": "pohon",
    "blume": "bunga",
    "gras": "rumput",
    "hund": "anjing",
    "katze": "kucing",
    "vogel": "burung",
    "fisch": "ikan",
    "brot": "roti",
    "wasser": "air",
    "milch": "susu",
    "kaffee": "kopi",
    "tee": "teh",
    "zucker": "gula",
    "salz": "garam",
    "fleisch": "daging",
    "reis": "nasi",
    "apfel": "apel",
    "banane": "pisang",
    "orange": "jeruk",
    "tomate": "tomat",
    "kartoffel": "kentang",
    "zwiebel": "bawang",
    "tag": "hari",
    "nacht": "malam",
    "morgen": "pagi",
    "abend": "sore/malam",
    "woche": "minggu (pekan)",
    "monat": "bulan (kalender)",
    "jahr": "tahun",
    "zeit": "waktu",
    "uhr": "jam",
    "minute": "menit",
    "sekunde": "detik",
    "kopf": "kepala",
    "auge": "mata",
    "ohr": "telinga",
    "nase": "hidung",
    "mund": "mulut",
    "hand": "tangan",
    "finger": "jari",
    "bein": "kaki",
    "herz": "jantung / hati",
    "gesundheit": "kesehatan",
    "krank": "sakit",
    "arbeit": "pekerjaan",
    "beruf": "profesi",
    "geld": "uang",
    "markt": "pasar",
    "laden": "toko",
    "computer": "komputer",
    "telefon": "telepon",
    "internet": "internet",
    "musik": "musik",
    "film": "film",
    "spiel": "permainan",
    "sport": "olahraga",
    "liebe": "cinta",
    "familie": "keluarga",
    "freundschaft": "persahabatan"
}

# UI Streamlit
st.title("📘 Kamus Bahasa Jerman - Indonesia")
st.subheader("Cari arti kata dari Bahasa Jerman ke Bahasa Indonesia")

kata = st.text_input("Masukkan kata dalam Bahasa Jerman:", "")

if kata:
    kata = kata.lower().strip()
    arti = kamus_jerman.get(kata)
    if arti:
        st.success(f"**Arti '{kata}'**: {arti}")
    else:
        st.error(f"Kata '{kata}' tidak ditemukan dalam kamus.")

st.markdown("---")
with st.expander("📚 Lihat semua kata dalam kamus"):
    st.write(", ".join(sorted(kamus_jerman.keys())))
