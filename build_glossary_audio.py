#!/usr/bin/env python3
"""
Builds glossary_audiobook.mp3 — English term, Ukrainian translation, brief description.
Run: python3 build_glossary_audio.py
"""
import asyncio, edge_tts, os

# ── DEFINITIONS DATABASE ───────────────────────────────────────────────────────
# Format: "English Term": ("Ukrainian", "Brief definition read aloud")

GLOSSARY = {

# ════════════════════════════════════════════════════════════
# SECTION 1 — GENERAL MEDICAL VOCABULARY (75 terms)
# ════════════════════════════════════════════════════════════
"Bloodwork": (
    "Аналіз крові",
    "A lab test where a sample of blood is drawn and analyzed to check for diseases, deficiencies, or organ function."
),
"Anemia": (
    "Анемія",
    "A condition where the blood lacks enough healthy red blood cells to carry adequate oxygen to the body's tissues."
),
"Weight gain": (
    "Набір ваги",
    "An increase in body weight, which can be due to fluid retention, fat accumulation, or muscle growth."
),
"Weight loss": (
    "Втрата ваги",
    "A decrease in body weight, which may be intentional through diet and exercise or unintentional due to illness."
),
"High blood pressure": (
    "Високий кров'яний тиск",
    "Also called hypertension. A condition where the force of blood against artery walls is consistently too high, increasing the risk of heart disease and stroke."
),
"Low blood pressure": (
    "Низький кров'яний тиск",
    "Also called hypotension. A condition where blood pressure is too low, which can cause dizziness or fainting."
),
"Diabetes": (
    "Діабет",
    "A chronic condition where the body cannot properly regulate blood sugar levels, either due to insufficient insulin production or insulin resistance."
),
"Cholesterol": (
    "Холестерин",
    "A fatty substance in the blood. High levels of bad cholesterol can block arteries and increase the risk of heart disease."
),
"Blood sugar": (
    "Рівень цукру в крові",
    "The concentration of glucose in the blood. Monitoring this is essential for managing diabetes."
),
"Heart rate": (
    "Частота серцевих скорочень",
    "The number of times the heart beats per minute. A normal resting rate is 60 to 100 beats per minute."
),
"Pulse": (
    "Пульс",
    "The rhythmic throbbing of arteries produced by the heartbeat, felt at the wrist or neck."
),
"Fever": (
    "Лихоманка",
    "An elevated body temperature above 38 degrees Celsius, usually a sign that the body is fighting an infection."
),
"Nausea": (
    "Нудота",
    "An uncomfortable sensation in the stomach with an urge to vomit, often a symptom of illness, medication, or motion sickness."
),
"Vomiting": (
    "Блювання",
    "The forceful expulsion of stomach contents through the mouth, commonly caused by illness, infection, or ingestion of toxins."
),
"Diarrhea": (
    "Діарея",
    "Frequent, loose, or watery bowel movements, often caused by infection, food intolerance, or medication."
),
"Constipation": (
    "Запор",
    "Difficulty having bowel movements, characterized by infrequent, hard, or painful stools."
),
"Fatigue": (
    "Втома",
    "Persistent tiredness or exhaustion that is not relieved by rest, often a symptom of an underlying health condition."
),
"Shortness of breath": (
    "Задишка",
    "Difficulty breathing or feeling unable to get enough air. Can be a symptom of heart or lung conditions."
),
"Chest pain": (
    "Біль у грудях",
    "Pain or discomfort in the chest area, which can range from a dull ache to a sharp stabbing sensation. A potential symptom of a heart attack."
),
"Rash": (
    "Висип",
    "An area of irritated or swollen skin, often red and itchy. Can be caused by allergies, infections, or skin conditions."
),
"Swelling": (
    "Набряк",
    "An abnormal enlargement of a body part due to buildup of fluid in the tissues, often indicating inflammation or injury."
),
"Infection": (
    "Інфекція",
    "The invasion and multiplication of harmful microorganisms such as bacteria, viruses, or fungi in the body."
),
"Inflammation": (
    "Запалення",
    "The body's protective response to injury or infection, characterized by redness, swelling, heat, and pain."
),
"Fracture": (
    "Перелом",
    "A break in a bone, ranging from a hairline crack to a complete break."
),
"Sprain": (
    "Розтягнення",
    "An injury to a ligament, the tissue that connects bones, caused by overstretching or tearing."
),
"Allergy": (
    "Алергія",
    "An exaggerated immune response to a normally harmless substance, such as pollen, food, or medication."
),
"Asthma": (
    "Астма",
    "A chronic condition that causes the airways to become inflamed and narrow, making breathing difficult."
),
"Cancer": (
    "Рак",
    "A disease in which abnormal cells divide uncontrollably and can invade nearby tissues or spread to other parts of the body."
),
"Stroke": (
    "Інсульт",
    "A medical emergency in which blood supply to part of the brain is cut off, causing brain cells to die and potentially leading to paralysis or speech problems."
),
"Heart attack": (
    "Серцевий напад",
    "A medical emergency where blood flow to part of the heart is blocked, causing heart muscle damage."
),
"Seizure": (
    "Судоми",
    "A sudden, uncontrolled electrical disturbance in the brain that can cause convulsions, loss of consciousness, or unusual behavior."
),
"Migraine": (
    "Мігрень",
    "A severe recurring headache, often on one side of the head, accompanied by nausea, vomiting, and sensitivity to light or sound."
),
"Arthritis": (
    "Артрит",
    "Inflammation of one or more joints, causing pain, stiffness, and swelling. Common types include osteoarthritis and rheumatoid arthritis."
),
"Pregnancy": (
    "Вагітність",
    "The condition of carrying a developing baby in the uterus, lasting approximately 40 weeks."
),
"Miscarriage": (
    "Викидень",
    "The spontaneous loss of a pregnancy before the 20th week, often due to chromosomal abnormalities."
),
"Discharge": (
    "Виділення",
    "Fluid that flows out of a body part, such as the nose, vagina, or wound. May be normal or a sign of infection."
),
"Urine": (
    "Сеча",
    "Liquid waste produced by the kidneys and stored in the bladder before being expelled from the body."
),
"Stool": (
    "Кал",
    "Solid waste matter eliminated from the body through the bowels. Also referred to as feces."
),
"X-ray": (
    "Рентген",
    "A type of imaging that uses radiation to create pictures of bones and certain tissues inside the body."
),
"MRI": (
    "МРТ",
    "Magnetic Resonance Imaging. A scan that uses magnetic fields and radio waves to produce detailed images of organs and tissues."
),
"Ultrasound": (
    "УЗД",
    "An imaging technique that uses sound waves to create pictures of structures inside the body, commonly used during pregnancy."
),
"Biopsy": (
    "Біопсія",
    "A medical procedure where a small sample of tissue is removed from the body and examined under a microscope to check for disease."
),
"Surgery": (
    "Хірургічна операція",
    "A medical procedure involving an incision into the body to treat, repair, or remove a diseased or damaged organ or tissue."
),
"Anesthesia": (
    "Анестезія",
    "Medication used to prevent pain during surgery or procedures, either by numbing a specific area or putting the patient into a temporary unconscious state."
),
"Wound": (
    "Рана",
    "An injury to the body caused by a cut, puncture, or other trauma that breaks the skin or underlying tissue."
),
"Sutures": (
    "Шви",
    "Stitches used to close a wound or surgical incision, allowing the tissue to heal properly."
),
"Catheter": (
    "Катетер",
    "A thin, flexible tube inserted into the body to drain fluids, such as urine from the bladder, or to deliver medications."
),
"IV (Intravenous)": (
    "Внутрішньовенне введення",
    "A method of delivering fluids, medications, or nutrients directly into a vein through a small needle or tube."
),
"Vaccination": (
    "Вакцинація",
    "The administration of a vaccine to stimulate the immune system to protect against a specific infectious disease."
),
"Immunization": (
    "Імунізація",
    "The process by which a person becomes protected against a disease through vaccination."
),
"Blood type": (
    "Група крові",
    "A classification of blood based on the presence or absence of specific antigens on red blood cells. Main types are A, B, AB, and O."
),
"Platelet": (
    "Тромбоцит",
    "A tiny blood cell that helps the blood clot to stop bleeding when a blood vessel is damaged."
),
"White blood cell": (
    "Лейкоцит",
    "A blood cell that is part of the immune system. It helps the body fight infection and disease."
),
"Red blood cell": (
    "Еритроцит",
    "A blood cell that contains hemoglobin and carries oxygen from the lungs to the rest of the body."
),
"Hemoglobin": (
    "Гемоглобін",
    "A protein in red blood cells that carries oxygen. Low hemoglobin levels indicate anemia."
),
"Antibiotic": (
    "Антибіотик",
    "A medication that kills or inhibits the growth of bacteria. It does not work against viruses."
),
"Antiviral": (
    "Противірусний препарат",
    "A medication used to treat viral infections by stopping the virus from multiplying."
),
"Anti-inflammatory": (
    "Протизапальний препарат",
    "A medication that reduces inflammation and associated pain, such as ibuprofen."
),
"Painkiller": (
    "Знеболюючий препарат",
    "A medication used to relieve pain. Also called an analgesic."
),
"Insulin": (
    "Інсулін",
    "A hormone produced by the pancreas that regulates blood sugar. People with diabetes often require insulin injections."
),
"Blood pressure cuff": (
    "Тонометр",
    "A medical device used to measure blood pressure, consisting of an inflatable cuff placed around the arm."
),
"Stethoscope": (
    "Стетоскоп",
    "A medical instrument used to listen to sounds inside the body, such as the heartbeat and breathing."
),
"Thermometer": (
    "Термометр",
    "A device used to measure body temperature."
),
"Oxygen": (
    "Кисень",
    "A gas essential for life. In medical settings, supplemental oxygen is given to patients who cannot breathe adequately on their own."
),
"Ventilator": (
    "Апарат штучної вентиляції легенів",
    "A machine that breathes for a patient who cannot breathe adequately on their own, delivering air and oxygen through a tube."
),
"Intubation": (
    "Інтубація",
    "A procedure where a tube is inserted into the airway through the mouth or nose to help a patient breathe."
),
"CPR": (
    "Серцево-легенева реанімація",
    "Cardiopulmonary Resuscitation. An emergency procedure combining chest compressions and rescue breathing to maintain circulation when the heart has stopped."
),
"AED": (
    "Автоматичний зовнішній дефібрилятор",
    "Automated External Defibrillator. A portable device that delivers an electric shock to restore a normal heart rhythm during cardiac arrest."
),
"Emergency": (
    "Невідкладна допомога",
    "A serious, unexpected situation that requires immediate medical attention."
),
"ICU": (
    "Відділення інтенсивної терапії",
    "Intensive Care Unit. A specialized hospital ward for patients who are critically ill and require continuous monitoring."
),
"ER (Emergency Room)": (
    "Відділення швидкої допомоги",
    "The section of a hospital that provides immediate treatment for urgent and life-threatening conditions."
),
"Ambulance": (
    "Швидка допомога",
    "A vehicle equipped with medical equipment used to transport patients to the hospital in an emergency."
),
"Discharge (hospital)": (
    "Виписка зі стаціонару",
    "The formal process of releasing a patient from the hospital after their treatment is complete."
),
"Referral": (
    "Направлення",
    "A recommendation from a primary care provider to see a specialist or receive a specific service."
),
"Prescription": (
    "Рецепт",
    "A written order from a licensed healthcare provider authorizing a patient to receive medication."
),

# ════════════════════════════════════════════════════════════
# SECTION 2 — PROCEDURE ACRONYMS (16 terms)
# ════════════════════════════════════════════════════════════
"CAT scan (Computer Axial Tomography)": (
    "КТ — комп'ютерна аксіальна томографія",
    "Also called a CT scan. An imaging procedure that uses X-rays and computer processing to create detailed cross-sectional images of the body."
),
"DPT (Diphtheria, Pertussis, Tetanus)": (
    "АКДП — дифтерія, кашлюк, правець",
    "A combination vaccine that protects against three serious bacterial diseases: diphtheria, whooping cough, and tetanus."
),
"PCOS (Polycystic Ovarian Syndrome)": (
    "СПКЯ — синдром полікістозних яєчників",
    "A hormonal disorder common among women of reproductive age, characterized by irregular periods and cysts on the ovaries."
),
"COPD (Chronic Obstructive Pulmonary Disease)": (
    "ХОЗЛ — хронічне обструктивне захворювання легенів",
    "A chronic inflammatory lung disease that causes obstructed airflow from the lungs, commonly caused by long-term smoking."
),
"EKG/ECG (Electrocardiogram)": (
    "ЕКГ — електрокардіограма",
    "A test that records the electrical activity of the heart, used to detect heart problems."
),
"BMI (Body Mass Index)": (
    "ІМТ — індекс маси тіла",
    "A measure of body fat based on height and weight. Used to categorize individuals as underweight, normal, overweight, or obese."
),
"BP (Blood Pressure)": (
    "АТ — артеріальний тиск",
    "The pressure of circulating blood against the walls of blood vessels. Measured as systolic over diastolic, for example 120 over 80."
),
"HR (Heart Rate)": (
    "ЧСС — частота серцевих скорочень",
    "The number of times the heart beats per minute. Used to assess cardiovascular health."
),
"CBC (Complete Blood Count)": (
    "ЗАК — загальний аналіз крові",
    "A blood test that measures the levels of red blood cells, white blood cells, and platelets, giving an overview of overall health."
),
"UTI (Urinary Tract Infection)": (
    "ІСШ — інфекція сечовивідних шляхів",
    "An infection in any part of the urinary system, including kidneys, bladder, or urethra. Causes frequent, painful urination."
),
"STI (Sexually Transmitted Infection)": (
    "ІПСШ — інфекція, що передається статевим шляхом",
    "An infection spread primarily through sexual contact, such as chlamydia, gonorrhea, or syphilis."
),
"HIV (Human Immunodeficiency Virus)": (
    "ВІЛ — вірус імунодефіциту людини",
    "A virus that attacks the immune system. If untreated, it can lead to AIDS."
),
"AIDS (Acquired Immunodeficiency Syndrome)": (
    "СНІД — синдром набутого імунодефіциту",
    "The most advanced stage of HIV infection, in which the immune system is severely damaged and the body cannot fight infections."
),
"TB (Tuberculosis)": (
    "ТБ — туберкульоз",
    "A serious bacterial infection that mainly affects the lungs, spread through the air when an infected person coughs or sneezes."
),
"GI (Gastrointestinal)": (
    "ШКТ — шлунково-кишковий тракт",
    "Relating to the stomach and intestines. GI issues include conditions like ulcers, Crohn's disease, and irritable bowel syndrome."
),
"OB/GYN (Obstetrics/Gynecology)": (
    "Акушерство та Гінекологія",
    "A medical specialty covering pregnancy and childbirth, as well as the female reproductive system."
),

# ════════════════════════════════════════════════════════════
# SECTION 3 — MEDICATIONS (13 terms)
# ════════════════════════════════════════════════════════════
"Brand Name": (
    "Торгова назва",
    "The commercial name given to a drug by the manufacturer. For example, Tylenol is the brand name for acetaminophen."
),
"Generic Name": (
    "Міжнародна непатентована назва",
    "The official, non-proprietary name of a drug. Generic versions contain the same active ingredient as the brand-name drug but are usually less expensive."
),
"Over-the-Counter (OTC)": (
    "Безрецептурний препарат",
    "Medications that can be purchased without a prescription, such as aspirin or cold medicine."
),
"Dosage": (
    "Дозування",
    "The specific amount and frequency of a medication to be taken. For example, 500 milligrams twice a day."
),
"Side Effects": (
    "Побічні ефекти",
    "Unintended effects caused by a medication in addition to its intended effect. For example, drowsiness caused by antihistamines."
),
"Drug Interactions": (
    "Взаємодія ліків",
    "When two or more medications taken together change how each drug works, potentially causing harmful effects."
),
"Refill": (
    "Поповнення рецепту",
    "An additional supply of a prescription medication authorized by the doctor and dispensed by the pharmacy."
),
"Pharmacy": (
    "Аптека",
    "A store or department where prescription and over-the-counter medications are dispensed and sold."
),
"Pharmacist": (
    "Фармацевт",
    "A licensed healthcare professional trained in dispensing medications and advising patients on their safe use."
),
"Controlled Substance": (
    "Контрольована речовина",
    "A drug regulated by the government due to its potential for abuse or addiction. These require special prescriptions."
),
"Narcotics": (
    "Наркотичні речовини",
    "Powerful pain-relieving drugs that can be addictive if misused, such as opioids. They are a category of controlled substances."
),
"Supplement": (
    "Харчова добавка",
    "A product taken to add nutrients to the diet or to lower the risk of health problems, such as vitamins, minerals, or herbal products."
),
"Prescription (medication)": (
    "Рецептурний препарат",
    "A medication that requires a doctor's written authorization and cannot be purchased over the counter."
),

# ════════════════════════════════════════════════════════════
# SECTION 4 — ROUTINE VISITS (29 terms)
# ════════════════════════════════════════════════════════════
"Annual Check-up": (
    "Щорічний медичний огляд",
    "A yearly visit to the doctor for a general health review, even when the patient is not sick."
),
"Physical Exam": (
    "Фізикальний огляд",
    "A thorough head-to-toe examination by a doctor to assess overall health and detect any problems."
),
"Pap Smear": (
    "ПАП-тест",
    "A screening test for cervical cancer in women, where cells from the cervix are collected and examined."
),
"Mammogram": (
    "Мамографія",
    "An X-ray of the breast used to detect early signs of breast cancer."
),
"Colonoscopy": (
    "Колоноскопія",
    "A procedure where a flexible camera is inserted into the colon to examine it for polyps, cancer, or other abnormalities."
),
"Eye Exam": (
    "Огляд очей",
    "An evaluation of vision and eye health by an optometrist or ophthalmologist."
),
"Dental Exam": (
    "Стоматологічний огляд",
    "A routine check of teeth, gums, and mouth by a dentist to detect cavities, gum disease, or other issues."
),
"Well-Child Visit": (
    "Плановий педіатричний огляд",
    "A routine checkup for children at specific ages to monitor growth, development, and receive vaccinations."
),
"Immunization Record": (
    "Карта вакцинації",
    "A document listing all vaccines a person has received, including dates and types."
),
"Height and Weight": (
    "Зріст і вага",
    "Measurements routinely taken at medical visits to monitor growth and calculate BMI."
),
"Blood Pressure Check": (
    "Вимірювання артеріального тиску",
    "A routine measurement of the force of blood against artery walls using a blood pressure cuff."
),
"Urinalysis": (
    "Загальний аналіз сечі",
    "A lab test of a urine sample to detect signs of infection, kidney disease, diabetes, or other conditions."
),
"Cholesterol Test": (
    "Аналіз на холестерин",
    "A blood test measuring levels of cholesterol and triglycerides to assess cardiovascular risk."
),
"Blood Glucose Test": (
    "Аналіз на глюкозу крові",
    "A test that measures the amount of sugar in the blood, used to diagnose and monitor diabetes."
),
"Prostate Exam": (
    "Дослідження простати",
    "An examination to check the health of the prostate gland in men, often including a blood test and physical check."
),
"Skin Cancer Screening": (
    "Скринінг раку шкіри",
    "A visual examination of the skin by a dermatologist to detect suspicious moles or lesions that may be cancerous."
),
"STI Screening": (
    "Скринінг ІПСШ",
    "Testing for sexually transmitted infections, recommended regularly for sexually active individuals."
),
"Depression Screening": (
    "Скринінг депресії",
    "A questionnaire or assessment used to identify symptoms of depression and evaluate the need for treatment."
),
"Hearing Test": (
    "Тест на слух",
    "An evaluation of hearing ability conducted by an audiologist to detect hearing loss."
),
"Bone Density Test": (
    "Денситометрія",
    "A scan that measures the strength and density of bones, used to detect osteoporosis."
),
"Thyroid Function Test": (
    "Аналіз функції щитовидної залози",
    "A blood test measuring thyroid hormone levels to detect conditions like hypothyroidism or hyperthyroidism."
),
"Vitamin D Level": (
    "Рівень вітаміну D",
    "A blood test measuring vitamin D, which is essential for bone health and immune function."
),
"Iron Level": (
    "Рівень заліза",
    "A blood test that measures iron in the blood. Low iron levels can lead to anemia."
),
"Liver Function Test": (
    "Аналіз функції печінки",
    "A blood test that checks how well the liver is working by measuring enzymes and proteins it produces."
),
"Kidney Function Test": (
    "Аналіз функції нирок",
    "A blood or urine test that checks how well the kidneys are filtering waste from the blood."
),
"Follow-up Appointment": (
    "Повторний прийом",
    "A scheduled visit after an initial appointment or treatment to monitor progress or adjust care."
),
"Medical History": (
    "Медична історія",
    "A record of a person's past illnesses, surgeries, medications, allergies, and family health conditions."
),
"Vital Signs": (
    "Показники життєдіяльності",
    "Basic measurements of bodily functions including temperature, pulse, breathing rate, and blood pressure."
),

# ════════════════════════════════════════════════════════════
# SECTION 5 — SPECIALTY CARE (39 terms)
# ════════════════════════════════════════════════════════════
"Internal medicine doctors": (
    "Лікарі внутрішньої медицини",
    "Physicians who specialize in the prevention, diagnosis, and treatment of adult diseases."
),
"Pediatricians": (
    "Педіатри",
    "Doctors who specialize in the health and medical care of infants, children, and adolescents."
),
"Family medicine doctors": (
    "Лікарі сімейної медицини",
    "Physicians who provide comprehensive care for patients of all ages, serving as the primary care provider for families."
),
"Obstetricians and gynecologists": (
    "Акушери-гінекологи",
    "Doctors specializing in pregnancy, childbirth, and the female reproductive system."
),
"Cardiologists": (
    "Кардіологи",
    "Specialists in the diagnosis and treatment of heart and cardiovascular diseases."
),
"Orthopedic surgeons": (
    "Ортопедичні хірурги",
    "Surgeons who treat conditions involving bones, joints, ligaments, tendons, and muscles."
),
"Dermatologists": (
    "Дерматологи",
    "Doctors who diagnose and treat conditions of the skin, hair, and nails."
),
"Ophthalmologists": (
    "Офтальмологи",
    "Medical doctors who specialize in eye and vision care, including surgery."
),
"Psychiatrists": (
    "Психіатри",
    "Medical doctors who specialize in mental health disorders, including depression, anxiety, and schizophrenia. They can prescribe medication."
),
"Urologists": (
    "Урологи",
    "Doctors who treat conditions of the urinary tract in men and women, and the male reproductive system."
),
"Neurologists": (
    "Неврологи",
    "Specialists in disorders of the brain, spinal cord, and nervous system, such as epilepsy, stroke, and Parkinson's disease."
),
"Endocrinologists": (
    "Ендокринологи",
    "Doctors who treat hormonal disorders, including diabetes, thyroid disease, and hormonal imbalances."
),
"Gastroenterologists": (
    "Гастроентерологи",
    "Specialists in diseases of the digestive system, including the stomach, intestines, liver, and pancreas."
),
"Rheumatologists": (
    "Ревматологи",
    "Doctors who treat autoimmune and inflammatory diseases affecting joints, muscles, and bones, such as arthritis and lupus."
),
"Pulmonologists": (
    "Пульмонологи",
    "Specialists in lung and respiratory system diseases, such as asthma, COPD, and pneumonia."
),
"Oncologists": (
    "Онкологи",
    "Doctors who specialize in the diagnosis and treatment of cancer."
),
"Hematologists": (
    "Гематологи",
    "Specialists in blood disorders, including anemia, clotting problems, and blood cancers like leukemia."
),
"Nephrologists": (
    "Нефрологи",
    "Doctors who specialize in kidney diseases and conditions such as chronic kidney disease and kidney failure."
),
"Infectious disease specialists": (
    "Спеціалісти з інфекційних хвороб",
    "Doctors who diagnose and treat complex infections caused by bacteria, viruses, fungi, or parasites."
),
"Allergists": (
    "Алергологи",
    "Doctors who diagnose and treat allergies, asthma, and immune system disorders."
),
"Immunologists": (
    "Імунологи",
    "Specialists in disorders of the immune system, including autoimmune diseases and immunodeficiency conditions."
),
"Surgeons": (
    "Хірурги",
    "Doctors trained to perform operations to treat injuries, diseases, or deformities."
),
"Anesthesiologists": (
    "Анестезіологи",
    "Doctors who administer anesthesia and monitor patients before, during, and after surgical procedures."
),
"Radiologists": (
    "Радіологи",
    "Doctors who specialize in interpreting medical images such as X-rays, MRIs, and CT scans."
),
"Pathologists": (
    "Патологоанатоми",
    "Doctors who examine tissue samples in the lab to diagnose diseases, including cancer."
),
"Emergency medicine doctors": (
    "Лікарі швидкої допомоги",
    "Physicians who specialize in treating urgent and life-threatening conditions in the emergency room."
),
"Physical therapists": (
    "Фізіотерапевти",
    "Healthcare professionals who help patients recover movement and manage pain through exercises and physical treatments."
),
"Occupational therapists": (
    "Ерготерапевти",
    "Therapists who help patients regain the ability to perform daily activities after illness or injury."
),
"Speech therapists": (
    "Логопеди",
    "Specialists who assess and treat communication disorders and swallowing difficulties."
),
"Audiologists": (
    "Аудіологи",
    "Healthcare professionals who diagnose and treat hearing and balance disorders."
),
"Optometrists": (
    "Оптометристи",
    "Eye care providers who examine vision and prescribe glasses or contact lenses. They are not medical doctors."
),
"Dentists": (
    "Стоматологи",
    "Healthcare professionals who diagnose and treat conditions of the teeth and mouth."
),
"Oral surgeons": (
    "Щелепно-лицьові хірурги",
    "Specialists who perform surgery on the mouth, jaw, and face, including tooth extractions and jaw reconstruction."
),
"Orthodontists": (
    "Ортодонти",
    "Dental specialists who correct irregularities of the teeth and jaw, using braces or aligners."
),
"Chiropractors": (
    "Мануальні терапевти",
    "Healthcare professionals who treat musculoskeletal disorders, mainly through spinal manipulation and adjustment."
),
"Podiatrists": (
    "Подіатри",
    "Specialists in disorders of the foot, ankle, and lower leg."
),
"Dietitians/Nutritionists": (
    "Дієтологи та Нутриціоністи",
    "Experts in food and nutrition who advise patients on healthy eating and manage diet-related conditions."
),
"Social workers": (
    "Соціальні працівники",
    "Professionals who help patients and families access resources and services, and provide counseling support."
),
"Psychologists": (
    "Психологи",
    "Mental health professionals who assess and treat psychological disorders through therapy. Unlike psychiatrists, they typically cannot prescribe medication."
),

# ════════════════════════════════════════════════════════════
# SECTION 6 — PAIN DESCRIPTORS (selected 40 most important)
# ════════════════════════════════════════════════════════════
"Abrupt": ("Раптовий", "Sudden in onset. Pain that starts very quickly without warning."),
"Aching": ("Той, що болить", "A dull, persistent pain, like a sore muscle."),
"Acute": ("Гострий", "Severe and short-lived pain, usually with a sudden onset."),
"Bearable": ("Терпимий", "Pain that is uncomfortable but can be tolerated without medication."),
"Burning": ("Пекучий", "A pain that feels like heat or fire on or under the skin."),
"Chronic": ("Хронічний", "Pain that persists for a long time, typically more than three months."),
"Constant": ("Постійний", "Pain that does not stop or go away. Always present."),
"Cramping": ("Судомний", "A tight, squeezing pain caused by a muscle contraction, like a leg cramp or menstrual pain."),
"Crushing": ("Розчавлюючий", "An extremely heavy, pressing pain, often associated with a heart attack."),
"Debilitating": ("Виснажливий", "Pain so severe that it prevents the person from functioning normally."),
"Deep": ("Глибокий", "Pain that is felt inside the body rather than on the surface."),
"Dull": ("Тупий", "A low-intensity, diffuse pain that is not sharp."),
"Excruciating": ("Нестерпний", "The most intense level of pain. Unbearable and overwhelming."),
"Intermittent": ("Переривчастий", "Pain that comes and goes at intervals rather than being constant."),
"Lancinating": ("Стріляючий", "Sharp, cutting, stabbing pain. Like being cut with a knife."),
"Localized": ("Локалізований", "Pain confined to a specific area of the body."),
"Mild": ("Легкий", "Low-level pain that is noticeable but does not significantly interfere with daily activities."),
"Moderate": ("Помірний", "Pain of medium intensity. Noticeable and affecting daily function but not overwhelming."),
"Numbness": ("Оніміння", "A loss of sensation or feeling in a body part."),
"Persistent": ("Стійкий", "Pain that continues without relief."),
"Piercing": ("Пронизливий", "An intense, penetrating sharp pain."),
"Pins and needles": ("Поколювання", "A tingling sensation in a body part, as if tiny pins are being stuck into it, often from reduced blood flow."),
"Pressure": ("Тиснучий", "A pain that feels like something is pressing or squeezing from the outside."),
"Pulsating": ("Пульсуючий", "Pain that throbs in rhythm with the heartbeat, like a bad toothache or headache."),
"Radiating": ("Іррадіюючий", "Pain that spreads from its origin to other parts of the body, like sciatic nerve pain moving down the leg."),
"Recurring": ("Повторний", "Pain that goes away and then comes back repeatedly."),
"Severe": ("Тяжкий", "Intense pain that significantly impacts daily life and requires medical attention."),
"Sharp": ("Гострий", "A sudden, intense, and clearly defined pain, like being cut."),
"Shooting": ("Стріляючий", "Pain that travels quickly along a nerve, like an electric shock."),
"Sore": ("Болючий", "Tenderness or pain in a muscle or area of the body, especially after injury or overuse."),
"Spasmodic": ("Спазматичний", "Pain that occurs in sudden, involuntary muscle contractions."),
"Stabbing": ("Колючий", "Sudden, sharp, intense pain, like being stabbed."),
"Stinging": ("Пекучий", "A sharp, superficial burning pain, like a bee sting."),
"Tender": ("Чутливий до дотику", "Pain that occurs when the affected area is touched or pressed."),
"Throbbing": ("Пульсуючий", "A beating or pounding pain that intensifies with each heartbeat."),
"Tingling": ("Поколювання", "A slight prickling or stinging sensation, like pins and needles."),
"Unbearable": ("Нестерпний", "Pain that is too intense to tolerate without medical intervention."),
"Vague": ("Невизначений", "Pain that is difficult to describe precisely or to locate accurately."),
"Wandering": ("Блукаючий", "Pain that moves from one location in the body to another."),
"Worsening": ("Наростаючий", "Pain that is increasing in intensity over time."),

# ════════════════════════════════════════════════════════════
# SECTION 7 — ANATOMY (selected 50 key terms)
# ════════════════════════════════════════════════════════════
"Clavicle": ("Ключиця", "The collarbone. A long bone that connects the shoulder to the breastbone."),
"Femur": ("Стегнова кістка", "The thigh bone. The longest and strongest bone in the human body."),
"Fibula": ("Мала гомілкова кістка", "The thinner of the two bones in the lower leg, running alongside the tibia."),
"Humerus": ("Плечова кістка", "The upper arm bone, connecting the shoulder to the elbow."),
"Patella": ("Колінна чашечка", "The kneecap. A small, flat bone at the front of the knee joint."),
"Pelvis": ("Таз", "The bony structure at the base of the spine that supports the abdominal organs."),
"Scapula": ("Лопатка", "The shoulder blade. A flat, triangular bone at the back of the shoulder."),
"Skull": ("Череп", "The bony structure that encloses and protects the brain."),
"Spine": ("Хребет", "The backbone or vertebral column. A series of bones that protect the spinal cord and support the body."),
"Sternum": ("Грудина", "The breastbone. A flat bone in the center of the chest."),
"Tibia": ("Велика гомілкова кістка", "The shinbone. The larger of the two bones in the lower leg."),
"Achilles tendon": ("Ахіллесове сухожилля", "The large tendon connecting the calf muscle to the heel bone. The strongest tendon in the body."),
"Ligament": ("Зв'язка", "A tough band of fibrous tissue that connects bones to other bones at a joint."),
"Tendon": ("Сухожилля", "A tough cord of fibrous tissue that connects a muscle to a bone."),
"Aorta": ("Аорта", "The largest artery in the body, carrying oxygenated blood from the heart to the rest of the body."),
"Artery": ("Артерія", "A blood vessel that carries oxygenated blood away from the heart to the body's tissues."),
"Vein": ("Вена", "A blood vessel that carries deoxygenated blood back to the heart."),
"Appendix": ("Апендикс", "A small pouch attached to the large intestine. Its exact function is unclear, but inflammation causes appendicitis."),
"Colon": ("Товста кишка", "The large intestine. It absorbs water from digested food and passes waste to the rectum."),
"Esophagus": ("Стравохід", "The muscular tube connecting the throat to the stomach, through which food passes."),
"Gallbladder": ("Жовчний міхур", "A small organ beneath the liver that stores bile, a fluid that helps digest fats."),
"Liver": ("Печінка", "The largest internal organ. It filters blood, produces bile, and processes nutrients."),
"Pancreas": ("Підшлункова залоза", "A gland that produces digestive enzymes and insulin to regulate blood sugar."),
"Stomach": ("Шлунок", "The muscular organ that receives food from the esophagus and begins the digestion process."),
"Bladder": ("Сечовий міхур", "A hollow organ in the pelvis that stores urine until it is expelled from the body."),
"Kidney": ("Нирка", "One of two bean-shaped organs that filter waste from the blood and produce urine."),
"Ovary": ("Яєчник", "One of two female reproductive organs that produce eggs and the hormones estrogen and progesterone."),
"Prostate": ("Простата", "A gland in the male reproductive system that produces fluid that nourishes sperm."),
"Thyroid": ("Щитовидна залоза", "A butterfly-shaped gland in the neck that produces hormones regulating metabolism."),
"Uterus": ("Матка", "The womb. The organ in the female pelvis where a fetus develops during pregnancy."),
"Lung": ("Легеня", "One of two organs in the chest responsible for gas exchange, bringing oxygen into the blood and removing carbon dioxide."),
"Trachea": ("Трахея", "The windpipe. A tube that carries air from the throat to the lungs."),
"Brain": ("Мозок", "The organ inside the skull that controls all body functions, thought, memory, and emotion."),
"Spinal cord": ("Спинний мозок", "A bundle of nerves running through the spine that carries signals between the brain and the body."),
"Cornea": ("Рогівка", "The transparent front layer of the eye that covers the iris and pupil."),
"Retina": ("Сітківка", "The light-sensitive layer at the back of the eye that sends visual signals to the brain."),
"Lymph node": ("Лімфатичний вузол", "Small, bean-shaped glands that filter lymph fluid and are part of the immune system."),
"Spleen": ("Селезінка", "An organ that filters blood and plays a role in immune function."),
"Skin (dermis)": ("Шкіра — дерма", "The outer covering of the body. The largest organ, protecting against injury, infection, and temperature changes."),
"Ankle": ("Кісточка", "The joint connecting the foot to the lower leg."),
"Elbow": ("Лікоть", "The joint between the upper and lower arm."),
"Knee": ("Коліно", "The joint between the upper and lower leg."),
"Shoulder": ("Плече", "The joint where the arm connects to the body."),
"Wrist": ("Зап'ясток", "The joint between the hand and the forearm."),
"Hip": ("Стегно", "The joint where the thigh bone meets the pelvis."),
"Heel": ("П'ята", "The back portion of the foot."),

# ════════════════════════════════════════════════════════════
# SECTION 8 — MEDICAL INSURANCE (key terms)
# ════════════════════════════════════════════════════════════
"ACA (Affordable Care Act)": (
    "Закон про доступну медичну допомогу",
    "A US federal law enacted in 2010 that expanded access to health insurance and added consumer protections."
),
"Allowed Amount": (
    "Дозволена сума",
    "The maximum amount an insurance plan will pay for a covered service. The patient may owe the difference."
),
"Coinsurance": (
    "Співстрахування",
    "The percentage of costs the patient pays after meeting their deductible. For example, 20% coinsurance means the patient pays 20% and the insurer pays 80%."
),
"Copayment (Copay)": (
    "Співплата",
    "A fixed amount the patient pays for a covered service, such as 20 dollars for a doctor visit."
),
"Cost Sharing": (
    "Розподіл витрат",
    "The portion of healthcare costs paid by the patient, including deductibles, copays, and coinsurance."
),
"Deductible": (
    "Франшиза",
    "The amount a patient must pay out-of-pocket for healthcare services each year before the insurance begins to pay."
),
"Dependent": (
    "Залежний",
    "A person, typically a spouse or child, who is covered under another person's health insurance plan."
),
"Drug Formulary": (
    "Перелік лікарських препаратів",
    "A list of prescription drugs covered by an insurance plan, often organized into tiers based on cost."
),
"Durable Medical Equipment (DME)": (
    "Медичне обладнання тривалого користування",
    "Equipment prescribed by a doctor for home use, such as wheelchairs, oxygen equipment, or hospital beds."
),
"EOB (Explanation of Benefits)": (
    "Пояснення щодо виплат",
    "A document sent by the insurance company after a claim, explaining what was covered and what the patient owes."
),
"Essential Health Benefits": (
    "Основні медичні послуги",
    "Ten categories of services that must be covered by plans sold under the ACA, including hospitalization, maternity care, and mental health services."
),
"Fee-for-Service (FFS)": (
    "Оплата за надані послуги",
    "A payment model where providers are paid separately for each service provided."
),
"FSA (Flexible Spending Account)": (
    "Рахунок для гнучких витрат",
    "An employer-sponsored account where employees set aside pre-tax money to pay for eligible medical expenses."
),
"Grace Period": (
    "Пільговий період",
    "A period of time after the payment due date during which the insurance policy remains in effect while the overdue payment can still be made."
),
"HMO (Health Maintenance Organization)": (
    "Організація з підтримки здоров'я",
    "A type of health insurance plan that requires members to use a network of specific doctors and get referrals to see specialists."
),
"HSA (Health Savings Account)": (
    "Рахунок медичних ощадних витрат",
    "A tax-advantaged savings account for individuals with high-deductible health plans to save and pay for medical expenses."
),
"In-Network": (
    "Внутрішньомережеві",
    "Providers who have contracted with an insurance plan. Patients pay less for in-network care."
),
"Maximum Out-of-Pocket": (
    "Максимальна сума власних витрат",
    "The most a patient will have to pay for covered services in a plan year. After reaching this limit, insurance covers 100%."
),
"Medically Necessary": (
    "Медична необхідність",
    "Healthcare services or supplies that are needed to diagnose or treat an illness, injury, or condition."
),
"Open Enrollment Period": (
    "Період відкритої реєстрації",
    "A specific period each year when people can sign up for or change their health insurance plan."
),
"Out-of-Network": (
    "Позамережеві",
    "Providers who have not contracted with an insurance plan. Patients typically pay more for out-of-network care."
),
"PCP (Primary Care Provider)": (
    "Постачальник первинної медичної допомоги",
    "A doctor, nurse practitioner, or physician assistant who provides general healthcare and refers patients to specialists."
),
"PPO (Preferred Provider Organization)": (
    "Організація пріоритетного постачальника",
    "A type of health plan that allows patients to see any doctor without a referral, but costs less when using in-network providers."
),
"Preauthorization (Precertification)": (
    "Попередня авторизація",
    "Approval required from the insurance company before receiving certain medical services or medications."
),
"Pre-Existing Condition": (
    "Наявний стан здоров'я",
    "A health condition that existed before the patient enrolled in a health plan. Under the ACA, insurers cannot deny coverage for pre-existing conditions."
),
"Premium": (
    "Страховий внесок",
    "The monthly amount paid for health insurance coverage, regardless of whether medical services are used."
),
"Prior Authorization": (
    "Попередня авторизація",
    "Approval required from the insurer before a specific service, procedure, or medication can be covered."
),
"Referral": (
    "Направлення до спеціаліста",
    "A recommendation from a primary care provider for a patient to see a specialist for further evaluation or treatment."
),
"Special Enrollment Period": (
    "Спеціальний період реєстрації",
    "A time outside the open enrollment period when a person can sign up for health insurance due to a qualifying life event, such as marriage or job loss."
),
"Subsidy": (
    "Субсидія",
    "Financial assistance provided by the government to help lower-income individuals pay for health insurance premiums."
),
"Telehealth": (
    "Телемедицина",
    "Healthcare services delivered remotely using technology, such as video calls or phone consultations with a doctor."
),
"Deductible (Medicaid context)": (
    "Франшиза в контексті Medicaid",
    "In Medicaid, the share of costs a beneficiary must pay before Medicaid begins paying for services."
),
"Medicaid": (
    "Medicaid",
    "A joint federal and state program that provides free or low-cost health coverage to eligible low-income adults, children, pregnant women, and people with disabilities."
),
"Medicare": (
    "Medicare",
    "A federal health insurance program for people aged 65 and older, and for some younger people with disabilities."
),
"Medicare Part A": (
    "Medicare Частина A",
    "Covers inpatient hospital care, skilled nursing facility care, hospice, and some home health services."
),
"Medicare Part B": (
    "Medicare Частина B",
    "Covers outpatient care, doctor visits, preventive services, and medical equipment."
),
"Medicare Part C": (
    "Medicare Частина C — Medicare Advantage",
    "An alternative to original Medicare offered by private insurers, often including drug coverage."
),
"Medicare Part D": (
    "Medicare Частина D",
    "Adds prescription drug coverage to Medicare. Offered through private insurers."
),
"Beneficiary": (
    "Бенефіціар — вигодонабувач",
    "A person who is covered by and receives benefits from an insurance plan."
),
"Coordination of Benefits (COB)": (
    "Координація виплат",
    "A process used when a patient has two or more health insurance plans to determine which plan pays first and how much each plan pays."
),
"Waiting Period": (
    "Період очікування",
    "The time between enrolling in a health plan and when coverage actually begins."
),
"Wellness Program": (
    "Програма оздоровлення",
    "A program offered by employers or insurers to encourage healthy behaviors, such as fitness challenges or smoking cessation support."
),
}

