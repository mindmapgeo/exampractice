import json

chats = [
    # ANEMIA
    {
        "title": "She's been exhausted for months",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "Natalia, I've looked at your blood work and I want to be straight with you — your iron stores are seriously depleted. Your ferritin is at 6. Normal is between 12 and 150. So something has been draining you for a while.", "lang": "en"},
            {"role": "Interpreter", "text": "Наталю, я переглянула ваші аналізи і хочу бути з вами чесною — ваші запаси заліза серйозно виснажені. Ваш феритин становить 6. Норма — від 12 до 150. Тобто щось уже якийсь час вас виснажує.", "lang": "uk"},
            {"role": "Patient", "text": "Я думала, що просто стара стаю. Мені 47, усі мої подруги скаржаться на втому. Я не хотіла скаржитися.", "lang": "uk"},
            {"role": "Interpreter", "text": "I thought I was just getting old. I'm 47, all my friends complain about being tired. I didn't want to be the one complaining.", "lang": "en"},
            {"role": "Doctor", "text": "No, no — I'm glad you came in. This is not 'getting old', this is your body sending up a flare. When your iron is this low, your heart actually has to beat faster just to move oxygen around. That's why you're exhausted. You're working hard all day and your blood can't even keep up.", "lang": "en"},
            {"role": "Interpreter", "text": "Ні, ні — я рада, що ви прийшли. Це не 'старіння', це ваш організм подає сигнал тривоги. Коли залізо настільки низьке, вашому серцю доводиться битися швидше тільки щоб перекачати кисень. Саме тому ви так виснажені. Ви важко працюєте цілий день, а ваша кров просто не може за вами встигнути.", "lang": "uk"},
            {"role": "Patient", "text": "Ого. Тобто це справжнє? Це не в мене в голові?", "lang": "uk"},
            {"role": "Interpreter", "text": "Wow. So it's real? It's not in my head?", "lang": "en"},
            {"role": "Doctor", "text": "Absolutely real. And I want to figure out *why* it got this low, not just throw supplements at you. Can I ask — are your periods on the heavier side?", "lang": "en"},
            {"role": "Interpreter", "text": "Абсолютно реальне. І я хочу зрозуміти, *чому* воно так знизилося, а не просто прописати вам добавки. Можна запитати — у вас рясні місячні?", "lang": "uk"},
            {"role": "Patient", "text": "Дуже рясні, останні два роки. Я думала, це просто перед менопаузою так буває.", "lang": "uk"},
            {"role": "Interpreter", "text": "Very heavy, for the last two years. I thought it was just what happens before menopause.", "lang": "en"},
            {"role": "Doctor", "text": "It can be, yes. But it can also be fibroids or a hormonal imbalance that we can actually treat. So here's what I want to do: we start you on iron today, but I also want to send you to a gynecologist — not because anything is wrong, but because I want someone to look at the source. Does that make sense?", "lang": "en"},
            {"role": "Interpreter", "text": "Так буває. Але це також можуть бути міоми або гормональний дисбаланс, який ми дійсно можемо лікувати. Тому ось що я хочу зробити: починаємо залізо сьогодні, але я також хочу направити вас до гінеколога — не тому що щось не так, а тому що хочу, щоб хтось подивився на першопричину. Це зрозуміло?", "lang": "uk"},
            {"role": "Patient", "text": "Так. Дякую, що не просто сказали 'пийте вітаміни'.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes. Thank you for not just saying 'take vitamins'.", "lang": "en"},
            {"role": "Doctor", "text": "You deserve to feel good. That's the whole point of this.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви заслуговуєте почуватися добре. Саме для цього ми тут.", "lang": "uk"}
        ]
    },
    {
        "title": "Why does my food not fix it?",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "Your B12 is very low, Oksana. This type of anemia is actually different from iron deficiency — it affects how your nerves work, not just your energy.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш B12 дуже низький, Оксано. Цей тип анемії насправді відрізняється від залізодефіцитного — він впливає на роботу ваших нервів, а не лише на енергію.", "lang": "uk"},
            {"role": "Patient", "text": "Але я їжу гарно! У мене завжди є буряк, гранати, шпинат. Бабуся казала, що це найкраще для крові.", "lang": "uk"},
            {"role": "Interpreter", "text": "But I eat well! I always have beets, pomegranates, spinach. My grandmother said those are the best for blood.", "lang": "en"},
            {"role": "Doctor", "text": "Your grandmother was right about iron — those are fantastic for iron. But B12 is a completely different vitamin and it lives almost exclusively in animal foods. Meat, dairy, eggs. If you're eating mostly plant-based, your body just doesn't have a source for it.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваша бабуся мала рацію щодо заліза — це справді чудово для заліза. Але B12 — це зовсім інший вітамін і він міститься майже виключно в продуктах тваринного походження. М'ясо, молочне, яйця. Якщо ви харчуєтеся переважно рослинною їжею, ваш організм просто не має джерела для нього.", "lang": "uk"},
            {"role": "Patient", "text": "Я не їжу м'ясо з 18 років. І ніколи не хворіла на це раніше.", "lang": "uk"},
            {"role": "Interpreter", "text": "I haven't eaten meat since I was 18. And I never had this problem before.", "lang": "en"},
            {"role": "Doctor", "text": "That's actually really common. B12 depletes slowly — it can take 3 to 5 years for deficiency to show up even after you stop getting it. Your body had reserves, and now they're gone. Also — are you noticing any numbness, tingling, especially in your hands or feet?", "lang": "en"},
            {"role": "Interpreter", "text": "Це насправді дуже поширено. B12 виснажується повільно — може знадобитися 3-5 років щоб дефіцит проявився навіть після того, як ви перестали його отримувати. У вашому організмі були запаси, і тепер вони вичерпані. До речі — чи відчуваєте ви оніміння, поколювання, особливо в руках або ногах?", "lang": "uk"},
            {"role": "Patient", "text": "Так! Мої пальці ніг іноді так поколює ввечері. Я думала, що погано сиджу.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes! My toes tingle sometimes in the evening. I thought I was sitting badly.", "lang": "en"},
            {"role": "Doctor", "text": "That's the nerves. That's the B12. We need to get your levels up quickly — I want to start with B12 injections, once a week for a month, then we switch to daily supplements. The shots are faster.", "lang": "en"},
            {"role": "Interpreter", "text": "Це нерви. Це B12. Нам потрібно швидко підняти ваш рівень — я хочу почати з ін'єкцій B12, раз на тиждень протягом місяця, а потім перейдемо на щоденні добавки. Ін'єкції діють швидше.", "lang": "uk"},
            {"role": "Patient", "text": "Добре. А чи повернеться відчуття в пальцях?", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. And will the feeling come back in my toes?", "lang": "en"},
            {"role": "Doctor", "text": "Most likely yes, over several months. The nerves are slow to heal but they do heal. Let's get started.", "lang": "en"},
            {"role": "Interpreter", "text": "Швидше за все так, протягом кількох місяців. Нерви загоюються повільно, але вони загоюються. Давайте почнемо.", "lang": "uk"}
        ]
    },
    {
        "title": "When rest doesn't help",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "Mykola, your hemoglobin is at 8.2. To put that in perspective, healthy range for a man your age is 13.5 to 17. You're running at about 60% capacity right now.", "lang": "en"},
            {"role": "Interpreter", "text": "Миколо, ваш гемоглобін становить 8,2. Для порівняння, нормальний діапазон для чоловіка вашого віку — від 13,5 до 17. Зараз ви функціонуєте приблизно на 60% від вашої норми.", "lang": "uk"},
            {"role": "Patient", "text": "Тому я так задихаюся? Я піднявся на другий поверх вчора і думав, що помру.", "lang": "uk"},
            {"role": "Interpreter", "text": "Is that why I'm so short of breath? I walked up to the second floor yesterday and thought I was going to die.", "lang": "en"},
            {"role": "Doctor", "text": "Yes, exactly. Your lungs are working fine — it's the delivery system. The blood isn't carrying enough oxygen. Going up stairs at this level, your heart is actually working incredibly hard.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, саме так. Ваші легені працюють нормально — проблема в системі доставки. Кров не переносить достатньо кисню. При такому рівні підйом сходами — це величезне навантаження на ваше серце.", "lang": "uk"},
            {"role": "Patient", "text": "Я лягаю спати рано, намагаюся відпочивати. Чому відпочинок не допомагає?", "lang": "uk"},
            {"role": "Interpreter", "text": "I go to bed early, I try to rest. Why isn't rest helping?", "lang": "en"},
            {"role": "Doctor", "text": "Because it's not a fatigue problem, it's a blood problem. Rest can't fix low hemoglobin. Your cells are literally not getting what they need. Tell me — have you noticed any blood in your stool, or darker stool than usual?", "lang": "en"},
            {"role": "Interpreter", "text": "Тому що це не проблема втоми, це проблема крові. Відпочинок не може виправити низький гемоглобін. Ваші клітини буквально не отримують того, що їм потрібно. Скажіть — чи помічали ви кров у стільці або стілець темніший ніж зазвичай?", "lang": "uk"},
            {"role": "Patient", "text": "Інколи темний. Але я їм багато буряка.", "lang": "uk"},
            {"role": "Interpreter", "text": "Sometimes darker. But I eat a lot of beets.", "lang": "en"},
            {"role": "Doctor", "text": "Beets can do that — good thinking. But with hemoglobin this low in a man your age, I want to rule out internal bleeding. I'd like to refer you for a colonoscopy. Not to alarm you — but I'd rather check and find nothing than miss something.", "lang": "en"},
            {"role": "Interpreter", "text": "Буряк може так робити — правильно думаєте. Але при такому низькому гемоглобіні у чоловіка вашого віку я хочу виключити внутрішню кровотечу. Я хотів би направити вас на колоноскопію. Не хочу вас лякати — але краще перевірити і нічого не знайти, ніж щось пропустити.", "lang": "uk"},
            {"role": "Patient", "text": "Добре. Я довіряю вам. Що мені робити вдома поки?", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. I trust you. What do I do at home in the meantime?", "lang": "en"},
            {"role": "Doctor", "text": "Take it easy on stairs, don't push through the breathlessness — that's your body talking to you. I'll start you on iron supplements today. And drink the juice, not the tea.", "lang": "en"},
            {"role": "Interpreter", "text": "Будьте обережні зі сходами, не примушуйте себе через задишку — це ваш організм з вами говорить. Починаємо препарати заліза сьогодні. І пийте сік, а не чай.", "lang": "uk"}
        ]
    },

    # THYROID
    {
        "title": "I thought it was depression",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "Iryna, I want to talk to you about your thyroid results because I think they explain a lot of what you've been going through.", "lang": "en"},
            {"role": "Interpreter", "text": "Ірино, я хочу поговорити з вами про результати щодо щитовидної залози, тому що думаю, вони пояснюють багато з того, через що ви проходите.", "lang": "uk"},
            {"role": "Patient", "text": "Я слухаю. Моя подруга сказала: іди до лікаря, перестань думати що ти просто лінива. Вона змусила мене записатися.", "lang": "uk"},
            {"role": "Interpreter", "text": "I'm listening. My friend said: go to the doctor, stop thinking you're just being lazy. She pushed me to make the appointment.", "lang": "en"},
            {"role": "Doctor", "text": "Your friend was right to push. Your TSH is at 11 — it should be under 4. This means your thyroid is barely functioning. Everything you've been feeling — the brain fog, the weight gain even when you're not eating more, the cold hands, the low mood — that's not you being lazy. That's your body operating with almost no thyroid hormone.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваша подруга мала рацію, що підштовхнула вас. Ваш ТТГ на рівні 11 — він має бути нижче 4. Це означає, що ваша щитовидна залоза ледь функціонує. Все, що ви відчували — туман у голові, набір ваги навіть коли ви не їсте більше, холодні руки, пригнічений настрій — це не лінощі. Це ваш організм, що працює майже без гормону щитовидної залози.", "lang": "uk"},
            {"role": "Patient", "text": "Боже мій. Я думала що в мене депресія. Я навіть собі докоряла.", "lang": "uk"},
            {"role": "Interpreter", "text": "Oh my god. I thought I had depression. I was even blaming myself.", "lang": "en"},
            {"role": "Doctor", "text": "I know. And I'm sorry you've been carrying that. Hypothyroidism and depression look almost identical from the inside. The difference is — this we can fix with a small daily pill. I want to start you on Levothyroxine.", "lang": "en"},
            {"role": "Interpreter", "text": "Я знаю. І мені шкода, що ви несли це в собі. Гіпотиреоз і депресія зсередини виглядають майже однаково. Різниця в тому — це ми можемо вилікувати маленькою щоденною таблеткою. Я хочу призначити вам Левотироксин.", "lang": "uk"},
            {"role": "Patient", "text": "Це назавжди? Я маю приймати таблетки все своє життя?", "lang": "uk"},
            {"role": "Interpreter", "text": "Is it forever? Do I have to take pills my whole life?", "lang": "en"},
            {"role": "Doctor", "text": "Most likely yes — but that's not a bad thing. Think of it like glasses for your thyroid. One tiny pill in the morning, and your whole system works again. Most people feel dramatically better within six to eight weeks.", "lang": "en"},
            {"role": "Interpreter", "text": "Швидше за все так — але це не погано. Уявіть це як окуляри для вашої щитовидної залози. Одна маленька таблетка зранку, і вся ваша система знову працює. Більшість людей відчувають разючу різницю вже через шість-вісім тижнів.", "lang": "uk"},
            {"role": "Patient", "text": "Мені вже легше на душі від того, що є причина. Дякую.", "lang": "uk"},
            {"role": "Interpreter", "text": "I already feel lighter just knowing there's a reason. Thank you.", "lang": "en"},
            {"role": "Doctor", "text": "That's the best part of my job. We check levels in 6 weeks and adjust the dose if needed. You're going to feel like yourself again.", "lang": "en"},
            {"role": "Interpreter", "text": "Це найкраща частина моєї роботи. Через 6 тижнів перевіряємо рівні і якщо потрібно, коригуємо дозу. Ви знову будете почуватися собою.", "lang": "uk"}
        ]
    },
    {
        "title": "My heart races and I can't explain why",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "Dmytro, I'm looking at your EKG and your resting heart rate is 108. And your TSH is almost zero, which means your thyroid is producing way too much hormone. These are connected.", "lang": "en"},
            {"role": "Interpreter", "text": "Дмитре, я дивлюся на вашу ЕКГ, і ваш пульс у стані спокою — 108. І ваш ТТГ майже нульовий, що означає: ваша щитовидна залоза виробляє надто багато гормону. Це пов'язано.", "lang": "uk"},
            {"role": "Patient", "text": "Я думав, що в мене тривожність. Я навіть почав пити заспокійливі чаї. Нічого не допомагало.", "lang": "uk"},
            {"role": "Interpreter", "text": "I thought I had anxiety. I even started drinking calming teas. Nothing helped.", "lang": "en"},
            {"role": "Doctor", "text": "The teas weren't going to help because the anxiety isn't coming from your mind — it's coming from your thyroid flooding your whole system with hormones. It's like your body is stuck with its foot on the gas pedal. Does your hand shake? Do you feel hot all the time?", "lang": "en"},
            {"role": "Interpreter", "text": "Чаї не могли допомогти, тому що тривожність іде не з голови — вона йде від щитовидної залози, яка заливає весь ваш організм гормонами. Це ніби ваше тіло застрягло з ногою на педалі газу. Тремтить рука? Вам весь час жарко?", "lang": "uk"},
            {"role": "Patient", "text": "Так! Моя дружина відкриває вікно, а мені ще жарко. Вона думала, що я перебільшую.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes! My wife opens the window and I'm still hot. She thought I was exaggerating.", "lang": "en"},
            {"role": "Doctor", "text": "You weren't exaggerating. Everything checks out. I'm going to start you on a medication called Methimazole — it slows down your thyroid's hormone factory. It takes a few weeks to work so I also want to give you a beta-blocker for the racing heart, just to get you comfortable in the meantime.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви не перебільшували. Все сходиться. Я призначу вам препарат під назвою Метимазол — він уповільнює вироблення гормонів щитовидною залозою. Він починає діяти через кілька тижнів, тому я також хочу дати вам бета-блокатор від прискореного серцебиття, просто щоб ви почувалися комфортніше тим часом.", "lang": "uk"},
            {"role": "Patient", "text": "Два ліки одночасно — це безпечно?", "lang": "uk"},
            {"role": "Interpreter", "text": "Two medications at the same time — is that safe?", "lang": "en"},
            {"role": "Doctor", "text": "Absolutely. They do different things. The beta-blocker is a bridge — it protects your heart while the Methimazole does its job. Once your levels normalize, we'll take you off the beta-blocker.", "lang": "en"},
            {"role": "Interpreter", "text": "Абсолютно. Вони виконують різні функції. Бета-блокатор — це місток — він захищає ваше серце поки Метимазол робить свою роботу. Коли ваші показники нормалізуються, ми відмінимо бета-блокатор.", "lang": "uk"}
        ]
    },
    {
        "title": "They found something on ultrasound",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "Halyna, the ultrasound came back and there's a nodule on your thyroid — 1.8 centimeters. I want to be honest with you about what that means and what it doesn't mean.", "lang": "en"},
            {"role": "Interpreter", "text": "Галино, результат УЗД прийшов, і на вашій щитовидній залозі є вузол — 1,8 сантиметра. Я хочу бути з вами чесною щодо того, що це означає і що не означає.", "lang": "uk"},
            {"role": "Patient", "text": "Вузол. Коли я почула це слово по телефону, я не спала три ночі.", "lang": "uk"},
            {"role": "Interpreter", "text": "A nodule. When I heard that word on the phone, I didn't sleep for three nights.", "lang": "en"},
            {"role": "Doctor", "text": "I completely understand. That word is terrifying. So let me give you the real picture: over 95% of thyroid nodules are completely benign. Most people walk around with them and never know. But because of its size and because I want to take care of you properly, I want to do a biopsy.", "lang": "en"},
            {"role": "Interpreter", "text": "Я повністю розумію. Це слово лякає. Тому дозвольте мені дати вам реальну картину: понад 95% вузлів щитовидної залози абсолютно доброякісні. Більшість людей живе з ними і ніколи не знає. Але через його розмір і тому що я хочу належно про вас подбати, я хочу зробити біопсію.", "lang": "uk"},
            {"role": "Patient", "text": "Біопсія звучить страшно. Це операція?", "lang": "uk"},
            {"role": "Interpreter", "text": "Biopsy sounds scary. Is that surgery?", "lang": "en"},
            {"role": "Doctor", "text": "No surgery. We numb the skin on your neck with a little injection — like at the dentist — and then I use an ultrasound to guide a very thin needle to take a tiny sample. You're awake. It takes fifteen minutes. Many people say the numbing injection is the worst part.", "lang": "en"},
            {"role": "Interpreter", "text": "Ніякої операції. Ми знеболюємо шкіру на шиї невеличкою ін'єкцією — як у стоматолога — а потім я за допомогою УЗД направляю дуже тонку голку, щоб взяти крихітний зразок. Ви будете при свідомості. Це займає п'ятнадцять хвилин. Багато людей кажуть, що найгірша частина — це сама знеболювальна ін'єкція.", "lang": "uk"},
            {"role": "Patient", "text": "А якщо результат поганий?", "lang": "uk"},
            {"role": "Interpreter", "text": "And if the result is bad?", "lang": "en"},
            {"role": "Doctor", "text": "Then we deal with it together and we have very good treatment options. But I genuinely believe we're going to find nothing worrying. Let's not borrow trouble we may not have. One step at a time.", "lang": "en"},
            {"role": "Interpreter", "text": "Тоді ми разом з цим впораємося, і у нас є дуже хороші варіанти лікування. Але я щиро вірю, що ми не знайдемо нічого тривожного. Не запозичуймо клопоти, яких може і не бути. Крок за кроком.", "lang": "uk"},
            {"role": "Patient", "text": "Добре. Ви мене заспокоїли. Дякую що не поспішаєте.", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. You calmed me down. Thank you for not rushing.", "lang": "en"},
            {"role": "Doctor", "text": "This is exactly what I'm here for.", "lang": "en"},
            {"role": "Interpreter", "text": "Саме для цього я тут.", "lang": "uk"}
        ]
    },

    # SEIZURES
    {
        "title": "She doesn't remember it happening",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "Larysa, your husband called 911 when it happened. He's here — would it be okay if I ask him to describe what he saw? It would really help me understand.", "lang": "en"},
            {"role": "Interpreter", "text": "Ларисо, ваш чоловік викликав 911 коли це сталося. Він тут — чи можна мені запитати його описати що він бачив? Це дуже допоможе мені зрозуміти.", "lang": "uk"},
            {"role": "Patient", "text": "Так, звісно. Я нічого не пам'ятаю. Для мене це найстрашніше — що я просто зникла.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, of course. I don't remember anything. For me that's the scariest part — that I just disappeared.", "lang": "en"},
            {"role": "Doctor", "text": "That feeling of missing time is one of the most disorienting parts of a seizure. You didn't disappear — your brain had an electrical storm and essentially rebooted. The fact that you came back quickly is actually reassuring. Now — before it happened, did you notice anything? A smell, a strange feeling, a taste?", "lang": "en"},
            {"role": "Interpreter", "text": "Це відчуття втраченого часу — одна з найдезорієнтуючих частин нападу. Ви не зникали — у вашому мозку стався електричний шторм і він по суті перезавантажився. Те, що ви швидко прийшли до тями — насправді заспокоює. Тепер — до того як це сталося, чи помічали ви щось? Запах, дивне відчуття, смак?", "lang": "uk"},
            {"role": "Patient", "text": "Було таке відчуття... як ностальгія, але дуже сильна і без причини. Потім запах паленого. Потім нічого.", "lang": "uk"},
            {"role": "Interpreter", "text": "There was a feeling... like nostalgia, but very strong and for no reason. Then a smell of burning. Then nothing.", "lang": "en"},
            {"role": "Doctor", "text": "That nostalgia feeling — that's called a déjà vu aura, and it's actually very specific. It means the seizure started in the temporal lobe of your brain, which is the area that handles memory and emotion. This gives us a lot of information. This was not random.", "lang": "en"},
            {"role": "Interpreter", "text": "Те відчуття ностальгії — воно називається аура дежавю, і воно дуже специфічне. Це означає, що напад почався у скроневій частці вашого мозку — ділянці, яка відповідає за пам'ять та емоції. Це дає нам багато інформації. Це було не випадково.", "lang": "uk"},
            {"role": "Patient", "text": "Це лікується? Чи я тепер небезпечна для себе?", "lang": "uk"},
            {"role": "Interpreter", "text": "Is it treatable? Am I a danger to myself now?", "lang": "en"},
            {"role": "Doctor", "text": "Most temporal lobe epilepsy responds very well to medication. And you are not dangerous to yourself — we just need to take some precautions until we get this under control. No swimming alone, no baths, careful on stairs. But I want you to hear this: people with epilepsy live full, complete lives.", "lang": "en"},
            {"role": "Interpreter", "text": "Більшість випадків скроневої епілепсії дуже добре реагує на ліки. І ви не небезпечні для себе — нам просто потрібно вжити деяких заходів обережності поки ми не взяли це під контроль. Не плавайте самостійно, не приймайте ванну наодинці, будьте обережні на сходах. Але я хочу, щоб ви почули це: люди з епілепсією живуть повноцінним, насиченим життям.", "lang": "uk"},
            {"role": "Patient", "text": "Дякую що скажили це останнє. Мені це було потрібно почути.", "lang": "uk"},
            {"role": "Interpreter", "text": "Thank you for saying that last part. I needed to hear it.", "lang": "en"}
        ]
    },
    {
        "title": "The medication makes me someone else",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "Vasyl, you told the nurse you want to stop your Keppra. I'm not going to dismiss that — can you tell me what's been happening?", "lang": "en"},
            {"role": "Interpreter", "text": "Василю, ви сказали медсестрі, що хочете припинити прийом Кеппри. Я не збираюся відмахнутися від цього — розкажіть мені що відбувається.", "lang": "uk"},
            {"role": "Patient", "text": "Я накричав на свою дружину. Я б ніколи так не зробив. Я накричав на дітей. Я — не такий. Я не хочу бути таким.", "lang": "uk"},
            {"role": "Interpreter", "text": "I screamed at my wife. I would never do that. I screamed at the kids. I'm not like that. I don't want to be like that.", "lang": "en"},
            {"role": "Doctor", "text": "Vasyl, thank you for telling me this. What you're describing is a real, documented side effect of Keppra — we actually call it 'Keppra rage' among ourselves. It's not who you are. The drug is doing this to you, not some hidden part of your character. Do you hear what I'm saying?", "lang": "en"},
            {"role": "Interpreter", "text": "Василю, дякую що розповіли мені це. Те, що ви описуєте — реальний, задокументований побічний ефект Кеппри — ми навіть називаємо це між собою 'лють Кеппри'. Це не те, хто ви є. Це ліки роблять так з вами, а не якась прихована частина вашого характеру. Ви чуєте що я кажу?", "lang": "uk"},
            {"role": "Patient", "text": "Але що ж мені робити? Якщо я кину ліки і буду мати напад — це теж небезпечно для сім'ї.", "lang": "uk"},
            {"role": "Interpreter", "text": "But what do I do? If I stop the medication and have a seizure — that's also dangerous for the family.", "lang": "en"},
            {"role": "Doctor", "text": "You're thinking about this exactly right and I respect that. Here's the answer: we don't stop — we switch. There's a medication called Lamictal that controls seizures just as well without the mood effects for most people. We'll taper you off Keppra slowly while bringing Lamictal up.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви думаєте про це саме правильно, і я це поважаю. Ось відповідь: ми не зупиняємось — ми переходимо. Є препарат під назвою Ламіктал, який контролює напади так само добре, але без впливу на настрій у більшості людей. Ми будемо повільно знижувати Кеппру, одночасно вводячи Ламіктал.", "lang": "uk"},
            {"role": "Patient", "text": "І ваша дружина — вона знає як це важко для сім'ї?", "lang": "uk"},
            {"role": "Interpreter", "text": "And your wife — does she know how hard this is for the family?", "lang": "en"},
            {"role": "Doctor", "text": "Would it help if I spoke with her together with you today, to explain that this was the medication and not you? Sometimes families need to hear it from the doctor.", "lang": "en"},
            {"role": "Interpreter", "text": "Чи допомогло б якщо б я поговорила з нею разом з вами сьогодні, щоб пояснити, що це були ліки, а не ви? Іноді сім'ям потрібно почути це від лікаря.", "lang": "uk"},
            {"role": "Patient", "text": "Так. Будь ласка. Це б багато значило.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes. Please. That would mean a lot.", "lang": "en"}
        ]
    },
    {
        "title": "She can't drive and her world fell apart",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "Olena, I need to tell you something difficult today. The law requires me to report your seizure to the DMV, which means your license will be suspended until you've been seizure-free for six months.", "lang": "en"},
            {"role": "Interpreter", "text": "Олено, сьогодні мені потрібно сказати вам щось важке. Закон зобов'язує мене повідомити про ваш напад до Департаменту автотранспорту, що означає: ваше посвідчення буде призупинено до того, як ви будете без нападів протягом шести місяців.", "lang": "uk"},
            {"role": "Patient", "text": "Шість місяців... мої діти. Я відвожу їх до школи. Мій чоловік їде о п'ятій ранку на роботу. Хто... хто тепер відвезе їх?", "lang": "uk"},
            {"role": "Interpreter", "text": "Six months... my children. I drive them to school. My husband leaves for work at five in the morning. Who... who takes them now?", "lang": "en"},
            {"role": "Doctor", "text": "I know. I know how much this disrupts everything. And I'm sorry I can't make this easier. Tell me — what's the school situation? How far is it?", "lang": "en"},
            {"role": "Interpreter", "text": "Я знаю. Я знаю наскільки це все порушує. І мені шкода що я не можу полегшити це. Розкажіть — яка ситуація зі школою? Як далеко вона?", "lang": "uk"},
            {"role": "Patient", "text": "Три кілометри. Але немає автобуса в нашому районі. Чи можна мені їздити тільки дітей відвозити? Я дуже обережна.", "lang": "uk"},
            {"role": "Interpreter", "text": "Three kilometers. But there's no bus in our neighborhood. Can I drive just to take the kids? I'm very careful.", "lang": "en"},
            {"role": "Doctor", "text": "I have to be honest with you: legally, no. And I have to tell you why — not to punish you, but because I need you to understand. When a seizure comes, there's no warning. You can't be careful. You would have no control. If you're driving, it could kill your children or someone else's. You know that, don't you?", "lang": "en"},
            {"role": "Interpreter", "text": "Я маю бути з вами чесною: юридично, ні. І я повинна сказати вам чому — не щоб покарати вас, а тому що мені потрібно щоб ви зрозуміли. Коли напад наближається, немає попереджень. Ви не можете бути обережною. У вас не буде контролю. Якщо ви за кермом, це може вбити ваших дітей або чиїхось інших. Ви це розумієте?", "lang": "uk"},
            {"role": "Patient", "text": "Так. Я розумію. Мені просто... важко. Вибачте що попросила.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes. I understand. I just... it's hard. I'm sorry I asked.", "lang": "en"},
            {"role": "Doctor", "text": "Please don't apologize. It's a reasonable question from a mother. Let's spend a few minutes problem-solving together — neighbors, carpools, the school office sometimes knows families going the same way. I won't just leave you with a problem.", "lang": "en"},
            {"role": "Interpreter", "text": "Будь ласка, не вибачайтеся. Це розумне питання від матері. Давайте разом витратимо кілька хвилин на вирішення проблеми — сусіди, спільні поїздки, шкільна канцелярія іноді знає сім'ї, що їдуть у тому ж напрямку. Я не залишу вас сам на сам з проблемою.", "lang": "uk"}
        ]
    },

    # GENERAL WELLNESS
    {
        "title": "He came in for a checkup and doesn't know what to ask",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "Serhiy, your results are honestly pretty solid for someone your age. But you look like something's on your mind. What made you come in today?", "lang": "en"},
            {"role": "Interpreter", "text": "Сергію, ваші результати чесно кажучи досить хороші для людини вашого віку. Але ви виглядаєте так, ніби щось вас турбує. Що змусило вас прийти сьогодні?", "lang": "uk"},
            {"role": "Patient", "text": "Мій брат. Йому 52, і він мав серцевий напад минулого місяця. Він завжди був здоровішим за мене. Я злякався.", "lang": "uk"},
            {"role": "Interpreter", "text": "My brother. He's 52 and he had a heart attack last month. He was always healthier than me. I got scared.", "lang": "en"},
            {"role": "Doctor", "text": "I'm sorry about your brother. And I'm glad that fear brought you here — that's your instinct working correctly. With a sibling who had a cardiac event, your risk does go up. That's not a reason to panic, it's a reason to be smart. Are you a smoker?", "lang": "en"},
            {"role": "Interpreter", "text": "Мені шкода щодо вашого брата. І я рада, що цей страх привів вас сюди — це ваш інстинкт спрацював правильно. Коли у брата або сестри стався серцевий випадок, ваш ризик зростає. Це не привід для паніки — це привід бути розумним. Ви курите?", "lang": "uk"},
            {"role": "Patient", "text": "Я кинув сім років тому. До цього курив двадцять років.", "lang": "uk"},
            {"role": "Interpreter", "text": "I quit seven years ago. I smoked for twenty years before that.", "lang": "en"},
            {"role": "Doctor", "text": "Quitting was one of the best things you could have done. After seven years your risk has dropped dramatically. I want to check your cholesterol in detail today and also do a quick test to see how well your arteries are moving blood. Non-invasive, no needles — just a cuff on your arm and ankle.", "lang": "en"},
            {"role": "Interpreter", "text": "Кинути курити — одне з найкращих рішень, які ви могли прийняти. Після семи років ваш ризик різко знизився. Я хочу сьогодні детально перевірити ваш холестерин і також зробити невеличкий тест, щоб подивитися наскільки добре ваші артерії рухають кров. Неінвазивний, без голок — просто манжета на руці і щиколотці.", "lang": "uk"},
            {"role": "Patient", "text": "Дякую що не кажете просто 'ви здорові, до побачення'.", "lang": "uk"},
            {"role": "Interpreter", "text": "Thank you for not just saying 'you're healthy, goodbye'.", "lang": "en"},
            {"role": "Doctor", "text": "You came in scared and wanting answers. You deserve answers.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви прийшли наляканим і хотіли відповідей. Ви заслуговуєте на відповіді.", "lang": "uk"}
        ]
    },
    {
        "title": "She hasn't slept properly in two years",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "Tetiana, you mentioned sleep on your intake form. Tell me more — what does a bad night look like for you?", "lang": "en"},
            {"role": "Interpreter", "text": "Тетяно, ви згадали сон у вашій анкеті. Розкажіть більше — як виглядає для вас погана ніч?", "lang": "uk"},
            {"role": "Patient", "text": "Я засинаю добре. Але прокидаюся о третій чи четвертій і лежу і думаю. Думаю про все. Про дітей, про гроші, про минуле. Просто не можу зупинити голову.", "lang": "uk"},
            {"role": "Interpreter", "text": "I fall asleep fine. But I wake up at three or four and lie there and think. I think about everything. The kids, money, the past. I just can't stop my head.", "lang": "en"},
            {"role": "Doctor", "text": "Early morning waking with a racing mind — that's a really distinct pattern and it tells me something specific. That's not just 'stress'. That's often how anxiety manifests physically. Your body is on alert. How long has this been going on?", "lang": "en"},
            {"role": "Interpreter", "text": "Раннє ранкове пробудження з активним розумом — це дуже характерна картина і вона говорить мені щось конкретне. Це не просто 'стрес'. Так часто фізично проявляється тривожність. Ваш організм в стані готовності. Як давно це відбувається?", "lang": "uk"},
            {"role": "Patient", "text": "Два роки. Після того як ми приїхали сюди. Ми переїхали з України.", "lang": "uk"},
            {"role": "Interpreter", "text": "Two years. After we came here. We moved from Ukraine.", "lang": "en"},
            {"role": "Doctor", "text": "I hear you. That's not just a move — that's a complete upheaval of every familiar thing. I want to ask something gently: do you have anyone here you can talk to? A community, a counselor, family?", "lang": "en"},
            {"role": "Interpreter", "text": "Я вас чую. Це не просто переїзд — це повна руйнація всього звичного. Я хочу обережно запитати: чи є у вас тут хтось, з ким ви можете поговорити? Спільнота, консультант, родина?", "lang": "uk"},
            {"role": "Patient", "text": "Є сусідка-українка. Більше нікого. Я не хочу обтяжувати дітей.", "lang": "uk"},
            {"role": "Interpreter", "text": "There's a Ukrainian neighbor. No one else. I don't want to burden my children.", "lang": "en"},
            {"role": "Doctor", "text": "You are not a burden. But let me offer you something concrete: we have a group that meets weekly for Ukrainian and Russian-speaking newcomers — run by a Ukrainian-speaking therapist. Many of my patients have found it life-changing. Can I give you the information?", "lang": "en"},
            {"role": "Interpreter", "text": "Ви не є тягарем. Але дозвольте запропонувати вам щось конкретне: у нас є група, яка збирається щотижня для україно- і російськомовних переселенців — нею керує терапевт, що говорить українською. Багато моїх пацієнтів вважають це переломним моментом. Чи можна мені дати вам інформацію?", "lang": "uk"},
            {"role": "Patient", "text": "Так. Будь ласка. Я навіть не знала що таке існує.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes. Please. I didn't even know something like that existed.", "lang": "en"}
        ]
    },
    {
        "title": "He thinks he's too young to worry",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "Andriy, you're 34. Most people your age don't come in for checkups. What made you think to come?", "lang": "en"},
            {"role": "Interpreter", "text": "Андрію, вам 34. Більшість людей вашого віку не приходять на профілактичний огляд. Що спонукало вас прийти?", "lang": "uk"},
            {"role": "Patient", "text": "Моя мама. Вона сказала, якщо ти не підеш до лікаря, я перестану тебе годувати. Вона жартувала. Напевно.", "lang": "uk"},
            {"role": "Interpreter", "text": "My mom. She said if you don't go to the doctor, I'll stop feeding you. She was joking. Probably.", "lang": "en"},
            {"role": "Doctor", "text": "Ha — smart mom. Well, while you're here, let me check a few things. Your blood pressure is 138 over 88. That's on the high side for a 34-year-old. Do you know if anyone in your family has hypertension?", "lang": "en"},
            {"role": "Interpreter", "text": "Ха — розумна мама. Що ж, раз ви вже тут, дозвольте перевірити кілька речей. Ваш артеріальний тиск 138 на 88. Це зависоко для 34-річного. Чи знаєте ви, чи є у когось у вашій сім'ї гіпертонія?", "lang": "uk"},
            {"role": "Patient", "text": "Тато і дід. Але їм вже по 60. Зі мною це не може статися в 34, правда?", "lang": "uk"},
            {"role": "Interpreter", "text": "Dad and grandfather. But they're in their 60s. This can't happen to me at 34, right?", "lang": "en"},
            {"role": "Doctor", "text": "It absolutely can happen at 34 — actually this is exactly the right time to catch it, because right now we can manage it with lifestyle alone. No medication needed yet. But if we ignore it for ten years, that's ten years of pressure on your heart, your kidneys, your brain.", "lang": "en"},
            {"role": "Interpreter", "text": "Це абсолютно може статися в 34 — і насправді це саме правильний час щоб виявити це, тому що зараз ми можемо впоратися з цим лише зміною способу життя. Поки що ніяких ліків. Але якщо ми ігноруватимемо це десять років, це десять років тиску на ваше серце, нирки, мозок.", "lang": "uk"},
            {"role": "Patient", "text": "Мені треба дієту? Я їм нормально. Я не їжу фаст-фуд кожен день.", "lang": "uk"},
            {"role": "Interpreter", "text": "Do I need a diet? I eat normally. I don't eat fast food every day.", "lang": "en"},
            {"role": "Doctor", "text": "Tell me about sodium. Do you add salt at the table? Eat a lot of pickled things, canned soup?", "lang": "en"},
            {"role": "Interpreter", "text": "Розкажіть мені про сіль. Чи підсолюєте ви їжу за столом? Їсте багато маринованого, консервованих супів?", "lang": "uk"},
            {"role": "Patient", "text": "Солоні огірки щодня. Це в нас традиція. Мама маринує.", "lang": "uk"},
            {"role": "Interpreter", "text": "Pickles every day. It's our tradition. Mom pickles them.", "lang": "en"},
            {"role": "Doctor", "text": "There might be our answer. Pickles are extraordinarily high in sodium — every pickle you eat is like squeezing a tiny blood pressure spike. We don't have to eliminate them, but let's try cutting back significantly for three months and see what happens to your numbers.", "lang": "en"},
            {"role": "Interpreter", "text": "Можливо ось наша відповідь. Мариновані огірки надзвичайно багаті на натрій — кожен огірок, який ви їсте, — це як невеликий стрибок артеріального тиску. Ми не мусимо їх повністю прибирати, але давайте спробуємо значно скоротити їх протягом трьох місяців і подивимося що станеться з вашими показниками.", "lang": "uk"},
            {"role": "Patient", "text": "Мамі не кажіть. Вона образиться.", "lang": "uk"},
            {"role": "Interpreter", "text": "Don't tell my mom. She'll be offended.", "lang": "en"},
            {"role": "Doctor", "text": "Our secret.", "lang": "en"},
            {"role": "Interpreter", "text": "Наш секрет.", "lang": "uk"}
        ]
    },

    # HEART ISSUES
    {
        "title": "He walked off chest pain for six months",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "Viktor, I want to understand what you mean when you say 'pressure in the chest'. Can you show me — point to where it is?", "lang": "en"},
            {"role": "Interpreter", "text": "Вікторе, я хочу зрозуміти що ви маєте на увазі коли кажете 'тиск у грудях'. Покажіть мені — вкажіть де це?", "lang": "uk"},
            {"role": "Patient", "text": "Тут. Посередині. Як хтось поставив коліно на груди. Воно приходить коли я поспішаю або несу щось важке. Я думав, що це м'язи.", "lang": "uk"},
            {"role": "Interpreter", "text": "Here. In the middle. Like someone put a knee on my chest. It comes when I hurry or carry something heavy. I thought it was my muscles.", "lang": "en"},
            {"role": "Doctor", "text": "How long has this been happening?", "lang": "en"},
            {"role": "Interpreter", "text": "Як довго це відбувається?", "lang": "uk"},
            {"role": "Patient", "text": "Місяців шість. Може більше. Я не хотів турбувати дружину.", "lang": "uk"},
            {"role": "Interpreter", "text": "Six months. Maybe more. I didn't want to worry my wife.", "lang": "en"},
            {"role": "Doctor", "text": "Viktor, I need you to hear this calmly: what you're describing — pressure in the center of your chest that comes with exertion and goes away with rest — is angina until proven otherwise. That means your heart is asking for more blood than it's getting during effort. This is serious, and I'm glad you're here today and not later.", "lang": "en"},
            {"role": "Interpreter", "text": "Вікторе, мені потрібно щоб ви спокійно почули це: те що ви описуєте — тиск в центрі грудей, що приходить при навантаженні і зникає при відпочинку — це стенокардія поки не доведено інше. Це означає, що ваше серце просить більше крові ніж отримує під час зусилля. Це серйозно, і я рада, що ви тут сьогодні, а не пізніше.", "lang": "uk"},
            {"role": "Patient", "text": "Стенокардія. Це і є серцевий напад?", "lang": "uk"},
            {"role": "Interpreter", "text": "Angina. Is that a heart attack?", "lang": "en"},
            {"role": "Doctor", "text": "No — but it can be a warning sign that a heart attack is possible if we don't act. Think of it as your heart waving a flag. We're going to do an EKG right now in this room, and then I want you to see a cardiologist this week — not next month, this week.", "lang": "en"},
            {"role": "Interpreter", "text": "Ні — але це може бути попереджувальним сигналом, що серцевий напад можливий якщо ми не будемо діяти. Думайте про це як про те, що ваше серце махає прапором. Ми зробимо ЕКГ прямо зараз у цій кімнаті, а потім я хочу щоб ви відвідали кардіолога цього тижня — не наступного місяця, цього тижня.", "lang": "uk"},
            {"role": "Patient", "text": "Добре. Можете сказати дружині? Вона більше розуміє ці речі. Я не знаю як їй пояснити.", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. Can you tell my wife? She understands these things better. I don't know how to explain it to her.", "lang": "en"},
            {"role": "Doctor", "text": "Of course. I'll ask her to step in after the EKG. You did the right thing by coming today, Viktor. I mean that.", "lang": "en"},
            {"role": "Interpreter", "text": "Звичайно. Я попрошу її зайти після ЕКГ. Ви зробили правильне, що прийшли сьогодні, Вікторе. Я це серйозно.", "lang": "uk"}
        ]
    },
    {
        "title": "She's afraid of the blood thinner",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "Liudmyla, the Holter monitor caught what we were looking for — you're going into atrial fibrillation. It happened fourteen times over 24 hours.", "lang": "en"},
            {"role": "Interpreter", "text": "Людмило, холтерівський монітор зафіксував те, що ми шукали — у вас виникає фібриляція передсердь. Це відбулося чотирнадцять разів за 24 години.", "lang": "uk"},
            {"role": "Patient", "text": "Чотирнадцять разів. Боже мій. Я це відчувала? Воно б'ється так... нерівно. Це відбувається увечері зазвичай.", "lang": "uk"},
            {"role": "Interpreter", "text": "Fourteen times. Oh my God. Did I feel it? It beats so... unevenly. It usually happens in the evening.", "lang": "en"},
            {"role": "Doctor", "text": "Yes, many people feel it as a flutter or a missed beat. The evening timing is common — the vagus nerve, which calms your heart, is more active then. Now, here's the important part I need to explain carefully: AFib creates a situation where blood pools in your heart and can form clots. A clot that travels to the brain is a stroke.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, багато людей відчувають це як тріпотіння або пропущений удар. Вечірня поява — поширене явище — блукаючий нерв, який заспокоює серце, тоді більш активний. Тепер важлива частина, яку мені потрібно ретельно пояснити: фібриляція передсердь створює ситуацію, коли кров застоюється в серці і може утворювати тромби. Тромб, що потрапляє в мозок, — це інсульт.", "lang": "uk"},
            {"role": "Patient", "text": "Тому ви хочете дати мені розріджувач крові. Але я читала що від нього можна кровоточити до смерті.", "lang": "uk"},
            {"role": "Interpreter", "text": "That's why you want to give me a blood thinner. But I read that you can bleed to death from it.", "lang": "en"},
            {"role": "Doctor", "text": "That fear is real and I take it seriously. Can I give you the full picture though? With uncontrolled AFib and no anticoagulation, your annual stroke risk is around 4 to 5 percent. With Eliquis, we bring that down to under 1 percent. And the modern anticoagulants are much safer than the old Warfarin — the bleeding risk is real but it's manageable.", "lang": "en"},
            {"role": "Interpreter", "text": "Цей страх реальний і я сприймаю його серйозно. Але чи можу я дати вам повну картину? При неконтрольованій фібриляції передсердь без антикоагулянтів ваш річний ризик інсульту становить близько 4-5 відсотків. З Еліквісом ми знижуємо його до менш ніж 1 відсотка. А сучасні антикоагулянти набагато безпечніші ніж старий Варфарин — ризик кровотечі реальний, але ним можна управляти.", "lang": "uk"},
            {"role": "Patient", "text": "Чотири відсотки на рік... Якщо я проживу ще двадцять років, це майже напевно стане інсульт.", "lang": "uk"},
            {"role": "Interpreter", "text": "Four percent a year... If I live another twenty years, that's almost certainly a stroke.", "lang": "en"},
            {"role": "Doctor", "text": "Exactly. You did that math yourself and you did it right. The pill I'm offering you protects the next twenty years. I want you to have them all, as fully as possible.", "lang": "en"},
            {"role": "Interpreter", "text": "Точно. Ви самі зробили це підрахування, і зробили правильно. Таблетка, яку я вам пропоную, захищає наступні двадцять років. Я хочу щоб ви прожили їх усі, якнайповніше.", "lang": "uk"},
            {"role": "Patient", "text": "Добре. Ви переконали мене. Давайте спробуємо.", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. You convinced me. Let's try.", "lang": "en"}
        ]
    },
    {
        "title": "Too much fluid, not enough heart",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "Petro, you've gained 9 pounds since your visit three weeks ago. Nine pounds in three weeks. That's fluid. Your body is holding water because your heart isn't moving it.", "lang": "en"},
            {"role": "Interpreter", "text": "Петре, ви набрали 9 фунтів з моменту вашого візиту три тижні тому. Дев'ять фунтів за три тижні. Це рідина. Ваш організм затримує воду, тому що серце не перекачує її.", "lang": "uk"},
            {"role": "Patient", "text": "Мої черевики не налазять. Думав, просто ноги набрякли від спеки.", "lang": "uk"},
            {"role": "Interpreter", "text": "My shoes don't fit. I thought my legs were just swollen from the heat.", "lang": "en"},
            {"role": "Doctor", "text": "How many pillows do you sleep on?", "lang": "en"},
            {"role": "Interpreter", "text": "На скількох подушках ви спите?", "lang": "uk"},
            {"role": "Patient", "text": "Трьох. А що? Я завжди так спав.", "lang": "uk"},
            {"role": "Interpreter", "text": "Three. Why? I always slept like that.", "lang": "en"},
            {"role": "Doctor", "text": "Actually that's something that changed. When fluid builds up around the heart and lungs, lying flat makes it worse because gravity redistributes it. Your body learned to prop itself up to breathe. Three pillows is your body's solution to a problem you didn't know you had.", "lang": "en"},
            {"role": "Interpreter", "text": "Насправді це щось що змінилося. Коли рідина накопичується навколо серця та легенів, горизонтальне положення погіршує ситуацію тому що гравітація її перерозподіляє. Ваш організм навчився підпирати себе щоб дихати. Три подушки — це рішення вашого тіла для проблеми, про яку ви не знали.", "lang": "uk"},
            {"role": "Patient", "text": "Тобто це серйозно. Більш серйозно ніж я думав.", "lang": "uk"},
            {"role": "Interpreter", "text": "So this is serious. More serious than I thought.", "lang": "en"},
            {"role": "Doctor", "text": "Yes. But it's manageable if we act now. I want to increase your diuretic to help your kidneys pull that fluid out. And — this is important — I need you to weigh yourself every morning. If you gain more than two pounds overnight, you call us that day. Not tomorrow. That day.", "lang": "en"},
            {"role": "Interpreter", "text": "Так. Але з цим можна впоратися якщо ми діємо зараз. Я хочу збільшити ваш сечогінний препарат, щоб допомогти ниркам вивести цю рідину. І — це важливо — мені потрібно щоб ви зважувалися щоранку. Якщо ви наберете більше двох фунтів за ніч — дзвоніть нам того ж дня. Не завтра. Того ж дня.", "lang": "uk"},
            {"role": "Patient", "text": "Я ніколи не мав ваги вдома.", "lang": "uk"},
            {"role": "Interpreter", "text": "I've never owned a scale.", "lang": "en"},
            {"role": "Doctor", "text": "That changes today. There's a pharmacy two blocks from here — they usually have basic scales for ten dollars. This is now one of the most important tools you own. Your weight is a window into what your heart is doing.", "lang": "en"},
            {"role": "Interpreter", "text": "Це змінюється сьогодні. За два квартали звідси є аптека — там зазвичай є прості ваги за десять доларів. Тепер це один з найважливіших інструментів, які у вас є. Ваша вага — це вікно в те, що робить ваше серце.", "lang": "uk"}
        ]
    },

    # DIABETES
    {
        "title": "She's been managing alone for years",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "Svitlana, your A1C is 10.2. I want to be honest with you — this is high enough that I'm worried about your kidneys and your eyes. But before we talk numbers, help me understand: what does a typical day look like for you with managing this?", "lang": "en"},
            {"role": "Interpreter", "text": "Світлано, ваш глікований гемоглобін 10,2. Я хочу бути з вами чесною — це достатньо високо щоб мене турбували ваші нирки та очі. Але перш ніж говорити про цифри, допоможіть мені зрозуміти: як виглядає для вас звичайний день з управлінням цим?", "lang": "uk"},
            {"role": "Patient", "text": "Я намагаюся. Я перевіряю цукор... іноді. Коли є час. Я працюю дві роботи. Ввечері — занадто втомилася щоб готувати правильно. Я знаю що роблю погано.", "lang": "uk"},
            {"role": "Interpreter", "text": "I try. I check my sugar... sometimes. When there's time. I work two jobs. In the evening I'm too tired to cook properly. I know I'm doing badly.", "lang": "en"},
            {"role": "Doctor", "text": "Stop right there. You are not 'doing badly'. You are doing what you can with the resources you have. Managing diabetes is practically a part-time job and you already have two real jobs. I don't want blame here — I want solutions that actually fit your life.", "lang": "en"},
            {"role": "Interpreter", "text": "Стоп. Ви не 'робите погано'. Ви робите те, що можете з тими ресурсами, які у вас є. Управління діабетом — це фактично робота на пів ставки, а у вас вже є дві реальні роботи. Я не хочу тут докорів — я хочу рішень, які дійсно відповідають вашому житті.", "lang": "uk"},
            {"role": "Patient", "text": "Це зовсім інший підхід. Зазвичай лікарі говорять мені що я роблю не так.", "lang": "uk"},
            {"role": "Interpreter", "text": "This is a very different approach. Doctors usually tell me what I'm doing wrong.", "lang": "en"},
            {"role": "Doctor", "text": "What gets done is what's realistic. Tell me — on a tired evening, what do you actually eat?", "lang": "en"},
            {"role": "Interpreter", "text": "Те, що виконується — це те, що реалістично. Скажіть мені — у втомлений вечір, що ви насправді їсте?", "lang": "uk"},
            {"role": "Patient", "text": "Хліб. Може яйця. Іноді залишки. Іноді нічого.", "lang": "uk"},
            {"role": "Interpreter", "text": "Bread. Maybe eggs. Sometimes leftovers. Sometimes nothing.", "lang": "en"},
            {"role": "Doctor", "text": "Okay. Let's work with that. Eggs are actually perfect for diabetes — protein, almost no carbs. Greek yogurt is another one. I want to connect you with our diabetes dietitian — she works evenings twice a week specifically for working patients. She'll build something around your actual life, not a fantasy version.", "lang": "en"},
            {"role": "Interpreter", "text": "Добре. Попрацюємо з цим. Яйця насправді чудові для діабету — білок, майже без вуглеводів. Грецький йогурт — ще один варіант. Я хочу познайомити вас з нашим дієтологом з діабету — вона працює ввечері двічі на тиждень спеціально для пацієнтів, що працюють. Вона побудує щось навколо вашого реального життя, а не ідеальної версії.", "lang": "uk"},
            {"role": "Patient", "text": "Це безкоштовно? Я не можу дозволити собі зайві витрати.", "lang": "uk"},
            {"role": "Interpreter", "text": "Is that free? I can't afford extra costs.", "lang": "en"},
            {"role": "Doctor", "text": "It's covered by your insurance. Zero out of pocket. And let me be very direct with you: treating complications of uncontrolled diabetes is enormously expensive. Preventing them is free. This is the investment.", "lang": "en"},
            {"role": "Interpreter", "text": "Це покривається вашою страховкою. Жодних витрат з вашої кишені. І дозвольте мені бути дуже прямою: лікування ускладнень неконтрольованого діабету надзвичайно дороге. Їх профілактика — безкоштовна. Це і є інвестиція.", "lang": "uk"}
        ]
    },
    {
        "title": "He's scared of going low at night",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "Mykhailo, your continuous glucose monitor data is really interesting. You have good control during the day but you're going low — below 60 — almost every night around 2 am. Are you waking up with night sweats or heart pounding?", "lang": "en"},
            {"role": "Interpreter", "text": "Михайле, дані вашого апарату безперервного моніторингу глюкози дуже цікаві. Вдень у вас хороший контроль, але вночі — майже щоночі близько 2 години — ви опускаєтеся нижче 60. Чи прокидаєтесь ви від нічної пітливості або серцебиття?", "lang": "uk"},
            {"role": "Patient", "text": "Так. Іноді прокидаюся весь мокрий. Іноді — ні. Іноді я просто не прокидаюся. І це мене лякає найбільше — що я не прокинуся.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes. Sometimes I wake up soaking wet. Sometimes not. Sometimes I just don't wake up. And that scares me the most — that I won't wake up.", "lang": "en"},
            {"role": "Doctor", "text": "That fear is very reasonable and I want to take it seriously. Nocturnal hypoglycemia is one of the things I worry about most with insulin. The fact that you're sometimes not waking up means your body's alarm system — which should shake you awake — is starting to miss. We call this hypoglycemia unawareness.", "lang": "en"},
            {"role": "Interpreter", "text": "Цей страх цілком обґрунтований і я хочу поставитися до нього серйозно. Нічна гіпоглікемія — одна з речей, що мене найбільше турбує при інсуліні. Те, що ви іноді не прокидаєтесь, означає, що система тривоги вашого тіла — яка має розбудити вас — починає не спрацьовувати. Ми називаємо це нечутливістю до гіпоглікемії.", "lang": "uk"},
            {"role": "Patient", "text": "Нечутливість. Значить моє тіло перестає відчувати небезпеку?", "lang": "uk"},
            {"role": "Interpreter", "text": "Unawareness. So my body is losing the ability to feel danger?", "lang": "en"},
            {"role": "Doctor", "text": "Exactly. And that develops when you have too many lows too often. The good news: it's reversible if we prevent the lows. I want to reduce your bedtime insulin dose significantly — and I want to set your CGM alarm at 80 mg/dL going down, not 70. We want to catch it before the cliff, not on the way down.", "lang": "en"},
            {"role": "Interpreter", "text": "Точно. І вона розвивається коли у вас занадто багато падінь занадто часто. Хороша новина: це оборотно якщо ми запобіжимо падінням. Я хочу значно зменшити вашу дозу інсуліну перед сном — і я хочу встановити сигнал тривоги вашого CGM на 80 мг/дл при зниженні, а не на 70. Ми хочемо зловити це до урвища, а не вже на шляху вниз.", "lang": "uk"},
            {"role": "Patient", "text": "Але якщо я зменшу інсулін, мій цукор вночі злетить. Я зіпсую свій A1C.", "lang": "uk"},
            {"role": "Interpreter", "text": "But if I reduce insulin, my sugar will spike overnight. I'll ruin my A1C.", "lang": "en"},
            {"role": "Doctor", "text": "Let me reframe that for you: a slightly higher A1C means you'll live longer to work on it. An undetected nighttime low can be fatal. An A1C of 7.5 that you're alive for beats an A1C of 6.8 that you didn't wake up from.", "lang": "en"},
            {"role": "Interpreter", "text": "Дозвольте мені переформулювати це для вас: трохи вищий глікований гемоглобін означає що ви будете жити довше щоб над ним працювати. Невиявлене нічне падіння може бути смертельним. Гемоглобін 7,5 при якому ви живі кращий за 6,8 від якого ви не прокинулися.", "lang": "uk"},
            {"role": "Patient", "text": "Ви маєте рацію. Я не думав про це так.", "lang": "uk"},
            {"role": "Interpreter", "text": "You're right. I hadn't thought about it that way.", "lang": "en"}
        ]
    },
    {
        "title": "His feet are telling him something he ignored",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "Vasyl, I need you to take off your shoes and socks. I do this with every diabetic patient, every visit. Is that okay?", "lang": "en"},
            {"role": "Interpreter", "text": "Василю, мені потрібно щоб ви зняли взуття та шкарпетки. Я роблю це з кожним пацієнтом з діабетом, на кожному візиті. Це добре?", "lang": "uk"},
            {"role": "Patient", "text": "Добре. Але там є... є ранка на п'яті. Вже якийсь час. Я забув згадати.", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay. But there's... there's a sore on my heel. For some time already. I forgot to mention it.", "lang": "en"},
            {"role": "Doctor", "text": "How long is 'some time'?", "lang": "en"},
            {"role": "Interpreter", "text": "Як довго — це 'якийсь час'?", "lang": "uk"},
            {"role": "Patient", "text": "Може... два місяці? Воно не болить. Я тому і не звернув уваги.", "lang": "uk"},
            {"role": "Interpreter", "text": "Maybe... two months? It doesn't hurt. That's why I didn't pay attention.", "lang": "en"},
            {"role": "Doctor", "text": "Vasyl, that it doesn't hurt is actually the danger. That's your neuropathy — the nerves in your feet are damaged enough that pain signals aren't getting through. Can you feel this? — [touches foot with instrument] This? This?", "lang": "en"},
            {"role": "Interpreter", "text": "Василю, те що воно не болить — це власне і є небезпека. Це ваша нейропатія — нерви у ваших стопах пошкоджені настільки, що сигнали болю не проходять. Ви відчуваєте це? — [торкається стопи інструментом] Це? Це?", "lang": "uk"},
            {"role": "Patient", "text": "Ні. Нічого не відчуваю.", "lang": "uk"},
            {"role": "Interpreter", "text": "No. I feel nothing.", "lang": "en"},
            {"role": "Doctor", "text": "This wound has been there for two months and it's not healing because your circulation is compromised. I need to bring in our wound care specialist today — not next week. This type of ulcer, if not treated properly, can lead to infection that spreads to the bone.", "lang": "en"},
            {"role": "Interpreter", "text": "Ця рана є вже два місяці і вона не загоюється тому що ваше кровообіг порушений. Мені потрібно сьогодні залучити нашого спеціаліста з лікування ран — не наступного тижня. Такий тип виразки, якщо його неправильно лікувати, може призвести до інфекції що поширюється на кістку.", "lang": "uk"},
            {"role": "Patient", "text": "Я злякався зараз. Це може закінчитися ампутацією?", "lang": "uk"},
            {"role": "Interpreter", "text": "I'm scared now. Could this end in amputation?", "lang": "en"},
            {"role": "Doctor", "text": "I want to be honest: untreated, yes, that's a risk. Treated promptly, by today, with the right care — I expect this to heal. But you have to promise me something: from now on, every day, you look at your feet. Both of them. Every single day. This is not optional anymore.", "lang": "en"},
            {"role": "Interpreter", "text": "Я хочу бути чесною: нелікована — так, це ризик. Пролікована своєчасно, сьогодні, з належним доглядом — я очікую що це загоїться. Але ви повинні пообіцяти мені щось: відтепер, кожного дня, ви дивитесь на свої стопи. На обидві. Кожного єдиного дня. Це більше не є необов'язковим.", "lang": "uk"},
            {"role": "Patient", "text": "Обіцяю. Дякую що не засудили мене.", "lang": "uk"},
            {"role": "Interpreter", "text": "I promise. Thank you for not judging me.", "lang": "en"},
            {"role": "Doctor", "text": "You came in. That's what matters now.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви прийшли. Це те що зараз важливо.", "lang": "uk"}
        ]
    },

    # PREGNANCY
    {
        "title": "First visit and she's terrified",
        "topic": "PREGNANCY",
        "messages": [
            {"role": "Doctor", "text": "Daryna, welcome. This is your first prenatal visit, right? How are you feeling — emotionally, I mean. Not just physically.", "lang": "en"},
            {"role": "Interpreter", "text": "Дарино, вітаємо. Це ваш перший пренатальний візит, правда? Як ви себе почуваєте — емоційно, я маю на увазі. Не лише фізично.", "lang": "uk"},
            {"role": "Patient", "text": "Чесно? Я боюся. Ми з чоловіком щойно приїхали вісім місяців тому. Ніякої родини тут. Я не знаю як все влаштовано тут. Як пологи, страховка, всі ці речі.", "lang": "uk"},
            {"role": "Interpreter", "text": "Honestly? I'm scared. My husband and I only arrived eight months ago. No family here. I don't know how things work here. Childbirth, insurance, all of that.", "lang": "en"},
            {"role": "Doctor", "text": "That is so much to carry. And I want you to know — by the time you walk out of this office today, we'll have addressed every single one of those things. That's my promise to you for this visit. But first — how far along are you?", "lang": "en"},
            {"role": "Interpreter", "text": "Це так багато нести в собі. І я хочу щоб ви знали — до того, як ви вийдете з цього кабінету сьогодні, ми вирішимо кожну з цих речей. Це моя обіцянка вам на цей візит. Але спершу — на якому ви тижні?", "lang": "uk"},
            {"role": "Patient", "text": "Я думаю на дванадцятому. Але я не впевнена. У мене нерегулярний цикл.", "lang": "uk"},
            {"role": "Interpreter", "text": "I think twelve weeks. But I'm not sure. I have an irregular cycle.", "lang": "en"},
            {"role": "Doctor", "text": "That's exactly why we do an ultrasound today — to date the pregnancy precisely. We'll hear the heartbeat, see the size. That usually makes things feel more real in a good way. Are you nervous about what we might see?", "lang": "en"},
            {"role": "Interpreter", "text": "Саме тому ми робимо УЗД сьогодні — щоб точно визначити термін вагітності. Ми почуємо серцебиття, побачимо розміри. Зазвичай це робить все більш реальним у хорошому сенсі. Ви хвилюєтесь щодо того що ми можемо побачити?", "lang": "uk"},
            {"role": "Patient", "text": "Мій перший тест був позитивним, але я зробила ще три. Я не могла повірити. У нас були проблеми з завагітнінням два роки.", "lang": "uk"},
            {"role": "Interpreter", "text": "My first test was positive but I took three more. I couldn't believe it. We had trouble getting pregnant for two years.", "lang": "en"},
            {"role": "Doctor", "text": "Two years of trying — and now here you are. That's a long road and I understand why every step feels fragile. Let's go see this baby.", "lang": "en"},
            {"role": "Interpreter", "text": "Два роки спроб — і ось ви тут. Це довгий шлях і я розумію чому кожен крок відчувається крихким. Давайте підемо подивимося на цю дитину.", "lang": "uk"},
            {"role": "Patient", "text": "Чекайте — серцебиття — це точно буде?", "lang": "uk"},
            {"role": "Interpreter", "text": "Wait — the heartbeat — will it definitely be there?", "lang": "en"},
            {"role": "Doctor", "text": "At twelve weeks, the heartbeat is almost always clearly visible. I'm going to be right beside you and tell you what you're seeing, every step. You won't be alone in that room for even a second.", "lang": "en"},
            {"role": "Interpreter", "text": "На дванадцятому тижні серцебиття майже завжди чітко видно. Я буду поруч з вами і розповідатиму вам що ви бачите, крок за кроком. Ви не будете самі в тій кімнаті навіть секунди.", "lang": "uk"}
        ]
    },
    {
        "title": "Something feels wrong and she can't explain it",
        "topic": "PREGNANCY",
        "messages": [
            {"role": "Doctor", "text": "Olena, you called the after-hours line last night. You said 'something feels wrong'. Tell me everything.", "lang": "en"},
            {"role": "Interpreter", "text": "Олено, ви дзвонили на нічну лінію вчора ввечері. Ви сказали 'щось не так'. Розкажіть мені все.", "lang": "uk"},
            {"role": "Patient", "text": "Я не можу пояснити. Просто — дитина рухалася по-іншому. Або... менше? Я не знаю. Може я параноїдна. Тридцять четвертий тиждень.", "lang": "uk"},
            {"role": "Interpreter", "text": "I can't explain it. Just — the baby was moving differently. Or... less? I don't know. Maybe I'm paranoid. Thirty-four weeks.", "lang": "en"},
            {"role": "Doctor", "text": "You are not paranoid. You know this baby's movements better than any machine in this office. When a mother says 'something is different', I take it seriously. Every time. How long since you felt a strong kick?", "lang": "en"},
            {"role": "Interpreter", "text": "Ви не параноїчна. Ви знаєте рухи цієї дитини краще ніж будь-який апарат у цьому кабінеті. Коли мати каже 'щось інакше', я ставлюся до цього серйозно. Кожного разу. Як давно ви відчували сильний поштовх?", "lang": "uk"},
            {"role": "Patient", "text": "Вчора вранці. Після цього — тихо. Ніч пройшла тихо. Зранку — теж тихо.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yesterday morning. After that — quiet. The night was quiet. The morning was quiet too.", "lang": "en"},
            {"role": "Doctor", "text": "Okay. We're doing a non-stress test right now and an ultrasound. I want to hear the heartbeat and look at fluid levels. This is not an overreaction — this is exactly the right thing to do.", "lang": "en"},
            {"role": "Interpreter", "text": "Добре. Ми зараз зробимо нестресовий тест і УЗД. Я хочу почути серцебиття і подивитися на рівень навколоплідних вод. Це не надмірна реакція — це саме правильне, що треба зробити.", "lang": "uk"},
            {"role": "Patient", "text": "Мій чоловік сказав що я надто хвилуюся. Що всі мами так. Я почала сумніватися в собі.", "lang": "uk"},
            {"role": "Interpreter", "text": "My husband said I worry too much. That all moms are like that. I started doubting myself.", "lang": "en"},
            {"role": "Doctor", "text": "Your husband loves you and was trying to reassure you. But in medicine, a mother's gut feeling about fetal movement is a clinical sign we take as seriously as a lab result. You did the right thing. You should always call.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш чоловік любить вас і намагався вас заспокоїти. Але в медицині інтуїція матері щодо рухів плода — це клінічна ознака, до якої ми ставимось так само серйозно як до результату аналізу. Ви зробили правильно. Ви завжди повинні дзвонити.", "lang": "uk"},
            {"role": "Patient", "text": "Дякую. Це перша людина, яка не зробила мене відчути себе дурною за цей дзвінок.", "lang": "uk"},
            {"role": "Interpreter", "text": "Thank you. You are the first person who hasn't made me feel stupid for calling.", "lang": "en"},
            {"role": "Doctor", "text": "Never feel stupid for calling. That's what we're here for. Now let's go listen to this baby.", "lang": "en"},
            {"role": "Interpreter", "text": "Ніколи не почувайтеся дурною через дзвінок. Ми тут саме для цього. А тепер давайте підемо послухаємо цю дитину.", "lang": "uk"}
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Playscape — Virtual Discovery Worlds</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #050608;
    --bg2: #0a0c12;
    --bg-glow: radial-gradient(circle at top right, #1a153a 0%, #050608 60%);
    --card: rgba(20, 24, 36, 0.6);
    --card-hover: rgba(30, 38, 55, 0.8);
    --border: rgba(255, 255, 255, 0.05);
    --border-glow: rgba(91, 156, 246, 0.4);
    --accent: #5b9cf6;
    --accent2: #8b6ef7;
    --text: #dde3f0;
    --text2: #8a95b0;
    --text3: #505878;
    --doctor: #3ecf8e;
    --interpreter: #b48ef7;
    --patient: #f5c842;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  
  body {
    background: var(--bg);
    background-image: var(--bg-glow);
    background-attachment: fixed;
    color: var(--text);
    font-family: 'Inter', sans-serif;
    height: 100vh;
    overflow: hidden;
  }
  
  /* HEADER */
  header {
    padding: 24px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 80px;
    z-index: 10;
    position: relative;
  }
  .logo { 
    font-weight: 800;
    font-size: 18px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }

  /* HOME HUB VIEW */
  #homeView {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    position: absolute;
    top: 0; left: 0;
    transition: opacity 0.5s ease, transform 0.5s ease;
  }
  .hub-content {
    padding: 20px 40px;
    flex: 1;
    overflow-y: auto;
  }
  .hub-content::-webkit-scrollbar { width: 6px; }
  .hub-content::-webkit-scrollbar-track { background: transparent; }
  .hub-content::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
  
  .hub-title {
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .hub-subtitle {
    color: var(--text2);
    margin-bottom: 32px;
    font-size: 15px;
  }
  
  .scenario-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 24px;
    padding-bottom: 60px;
  }
  .scenario-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    cursor: pointer;
    backdrop-filter: blur(10px);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    position: relative;
    overflow: hidden;
  }
  .scenario-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    opacity: 0;
    transition: opacity 0.3s ease;
  }
  .scenario-card:hover {
    transform: translateY(-5px);
    background: var(--card-hover);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 20px var(--border-glow);
    border-color: rgba(255,255,255,0.1);
  }
  .scenario-card:hover::before {
    opacity: 1;
  }
  .card-topic {
    font-size: 11px;
    color: var(--accent);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 12px;
  }
  .card-title {
    font-size: 18px;
    font-weight: 600;
    line-height: 1.4;
  }

  /* INSTANCE VIEW */
  #instanceView {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    position: absolute;
    top: 0; left: 0;
    background: radial-gradient(circle at center, #111424 0%, #050608 100%);
    opacity: 0;
    pointer-events: none;
    transform: scale(0.95);
    transition: opacity 0.5s ease, transform 0.5s ease;
    z-index: 50;
  }
  #instanceView.active {
    opacity: 1;
    pointer-events: all;
    transform: scale(1);
  }
  
  .instance-header {
    padding: 20px 40px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid var(--border);
    background: rgba(0,0,0,0.3);
    backdrop-filter: blur(20px);
  }
  .btn-exit {
    background: rgba(255,255,255,0.05);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 8px;
    margin-right: 24px;
  }
  .btn-exit:hover {
    background: rgba(255,255,255,0.1);
  }
  
  .instance-title-area h2 {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 4px;
  }
  .instance-meta {
    font-size: 13px;
    color: var(--text3);
    font-family: 'JetBrains Mono', monospace;
  }

  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 40px;
    display: flex;
    flex-direction: column;
    gap: 16px;
    max-width: 900px;
    margin: 0 auto;
    width: 100%;
  }
  .chat-messages::-webkit-scrollbar { width: 6px; }
  .chat-messages::-webkit-scrollbar-track { background: transparent; }
  .chat-messages::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

  .message {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.4s ease, transform 0.4s ease;
    display: none;
    position: relative;
    backdrop-filter: blur(10px);
  }
  .message.visible {
    display: block;
    opacity: 1;
    transform: translateY(0);
  }
  .message-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
    display: inline-block;
  }
  .message.Doctor .message-label { color: var(--doctor); }
  .message.Patient .message-label { color: var(--patient); }
  .message.Interpreter .message-label { color: var(--interpreter); }
  .message.Doctor { border-left: 3px solid var(--doctor); align-self: flex-start; }
  .message.Patient { border-left: 3px solid var(--patient); align-self: flex-end; }
  .message.Interpreter { border-left: 3px solid var(--interpreter); align-self: center; background: rgba(255,255,255,0.05); }
  
  .message-bubble {
    font-size: 15px;
    line-height: 1.5;
    color: var(--text);
  }

  .controls {
    padding: 24px;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    display: flex;
    justify-content: center;
    gap: 16px;
  }
  .btn {
    padding: 12px 24px;
    border-radius: 30px;
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    border: none;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    color: white;
    box-shadow: 0 4px 15px rgba(91, 156, 246, 0.3);
  }
  .btn-primary:hover:not(:disabled) {
    box-shadow: 0 6px 20px rgba(91, 156, 246, 0.5);
    transform: translateY(-2px);
  }
  .btn-primary:disabled {
    background: var(--border);
    color: var(--text3);
    cursor: not-allowed;
    box-shadow: none;
  }
  .btn-secondary {
    background: rgba(255,255,255,0.05);
    color: var(--text);
    border: 1px solid var(--border);
  }
  .btn-secondary:hover {
    background: rgba(255,255,255,0.1);
  }
