# Problem Definition – BikeSharing ML Pipeline Project

08 Aralık 2025


## 1. Dataset Seçimi: Düşünce Süreci

Zero2End Machine Learning Bootcamp sürecinde oluşturduğum proje yapısı, raporlama disiplini ve uçtan uca düşünme biçimi beni ciddi anlamda geliştirdi. O projede büyük hacimli bir e-ticaret datasıyla çalışmak, veri mühendisliği bakış açımı güçlendirmiş ve gerçek bir ML sisteminin nasıl uçtan uca kurulacağını deneyimlememi sağlamıştı. Şimdi ise aynı standartları farklı sektörlerde uygulayarak portföyümü genişletmek ve üretim kapasitemi artırmak istiyorum.

Yeni proje için kendime şu soruyu sordum:
“Gerçek hayatta sık karşılaşılan, operasyonel etkisi yüksek ve makine öğrenimiyle doğrudan çözülebilir bir problem ne olabilir?”

Bu kez odağımı şehir içi ulaşım ve mikromobilite sektörüne çevirdim. Giderek büyüyen bisiklet paylaşım sistemleri; filo yönetimi, talep dalgalanmaları, boş/dolu istasyon problemleri ve sürdürülebilirlik gibi konularla yüksek veri potansiyeline sahip. Üstelik zaman serisi, regresyon, hava durumu etkisi gibi konuların birleşmesi, model geliştirmek için zengin bir alan oluşturuyor.

Bu nedenle, Bike Sharing Demand veri setinin hem operasyonel bir problemi doğrudan temsil etmesi hem de Kaggle yarışması yapısında olması, bu projeyi seçmem için güçlü bir motivasyon oluşturdu.

## 2. Veri Seti

Kullandığım veri seti, Kaggle’ın Bike Sharing Demand yarışmasında sunulan ve Washington DC’deki Capital Bikeshare sisteminden elde edilen gerçek kiralama verileridir.

Bike Sharing Demand dataset linki: https://www.kaggle.com/competitions/bike-sharing-demand/overview

Bu veri seti, küçük bir veri değil; özellik mühendisliği, mevsimsellik analizi, hava durumu etkileri, zaman temelli validasyon gibi ML mühendisi olarak geliştirmem gereken pek çok beceriyi üzerinde çalışarak uygulayabileceğim dengeli bir zorluk sunuyor. Dolayısıyla hem sektörel anlamda anlamlı hem de teknik anlamda büyütücü bir proje.

3. İş Problemi (Business Context)

Şehir içi ulaşım ve mikromobilite sektöründe temel problem, kullanıcı talebinin gün içinde sürekli değişmesi ve bu değişimin operasyonel süreçleri doğrudan etkilemesidir. Paylaşımlı bisiklet, scooter ve e-mobilite sistemlerinde talep doğru öngörülemediğinde:

- Bazı bölgelerde araçlar hızla tükenirken,
- Bazı bölgelerde gereğinden fazla araç boşa bekler,
- Operasyon ekipleri araç taşımak için gereksiz rota oluşturmak zorunda kalır,
- Hem operasyon maliyetleri artar hem de kullanıcı memnuniyeti düşer.

Mikromobilite altyapısının sürdürülebilir bir şekilde yönetilebilmesi için talep tahmini, sektörün en kritik bileşenlerinden biridir. Saatlik talep tahminleri; filo planlaması, yeniden konumlandırma stratejileri, bakım–onarım planlaması ve enerji yönetimi gibi birçok sürecin temel girdisidir.

Bu proje yalnızca bu dataset özelinde bir tahmin modeli geliştirmek için değil, aynı zamanda mikromobilite alanındaki ileride yapacağım diğer veri bilim projeleri için de bir temel oluşturmak adına seçilmiştir. Bu sayede farklı şehirler, farklı ulaşım araçları veya farklı kullanıcı davranış modelleri üzerine geliştireceğim yeni projeler için ortak bir çerçeve oluşturmuş oluyorum.