# ── Build narration script ─────────────────────────────────────────────────────

SECTIONS = [
    ("GENERAL MEDICAL VOCABULARY",   [k for k in GLOSSARY if k in [
        "Bloodwork","Anemia","Weight gain","Weight loss","High blood pressure",
        "Low blood pressure","Diabetes","Cholesterol","Blood sugar","Heart rate",
        "Pulse","Fever","Nausea","Vomiting","Diarrhea","Constipation","Fatigue",
        "Shortness of breath","Chest pain","Rash","Swelling","Infection",
        "Inflammation","Fracture","Sprain","Allergy","Asthma","Cancer","Stroke",
        "Heart attack","Seizure","Migraine","Arthritis","Pregnancy","Miscarriage",
        "Discharge","Urine","Stool","X-ray","MRI","Ultrasound","Biopsy","Surgery",
        "Anesthesia","Wound","Sutures","Catheter","IV (Intravenous)","Vaccination",
        "Immunization","Blood type","Platelet","White blood cell","Red blood cell",
        "Hemoglobin","Antibiotic","Antiviral","Anti-inflammatory","Painkiller",
        "Insulin","Blood pressure cuff","Stethoscope","Thermometer","Oxygen",
        "Ventilator","Intubation","CPR","AED","Emergency","ICU","ER (Emergency Room)",
        "Ambulance","Discharge (hospital)","Referral","Prescription"
    ]]),
    ("MEDICAL PROCEDURE ACRONYMS",   [k for k in GLOSSARY if k in [
        "CAT scan (Computer Axial Tomography)","DPT (Diphtheria, Pertussis, Tetanus)",
        "PCOS (Polycystic Ovarian Syndrome)","COPD (Chronic Obstructive Pulmonary Disease)",
        "EKG/ECG (Electrocardiogram)","BMI (Body Mass Index)","BP (Blood Pressure)",
        "HR (Heart Rate)","CBC (Complete Blood Count)","UTI (Urinary Tract Infection)",
        "STI (Sexually Transmitted Infection)","HIV (Human Immunodeficiency Virus)",
        "AIDS (Acquired Immunodeficiency Syndrome)","TB (Tuberculosis)",
        "GI (Gastrointestinal)","OB/GYN (Obstetrics/Gynecology)"
    ]]),
    ("MEDICATIONS",                  [k for k in GLOSSARY if k in [
        "Brand Name","Generic Name","Over-the-Counter (OTC)","Dosage","Side Effects",
        "Drug Interactions","Refill","Pharmacy","Pharmacist","Controlled Substance",
        "Narcotics","Supplement","Prescription (medication)"
    ]]),
    ("ROUTINE VISITS",               [k for k in GLOSSARY if k in [
        "Annual Check-up","Physical Exam","Pap Smear","Mammogram","Colonoscopy",
        "Eye Exam","Dental Exam","Well-Child Visit","Immunization Record",
        "Height and Weight","Blood Pressure Check","Urinalysis","Cholesterol Test",
        "Blood Glucose Test","Prostate Exam","Skin Cancer Screening","STI Screening",
        "Depression Screening","Hearing Test","Bone Density Test","Thyroid Function Test",
        "Vitamin D Level","Iron Level","Liver Function Test","Kidney Function Test",
        "Follow-up Appointment","Medical History","Vital Signs"
    ]]),
    ("MEDICAL SPECIALISTS",          [k for k in GLOSSARY if k in [
        "Internal medicine doctors","Pediatricians","Family medicine doctors",
        "Obstetricians and gynecologists","Cardiologists","Orthopedic surgeons",
        "Dermatologists","Ophthalmologists","Psychiatrists","Urologists","Neurologists",
        "Endocrinologists","Gastroenterologists","Rheumatologists","Pulmonologists",
        "Oncologists","Hematologists","Nephrologists","Infectious disease specialists",
        "Allergists","Immunologists","Surgeons","Anesthesiologists","Radiologists",
        "Pathologists","Emergency medicine doctors","Physical therapists",
        "Occupational therapists","Speech therapists","Audiologists","Optometrists",
        "Dentists","Oral surgeons","Orthodontists","Chiropractors","Podiatrists",
        "Dietitians/Nutritionists","Social workers","Psychologists"
    ]]),
    ("PAIN DESCRIPTORS",             [k for k in GLOSSARY if k in [
        "Abrupt","Aching","Acute","Bearable","Burning","Chronic","Constant",
        "Cramping","Crushing","Debilitating","Deep","Dull","Excruciating",
        "Intermittent","Lancinating","Localized","Mild","Moderate","Numbness",
        "Persistent","Piercing","Pins and needles","Pressure","Pulsating",
        "Radiating","Recurring","Severe","Sharp","Shooting","Sore","Spasmodic",
        "Stabbing","Stinging","Tender","Throbbing","Tingling","Unbearable",
        "Vague","Wandering","Worsening"
    ]]),
    ("HUMAN ANATOMY",                [k for k in GLOSSARY if k in [
        "Clavicle","Femur","Fibula","Humerus","Patella","Pelvis","Scapula","Skull",
        "Spine","Sternum","Tibia","Achilles tendon","Ligament","Tendon","Aorta",
        "Artery","Vein","Appendix","Colon","Esophagus","Gallbladder","Liver",
        "Pancreas","Stomach","Bladder","Kidney","Ovary","Prostate","Thyroid",
        "Uterus","Lung","Trachea","Brain","Spinal cord","Cornea","Retina",
        "Lymph node","Spleen","Skin (dermis)","Ankle","Elbow","Knee","Shoulder",
        "Wrist","Hip","Heel"
    ]]),
    ("MEDICAL INSURANCE TERMS",      [k for k in GLOSSARY if k in [
        "ACA (Affordable Care Act)","Allowed Amount","Coinsurance","Copayment (Copay)",
        "Cost Sharing","Deductible","Dependent","Drug Formulary",
        "Durable Medical Equipment (DME)","EOB (Explanation of Benefits)",
        "Essential Health Benefits","Fee-for-Service (FFS)",
        "FSA (Flexible Spending Account)","Grace Period",
        "HMO (Health Maintenance Organization)","HSA (Health Savings Account)",
        "In-Network","Maximum Out-of-Pocket","Medically Necessary",
        "Open Enrollment Period","Out-of-Network","PCP (Primary Care Provider)",
        "PPO (Preferred Provider Organization)","Preauthorization (Precertification)",
        "Pre-Existing Condition","Premium","Prior Authorization","Referral",
        "Special Enrollment Period","Subsidy","Telehealth",
        "Medicaid","Medicare","Medicare Part A","Medicare Part B",
        "Medicare Part C","Medicare Part D","Beneficiary",
        "Coordination of Benefits (COB)","Waiting Period","Wellness Program"
    ]]),
]

