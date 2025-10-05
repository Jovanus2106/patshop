1. Apa perbedaan antara synchronous request dan asynchronous request?

Synchronous request adalah jenis request yang dimana browser akan menunggu server merespons sepenuhnya sebelum melakukan aksi lain. Contohnyaa ketika user melakuka submit pada form HTML biasa, maka seluruh halaman akan reload terlebih dahulu dan user tidak bisa melakukan interaksi lain sampai response dari server diterima. Sebaliknya ketika asynchronous request memungkinkan browser menjadi lebih responsif meskipun sambil menunggu response dari server. Jadi di asynchronous request nantinya user tetap bisa berinteraksi dengan halaman lain tanpa terganggu. 


2. Bagaimana AJAX bekerja di Django (alur request–response)?

AJAX bekerja dengan cara mengirim request ke server secara asynchronous menggunakan JavaScript, biasanya melalui fetch atau XMLHttpRequest. Ketika user melakukan aksi, misalnya menekan tombol submit pada form, JavaScript akan mengambil data form dan mengirimkannya ke server Django tanpa melakukan reload halaman. Server kemudian menerima request tersebut melalui view, memproses data (seperti validasi form, autentikasi, atau penyimpanan ke database), dan mengembalikan response dalam format JSON. JavaScript di sisi frontend akan menangkap response ini, dan berdasarkan hasilnya bisa menampilkan pesan sukses, error atau melakukan redirect. Cara ini membuat seluruh proses menjadi lebih cepat dan interaktif karena hanya data yang dipertukarkan. 

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?

Penggunaan AJAX memiliki banyak keuntungan yaitu  Pertama, halaman tidak perlu reload sehingga data yang sudah diisi oleh user tidak hilang dan proses menjadi lebih cepat. Kedua, jika ada halaman yang diperbarui maka hanya bagian tertentu saja yang diperbarui, misalnya form atau tabel produk sehingga dapat meningkatkan efisiensi dan juga menghemat bandwith. 
Ketiga, AJAX membuat pengalaman pengguna menjadi lebih interaktif dan responsif, misalnya saat melakukan penambahan produk, filter produk, atau mengedit produk tersebut. Keempat, AJAX memudahkan integrasi dengan teknologi frontend modern, seperti React, Vue, atau Tailwind, sehingga desain dan logika interaksi bisa lebih fleksibel.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?

Ada beberapa hal untuk memastikan keamanan pada fitur Login dan Register di Django. Pertama adalah penggunaan CSRF token yang wajib disertakan dalam setiap POST request agar Django dapat memverifikasi request tersebut valid dan juga berasal dari situs sendiri. Keduanya, validasi data juga harus dilakukan di sisi sever meskipun sudah divalidasi front end. Django nanti akan tetap meriksa username dan password valid melalui authenticationForm atau usercreation form. Ketiga, pastikan data terkirim melalui metode POST, bukan query string dan gunakan HTTPS agar data terutama password ,terenkripsi selama transmisi. Keempat, mengimplementasikan perlindungan terhadap bruteforce attack agar akun tidak mudah dibobol

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?

Penggunaan Ajax ini sangat membantu pengguna karena dengan menggunakan ajax, maka halaman akan tetap responsif dan interaktif sehingga user tidak perlu menunggu reload halaman setiap kali melakukan aksi (menambahkan produt, mengedit produk , atau mensubmit form). Selain itu pesan sukses atau error akan langsung muncul di halaman (menggunakan toast.html) dan juga tidak akan menganggu proses lainnya. Interaksi juga terasa lebih mulus , fitur seperti realtime, pencarian instan dan update produk juga menjadi lebih cepat dan nyaman. Sehingga dengan beberapa perubahan ini membuat website menjadi lebih modern dan efisien untuk user . 


-----------------------------------------------------------------------------------------------------------------------------------------------------------
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! 

Ketika sebuah elemen HTML dipengaruhi oleh banyak aturan CSS, maka browser akan menentukan aturan mana yang akan dipakai. Konsep ini sering disebut dengan specificity. Dengan urutannya adalah
- 1. Inline Style 
  Inline Style sering dikenal dengan aturan CSS yang ditulis langsung pada elemen HTML, misalnya: <p style="color: red;">Teks ini merah</p>
- 2. ID Selector 
  ID selector biasa ditulis dengan # kayak #judul { color: blue; }. Kalau elemen punya ID ini, aturannya akan lebih kuat daripada class atau tag biasa. 