</style>
</head>
<body>

<!-- HOME HUB -->
<div id="homeView">
  <header>
    <div class="logo">Playscape // Hub</div>
    <div class="hub-counter" id="hubCounter" style="display:none;"></div>
  </header>
  <div class="hub-content">
    <h1 class="hub-title">Virtual Scenarios</h1>
    <p class="hub-subtitle">Select an instance to enter the discovery world.</p>
    <div class="scenario-grid" id="scenarioGrid"></div>
  </div>
</div>

<!-- INSTANCE VIEW -->
<div id="instanceView">
  <div class="instance-header">
    <button class="btn-exit" onclick="exitInstance()">
      ← Return to Hub
    </button>
    <div class="instance-title-area">
      <h2 id="chatTitle"></h2>
      <div class="instance-meta">
        <span id="chatTopic" style="color:var(--accent);margin-right:12px;"></span>
        <span id="chatProgress"></span>
      </div>
    </div>
    <div id="worldCounter" style="margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--text3);"></div>
  </div>
  
  <div class="chat-messages" id="chatMessages"></div>

  <div class="controls">
    <button class="btn btn-secondary" onclick="resetChat()">↺ Reset</button>
    <button class="btn btn-primary" id="btnNext" onclick="revealNext()">Reveal Next Line (Space)</button>
  </div>

  <!-- COMPLETION PORTAL -->
  <div id="completionPortal" style="
    display:none;
    position:absolute;
    inset:0;
    background:radial-gradient(circle at center, rgba(91,156,246,0.15) 0%, rgba(5,6,8,0.97) 70%);
    z-index:100;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:24px;
    backdrop-filter:blur(20px);
  ">
    <div style="font-size:11px;letter-spacing:0.2em;text-transform:uppercase;color:var(--accent);font-weight:700;">Scenario Complete</div>
    <div id="portalTitle" style="font-size:28px;font-weight:800;text-align:center;max-width:600px;line-height:1.3;"></div>
    <div id="portalTopic" style="font-size:13px;color:var(--text2);"></div>
    <div style="width:60px;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);margin:8px 0;"></div>
    <div style="font-size:14px;color:var(--text2);">Next world loading...</div>
    <button class="btn btn-primary" id="btnEnterNext" style="margin-top:8px;padding:14px 36px;font-size:16px;" onclick="chainNext()">
      Enter Next World →
    </button>
    <div id="countdownBar" style="
      width:200px;height:3px;
      background:var(--border);
      border-radius:4px;
      overflow:hidden;
    ">
      <div id="countdownFill" style="
        height:100%;
        width:0%;
        background:linear-gradient(90deg,var(--accent),var(--accent2));
        transition:width 5s linear;
      "></div>
    </div>
    <div style="font-size:12px;color:var(--text3);">auto-advancing in 5s — or press Space</div>
  </div>
