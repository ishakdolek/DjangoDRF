# DjangoDRF
Django Rest framework,swagger, Jwt birlikte kullanabileceğimiz örnek bir uygulama yapılmıştır.
Kurulumları ve adımları sırasıyla anlatıp source kodu paylaşıyorum.

django projesi oluşturuyoruz. Pycharm kullanıyorum. Otomatik olarak 
virtual env üzerinde projeyi oluşturuyor. Vscode kullanıyorsanız bu işlemleri 
manuel yapmanız gerekiyor. Virtual env kurulduktan sonra aşağıdaki kurulumları venv
aktif edip venv'e kuruyoruz.


Kurulumların yapılması

`pip install Django django-rest-framework, pyyaml,django-rest-swagger,djangorestframework-simplejwt`

`django-rest-swagger` normalde  swagger için bunu kullanmıştım. Fakat paket bakımı artık olmayacak onun yerine 
https://drf-yasg.readthedocs.io/en/stable/readme.html bu paketi kullanacağım. Github sayfasında bakıldığı zaman
kurulumu gayet kolaydır.


Simple Jwt Token ile işlem yapmak için settings dosyasına aşağıdaki satırları eklemek lazım
`SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Basic': {
            'type': 'basic'
      },
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}`



# Kaynak 
https://drf-yasg.readthedocs.io/en/stable/readme.html
https://codesource.io/django-rest-api-documentation-with-swagger-ui/
