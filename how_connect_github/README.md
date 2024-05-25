# چگونگی اتصال به گیت هاب 


## کلون کردن ریپازتوری خود(یا ریپازتوری که میخواهید تغییر دهید)




## ورود به  ریپوزتری خود 

از کامند زیر استفاده کنید :‌

```bash

git clone https://username:token@url_of_repo


```
چندین پارامتر باید مشخص شود :‌ 



###   token  

از توکن زیر استفاده کنید : 
```bash
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
```

###  username 

نام کاربری گیت هاب خود را وارد کنید برای مثال  parvvarsh


### url_of_repo

در ریپو که میخواهید تغیر ایجاد کنید url ان را کپی کنید.
برای مثال : 

```bash

github.com/itrcAI/parvaresh/

```

اگر زمانی token  تغییر کرد شما قادر به کاری نیستید و برای اتصال از کامند زیر استفاده کنید : 

```bash

git remote set-url origin https://username:new_token@url_of_repo

```


بعد از کلون کردن باید داخل ریپازتوری خود شوید 

```bash

cd name_of_folder

```


## add 

حالا که با  کامند زیر فایل ها یا فالود های خود را ادد کنید : 

```bash

git add name_of_file(s) 

```
--- 
```bash

git add name_of_folder(s) 

```

## commit

بعد از انجام تغییرات باید تغییرات خود را commit یا ثبت کنیم
```bash

git commit -am "message for commit"

```




## push

پس از commit در ریپو مورد نظر در branch  که میخواهید ان را push کنید

```bash

git push -f origin main


```