</div>

<script>
  const chats = CHATS_JSON_PLACEHOLDER;
  
  let currentChat = null;
  let currentIndex = 0;
  let currentStep = 0;
  let totalWorldsVisited = 0;
  let autoChainTimer = null;

  const homeView = document.getElementById('homeView');
  const instanceView = document.getElementById('instanceView');
  const scenarioGrid = document.getElementById('scenarioGrid');
  const chatMessagesEl = document.getElementById('chatMessages');
  const chatTitle = document.getElementById('chatTitle');
  const chatTopic = document.getElementById('chatTopic');
  const chatProgress = document.getElementById('chatProgress');
  const btnNext = document.getElementById('btnNext');
  const worldCounter = document.getElementById('worldCounter');
  const completionPortal = document.getElementById('completionPortal');
  const portalTitle = document.getElementById('portalTitle');
  const portalTopic = document.getElementById('portalTopic');
  const countdownFill = document.getElementById('countdownFill');

  function initHub() {
    scenarioGrid.innerHTML = '';
    chats.forEach((chat, index) => {
      const card = document.createElement('div');
      card.className = 'scenario-card';
      card.innerHTML = `<div class="card-topic">${chat.topic}</div><div class="card-title">${chat.title}</div>`;
      card.onclick = () => enterInstance(index);
      scenarioGrid.appendChild(card);
    });
  }

  function enterInstance(index) {
    if (autoChainTimer) { clearTimeout(autoChainTimer); autoChainTimer = null; }
    completionPortal.style.display = 'none';

    currentIndex = index % chats.length;
    currentChat = chats[currentIndex];
    currentStep = 0;
    totalWorldsVisited++;

    // Transition UI from hub
    homeView.style.opacity = '0';
    homeView.style.pointerEvents = 'none';
    setTimeout(() => instanceView.classList.add('active'), 300);

    loadChatContent();
  }

  function loadChatContent() {
    chatTitle.textContent = currentChat.title;
    chatTopic.textContent = currentChat.topic;
    worldCounter.textContent = `World ${totalWorldsVisited} · ∞`;

    chatMessagesEl.innerHTML = '';
    currentChat.messages.forEach((msg, i) => {
      const wrapper = document.createElement('div');
      wrapper.className = `message ${msg.role}`;
      wrapper.id = `msg-${i}`;
      wrapper.innerHTML = `<div class="message-label">${msg.role}</div><div class="message-bubble">${msg.text}</div>`;
      chatMessagesEl.appendChild(wrapper);
    });
    chatMessagesEl.scrollTop = 0;
    updateUI();
  }

  function chainNext() {
    if (autoChainTimer) { clearTimeout(autoChainTimer); autoChainTimer = null; }
    completionPortal.style.display = 'none';
    currentIndex = (currentIndex + 1) % chats.length;
    currentChat = chats[currentIndex];
    currentStep = 0;
    totalWorldsVisited++;
    loadChatContent();
  }

  function showCompletionPortal() {
    const nextIndex = (currentIndex + 1) % chats.length;
    const nextChat = chats[nextIndex];
    portalTitle.textContent = nextChat.title;
    portalTopic.textContent = nextChat.topic;
    completionPortal.style.display = 'flex';

    // animate countdown bar
    countdownFill.style.width = '0%';
    requestAnimationFrame(() => {
      requestAnimationFrame(() => { countdownFill.style.width = '100%'; });
    });

    autoChainTimer = setTimeout(chainNext, 5000);
  }

  function exitInstance() {
    if (autoChainTimer) { clearTimeout(autoChainTimer); autoChainTimer = null; }
    completionPortal.style.display = 'none';
    instanceView.classList.remove('active');
    setTimeout(() => {
      homeView.style.opacity = '1';
      homeView.style.pointerEvents = 'all';
      currentChat = null;
    }, 300);
  }

  function revealNext() {
    if (!currentChat) return;
    // If portal is showing, Space advances to next world
    if (completionPortal.style.display === 'flex') { chainNext(); return; }
    if (currentStep >= currentChat.messages.length) return;
    const msgEl = document.getElementById(`msg-${currentStep}`);
    if (msgEl) {
      msgEl.classList.add('visible');
      setTimeout(() => msgEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 50);
    }
    currentStep++;
    updateUI();
  }

  function resetChat() {
    if (!currentChat) return;
    if (autoChainTimer) { clearTimeout(autoChainTimer); autoChainTimer = null; }
    completionPortal.style.display = 'none';
    currentStep = 0;
    document.querySelectorAll('.message').forEach(el => el.classList.remove('visible'));
    chatMessagesEl.scrollTop = 0;
    updateUI();
  }

  function updateUI() {
    const total = currentChat ? currentChat.messages.length : 0;
    const done = currentStep >= total;
    chatProgress.textContent = `${currentStep} / ${total} lines`;
    btnNext.textContent = done ? '→ Next World' : 'Reveal Next Line (Space)';
    btnNext.disabled = false;
    if (done) { showCompletionPortal(); }
  }

  document.addEventListener('keydown', e => {
    if (e.code === 'Space' && currentChat) {
      e.preventDefault();
      revealNext();
    }
    if (e.code === 'Escape' && currentChat) {
      exitInstance();
    }
  });

  initHub();
</script>
</body>
</html>
"""

import re
html_content = html_template.replace("CHATS_JSON_PLACEHOLDER", json.dumps(chats, ensure_ascii=False))

with open("/Users/rootv/Documents/job/exam/playscape.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Done. Generated playscape.html with", len(chats), "scenarios.")
