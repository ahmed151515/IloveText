from src.functions import IsToxic, translate, summarize, detect_language

text = "يقول مونتاني في مقدمة كتابه (محاولات أو تجارب):\
«إن هذا الكتاب حسن الطوية فهو ينبهك منذ البداية إني لا أستهدف من ورائه مقصداً إلا ما ينفع العام والخاص، ولم أرد به خدمتك أو إعلاء ذكرى فإن مواهبي تعجز عن تحقيق مثل هذه الغاية... لقد خصصته لمنفعة الخاصة من أهلي وأصدقائي حتى إذا ما افتقدوني استطاعوا أن يجدوا فيه صورة لطباعي وميولي، فيسترجعوا ذكراي التي خلفتها لهم حيّة كاملة ولو كان هدفي أن أظفر بإعجاب العالم لعملت على إطراء نفسي وإظهارها بطريقة منمّقة ولكني أريد أن أعرف في أبسط صوري الطبيعية العادية دون تكلف ولا تصنع لأني أنا الذي أصوّر نفسي لهذا تبرز مساوئي واضحة وسجيتي على طبيعتها ما سمح لي العرف بذلك...»\
يتضح في مقدمة كتاب ابن الجوزي صيد الخاطر إنما كتب هذه الفصول ليسجّل فيها خواطره التي أثارتها تجاربه وعلاقاته مع الأشياء. وهذه الخواطر ليست وليدة البحث والدرس العميق وإنما هي خواطر آنية تولد وتزول سريعاً إنْ لم تُدوّن لهذا سعى إلى تدوينها في هذا الكتاب وسمّاه (صيد الخاطر) كما سمّى فيما بعد أحمد أمين أشهر كتاب في المقالة الأدبية في الأدب العربي الحديث (فيض الخاطر) وهذا يعني أنَّ مفهوم ابن الجوزي لفصول كتابه قريب من مفهوم مونتاني لفصوله فهو جسّد فيها خواطره معلّقاً على هذا القول أو ذاك ومصوراً تجارب نفسه وعيوبها وما توصل إليه من أفكار تتعلق بالدين والحياة والمجتمع. "
success, result = summarize(text)
if success:
    print(result)