- 3. Class, Attribute, dan Pseudo-class Selector
  Biasanya contohnya berupa .card{}, input[type="text"] {} (attribute), dan a:hover {} (pseudo-class) . Biasanya ini ada di tengah
- 4. Tag/ Element Selector
  Tag/Element Selector biasanyaa ada di paling rendah. 
- 5. Urutan deklarasi
  Kalau sama sama kuat, browser akan memakai yang ditulis paling terakhir. Contoh: p{} dan div {}

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa! 

Responsive design adalah pendekatan desain web yang memastikan tampilan website bisa menyesuaikan ukuran layar perangkat, baik desktop, tablet ataupun handphone. Konsep ini sangat penting karena sebagian besar pengguna internet mayoritas menggunakan smartphone. Kalau website tidak responsive maka akan harus zoom in/out sehingga user experience untuk pengguna akan menjadi buruk. 

Contoh Web yang sudah responsive: 
- tokopedia karena kalau dibuka di hp maka tombol lebih besar dan layout jadi satu kolom sehingga lebih mudah di scroll. 
- Instagram Web karena feed otomatis menyesuaikan layar hp bukan dengan menampilkan layout dekstop.

Contoh web yang belum responsive: 
- Scele karena scele ketika dibuka di hp , teksnya akan menjadi sangat kecil sehingga pengguna harus geser atau melakukan zoom in agar dapat kebaca


3.Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! 

- Margin lebih ke ruang kosong di luar elemen dan fungsinya untuk memberi jarak antar elemen. 
- Border lebih ke garis tepi elemen, membungkus padding dan konten. Hal ini biasanya dikustomisasi melalui ketebalan, warna ataupun bentuk.
- Padding lebih ke ruang kosong di dalam elemen, antara konten dan border.
Visualisasinya bisa dalam seperti ini: 
[ Margin ]
   [ Border ]
      [ Padding ]
         [ Content ]

Contoh kode: 
.card {
  margin: 20px;          // jarak luar antar elemen 
  border: 2px solid red; // garis luar 
  padding: 15px;         //jarak dalam antara teks dan border 
}
Dengan ini kita bisa melihat bahwa box model: konten ada di tengah serta dibungkus padding lalu disusul border dan disusul terakhir oleh margin diluar.


4.Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox lebih dipakai untuk menyusun elemen secara horizontal (row ) atau vertikal (column). Biasanya cocok untuk navbar, daftar produk yang sejajar dan tombol yang mau diatur rapi. Contoh: 

.container {
  display: flex;
  justify-content: space-between; //atur jarak antar item 
  align-items: center;            // ratakan secara vertikal 
}
Hasilnya akan mendapat item sejajar rapi dalam satu baris, dengan jarak otomatis teratur. Kegunaan Flexbox: navbar, tombol yang sejajar, form, daftar produk rapi dalam baris, atau membuat layout responsif sederhana.

Properti penting pada container (display: flex;):
 -flex-direction: menentukan arah tata letak (row, column, row-reverse, column-reverse).
 -justify-content: mengatur posisi horizontal, misalnya flex-start, flex-end, center, space-between, space-around.
 -align-items: mengatur posisi vertikal item dalam satu baris (flex-start, flex-end, center, stretch, baseline).
 -flex-wrap: apakah elemen harus turun ke baris berikutnya kalau tidak muat (nowrap, wrap).

Properti penting pada item (untuk flex):
 -flex-grow: apakah item bisa meluas untuk mengisi ruang kosong.
 -flex-shrink: apakah item bisa mengecil jika ruang terbatas.
 -flex-basis: ukuran awal item sebelum grow/shrink bekerja.
 -order: menentukan urutan elemen, meski HTML-nya beda urutan.

Grid Layout biasanya dipakai untuk menyusun elemen dalam baris dan kolom. Biasanya cocok untuk layout dashboard, tabel atau galeri gambar. Contoh: 

.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr; /* bikin 3 kolom sama besar */
  gap: 10px; /* jarak antar kotak */
}
Hasilnya akan mendapat konten ditaruh dalam grid 3 kolom otomatis seperti tabel fleksibel.

Properti penting pada container (display: grid;):
 -grid-template-columns & grid-template-rows: mendefinisikan jumlah dan ukuran kolom/baris.
 -gap: jarak antar sel grid (bisa row-gap dan column-gap).
 -justify-items dan align-items: mengatur posisi konten dalam setiap sel.
 -grid-template-areas: memberi nama area grid, lalu item bisa diposisikan ke area tersebut.

