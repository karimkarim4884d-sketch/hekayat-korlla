import telebot
import requests
import firebase_admin
from firebase_admin import credentials, db

# --- بياناتك يا كيمو اللي هنشغل بيها الشغل ---
BOT_TOKEN = "8607322554:AAEhHNUfS8RRI3c9gvGnATVt3gx9lqiFvGw"
API_KEY = "AIzaSyAubyhMKRbUApvTtIpDVo5JbRFIeoEyT-o" 
API_URL = "https://smmcpan.com/api/v2" 
DATABASE_URL = "https://mmss-242e6-default-rtdb.firebaseio.com"

# ربط الفايربيس من غير ملفات خارجية عشان نسهل الدنيا
if not firebase_admin._apps:
    try:
        firebase_admin.initialize_app(options={'databaseURL': DATABASE_URL})
    except:
        pass

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    uid = str(message.chat.id)
    # بنسجل المستخدم في قاعدة البيانات لو جديد
    user_ref = db.ref(f'users/{uid}')
    user_data = user_ref.get()
    
    if not user_data:
        user_ref.set({'balance': 0.0, 'name': message.from_user.first_name})
        balance = 0.0
    else:
        balance = user_data.get('balance', 0.0)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📊 قائمة الخدمات", "💰 شحن رصيدك")
    markup.add("👤 حسابي", "🛠️ الدعم الفني")
    
    bot.send_message(uid, f"👑 مرحباً بك في بوت الـ SMM الملكي\n\n💰 رصيدك الحالي: {balance} ج.م\n\nإختر من القائمة بالأسفل لبدء تزويد متابعيك!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📊 قائمة الخدمات")
def show_services(message):
    try:
        # بنسحب الخدمات من الموقع اللي بعتهولي
        payload = {'key': API_KEY, 'action': 'services'}
        services = requests.post(API_URL, data=payload).json()
        
        text = "🚀 خدماتنا المميزة (الأسعار شاملة عمولتك 10ج):\n\n"
        # بنعرض أول 10 خدمات عشان الزبون ميتوهش
        for s in services[:10]:
            # السعر الأصلي + 10 جنيه بتوعك
            final_price = float(s['rate']) + 10.0 
            text += f"🔹 {s['name']}\n💰 السعر: {final_price} ج.م | الرمز: {s['service']}\n---\n"
        
        bot.send_message(message.chat.id, text + "\nلطلب خدمة، تواصل مع الدعم الفني.")
    except:
        bot.send_message(message.chat.id, "❌ عذراً، هناك ضغط على السيرفر، حاول مجدداً.")

@bot.message_handler(func=lambda m: m.text == "👤 حسابي")
def my_account(message):
    uid = str(message.chat.id)
    try:
        balance = db.ref(f'users/{uid}/balance').get() or 0.0
    except:
        balance = 0.0
    bot.send_message(message.chat.id, f"👤 الحساب: {message.from_user.first_name}\n🆔 المعرف (ID): {uid}\n💰 رصيدك: {balance} ج.م")

@bot.message_handler(func=lambda m: m.text == "🛠️ الدعم الفني")
def support(message):
    bot.send_message(message.chat.id, "لشحن الرصيد أو الاستفسارات، تواصل مع المدير كيمو: @Karim")

bot.polling(none_stop=True)
          
