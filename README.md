# CustomObjectDetectionWithYolov5
 
Yolov5 üzerinde özel bir nesne tanımlayabilmek için öncelikli olarak veri setini hazırlamamız gereklidir. Bunun için tanımlayacağımız özel nesnenin farklı açılardan fotoğrafları çekilmelidir. Daha sonra çektiğimiz bu fotoğraflar üzerinde nesnenin etiketlemesini gerçekleştiriyoruz. Ben nesne etiketlemesi için labelimg uygulamasını kullandım. Uygulamayı açtığınızda ilk olarak soldaki menü çubuğundan kaydetme formatını Yolo yapıyoruz ve nesnemizin resimlerini içeren klasörü uygulamamızda açıyoruz.

1.png
2.png

Daha sonra Create RectBox kısmına tıklayıp nesnemizi işaretliyoruz ve bu yaptığımız işlemleri kaydediyoruz. Labelimg bu işlemler sonucunda txt uzantılı veriler üretecektir. Veri setimizi oluşturmak için ilk olarak ‘data’ adını verdiğimiz bir klasör içerisine labels ve images adında iki ayrı klasör oluşturuyoruz. Daha sonra bu iki ayrı klasörün içine de training ve validation adında dosyalarımızı oluşturuyoruz. Bu dosyaların içine ise etiketlediğimiz verileri ve asıl fotoğraflarımızı yüklüyoruz. (örnek görseli aşağıda bulabilirsiniz.) 

3.png
4.png
5.png
6.png

Daha sonra data dosyamızı zip haline getiriyoruz ve drive hesabımıza yüklüyoruz. Bu sayede veri setimiz hazır olmuş hale geliyor.
Bir sonraki aşama ise yolov5’i eğitmek. Bunun için ipynb uzantılı dosyayı googlecolab üzerinden açmamız gerekli. (Bu dosyamızı açtıktan sonra yürütme zamanının GPU olduğundan emin olunuz.) 
İpynb uzantılı dosyayı colab üzerinden açtıktan sonra ilk 3 komutumuzu çalıştırıyoruz. Daha sonra 4. Kodumuzu çalıştırmadan önce soldaki menüde dosya kısmından data.yaml dosyasını düzenlememiz gerekli. Bu data.yaml dosyasını açtığınızda class sayımızı(tanımlanan nesne sayısı) ve nesnelerimizin adını giriyoruz.

7.png
8.png

Bu işlemi yapıp kaydettikten sonra artık son aşamamız olan eğitimi gerçekleştireceğiz. Bu yüzden son aşamayı çalıştırıyoruz ve eğitimin bitmesini bekliyoruz.
Eğitim işlemi sonra erdiğinde best.pt dosyasını bulup indiriyoruz ve kodların bulunduğu dosya ile ile aynı dosyaya atıyoruz. Hepsi bu kadar artık kodu çalıştırıp nesneyi tanımlamasını izleyebiliriz.

ODwithYolov5.mp4