Properti penting pada item:
 -grid-column: menentukan item menempati kolom ke berapa sampai berapa.
 -grid-row: menentukan item menempati baris ke berapa sampai berapa.
 -justify-self dan align-self: atur posisi spesifik untuk item tertentu.

Kegunaan Grid:
 -Membuat layout kompleks seperti halaman utama website dengan header, sidebar, konten utama, dan footer.
 -Membuat galeri gambar dengan kolom dinamis.
 -Membuat dashboard admin dengan banyak card.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama saya membuat tailwind, tailwind berguna untuk utility css frame work dan juga berguna una untuk membuat desain yang unik sesuai keinginan kita. Tailwind ini saya menggantinya di base.html. Setelah itu saya melakukan penambahan fitur edit produk di views.py dan juga menambahkan edit_produk.html agar nanti fitur editnya juga kelihatan di tampilannya. Jangan lupa ditambahkan di urls.py. Selain itu jangan lupa ditambahkan di main.html agar tombol edit nanti bisa kelihatan dan nanti juga dibawa ke fitur edit produk. Saya juga ada menambahkan satu fitur lagi yaitu delete produk yang berfungsi sebagai untuk melakukan delete produk, jadi saya akan menambahkan fungsi delete di views.py dan juga saya menambahkan di urls.py sama di main.html saya juga di main.html saya menambahkan button dan menghubungkan ke delete_produk. 

Setelah itu semua saya kemudian membuat navigation bar untuk menavigasi berbagai fitur dalam sebuah web. jadi saya menambahkan add product, log out, login dan register. Jangan lupa untuk dibuat konfigurasi static files pada seeting,py nya agar Django dapat mengelola file statis secara otomatis tanpa perlu konfigurasi yang kompleks. Setelah itu semua saya akan berfokus pada styling dengan menambahkan folder baru static dan di dalamnya ditambahkan folder static serta ada juga global.css untuk berfokus pada warna di website serta stylingnya (kotaknya,textnya gitu).Jangan lupa base.htmlnya juga dihubungin ke global.css

Saya juga ada memodifikasi di navbar.html agar lebih menarik dan juga saya bedain untuk tampilan di desktop dan mobile karena harus berbeda biar lebih gampang diakses untuk di mobile. Selain itu saya melakukan beberapa modifikasi di halaman login, register, halaman home, dan card produk . Card Produk saya melakukan beberapa perubahan dari tutorial dan juga di main.html saya juga melakukan perubahan agar lebih menarik dan berbeda dengan tutorial. Saya melakukan beberapa perubahan berupa tulisan font, ukuran tulisan dan letaknya. Di detail saya juga melakukan sedikit perubahan agar detail terlihat jauh lebih menarik dair yang sebelumnya . Jangan lupa juga untuk add product agar diganti dari sebelumnya agar pas melakukan add product lebih terlihat bagus dan gampang juga untuk diisi. Mungkin segitu perubahan saya untuk tugas 5 ini karena tugas 5 ini berfokus pada tampilan di mobile sama desktop agar user bisa mendapat experience yang bagus dan juga merasa gampang untuk mengakses

-----------------------------------------------------------------------------------------------------------------------------------------------------------

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.

Django AuthenticationForm adalah form bawaan Django yang sering dipakai untuk menangani login pengguna. Form ini  otomatis akan menyediakan field username dan password serta melakukan validasi apakah user dan password yang dimasukkan cocok dengan yang ada di database. Kelebihannya, developer tidak perlu membuat form login dari nol karena Django sudah menyiapkan validasi keamanan yang cukup kuat. Dengan kelebihan ini membuat django authentication form sering dikenal praktis, depat dipakai dan juga aman.

Kekurangannya, form ini cukup standar sehingga jika kita ingin menambahkan fitur khusus seperti login dengan email atau autentifikasi melalui faktor yang lain, maka kita harus melakukan penambahan atau custom sendiri.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

Menurut saya, Autentikasi adalah proses memverifikasi identitas pengguna, misalnya dengan username dan password untuk memastikan bahwa dia adalah orang yang telah memasukkan pasword dan username sesuai yang dia miliki. Sementara otorisasi adalah proses menentukan apa saja yang boleh dilakukan pengguna setelah berhasil login, misalnya dia hanya diperbolehkan hanya mengakses fitur belanja saja. Django mengimplementasikan autentikasi lewat sistem login/logout dan model User sedangkan otorisasi diatur lewat permission yang dapat menentukan hak akses pengguna terhadap resourcenya.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