def build_script():
    total = sum(len(terms) for _, terms in SECTIONS)
    lines = []
    lines.append(
        "EQT Ukrainian Interpreter Glossary. Audio Edition. "
        f"{total} terms across 8 sections. "
        "Each entry is read in English, then Ukrainian, followed by a brief description. "
        "Use this to build automatic recall while on the go."
    )
    lines.append("")

    for section_name, term_keys in SECTIONS:
        present = [k for k in term_keys if k in GLOSSARY]
        if not present:
            continue
        lines.append(f"Section: {section_name}. {len(present)} terms.")
        lines.append("")
        for key in present:
            uk, desc = GLOSSARY[key]
            lines.append(f"{key}.")
            lines.append(f"{uk}.")
            lines.append(f"{desc}")
            lines.append("")   # natural pause

    lines.append(f"End of glossary. {total} terms covered. You are well prepared. Good luck.")
    return "\n".join(lines)


async def main():
    output = "glossary_audiobook.mp3"
    print("Building narration script...")
    script = build_script()
    total_terms = sum(len(t) for _, t in SECTIONS)
    print(f"  {len(script):,} characters | ~{total_terms} terms with descriptions")
    print(f"  Voice: en-US-ChristopherNeural (clear, authoritative)")
    print(f"  Speed: -8% (slightly slower for clarity)")
    print(f"\nGenerating audio... this takes ~30-60 seconds...")

    comm = edge_tts.Communicate(script, "en-US-ChristopherNeural", rate="-8%", pitch="+0Hz")
    await comm.save(output)

    mb = os.path.getsize(output) / 1024 / 1024
    print(f"\n✅ Done! {output} — {mb:.1f} MB")
    print(f"   Open with: open {output}")
    os.system(f"open '{output}'")

if __name__ == "__main__":
    asyncio.run(main())
