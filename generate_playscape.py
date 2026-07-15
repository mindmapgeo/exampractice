import json

chats = [
    # ANEMIA
    {
        "title": "Fatigue and Dietary Iron Absorption",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "Hello Mrs. Kovalenko. Your recent blood work shows that your ferritin levels are quite low, confirming iron-deficiency anemia. This explains your persistent fatigue.", "lang": "en"},
            {"role": "Interpreter", "text": "Доброго дня, пані Коваленко. Ваші останні аналізи крові показують, що рівень феритину у вас досить низький, що підтверджує залізодефіцитну анемію. Це пояснює вашу постійну втому.", "lang": "uk"},
            {"role": "Patient", "text": "Я приймаю ті пігулки з залізом щодня, як ви казали. Запиваю їх міцним чорним чаєм зранку, щоб швидше прокинутися.", "lang": "uk"},
            {"role": "Interpreter", "text": "I take those iron pills every day as you said. I wash them down with strong black tea in the morning to wake up faster.", "lang": "en"},
            {"role": "Doctor", "text": "Ah, that might be the issue. The tannins in black tea actually prevent your body from absorbing the iron. You should take them with orange juice instead, as Vitamin C boosts absorption.", "lang": "en"},
            {"role": "Interpreter", "text": "А, можливо, саме в цьому проблема. Таніни, що містяться в чорному чаї, насправді заважають вашому організму засвоювати залізо. Натомість вам слід приймати їх з апельсиновим соком, оскільки вітамін С покращує засвоєння.", "lang": "uk"},
            {"role": "Patient", "text": "Ого, я цього не знала. А якщо в мене від соку печія?", "lang": "uk"},
            {"role": "Interpreter", "text": "Wow, I didn't know that. What if the juice gives me heartburn?", "lang": "en"},
            {"role": "Doctor", "text": "If orange juice causes acid reflux, you can just take the supplement with a glass of water on an empty stomach, about an hour before eating.", "lang": "en"},
            {"role": "Interpreter", "text": "Якщо апельсиновий сік викликає кислотний рефлюкс, ви можете просто приймати добавку зі склянкою води натщесерце, приблизно за годину до їжі.", "lang": "uk"}
        ]
    },
    {
        "title": "Severe Dizziness and Heavy Cycles",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "You mentioned experiencing orthostatic hypotension—that means getting dizzy or lightheaded when you stand up quickly.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви згадували, що відчуваєте ортостатичну гіпотензію — це означає запаморочення або потемніння в очах, коли ви швидко встаєте.", "lang": "uk"},
            {"role": "Patient", "text": "Так, іноді я мушу триматися за стіну, щоб не впасти. Це дуже лякає.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, sometimes I have to hold onto the wall so I don't fall. It's very scary.", "lang": "en"},
            {"role": "Doctor", "text": "Given your extremely low hemoglobin count of 8.5, this is expected. I need to ask, have your menstrual cycles been unusually heavy recently?", "lang": "en"},
            {"role": "Interpreter", "text": "З огляду на ваш вкрай низький рівень гемоглобіну — 8,5, це очікувано. Мушу запитати, чи були ваші менструальні цикли останнім часом надзвичайно рясними?", "lang": "uk"},
            {"role": "Patient", "text": "Так, останні кілька місяців вони дуже рясні і тривають довше, ніж зазвичай. Чи це пов'язано?", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, for the last few months they have been very heavy and last longer than usual. Is that connected?", "lang": "en"},
            {"role": "Doctor", "text": "Yes, heavy periods are a leading cause of anemia in women. I would like to refer you to a gynecologist for a pelvic ultrasound to check for fibroids.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, рясні менструації є головною причиною анемії у жінок. Я хотів би направити вас до гінеколога на УЗД органів малого таза, щоб перевірити наявність міоми.", "lang": "uk"}
        ]
    },
    {
        "title": "Vegetarian Diet and B12",
        "topic": "ANEMIA",
        "messages": [
            {"role": "Doctor", "text": "Your complete blood count shows macrocytic anemia. This means your red blood cells are larger than normal, which is often caused by a Vitamin B12 deficiency.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш загальний аналіз крові показує макроцитарну анемію. Це означає, що ваші еритроцити більші за норму, що часто спричинено дефіцитом вітаміну В12.", "lang": "uk"},
            {"role": "Patient", "text": "Дефіцит вітаміну В12? Але ж я їм багато шпинату та гранатів, як радила моя бабуся для хорошої крові.", "lang": "uk"},
            {"role": "Interpreter", "text": "Vitamin B12 deficiency? But I eat a lot of spinach and pomegranates, as my grandmother advised for good blood.", "lang": "en"},
            {"role": "Doctor", "text": "Those are great for iron, but B12 is almost exclusively found in animal products like meat, dairy, and eggs. Since you are on a strict vegan diet, you aren't getting enough.", "lang": "en"},
            {"role": "Interpreter", "text": "Вони чудово підходять для заліза, але В12 міститься майже виключно в продуктах тваринного походження, таких як м'ясо, молочні продукти та яйця. Оскільки ви дотримуєтесь суворої веганської дієти, ви не отримуєте його в достатній кількості.", "lang": "uk"},
            {"role": "Patient", "text": "Зрозуміло. Тоді що мені робити? Я не хочу починати їсти м'ясо.", "lang": "uk"},
            {"role": "Interpreter", "text": "I understand. What should I do then? I don't want to start eating meat.", "lang": "en"},
            {"role": "Doctor", "text": "You don't have to. We can start you on a sublingual B12 supplement, which you let dissolve under your tongue daily. We'll retest your levels in 6 weeks.", "lang": "en"},
            {"role": "Interpreter", "text": "Вам і не потрібно. Ми можемо призначити вам сублінгвальну добавку В12, яку ви будете щодня розсмоктувати під язиком. Ми повторно перевіримо ваш рівень через 6 тижнів.", "lang": "uk"}
        ]
    },

    # THYROID
    {
        "title": "Hashimoto's and Medication Switching",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "Your antibody tests came back positive for Hashimoto's thyroiditis, which is an autoimmune condition causing your hypothyroidism.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваші тести на антитіла дали позитивний результат на тиреоїдит Хашимото, це аутоімунне захворювання, яке викликає ваш гіпотиреоз.", "lang": "uk"},
            {"role": "Patient", "text": "Аутоімунне? Це звучить серйозно. Минулого місяця аптека видала мені інші таблетки, не такі, як завжди. Чи могло це вплинути?", "lang": "uk"},
            {"role": "Interpreter", "text": "Autoimmune? That sounds serious. Last month the pharmacy gave me different pills, not the usual ones. Could that have affected it?", "lang": "en"},
            {"role": "Doctor", "text": "Hashimoto's is common and very manageable. Regarding the pills, did they switch you from brand-name Synthroid to generic Levothyroxine?", "lang": "en"},
            {"role": "Interpreter", "text": "Хашимото є поширеним захворюванням і дуже добре піддається лікуванню. Щодо таблеток, вони перевели вас з фірмового Синтроїду на генеричний Левотироксин?", "lang": "uk"},
            {"role": "Patient", "text": "Так, упаковка інша. І я почуваюся більш втомленою.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, the packaging is different. And I've been feeling more tired.", "lang": "en"},
            {"role": "Doctor", "text": "Thyroid hormones can be very sensitive to formulation changes. I will write 'Dispense as Written' on your next prescription so they must give you the exact brand.", "lang": "en"},
            {"role": "Interpreter", "text": "Гормони щитовидної залози можуть бути дуже чутливими до зміни складу препарату. У вашому наступному рецепті я напишу «Відпускати без замін», щоб вони обов'язково видали вам саме цей бренд.", "lang": "uk"}
        ]
    },
    {
        "title": "Hyperthyroidism Symptoms",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "Your resting heart rate is 110 beats per minute, and you've lost 12 pounds without trying. Are you experiencing any tremors or anxiety?", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш пульс у стані спокою становить 110 ударів на хвилину, і ви схудли на 12 фунтів без жодних зусиль. Чи відчуваєте ви тремтіння або тривожність?", "lang": "uk"},
            {"role": "Patient", "text": "Так, мої руки постійно тремтять, і я не можу заснути. Мені здається, що я весь час кудись поспішаю.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, my hands tremble constantly, and I can't fall asleep. I feel like I'm rushing somewhere all the time.", "lang": "en"},
            {"role": "Doctor", "text": "These are classic signs of hyperthyroidism, an overactive thyroid. Your TSH level is almost undetectable.", "lang": "en"},
            {"role": "Interpreter", "text": "Це класичні ознаки гіпертиреозу, підвищеної функції щитовидної залози. Ваш рівень ТТГ майже не визначається.", "lang": "uk"},
            {"role": "Patient", "text": "Чи потрібна мені операція? Моя сусідка робила операцію на горлі через подібну проблему.", "lang": "uk"},
            {"role": "Interpreter", "text": "Do I need surgery? My neighbor had throat surgery for a similar problem.", "lang": "en"},
            {"role": "Doctor", "text": "Not necessarily. We'll start with medication like Methimazole to slow down hormone production before considering surgery or radioactive iodine.", "lang": "en"},
            {"role": "Interpreter", "text": "Не обов'язково. Ми почнемо з медикаментів, таких як Метимазол, щоб уповільнити вироблення гормонів, перш ніж розглядати хірургічне втручання або радіоактивний йод.", "lang": "uk"}
        ]
    },
    {
        "title": "Thyroid Nodule Biopsy",
        "topic": "THYROID",
        "messages": [
            {"role": "Doctor", "text": "The ultrasound showed a 2-centimeter solid nodule on the right lobe of your thyroid. It has some irregular borders.", "lang": "en"},
            {"role": "Interpreter", "text": "УЗД показало щільний вузол розміром 2 сантиметри на правій частці вашої щитовидної залози. Він має трохи нерівні контури.", "lang": "uk"},
            {"role": "Patient", "text": "Нерівні контури? Це означає, що це рак?", "lang": "uk"},
            {"role": "Interpreter", "text": "Irregular borders? Does that mean it's cancer?", "lang": "en"},
            {"role": "Doctor", "text": "Not necessarily, the vast majority of thyroid nodules are benign. But to be safe, I want to perform a Fine Needle Aspiration, or FNA biopsy.", "lang": "en"},
            {"role": "Interpreter", "text": "Не обов'язково, переважна більшість вузлів щитовидної залози є доброякісними. Але для впевненості я хочу зробити тонкоголкову аспіраційну біопсію.", "lang": "uk"},
            {"role": "Patient", "text": "Це боляче? Мені будуть робити загальний наркоз?", "lang": "uk"},
            {"role": "Interpreter", "text": "Is it painful? Will I have general anesthesia?", "lang": "en"},
            {"role": "Doctor", "text": "We only use local anesthesia to numb the skin on your neck. You will feel some pressure, but it takes less than 15 minutes and you can go home right after.", "lang": "en"},
            {"role": "Interpreter", "text": "Ми використовуємо лише місцеву анестезію, щоб знеболити шкіру на шиї. Ви відчуєте невеликий тиск, але це займає менше 15 хвилин, і ви зможете одразу піти додому.", "lang": "uk"}
        ]
    },

    # SEIZURES
    {
        "title": "Focal Seizures and Auras",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "Your husband mentioned that right before you lost consciousness, you were smacking your lips and staring blankly into space.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш чоловік згадав, що безпосередньо перед втратою свідомості ви прицмокували губами і дивилися порожнім поглядом у простір.", "lang": "uk"},
            {"role": "Patient", "text": "Так, я цього не пам'ятаю. Але перед тим я відчула сильний запах паленої гуми, хоча нічого не горіло.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, I don't remember that. But before that I smelled a strong odor of burning rubber, even though nothing was burning.", "lang": "en"},
            {"role": "Doctor", "text": "That phantom smell is called an aura, which is actually a small, localized seizure in the brain before it spreads. We call this a focal impaired awareness seizure.", "lang": "en"},
            {"role": "Interpreter", "text": "Цей фантомний запах називається аурою, яка насправді є невеликим, локалізованим нападом у мозку до його поширення. Ми називаємо це фокальним нападом із порушенням свідомості.", "lang": "uk"},
            {"role": "Patient", "text": "Чи означає це, що в мене епілепсія? Я дуже хвилююся за свою роботу.", "lang": "uk"},
            {"role": "Interpreter", "text": "Does this mean I have epilepsy? I am very worried about my job.", "lang": "en"},
            {"role": "Doctor", "text": "We cannot diagnose epilepsy from a single event. We need to schedule an EEG and a brain MRI first to look for any structural causes.", "lang": "en"},
            {"role": "Interpreter", "text": "Ми не можемо поставити діагноз «епілепсія» на підставі одного випадку. Спершу нам потрібно призначити ЕЕГ та МРТ головного мозку, щоб перевірити наявність структурних причин.", "lang": "uk"}
        ]
    },
    {
        "title": "Anti-Epileptic Medication Side Effects",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "You've been on Keppra for a month now. Have you had any breakthrough seizures since you started the medication?", "lang": "en"},
            {"role": "Interpreter", "text": "Ви приймаєте Кеппру вже місяць. Чи були у вас проривні напади з моменту початку прийому ліків?", "lang": "uk"},
            {"role": "Patient", "text": "Нападів не було. Але я почуваюся жахливо. Я постійно зла на свою сім'ю без жодної причини.", "lang": "uk"},
            {"role": "Interpreter", "text": "No seizures. But I feel terrible. I am constantly angry at my family for no reason.", "lang": "en"},
            {"role": "Interpreter", "text": "Excuse me, doctor, the interpreter needs to clarify a term with the patient.", "lang": "en"},
            {"role": "Interpreter", "text": "Вибачте, ви маєте на увазі роздратування чи спалахи гніву?", "lang": "uk"},
            {"role": "Patient", "text": "Спалахи гніву. Я дуже агресивна.", "lang": "uk"},
            {"role": "Interpreter", "text": "The patient clarified she is experiencing outbursts of anger and aggression.", "lang": "en"},
            {"role": "Doctor", "text": "I appreciate the clarification. Keppra is known to cause severe mood changes, sometimes called 'Keppra rage'. We will slowly taper you off this and start you on Lamictal instead.", "lang": "en"},
            {"role": "Interpreter", "text": "Дякую за уточнення. Відомо, що Кеппра спричиняє серйозні зміни настрою, іноді це називають «лють Кеппри». Ми будемо повільно знижувати вашу дозу і натомість почнемо прийом Ламікталу.", "lang": "uk"}
        ]
    },
    {
        "title": "Post-Ictal State and Driving Laws",
        "topic": "SEIZURES",
        "messages": [
            {"role": "Doctor", "text": "The paramedics noted you were extremely confused and lethargic for about an hour after the convulsions stopped. This is known as the post-ictal state.", "lang": "en"},
            {"role": "Interpreter", "text": "Фельдшери відзначили, що ви були вкрай розгублені та мляві близько години після того, як припинилися судоми. Це називається постіктальним станом.", "lang": "uk"},
            {"role": "Patient", "text": "Мої м'язи дуже боліли, і я прикусила язика. Лікарю, коли я зможу знову водити машину? Мені треба відвозити дітей до школи.", "lang": "uk"},
            {"role": "Interpreter", "text": "My muscles ached a lot, and I bit my tongue. Doctor, when can I drive again? I need to take my kids to school.", "lang": "en"},
            {"role": "Doctor", "text": "By state law, I am required to report this seizure to the DMV. Your license will be suspended for a mandatory six-month seizure-free period.", "lang": "en"},
            {"role": "Interpreter", "text": "Згідно із законом штату, я зобов'язаний повідомити про цей напад до Департаменту автотранспорту. Вашу ліцензію буде призупинено на обов'язковий шестимісячний період без нападів.", "lang": "uk"},
            {"role": "Patient", "text": "Шість місяців?! Це зруйнує моє життя. Чи є якісь винятки, якщо я буду обережною?", "lang": "uk"},
            {"role": "Interpreter", "text": "Six months?! This will ruin my life. Are there any exceptions if I am careful?", "lang": "en"},
            {"role": "Doctor", "text": "I know this is incredibly difficult news. Unfortunately, there are no exceptions. If you drive and have a seizure, it could be fatal.", "lang": "en"},
            {"role": "Interpreter", "text": "Я знаю, що це неймовірно важка новина. На жаль, винятків немає. Якщо ви керуватимете автомобілем і у вас станеться напад, це може призвести до летальних наслідків.", "lang": "uk"}
        ]
    },

    # GENERAL WELLNESS
    {
        "title": "Prostate Screening Concerns",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "Since you recently turned 50, it is time to discuss prostate cancer screening. We typically start with a PSA blood test.", "lang": "en"},
            {"role": "Interpreter", "text": "Оскільки вам нещодавно виповнилося 50 років, настав час обговорити скринінг на рак передміхурової залози. Зазвичай ми починаємо з аналізу крові на ПСА.", "lang": "uk"},
            {"role": "Patient", "text": "Мій батько мав рак простати, тому я хочу перевіритися. Але я чув, що цей тест дуже незручний і болісний.", "lang": "uk"},
            {"role": "Interpreter", "text": "My father had prostate cancer, so I want to get checked. But I heard this test is very uncomfortable and painful.", "lang": "en"},
            {"role": "Doctor", "text": "You might be thinking of the digital rectal exam. While still useful, the PSA is just a standard blood draw from your arm. It measures a specific protein produced by the prostate gland.", "lang": "en"},
            {"role": "Interpreter", "text": "Можливо, ви маєте на увазі пальцеве ректальне дослідження. Хоча воно досі корисне, ПСА — це просто стандартний забір крові з вени на руці. Він вимірює специфічний білок, що виробляється передміхуровою залозою.", "lang": "uk"},
            {"role": "Patient", "text": "О, це набагато краще. Так, давайте зробимо аналіз крові.", "lang": "uk"},
            {"role": "Interpreter", "text": "Oh, that is much better. Yes, let's do the blood test.", "lang": "en"}
        ]
    },
    {
        "title": "Cholesterol and Statin Hesitancy",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "Your lipid panel came back, and your LDL, or 'bad' cholesterol, is quite high at 190. Given your family history of heart disease, I recommend starting a statin medication.", "lang": "en"},
            {"role": "Interpreter", "text": "Прийшли результати вашої ліпідограми, і ваш ЛПНЩ, або «поганий» холестерин, досить високий — 190. З огляду на сімейну історію серцевих захворювань, я рекомендую почати прийом статинів.", "lang": "uk"},
            {"role": "Patient", "text": "Я читала в інтернеті, що статини руйнують печінку і викликають біль у м'язах. Я б краще спробувала очищення організму травами.", "lang": "uk"},
            {"role": "Interpreter", "text": "I read online that statins destroy the liver and cause muscle pain. I would rather try an herbal detox.", "lang": "en"},
            {"role": "Doctor", "text": "I understand your hesitation. While muscle aches can be a side effect for a small percentage of people, severe liver damage is exceedingly rare. Herbal detoxes won't lower genetic cholesterol.", "lang": "en"},
            {"role": "Interpreter", "text": "Я розумію ваші вагання. Хоча біль у м'язах може бути побічним ефектом у невеликого відсотка людей, серйозне ушкодження печінки трапляється вкрай рідко. Трав'яні очищення не знизять генетичний холестерин.", "lang": "uk"},
            {"role": "Patient", "text": "Добре, але чи можемо ми дати мені три місяці, щоб спробувати знизити його за допомогою дієти та фізичних вправ, перш ніж починати прийом таблеток?", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay, but can we give me three months to try to lower it with diet and exercise before starting pills?", "lang": "en"},
            {"role": "Doctor", "text": "That is a reasonable compromise. We'll focus on a Mediterranean diet and recheck in three months. If it's still over 160, we'll revisit the medication.", "lang": "en"},
            {"role": "Interpreter", "text": "Це розумний компроміс. Ми зосередимося на середземноморській дієті та повторно перевіримо через три місяці. Якщо він все ще буде вищим за 160, ми повернемося до питання про ліки.", "lang": "uk"}
        ]
    },
    {
        "title": "Sleep Apnea Symptoms",
        "topic": "GENERAL WELLNESS",
        "messages": [
            {"role": "Doctor", "text": "You mentioned you wake up feeling unrefreshed, often with morning headaches. Does your partner ever complain about you snoring loudly?", "lang": "en"},
            {"role": "Interpreter", "text": "Ви згадали, що прокидаєтеся невиспаним, часто з ранковими головними болями. Чи скаржиться коли-небудь ваша партнерка на те, що ви голосно хропете?", "lang": "uk"},
            {"role": "Patient", "text": "Так, вона каже, що моє хропіння звучить так, ніби я задихаюся, і іноді я взагалі перестаю дихати на кілька секунд.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, she says my snoring sounds like I am choking, and sometimes I stop breathing altogether for a few seconds.", "lang": "en"},
            {"role": "Doctor", "text": "That is a textbook description of Obstructive Sleep Apnea. Your airway collapses during sleep, dropping your oxygen levels, which puts immense strain on your heart.", "lang": "en"},
            {"role": "Interpreter", "text": "Це класичний опис обструктивного апное сну. Ваші дихальні шляхи спадаються під час сну, знижуючи рівень кисню, що створює величезне навантаження на ваше серце.", "lang": "uk"},
            {"role": "Patient", "text": "Що мені потрібно робити? Я не хочу носити кисневу маску вночі.", "lang": "uk"},
            {"role": "Interpreter", "text": "What do I need to do? I don't want to wear an oxygen mask at night.", "lang": "en"},
            {"role": "Doctor", "text": "First, we will order an overnight sleep study. If you do have sleep apnea, a CPAP machine—which uses air pressure, not pure oxygen—is the gold standard treatment.", "lang": "en"},
            {"role": "Interpreter", "text": "Спершу ми призначимо нічне дослідження сну. Якщо у вас справді апное, апарат СІПАП, який використовує тиск повітря, а не чистий кисень, є золотим стандартом лікування.", "lang": "uk"}
        ]
    },

    # HEART ISSUES
    {
        "title": "Angina and Nitroglycerin",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "When you experience this chest tightness, how long does it usually last, and what makes it go away?", "lang": "en"},
            {"role": "Interpreter", "text": "Коли ви відчуваєте це стиснення в грудях, як довго воно зазвичай триває і що змушує його зникнути?", "lang": "uk"},
            {"role": "Patient", "text": "Воно з'являється, коли я піднімаюся сходами, і триває близько 5 хвилин. Коли я сідаю відпочити, воно минає.", "lang": "uk"},
            {"role": "Interpreter", "text": "It happens when I climb the stairs and lasts about 5 minutes. When I sit down to rest, it goes away.", "lang": "en"},
            {"role": "Doctor", "text": "This sounds like stable angina, which means your heart muscle isn't getting enough oxygen-rich blood during exertion. I am prescribing Nitroglycerin tablets.", "lang": "en"},
            {"role": "Interpreter", "text": "Це схоже на стабільну стенокардію, що означає, що ваш серцевий м'яз не отримує достатньо багатої на кисень крові під час фізичного навантаження. Я виписую вам таблетки нітрогліцерину.", "lang": "uk"},
            {"role": "Patient", "text": "Як їх приймати? Просто ковтати з водою?", "lang": "uk"},
            {"role": "Interpreter", "text": "How do I take them? Just swallow with water?", "lang": "en"},
            {"role": "Doctor", "text": "No, you must place the tablet under your tongue and let it dissolve at the first sign of chest pain. Do not swallow or chew it.", "lang": "en"},
            {"role": "Interpreter", "text": "Ні, ви повинні покласти таблетку під язик і дати їй розчинитися при перших ознаках болю в грудях. Не ковтайте і не жуйте її.", "lang": "uk"}
        ]
    },
    {
        "title": "Heart Failure Exacerbation",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "I see you've gained 8 pounds in the last week, and your ankles are very swollen. Are you having trouble breathing when you lie down flat?", "lang": "en"},
            {"role": "Interpreter", "text": "Я бачу, що ви набрали 8 фунтів за останній тиждень, і ваші щиколотки дуже набрякли. Чи важко вам дихати, коли ви лежите рівно?", "lang": "uk"},
            {"role": "Patient", "text": "Так, мені доводиться спати на трьох подушках, інакше я починаю задихатися і кашляти.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, I have to sleep on three pillows, otherwise I start gasping for air and coughing.", "lang": "en"},
            {"role": "Doctor", "text": "This means fluid is backing up into your lungs because your heart isn't pumping effectively. It's an exacerbation of your congestive heart failure.", "lang": "en"},
            {"role": "Interpreter", "text": "Це означає, що рідина накопичується у ваших легенях, оскільки ваше серце не перекачує кров ефективно. Це загострення вашої застійної серцевої недостатності.", "lang": "uk"},
            {"role": "Patient", "text": "Я намагався пити більше води, щоб вимити набряк з ніг. Це не допомогло?", "lang": "uk"},
            {"role": "Interpreter", "text": "I tried to drink more water to flush the swelling out of my legs. Did that not help?", "lang": "en"},
            {"role": "Doctor", "text": "Actually, drinking more fluid makes it worse. We need to restrict your fluid intake and double your Lasix (diuretic) dose for the next few days to help your kidneys eliminate the excess fluid.", "lang": "en"},
            {"role": "Interpreter", "text": "Насправді, вживання більшої кількості рідини робить тільки гірше. Нам потрібно обмежити споживання рідини та подвоїти дозу Лазиксу (сечогінного) на наступні кілька днів, щоб допомогти вашим ниркам вивести надлишок рідини.", "lang": "uk"}
        ]
    },
    {
        "title": "AFib and Blood Thinners",
        "topic": "HEART ISSUES",
        "messages": [
            {"role": "Doctor", "text": "The Holter monitor results show that your heart goes into an irregular rhythm called Atrial Fibrillation, or AFib.", "lang": "en"},
            {"role": "Interpreter", "text": "Результати холтерівського моніторингу показують, що ваше серце переходить у нерегулярний ритм, який називається фібриляцією передсердь, або миготливою аритмією.", "lang": "uk"},
            {"role": "Patient", "text": "Миготлива аритмія? Іноді я відчуваю, як серце тріпоче в грудях. Це небезпечно?", "lang": "uk"},
            {"role": "Interpreter", "text": "Atrial fibrillation? Sometimes I feel my heart fluttering in my chest. Is that dangerous?", "lang": "en"},
            {"role": "Doctor", "text": "The main risk with AFib is that blood can pool in the upper chambers of your heart and form clots. If a clot travels to the brain, it can cause a stroke.", "lang": "en"},
            {"role": "Interpreter", "text": "Основний ризик при фібриляції передсердь полягає в тому, що кров може накопичуватися у верхніх камерах вашого серця і утворювати тромби. Якщо тромб потрапить у мозок, це може спричинити інсульт.", "lang": "uk"},
            {"role": "Patient", "text": "Боже мій, як нам цьому запобігти?", "lang": "uk"},
            {"role": "Interpreter", "text": "Oh my god, how do we prevent this?", "lang": "en"},
            {"role": "Doctor", "text": "I am putting you on an anticoagulant, a blood thinner called Eliquis. It's crucial that you take it exactly as prescribed, every single day.", "lang": "en"},
            {"role": "Interpreter", "text": "Я призначаю вам антикоагулянт, препарат для розрідження крові під назвою Еліквіс. Дуже важливо, щоб ви приймали його точно за призначенням, кожного божого дня.", "lang": "uk"}
        ]
    },

    # DIABETES
    {
        "title": "Neuropathy vs Circulation",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "During the foot exam, I noticed you have lost sensation to the monofilament test on several toes.", "lang": "en"},
            {"role": "Interpreter", "text": "Під час огляду ваших стоп я помітив, що ви втратили чутливість до тесту з монофіламентом на кількох пальцях ніг.", "lang": "uk"},
            {"role": "Patient", "text": "Так, мої ноги часто відчуваються як онімілі або в них наче колють голками. Я думав, це просто поганий кровообіг через те, що я старію.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, my feet often feel numb or like needles are pricking them. I thought it was just poor circulation because I'm getting older.", "lang": "en"},
            {"role": "Doctor", "text": "This is actually diabetic peripheral neuropathy. High blood sugar levels over time have damaged the tiny nerves in your extremities.", "lang": "en"},
            {"role": "Interpreter", "text": "Насправді це діабетична периферична нейропатія. Високий рівень цукру в крові з часом пошкодив дрібні нерви у ваших кінцівках.", "lang": "uk"},
            {"role": "Patient", "text": "Чи можна це вилікувати? Моя дружина змушує мене носити теплі шкарпетки вночі.", "lang": "uk"},
            {"role": "Interpreter", "text": "Can this be cured? My wife makes me wear warm socks at night.", "lang": "en"},
            {"role": "Doctor", "text": "We cannot reverse the nerve damage, but we can stop it from getting worse by tightly controlling your A1C. You also need to inspect your feet daily for any cuts, since you won't feel them.", "lang": "en"},
            {"role": "Interpreter", "text": "Ми не можемо повернути назад пошкодження нервів, але ми можемо зупинити його прогресування шляхом суворого контролю вашого рівня глікованого гемоглобіну. Вам також потрібно щодня оглядати свої стопи на наявність порізів, оскільки ви їх не відчуєте.", "lang": "uk"}
        ]
    },
    {
        "title": "Hypoglycemia Management",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "Looking at your continuous glucose monitor logs, you've had several episodes where your blood sugar dropped below 60 mg/dL in the mid-afternoon.", "lang": "en"},
            {"role": "Interpreter", "text": "Дивлячись на журнали вашого апарату безперервного моніторингу глюкози, у вас було кілька епізодів, коли рівень цукру в крові падав нижче 60 мг/дл у другій половині дня.", "lang": "uk"},
            {"role": "Patient", "text": "Так, я починаю потіти, мої руки трясуться, і я відчуваю сильну слабкість. Я зазвичай з'їдаю великий шматок торта або плитку шоколаду, коли це трапляється.", "lang": "uk"},
            {"role": "Interpreter", "text": "Yes, I start sweating, my hands shake, and I feel very weak. I usually eat a large piece of cake or a chocolate bar when that happens.", "lang": "en"},
            {"role": "Doctor", "text": "Chocolate has fat, which slows down sugar absorption. For hypoglycemia, you should use the 'Rule of 15': eat 15 grams of fast-acting carbs, like 4 ounces of juice or 4 glucose tablets, then wait 15 minutes and recheck.", "lang": "en"},
            {"role": "Interpreter", "text": "Шоколад містить жир, який уповільнює засвоєння цукру. При гіпоглікемії вам слід використовувати «Правило 15»: з'їжте 15 грамів швидкозасвоюваних вуглеводів, наприклад, 4 унції соку або 4 таблетки глюкози, потім зачекайте 15 хвилин і перевірте знову.", "lang": "uk"},
            {"role": "Patient", "text": "Добре, я куплю ті таблетки глюкози. Можливо, мені варто зменшити дозу інсуліну перед обідом?", "lang": "uk"},
            {"role": "Interpreter", "text": "Okay, I will buy those glucose tablets. Maybe I should reduce my insulin dose before lunch?", "lang": "en"},
            {"role": "Doctor", "text": "Yes, let's reduce your lunchtime rapid-acting insulin by two units and see if that prevents the afternoon crashes.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, давайте зменшимо вашу дозу інсуліну короткої дії під час обіду на дві одиниці і подивимося, чи це запобіжить післяобіднім падінням цукру.", "lang": "uk"}
        ]
    },
    {
        "title": "A1C and Kidney Function",
        "topic": "DIABETES",
        "messages": [
            {"role": "Doctor", "text": "Your A1C is down to 7.1%, which is a fantastic improvement from 9% six months ago. You should be very proud of your diet changes.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш глікований гемоглобін знизився до 7,1%, що є фантастичним покращенням порівняно з 9% півроку тому. Ви повинні дуже пишатися своїми змінами в дієті.", "lang": "uk"},
            {"role": "Patient", "text": "Дякую, я повністю відмовився від хліба та макаронів. Але я бачив у своєму додатку, що аналіз сечі показав якісь відхилення?", "lang": "uk"},
            {"role": "Interpreter", "text": "Thank you, I completely gave up bread and pasta. But I saw in my app that the urine test showed some abnormalities?", "lang": "en"},
            {"role": "Doctor", "text": "Yes, we found trace amounts of albumin, a protein, in your urine. This is an early sign of diabetic nephropathy, meaning the kidneys are under stress.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, ми виявили сліди альбуміну, тобто білка, у вашій сечі. Це рання ознака діабетичної нефропатії, що означає, що нирки зазнають навантаження.", "lang": "uk"},
            {"role": "Patient", "text": "Чи означає це, що мені потрібен діаліз?", "lang": "uk"},
            {"role": "Interpreter", "text": "Does this mean I need dialysis?", "lang": "en"},
            {"role": "Doctor", "text": "No, this is very early. We will start you on a low dose of an ACE inhibitor, like Lisinopril, which protects the kidneys from further damage.", "lang": "en"},
            {"role": "Interpreter", "text": "Ні, це дуже рання стадія. Ми призначимо вам низьку дозу інгібітора АПФ, наприклад Лізиноприлу, який захищає нирки від подальшого пошкодження.", "lang": "uk"}
        ]
    },

    # PREGNANCY
    {
        "title": "Gestational Diabetes Screening",
        "topic": "PREGNANCY",
        "messages": [
            {"role": "Doctor", "text": "You are 26 weeks pregnant, so today we will be doing your Glucose Challenge Test to check for gestational diabetes.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви на 26-му тижні вагітності, тому сьогодні ми будемо робити тест на толерантність до глюкози, щоб перевірити наявність гестаційного діабету.", "lang": "uk"},
            {"role": "Patient", "text": "Це той густий сироп, який я маю випити? Моя сестра казала, що від нього її знудило.", "lang": "uk"},
            {"role": "Interpreter", "text": "Is that the thick syrup I have to drink? My sister said it made her throw up.", "lang": "en"},
            {"role": "Doctor", "text": "Yes, you have to drink the 50-gram glucose drink within 5 minutes. Then we draw your blood exactly one hour later.", "lang": "en"},
            {"role": "Interpreter", "text": "Так, ви повинні випити напій з 50 грамами глюкози протягом 5 хвилин. Потім ми візьмемо у вас кров рівно через годину.", "lang": "uk"},
            {"role": "Patient", "text": "Чи можу я пити воду, поки чекаю цієї години? Я відчуваю таку спрагу.", "lang": "uk"},
            {"role": "Interpreter", "text": "Can I drink water while I wait for that hour? I feel so thirsty.", "lang": "en"},
            {"role": "Doctor", "text": "You can have a few small sips of plain water if you feel nauseous, but do not eat anything or drink any large amounts of liquid, as it can dilute the test results.", "lang": "en"},
            {"role": "Interpreter", "text": "Ви можете зробити кілька невеликих ковтків звичайної води, якщо відчуваєте нудоту, але нічого не їжте і не пийте великої кількості рідини, оскільки це може розбавити результати тесту.", "lang": "uk"}
        ]
    },
    {
        "title": "Preeclampsia Warning Signs",
        "topic": "PREGNANCY",
        "messages": [
            {"role": "Doctor", "text": "Your blood pressure is slightly elevated today at 135 over 85, and I noticed some swelling in your hands and face.", "lang": "en"},
            {"role": "Interpreter", "text": "Ваш артеріальний тиск сьогодні трохи підвищений — 135 на 85, і я помітив деякий набряк на ваших руках та обличчі.", "lang": "uk"},
            {"role": "Patient", "text": "Мої обручки більше не налазять. Але я думала, що набряки — це нормально в третьому триместрі.", "lang": "uk"},
            {"role": "Interpreter", "text": "My wedding rings don't fit anymore. But I thought swelling was normal in the third trimester.", "lang": "en"},
            {"role": "Doctor", "text": "Mild swelling in the ankles is normal, but sudden swelling in the face and hands combined with elevated blood pressure can be a sign of preeclampsia.", "lang": "en"},
            {"role": "Interpreter", "text": "Легкий набряк щиколоток — це нормально, але раптовий набряк обличчя та рук у поєднанні з підвищеним артеріальним тиском може бути ознакою прееклампсії.", "lang": "uk"},
            {"role": "Patient", "text": "Тепер я хвилююся. Чи загрожує це моїй дитині?", "lang": "uk"},
            {"role": "Interpreter", "text": "Now I am worried. Is my baby in danger?", "lang": "en"},
            {"role": "Doctor", "text": "Right now, your baby's heart rate looks perfect. But I want to run a urine test to check for protein, and I need you to go to triage immediately if you develop a severe headache or blurry vision.", "lang": "en"},
            {"role": "Interpreter", "text": "Наразі серцебиття вашої дитини виглядає ідеально. Але я хочу зробити аналіз сечі, щоб перевірити наявність білка, і вам потрібно негайно звернутися до приймального відділення, якщо у вас з'явиться сильний головний біль або помутніння зору.", "lang": "uk"}
        ]
    }
]

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Playscape - Interpreter Chats</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0d14;
    --bg2: #111520;
    --card: #1a2035;
    --card-hover: #1f2640;
    --border: #2a3350;
    --accent: #4f8ef7;
    --accent2: #7c5af7;
    --text: #e2e8f0;
    --text2: #94a3b8;
    --doctor: #34d399;
    --interpreter: #a78bfa;
    --patient: #fbbf24;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: var(--bg); color: var(--text);
    font-family: 'Inter', sans-serif;
    height: 100vh; display: flex; flex-direction: column;
    overflow: hidden;
  }

  header {
    background: rgba(10,13,20,0.85);
    border-bottom: 1px solid var(--border);
    padding: 0 24px; display: flex; align-items: center;
    height: 64px; flex-shrink: 0; z-index: 10;
  }
  .logo {
    font-weight: 800; font-size: 18px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }

  .main-container {
    display: flex; flex: 1; overflow: hidden;
  }

  .sidebar {
    width: 320px; background: var(--bg2); border-right: 1px solid var(--border);
    display: flex; flex-direction: column;
  }
  .filters {
    padding: 16px; border-bottom: 1px solid var(--border);
  }
  .filters select {
    width: 100%; padding: 10px; background: var(--card); border: 1px solid var(--border);
    color: var(--text); border-radius: 8px; font-family: 'Inter'; outline: none;
  }
  
  .chat-list {
    flex: 1; overflow-y: auto;
  }
  .chat-item {
    padding: 16px; border-bottom: 1px solid var(--border); cursor: pointer;
    transition: background 0.2s;
  }
  .chat-item:hover, .chat-item.active {
    background: var(--card-hover);
  }
  .chat-item-topic {
    font-size: 11px; color: var(--accent); font-weight: 700; text-transform: uppercase;
    margin-bottom: 4px;
  }
  .chat-item-title {
    font-size: 15px; font-weight: 600; color: var(--text);
  }

  .chat-area {
    flex: 1; display: flex; flex-direction: column; background: var(--bg);
    position: relative;
  }
  .chat-header {
    padding: 20px 24px; border-bottom: 1px solid var(--border);
    background: var(--bg2);
  }
  .chat-header h2 { font-size: 20px; font-weight: 700; margin-bottom: 4px; }
  .chat-header p { color: var(--text2); font-size: 14px; }

  .chat-messages {
    flex: 1; overflow-y: auto; padding: 24px;
    display: flex; flex-direction: column; gap: 16px;
  }

  .message {
    max-width: 85%; padding: 16px; border-radius: 12px;
    position: relative; animation: fadeIn 0.3s ease-out;
    display: none; /* hidden until clicked */
  }
  .message.visible { display: block; }
  
  .message.Doctor { align-self: flex-start; background: rgba(52, 211, 153, 0.1); border: 1px solid rgba(52, 211, 153, 0.2); }
  .message.Patient { align-self: flex-start; background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.2); margin-left: 20px; }
  .message.Interpreter { align-self: flex-end; background: rgba(167, 139, 250, 0.1); border: 1px solid rgba(167, 139, 250, 0.2); }
  
  .message-role {
    font-size: 12px; font-weight: 700; margin-bottom: 6px; text-transform: uppercase;
  }
  .Doctor .message-role { color: var(--doctor); }
  .Patient .message-role { color: var(--patient); }
  .Interpreter .message-role { color: var(--interpreter); }

  .message-text { font-size: 15px; line-height: 1.5; }

  .controls {
    padding: 16px 24px; border-top: 1px solid var(--border); background: var(--bg2);
    display: flex; justify-content: space-between; align-items: center;
  }
  .btn {
    padding: 12px 24px; border-radius: 8px; border: none; font-weight: 600; font-family: 'Inter';
    cursor: pointer; transition: all 0.2s;
  }
  .btn-primary { background: var(--accent); color: white; }
  .btn-primary:hover { background: #3b76d6; }
  .btn-secondary { background: var(--card); color: var(--text); border: 1px solid var(--border); }
  .btn-secondary:hover { background: var(--card-hover); }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .empty-state {
    display: flex; flex: 1; align-items: center; justify-content: center;
    color: var(--text2); font-size: 16px; flex-direction: column; gap: 12px;
  }
</style>
</head>
<body>

<header>
  <div class="logo">PLAYSCAPE // Interactive Chat Training</div>
</header>

<div class="main-container">
  <div class="sidebar">
    <div class="filters">
      <select id="topicFilter">
        <option value="ALL">All Topics</option>
        <option value="ANEMIA">Anemia</option>
        <option value="THYROID">Thyroid</option>
        <option value="SEIZURES">Seizures</option>
        <option value="GENERAL WELLNESS">General Wellness</option>
        <option value="HEART ISSUES">Heart Issues</option>
        <option value="DIABETES">Diabetes</option>
        <option value="PREGNANCY">Pregnancy</option>
      </select>
    </div>
    <div class="chat-list" id="chatList"></div>
  </div>

  <div class="chat-area">
    <div class="chat-header" id="chatHeader" style="display:none;">
      <h2 id="chatTitle"></h2>
      <p id="chatTopic"></p>
    </div>
    
    <div class="chat-messages" id="chatMessages">
      <div class="empty-state">
        <svg width="48" height="48" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
        Select a scenario to start practicing
      </div>
    </div>

    <div class="controls" id="chatControls" style="display:none;">
      <button class="btn btn-secondary" id="btnReset">Reset Scenario</button>
      <button class="btn btn-primary" id="btnNext">Reveal Next Line (Space)</button>
    </div>
  </div>
</div>

<script>
  const chats = %s;
  
  let currentChat = null;
  let currentStep = 0;

  const chatListEl = document.getElementById('chatList');
  const chatMessagesEl = document.getElementById('chatMessages');
  const topicFilter = document.getElementById('topicFilter');
  const chatHeader = document.getElementById('chatHeader');
  const chatControls = document.getElementById('chatControls');
  const chatTitle = document.getElementById('chatTitle');
  const chatTopic = document.getElementById('chatTopic');
  const btnNext = document.getElementById('btnNext');
  const btnReset = document.getElementById('btnReset');

  function renderList(filter = 'ALL') {
    chatListEl.innerHTML = '';
    chats.forEach((chat, index) => {
      if (filter !== 'ALL' && chat.topic !== filter) return;
      
      const div = document.createElement('div');
      div.className = 'chat-item';
      div.innerHTML = `
        <div class="chat-item-topic">${chat.topic}</div>
        <div class="chat-item-title">${chat.title}</div>
      `;
      div.onclick = () => loadChat(index);
      chatListEl.appendChild(div);
    });
  }

  function loadChat(index) {
    currentChat = chats[index];
    currentStep = 0;
    
    document.querySelectorAll('.chat-item').forEach(el => el.classList.remove('active'));
    event.currentTarget.classList.add('active');

    chatHeader.style.display = 'block';
    chatControls.style.display = 'flex';
    
    chatTitle.textContent = currentChat.title;
    chatTopic.textContent = "Topic: " + currentChat.topic;

    chatMessagesEl.innerHTML = '';
    
    currentChat.messages.forEach((msg, i) => {
      const div = document.createElement('div');
      div.className = `message ${msg.role}`;
      div.id = `msg-${i}`;
      div.innerHTML = `
        <div class="message-role">${msg.role}</div>
        <div class="message-text">${msg.text}</div>
      `;
      chatMessagesEl.appendChild(div);
    });
    
    updateButtonState();
  }

  function revealNext() {
    if (!currentChat || currentStep >= currentChat.messages.length) return;
    
    const msgEl = document.getElementById(`msg-${currentStep}`);
    if (msgEl) {
      msgEl.classList.add('visible');
      msgEl.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }
    currentStep++;
    updateButtonState();
  }

  function resetChat() {
    if (!currentChat) return;
    currentStep = 0;
    document.querySelectorAll('.message').forEach(el => el.classList.remove('visible'));
    updateButtonState();
  }

  function updateButtonState() {
    if (currentStep >= currentChat.messages.length) {
      btnNext.textContent = "Scenario Complete";
      btnNext.disabled = true;
      btnNext.style.opacity = '0.5';
    } else {
      btnNext.textContent = "Reveal Next Line (Space)";
      btnNext.disabled = false;
      btnNext.style.opacity = '1';
    }
  }

  topicFilter.addEventListener('change', (e) => {
    renderList(e.target.value);
  });

  btnNext.addEventListener('click', revealNext);
  btnReset.addEventListener('click', resetChat);

  document.addEventListener('keydown', (e) => {
    if (e.code === 'Space' && currentChat) {
      e.preventDefault();
      revealNext();
    }
  });

  // Init
  renderList();
</script>
</body>
</html>
"""

html_content = html_template.replace("%s", json.dumps(chats))

with open("/Users/rootv/Documents/job/exam/playscape.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Created playscape.html successfully.")