Session dan cookies merupakan kedua hal yang sering digunakan untuk menyimpan state dalam aplikasi web. Cookies itu seperti “catatan kecil” yang disimpan di browser client. Setiap kali client melakukan request ke server, cookies ini otomatis ikut dikirim. Jadi cookies lebih berperan dalam menginformasikan data dari sisi client ke server, sedangkan Session  sebenarnya  lebih ke disimpan di server, bukan di client. Jadi ketika user login, server bikin data session (misalnya id pengguna, status login, role, dsb.) dan disimpan di database atau memori server. Lalu server kasih ke browser sebuah cookie kecil berisi sessionid.

Cookies memliliki kelebihan yaitu gampang diakses oleh client dan cocok untuk data ringan, namun untuk kekurangannya yaitu, gampang dimodifikasi user,kapasitas kecil, ada risiko keamanan kalau terlalu sensitif

Session memiliki kelebihan yaitu lebih aman karena data aslinya ada di server dan bukan di browser. Namun untuk kekurangannya adalah server jadi lebih berat karena harus menyimpan banyak session user.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak selalu aman karena ada beberapa resiko yang harus diwaspada. Ada beberapa risiko yang cukup sering diketahui yaitu: XSS dengan cara skrip jahat di halaman dan bisa baca cookie, CSRF akan terjadi dengan cara browser otomatis yang nantinya akan kirim cookie ke domain target, dan Man in the middle (MITM) akan terjadi jika koneksi tidak HTTPS sehingga cookie bisa disadap


Django mengatasi / rekomendasi konfigurasi:

- HttpOnly cookies
SESSION_COOKIE_HTTPONLY = True (default: True), hal ini dilakukan untuk  mencegah JS baca cookie session.
Tapi CSRF cookie tidak diset HttpOnly karena JS perlu baca token CSRF untuk AJAX. 

-Secure flag
SESSION_COOKIE_SECURE = True dan CSRF_COOKIE_SECURE = True , hal ini dilakukan untuk cookie hanya dikirim lewat HTTPS. Cara ini sangat disarankan di production

-SameSite
SESSION_COOKIE_SAMESITE dan CSRF_COOKIE_SAMESITE (opsi: 'Lax', 'Strict', atau 'None') . Hal ini dilakukan untuk membatasi kapan cookie dikirim untuk cross-site requests.
Lax juga sering jadi kompromi bagus karena mengizinkan navigasi top-level GET tapi melindungi dari sebagian besar CSRF.

-CSRF protection
Django memiliki CsrfViewMiddleware default. Kita juga harus pakai {% csrf_token %} pada form POST dan mengirim X-CSRFToken untuk AJAX. Django menolak POST tanpa token valid karena untuk  mencegah CSRF.

-Session management
Regenerasi session id setelah login (django.contrib.auth.login sudah aman tapi pastikan sesi lama tidak reuseable), atur SESSION_EXPIRE_AT_BROWSER_CLOSE atau SESSION_COOKIE_AGE sesuai kebutuhan.Untuk aplikasi sensitif, set timeout pendek (seperti SCELE).

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya memulai implementasi checklist ini dengan menambahkan fungsi registrasi, login, dan logout pada aplikasi. Pertama, saya membuat sebuah form registrasi dengan menambahkan UserCreationForm dari Django yang saya import  dan juga menaruh method register di views.py. Form ini saya hubungkan ke template HTML baru (yaitu register.html) agar user dapat melakukan pendaftaran akun baru. Selanjutnya, saya menambahkan method login_user di views.py untuk proses login ke dalam main aplikasi (proses login membutuhkan username dan password yang tepat), yang menggunakan AuthenticationForm dan fungsi authenticate dari Django. Jika pengguna berhasil login, maka sistem akan menyimpan session serta menambahkan cookie last_login untuk mencatat waktu terakhir kalau user masuk. Cookie last_login nanti akan ditampilkan di main aplikasi (client). Selain itu, saya juga membuat view logout_user yang bertugas menghapus session dan mengarahkan kembali pengguna ke halaman login. Semua view ini saya hubungkan melalui urls.py, dan saya memastikan untuk menambahkan link seperti login dan logout  pada template agar pengguna mudah mengakses fungsi login dan logout. Jangan lupa untuk menambahkan register dan login dalam bentuk html. Selain itu, saya juga ada menambahkan filter berupa my product dan all products agar bisa membedakan bahwa my product adalah produk yang telah ditambahkan oleh user login tersebut dan all products adalah semua produk yang ditambahkan oleh semua user dan ditampilkan dalam satu halaman.  Saya juga ada menambahkan di detail berupa "Ditambahkan oleh" agar bisa mengetahui produk ditambahkan oleh siapa.

