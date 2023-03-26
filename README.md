# CustomObjectDetectionWithYolov5
 
Yolov5 üzerinde özel bir nesne tanımlayabilmek için öncelikli olarak veri setini hazırlamamız gereklidir. Bunun için tanımlayacağımız özel nesnenin farklı açılardan fotoğrafları çekilmelidir. Daha sonra çektiğimiz bu fotoğraflar üzerinde nesnenin etiketlemesini gerçekleştiriyoruz. Ben nesne etiketlemesi için labelimg uygulamasını kullandım. Uygulamayı açtığınızda ilk olarak soldaki menü çubuğundan kaydetme formatını Yolo yapıyoruz ve nesnemizin resimlerini içeren klasörü uygulamamızda açıyoruz.

![1](https://user-images.githubusercontent.com/73904811/227752835-26947d2c-c5cd-433f-9d0d-d8f3f473bb6a.png)
![2](https://user-images.githubusercontent.com/73904811/227752840-882ecdcf-5a1c-481e-8649-8bb9c6c54203.png)

Daha sonra Create RectBox kısmına tıklayıp nesnemizi işaretliyoruz ve bu yaptığımız işlemleri kaydediyoruz. Labelimg bu işlemler sonucunda txt uzantılı veriler üretecektir. Veri setimizi oluşturmak için ilk olarak ‘data’ adını verdiğimiz bir klasör içerisine labels ve images adında iki ayrı klasör oluşturuyoruz. Daha sonra bu iki ayrı klasörün içine de training ve validation adında dosyalarımızı oluşturuyoruz. Bu dosyaların içine ise etiketlediğimiz verileri ve asıl fotoğraflarımızı yüklüyoruz. (örnek görseli aşağıda bulabilirsiniz.) 


![3](https://user-images.githubusercontent.com/73904811/227752845-eb2dd5bf-8b1c-40fc-8a9e-9e078a657650.png)
![4](https://user-images.githubusercontent.com/73904811/227752847-4b915e8d-5610-4b16-8baa-00f9f1b90cd4.png)
![5](https://user-images.githubusercontent.com/73904811/227752849-d967314b-990a-44e9-9d5a-499f3d7e897a.png)
![6](https://user-images.githubusercontent.com/73904811/227752851-1b76620b-a2d5-439d-8b3e-a45d19fd3c4e.png)


Daha sonra data dosyamızı zip haline getiriyoruz ve drive hesabımıza yüklüyoruz. Bu sayede veri setimiz hazır olmuş hale geliyor.
Bir sonraki aşama ise yolov5’i eğitmek. Bunun için ipynb uzantılı dosyayı googlecolab üzerinden açmamız gerekli. (Bu dosyamızı açtıktan sonra yürütme zamanının GPU olduğundan emin olunuz.) 
İpynb uzantılı dosyayı colab üzerinden açtıktan sonra ilk 3 komutumuzu çalıştırıyoruz. Daha sonra 4. Kodumuzu çalıştırmadan önce soldaki menüde dosya kısmından data.yaml dosyasını düzenlememiz gerekli. Bu data.yaml dosyasını açtığınızda class sayımızı(tanımlanan nesne sayısı) ve nesnelerimizin adını giriyoruz.

![7](https://user-images.githubusercontent.com/73904811/227752856-509b589d-a8c5-4e47-b084-6592f0f3d8c2.png)
![8](https://user-images.githubusercontent.com/73904811/227752859-e9f36587-0bdc-406d-8256-edba68baf3f1.png)


Bu işlemi yapıp kaydettikten sonra artık son aşamamız olan eğitimi gerçekleştireceğiz. Bu yüzden son aşamayı çalıştırıyoruz ve eğitimin bitmesini bekliyoruz.
Eğitim işlemi sonra erdiğinde best.pt dosyasını bulup indiriyoruz ve kodların bulunduğu dosya ile ile aynı dosyaya atıyoruz. Hepsi bu kadar artık kodu çalıştırıp nesneyi tanımlamasını izleyebiliriz.

https://user-images.githubusercontent.com/73904811/227752865-3e769821-9a31-41c8-847f-87e77a9ebd7e.mp4


