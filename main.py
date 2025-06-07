import matplotlib.pyplot as plt
import pandas as pd
from bidi.algorithm import get_display
import arabic_reshaper
import matplotlib.ticker as ticker






# داده‌ها
cities = ['تهران', 'مشهد', 'اصفهان', 'شیراز', 'کرج', 'تبریز', 'قم', 'اهواز', 'ارومیه', 'ساری']
users = [12000000, 4500000, 5000000, 4000000, 3700000, 3900000, 3000000, 2600000, 2700000, 2000000]

# تبدیل به دیتافریم
df = pd.DataFrame({
    'شهر': cities,
    'تعداد کاربران': users,
})

# ذخیره در فایل اکسل
df.to_excel('آمار_کاربران_اینترنت.xlsx', index=False)

# تابع نمایش فارسی
def persian_text(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)




# رسم نمودار
plt.figure(figsize=(12, 6))
bars = plt.bar([persian_text(c) for c in cities], users, color='mediumseagreen')

# تنظیمات محور Y
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

# عنوان و محورها
plt.title(persian_text('توزیع کاربران اینترنت در شهرهای ایران'), pad=20)
plt.xlabel(persian_text('شهر'), labelpad=10)
plt.ylabel(persian_text('تعداد کاربران'), labelpad=10)

plt.xticks(rotation=45)
plt.tight_layout()

# ذخیره نمودار
plt.savefig('نمودار_کاربران.png', dpi=300, bbox_inches='tight')
plt.show()