Setelah proses yang perlu ditambahin berupa login, registrasi dan logout sudah selesai. Maka saya mencoba langkah berikutnya yaitu untuk membuat 2 akun baru dengan masing masing menambahkan 3 produk di tiap akun. Jadi saya pertama akan melakukan register dulu sebanyak 2 kali dan saya juga membuat username dan password login untuk akun baru. Setelah melakukan register maka saya akan melakukan login dan mulai menambahkan produk sebanyak 3 kali. Produk yang sudah ditambahkan oleh user pertama maka akan ditampilkan di all products dan my product. Kemudian saya melakukan logout untuk user pertama dan kembali login lagi untuk user kedua. Saya melakukan cara yang sama dengan melakukan penambahan produk seperti tadi dan menambahkan 3 produk yang baru. Untuk di my Produk  akan hanya ditampilkan 3 produk yang ditambahkan oleh user kedua dan di all produk akan ditampilkan 6 produk yang sudah ditambahkan oleh user 1 dan user 2.

Langkah berikutnya adalah menghubungkan model Product dengan model User. Hal ini saya lakukan dengan menambahkan ForeignKey ke model Product yang mengacu ke model User. Dengan begitu, setiap produk akan tercatat sebagai milik dari satu pengguna tertentu. Setelah itu, saya melakukan migrasi agar perubahan pada model tercatat ke dalam basis data. Hal ini bisa juga diliat dari detail.html saya dengan ada "Ditambahkan oleh" agar mengetahui produk tersebut ditambahkan oleh siapa.

Kemudian, saya menambahkan fitur untuk menampilkan informasi pengguna yang sedang login pada halaman utama aplikasi. Informasi yang ditampilkan adalah username dari pengguna serta cookie last_login yang sebelumnya sudah disimpan saat proses login berhasil. Dengan cara ini, user bisa langsung mengetahui siapa yang sedang login dan kapan terakhir kali mereka masuk ke aplikasi.

-----------------------------------------------------------------------------------------------------------------------------------------------------------
1.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Menurut saya data delivery dibutuhkan dalam pengimplementasian sebuah platform karena mempunyai beberapa tujuan utama yaitu: 
- Memisahkan back end dan front end. Hal ini sangat berguna karena backend berfokus untuk bertanggung jawab serta menyediakan data, sedangkan front end bertugas menampilkan dan memudahkan pengembangan paralel dan manintenance
- Skalabilitas dan performa. API sangat memungkinkan caching, pagination dan juga optimasi transfer sehingga aplikasi akan lebih cepat dan hemat sumber daya. 
- Pengalaman pengguna. Data yang diberikan dan digunakan sebagai API dapat membuat antarmuka menjadi lebih responsif serta mendukung fitur realtime atau offline. 
- Keamanan. Keamanan bisa menjadi lebih terjamin dikarenakan terdapat endpoint terpisah sehingga kita bisa mengatur otorisasi, versioning API, dan pembatasan akses yang lebih mudah 

2.Menurutmu, mana yang lebih baik antara  XML atau JSON ? Mengapa Json lebih populer dibandingkan XML? 

Menurut saya keduanya cukup sama dan mempunyai peran yang cukup berbeda. JSON mungkin lebih poopuler untuk API web modernkarena ringan (payload kecil), terdapat Native untuk JavaScript, mudah dibaca/ditulis dan cocok untuk REST/HTTP/SPA. XML juga menurut saya masih tetap berguna karena ketika butuh beberapa fitur lanjutan seperti namespaces, XSD (untuk skema dan validasi dokumen) atau transformasi XLT (dokumen kompleks) maka sangat dibutuhkan XML. 

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method ini menjalankan proses validasi form dengan memanggil validasi tiap field, menjalankan clean_<field>() dan clean() pada form, serta mengisi form.cleaned_data. Method ini sangat penting karena dapat memastikan data yang masuk sesuai aturan (seperti tipe data, panjang maksimal dan pilihan yang sudah disediakan). Selain itu juga berguna untuk menghindari error saat menyimpan ke data base (string ke integerfield) dan juga mencegah data berbahaya karena validator dapat menolak jika input berbeda dengan yang diharapkan. 

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token sangat penting karena digunakan untuk mencegah serangan Cross-Site Request Forgery yaitu teknik yang dimana penyerang memanfaatkan sesi login para korban untuk melakukan aksi yang tidak sah. Jadi untuk cara kerjanya nanti Django akan mengeluarkan token dan meminta token itu untuk disertakan juga dalam form POST. Server nanti akan berusaha memverifikasi token setiap request yang mengubah state. 

Jadi hal tersebut dapat dimanfaatkan oleh penyerang pada saat penyerang buat halaman A yang berisi form POST otomatis ke misal BCA.com/transfer. Jika korban sudah login ke BCA.com maka nanti websitenya tidak memverifikasi tokennya sehingga nanti aksi pembobolan transfer bisa berhasil. Jadi jangan lupa untuk selalu sertakan {% csrf_token %} di form template dan gunakan header X-CSRFToken untuk AJAX. Django default  akan menolak request tanpa token, yang sebenarnya berguna untuk melindungi aplikasi.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Saya akan menjelaskan pertama dari mulai membuat Toko (di main/models.py) dimana nanti di dalam models.py akan diisi berupa atribut untuk toko tersebut (buat atribut data basenya ). Disini saya ada memberikan name (CharField(100)), price (IntegerField), description (TextField), thumbnail (URLField), category (CharField dengan CATEGORY_CHOICES), stock (IntegerField), is_featured (BooleanField default False). Untuk Category-choices saya ada melakukan pembatasan dengan hanya menyediakan pilihan electronics, fashion, home, food, sports. 

Setelah membuat models.py maka kemudian saya akan lanjut dengan membuat file baru di main yaitu forms.py yang berfungsi untuk add_product disana dan nanti produk yang sudah ditambahkan akan muncul di main. Di dalam forms.py saya ada mengisi dengan classTokoForm(ModelForm): Meta: model= Toko; fields= ["name","price","description","thumbnail","category","stock","is_featured"]. Kemudian saya melakukan beberapa perubahan di views.py dengan di show_mainnya ada saya tambahin Toko.objects.all() untuk bisa menunjukkan semua produknya. 

Selain itu saya ada tambahkan juga method add_product dan detail_produk di views.py agar nanti fungsi add_product dan detail_product tersebut bisa dijalankan pada saat di websitenya. Jangan lupa juga ada saya menambahkan untuk API end points dengan show_json, show_xml, show_json_by_id , show_xml_by_id dengan menggunakan django.core.serializers.serialize. Hal ini saya lakukan untuk memisahkan concerns agar views mengatur alur dan validasi sedangkan serializers untuk menangani data delivery untuk API

Setelah itu jangan lupa juga untuk mendefinisikan URLS di  main dan ke urls.py. Disana harus ada ditambahkan beberapa yaitu path('add/', add_product, name='add_product'), path('detail/<str:id>/', detail_product, name='detail_product'), plus API paths. API paths itu untuk yang XML dan JSON. 


Kemudian yang terakhir saya kembali ke template dan melengkapi bagian main.html dengan menambahkan for untuk bisa mengeluarkan list produk saya. Selain itu, saya juga menambahkan add_product.html agar saya bisa menambahkan produk dan juga bisa mengisi beberapa detail dari produk tersebut. Setelah saya membuat add_product, saya juga nanti akan mengembalikannya ke show_main untuk menampilkan skeilas mengenai produk tersebut dan saya juga menambahkan detail_produk agar saya bisa melihat tentang apa yang sudah saya tambahkan mengenai informasi produk tersebut. Untuk detail produk saya menambahkan juga product.nama, product.stock agar saat detail produk diakses maka bisa nanti mengeluarkan informasi seputar produk tersebut dan saya juga menggunakan for loop agar bisa menampilkan produk tersebut (for loop di main). Setelah itu saya juga membuat base.html untuk template dasar yang digunakan kerangka halaman web lainnya dalam projek. Untuk yang terakhirnya jangan lupa untuk mengecek juga di post man dengan http://localhost:8000/xml/ dan juga http://localhost:8000/json/ serta http://localhost:8000/xml/[produk.id] dan http://localhost:8000/json[produk.id]. hal ini berguna untuk mengecek apakah xml,json serta xml dan json dalam produk.id apakah sudah terlihat di dalam post man atau tidak. Postman semacam aplikasi yang membantu mempermudah untuk membuka xml dan json (menurut saya) 

6.  Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Menurut saya untuk asdos di tutorial 2 sudah baik dan sudah sesuai dengan kriteria sehingga saya untuk mengerjakannya tidak terllau susah dan mudah cukup mengerti. Saya juga mempelajari dari penjelasan yang diberikan serta saya mencoba mengingat dan mencatatnya. Terima kasih untuk kakak asdos telah membuat tutorial tidak terllau susah. 

Link untuk mengakses xml dan json:  https://docs.google.com/document/d/1cPnFUHBDGMFpsxMlgOQaGtbgYODdwTLNGGrRijRWZjw/edit?usp=sharing



--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban : Langkah pertama yang saya lakukan adalah membuat folder bernama PAT. Setelah itu, saya mengecek Django menggunakan terminal dengan perintah pip install django. Django saya sudah ada dan ternyata berada di versi 24.2 dan langsung diugprade secara otomatis ke versi 25.2 karena dari perintah pip install django. Kemudian, saya membuat proyek Django dengan menjalankan python -m django startproject PAT. Perlu dicatat, jika perintah ini dijalankan dari folder induk, maka Django akan membuat direktori PAT/ yang berisi manage.py serta subdirektori konfigurasi dengan nama yang sama. Namun, jika saya sudah berada di dalam folder kosong PAT, sebaiknya menggunakan python -m django startproject PAT . agar tidak terjadi struktur ganda PAT/PAT.

Setelah proyek berhasil dibuat, saya berpindah ke direktori yang berisi manage.py menggunakan cd PAT. Dari sana, saya menambahkan aplikasi baru bernama main dengan perintah python manage.py startapp main. Supaya aplikasi ini dikenali oleh Django, saya menambahkan 'main' pada bagian INSTALLED_APPS di berkas PAT/settings.py. Selain itu, saya juga memastikan pengaturan umum seperti TIME_ZONE, LANGUAGE_CODE, dan ALLOWED_HOSTS sudah sesuai kebutuhan. Langkah berikutnya adalah mengatur routing. Pada PAT/urls.py, saya menambahkan include('main.urls') agar permintaan ke alamat dasar diarahkan ke aplikasi main. Di dalam folder aplikasi, saya membuat berkas main/urls.py yang memetakan path kosong "" ke fungsi view utama. Pada main/views.py, saya menambahkan fungsi show_main(request) yang menyiapkan context berupa data (seperti nama aplikasi, nama saya, dan kelas) kemudian merendernya ke template.

Untuk menampilkan data tersebut, saya membuat folder main/templates/ dan di dalamnya sebuah berkas main.html. Template ini bertugas menerima context dari view dan mengubahnya menjadi halaman HTML yang utuh. Dengan begitu, alurnya menjadi jelas: urls.py → views.py → template. URL dipetakan ke view, view menyiapkan data yang diperlukan, lalu template menghasilkan respons HTML yang dikirim kembali ke client.Pada sisi data, saya mendefinisikan model di main/models.py. Saya membuat model Product dengan enam atribut utama, yaitu name, price, description, thumbnail, category, dan is_featured. Selain itu, saya menambahkan satu field baru bernama stock untuk menyimpan jumlah stok produk. Field ini penting karena mendukung kebutuhan aplikasi yang berkaitan dengan katalog atau toko online. Setelah model siap, saya menjalankan python manage.py makemigrations untuk membuat file migrasi, lalu python manage.py migrate agar struktur tabel benar-benar diterapkan di database.

Terakhir, untuk menguji aplikasi, saya menjalankan server dengan python manage.py runserver dan membuka http://127.0.0.1:8000/. Dari sana saya bisa memastikan bahwa routing berfungsi, view berjalan dengan baik, dan template menampilkan data yang saya kirim. Sebagai dokumentasi tambahan, saya membuat README.md di folder utama proyek (satu level dengan manage.py) untuk mencatat tujuan aplikasi, cara menjalankan proyek, perubahan yang saya lakukan pada tiap berkas, serta catatan penting tentang praktik terbaik menjalankan perintah startproject.

Setelah aplikasi berjalan dengan baik di lokal, langkah berikutnya adalah melakukan deployment ke PWS (PBP Web Service) supaya aplikasi dapat diakses melalui internet oleh teman-teman maupun asdos. Tahapan awalnya adalah membuat repositori GitHub untuk proyek Django saya. Seluruh folder proyek, termasuk manage.py, folder PAT, aplikasi main, dan berkas README.md, saya commit dan push ke repositori GitHub tersebut.Langkah selanjutnya adalah menghubungkan repositori GitHub dengan website PBP yang sudah disediakan. Website PBP ini berfungsi sebagai server online yang akan menjalankan aplikasi saya langsung secara otomatis. Dengan menghubungkan GitHub ke PWS, setiap kali saya melakukan push perubahan ke program saya, aplikasi saya di website PBP juga akan diperbarui. Setelah proses deployment berhasil, saya mendapatkan sebuah tautan URL dan saya juga menaruh di allowed host pada seetings.py . Hal ini membuat program aplikasi saya dapat diakses melalui browser. Dengan tautan ini, aplikasi yang sebelumnya hanya bisa dijalankan menggunakan python manage.py runserver di lokal, kini dapat diakses oleh siapa saja melalui jaringan internet.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban : https://docs.google.com/document/d/13DzXi1cfF6No6RQJgbK2OXols6LCuTtp_lSaZtLG6VY/edit?usp=sharing

3.Jelaskan peran settings.py dalam proyek Django
Jawaban : settings.py merupakan pusat pengaturan yang berperan penting dalam mengatur jalannya aplikasi Django. File ini menyimpan berbagai konfigurasi inti, seperti daftar aplikasi yang digunakan (INSTALLED_APPS) — misalnya ketika saya menambahkan 'main', maka Django akan mengetahui bahwa perlu dibuat tabel database dari model yang ada di aplikasi tersebut. Selain itu, settings.py juga mencakup pengaturan koneksi database, lokasi template HTML dan file statis, serta aspek keamanan seperti SECRET_KEY, DEBUG, dan ALLOWED_HOSTS. Tidak hanya itu, file ini juga memuat konfigurasi tambahan, antara lain bahasa, zona waktu, middleware, hingga opsi autentikasi. Dengan kata lain, settings.py dapat disebut sebagai otak dari proyek Django, karena tanpa adanya file ini, Django tidak akan mengetahui bagaimana aplikasi seharusnya dijalankan.

4. Bagaimana cara kerja migrasi database di Django? 
Jawaban : Migrasi database di Django adalah proses yang digunakan untuk menjaga agar struktur database selalu sesuai dengan model yang sudah didefinisikan pada models.py. Ketika kita membuat atau mengubah model, Django tidak langsung mengubah database, melainkan terlebih dahulu membuat file migrasi melalui perintah makemigrations. File ini berisi instruksi perubahan dalam bentuk Python yang nantinya diterjemahkan menjadi perintah SQL. Setelah itu,  perintah migrate akan dijalankan untuk benar-benar menerapkan perubahan tersebut ke dalam database. Dengan mekanisme ini, Django dapat secara otomatis menyesuaikan tabel dan kolom di database tanpa perlu menulis perintah SQL secara manual.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Jawaban : Menurut saya, Django lebih sering dijadikan permulaan daalam permulaan pembelajaran pengembangan perangkat lunak karena framework ini lengkap, terstruktur dan memiliki standar yang jelas. Django megikuti pola MVT yang memudahkan bagi para pemula seperti saya untuk memahami alur kerja aplikasi web, mulai dari request masuk sampai response kembali ke pengguna. Selain itu, Django memberikan banyak fitur bawaan seperti sistem autentikasi, admin panel, ORM untuk database, hingga keamanan dasar, sehingga pengembang pemula seperti saya tidak perlu membangun semuanya dari nol. Dokumentasi Django juga termasuk lengkap dan komunitasnya sangat besar, sehingga mudah untuk belajar dan mencari solusi di internet ketika menghadapi masalah. Jadi menurut saya, Django bukan hanya membantu memahami dasar pengembangan web, tetapi juga memperkenalkan konsep-konsep penting dalam rekayasa perangkat lunak seperti modularitas dan manajemen proyek.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Menurut saya sudah cukup baik dan instruksi yang diberikan sudah sangat jelas sehingga kami yang kurang mengerti dengan web , bisa langsung paham dengan membaca dan mengikuti panduan tutorial . Usahakan tutorial mirip seperti gitu terus yaa kak. Semangat untuk para kakak asdos. 