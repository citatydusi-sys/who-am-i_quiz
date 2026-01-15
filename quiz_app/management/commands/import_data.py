from django.core.management.base import BaseCommand
from quiz_app.models import Level, Category, Word

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Очищаем старые данные
        Word.objects.all().delete()
        Category.objects.all().delete()
        Level.objects.all().delete()
        
        all_words_data = {
            "Level 1: Humans": {
                "Moods": {"happy": "көңілді", "sad": "көңілсіз", "angry": "ашулы", "excited": "тамаша", "nervous": "қобалжу", "worried": "уайымдау", "calm": "сабырлы", "bored": "іші пысу", "confused": "шатасу", "tired": "шаршау", "energetic": "энергияға толы", "scared": "қорқу", "lonely": "жалғызсырау", "shy": "ұялу", "frustrated": "көңілі қалған", "surprised": "таңғалған", "relaxed": "еркін", "proud": "мақтанышты", "jealous": "қызғаншақ", "moody": "көңіл-күйі тұрақсыз"},
                "Appearance": {"tall": "ұзын", "short": "қысқа", "slim": "мүсінді", "overweight": "артық салмақ", "chubby": "томпақ", "muscular": "бұлшықетті", "medium height": "орташа бойлы", "thin": "арық", "beautiful": "сұлу", "handsome": "сымбатты", "pretty": "әдемі", "lovely": "көрікті", "cute": "сүйкімді", "attractive": "тартымды", "curvy": "ауқымды", "elegant": "талғампаз", "fit": "жинақы", "plain": "қарапайым", "ugly": "ұсқынсыз", "smart": "жинақы көрінетін"},
                "Hair": {"blonde": "аққұба", "brunette": "қараторы", "bald": "таз", "long hair": "ұзын шаш", "short hair": "қысқа шаш", "wavy": "толқынды", "straight": "түзу", "curly": "бұйра", "greasy": "майлы", "ginger": "жирен", "dyed": "боялған", "shoulder-length": "иыққа дейін", "ponytail": "ат құйрық", "braids": "өрімдер", "messy": "ұйпа-тұйпа"}
            },
            "Level 2: Society": {
                "Jobs": {"teacher": "мұғалім", "doctor": "дәрігер", "nurse": "медбике", "police": "полиция", "firefighter": "өрт сөндіруші", "chef": "аспаз", "waiter": "даяшы", "cleaner": "тазалықшы", "farmer": "фермер", "gardener": "бағбан", "cashier": "кассир", "receptionist": "ресепшн", "driver": "жүргізуші", "hairdresser": "шаштараз", "worker": "жұмысшы", "engineer": "инженер", "pilot": "ұшқыш", "lawyer": "заңгер", "dentist": "тіс дәрігері", "architect": "сәулетші"},
                "Weather": {"sunny": "шуақты", "cloudy": "бұлтты", "rainy": "жаңбырлы", "windy": "желді", "snowy": "қарлы", "stormy": "дауылды", "hot": "ыстық", "cold": "суық", "thunderstorm": "найзағай", "warm": "жылы", "cool": "салқын", "foggy": "тұманды", "lightning": "жасын", "humid": "дымқыл", "freezing": "аязды", "rainbow": "кемпірқосақ", "hail": "бұршақ", "breezy": "салқын самал"},
                "Face": {"oval face": "дөңгелек бет", "bright eyes": "жарқыраған көз", "pointed nose": "сүйір мұрын", "wide face": "кең бет", "symmetrical": "симметриялы", "sparkling": "жарқын", "button nose": "түйме мұрын", "narrow eyes": "тар көз", "wrinkled": "әжімді", "bloodshot": "қандыкөз", "straight nose": "тікмұрын", "full lips": "толы ерін", "angular": "бұрышты", "shiny": "нұрлы", "crooked": "қисық", "smiling": "жымиған", "freckles": "сепкіл", "dimples": "ұяшықтар", "thick eyebrows": "қалың қас", "long eyelashes": "ұзын кірпіктер", "pale": "бозарған", "tan": "күнге күйген", "beard": "сақал", "mustache": "мұрт", "chin": "иек"}
            },
            "Level 3: Home & Infrastructure": {
                "Technology": {"tablet": "планшет", "smartphone": "смартфон", "laptop": "ноутбук", "printer": "принтер", "airpods": "құлаққап", "headphones": "үлкен құлаққап", "keyboard": "пернетақта", "mouse": "тышқан", "flash drive": "флешка", "charger": "қуаттағыш", "smart watch": "смарт сағат", "screen": "экран", "speaker": "колонка", "cable": "кабель", "power bank": "пауэрбанк", "wifi": "вайфай", "remote": "пульт", "app": "қосымша", "software": "бағдарлама", "password": "құпия сөз"},
                "Family": {"grandfather": "ата", "grandmother": "әже", "mom": "ана", "dad": "әке", "uncle": "көке", "aunt": "тәте", "brother": "аға", "sister": "әпке", "parents": "ата-ана", "sibling": "ағайын", "husband": "күйеу", "wife": "әйел", "relatives": "туыстар", "cousin": "бауыр", "nephew": "жиен ұл", "niece": "жиен қыз", "mother-in-law": "ене", "son-in-law": "күйеу бала", "daughter-in-law": "келін", "brother-in-law": "балдыз", "sister-in-law": "қайын бике", "grandparents": "ата-әже", "stepmother": "өгей шеше", "stepfather": "өгей әке", "ancestors": "бабалар"},
                "Infrastructure": {"house": "үй", "kitchen": "ас үй", "bedroom": "жатын бөлме", "bathroom": "жуынатын бөлме", "living room": "қонақ бөлме", "yard": "аула", "roof": "шатыр", "door": "есік", "shelf": "сөре", "infrastructure": "инфрақұрылым", "transport": "көлік", "bridge": "көпір", "road": "жол", "building": "ғимарат", "design": "жобалау", "company": "компания", "office": "кеңсе", "street": "көше", "city": "қала", "village": "ауыл"}
            },
            "Level 4: Food World": {
                "Vegetables": {"lettuce": "салат жапырағы", "peppers": "бұрыштар", "beans": "бұршақтар", "turnip": "шалқан", "avocado": "авокадо", "onions": "пияз", "tomatoes": "қызанақтар", "cabbage": "қырыққабат", "cucumber": "қияр", "eggplant": "баклажан", "broccoli": "брокколи", "carrots": "сәбіз", "potato": "картоп", "garlic": "сарымсақ", "corn": "жүгері", "pumpkin": "асқабақ", "mushroom": "саңырауқұлақ", "radish": "шомыр", "spinach": "шпинат", "peas": "асбұршақ"},
                "Fruits": {"apple": "алма", "banana": "банан", "orange": "апельсин", "strawberry": "құлпынай", "grapes": "жүзім", "pineapple": "ананас", "lemon": "лимон", "mango": "манго", "kiwi": "киви", "watermelon": "қарбыз", "peach": "шабдалы", "pear": "алмұрт", "cherry": "шие", "plum": "өрік", "blueberry": "көкжидек", "apricot": "өрік", "melon": "қауын", "pomegranate": "анар", "coconut": "кокос", "lime": "лайм"},
                "Kitchen Items": {"pan": "таба", "kettle": "шәйнек", "spoon": "қасық", "knife": "пышақ", "bowl": "тостаған", "fork": "шанышқы", "cup": "кесе", "cutting board": "тақтайша", "dish": "ыдыс", "microwave": "микротолқынды пеш", "sink": "раковина", "mirror": "айна", "towel": "сүлгі", "fridge": "тоңазытқыш", "oven": "пеш", "plate": "тәрелке", "glass": "стақан", "napkin": "майлық", "pot": "кәстрөл", "mixer": "миксер"}
            },
            "Level 5: Kitchen & Dining": {
                "Proteins": {"chicken": "тауық", "beef": "сиыр", "fish": "балық", "eggs": "жұмыртқа", "pork": "доңыз", "turkey": "түйетауық", "lamb": "қозы", "sausage": "шұжық", "bacon": "бекон", "ham": "ветчина", "shrimp": "асшаян", "salmon": "ақсерке", "tuna": "түнец", "steak": "стейк", "meat": "ет"},
                "Grains & Drinks": {"bread": "нан", "rice": "күріш", "pasta": "макарон", "oats": "сұлы", "quinoa": "киноа", "water": "су", "coffee": "кофе", "tea": "шай", "juice": "шырын", "smoothie": "смузи", "milkshake": "сүтті коктейль", "soda": "газдалған су", "lemonade": "лимонад", "beer": "сыра", "wine": "шарап", "coke": "кола", "milk": "сүт", "cream": "кілегей"},
                "Cooking Actions": {"cook": "пісіру", "bake": "пеште пісіру", "fry": "қуыру", "peel": "аршу", "chop": "турау", "stir": "араластыру", "taste": "дәмін тату", "grill": "грильдеу", "serve": "ұсыну", "pour": "құю", "slice": "тілімдеу", "order": "тапсырыс беру", "boil": "қайнату", "roast": "қуыру", "steam": "булау", "mix": "араластыру", "whisk": "көпіршіту", "grate": "үгу", "melt": "еріту", "weigh": "өлшеу", "squeeze": "сығу", "add": "қосу"}
            },
            "Level 6: Daily Actions": {
                "Routine": {"wake up": "ояну", "sleep": "ұйықтау", "brush teeth": "тіс тазалау", "wash face": "бет жуу", "shower": "душқа түсу", "study": "оқу", "listen": "тыңдау", "play": "ойнау", "shop": "сауда", "run": "жүгіру", "clean": "тазалау", "dance": "билеу", "sing": "ән айту", "travel": "саяхат", "exercise": "жаттығу", "laugh": "күлу", "cry": "жылау", "sit": "отыру", "wait": "күту", "leave": "кету"},
                "Animals": {"lion": "арыстан", "rabbit": "қоян", "giraffe": "керік", "duck": "үйрек", "zebra": "зебра", "horse": "жылқы", "crocodile": "қолтырауын", "tiger": "жолбарыс", "elephant": "піл", "monkey": "маймыл", "bear": "аю", "wolf": "қасқыр", "fox": "түлкі", "cat": "мысық", "dog": "ит", "panther": "қара пантера", "snake": "жылан", "eagle": "бүркіт"},
                "Verbs": {"break": "сындыру", "build": "құру", "buy": "сатып алу", "do": "істеу", "drink": "ішу", "come": "келу", "forgive": "кешіру", "forget": "ұмыту", "get": "алу", "give": "беру", "fly": "ұшу", "eat": "жеу", "walk": "жүру", "read": "оқу", "write": "жазу", "meet": "кездесу", "drive": "жүргізу", "watch": "көру", "use": "қолдану", "talk": "сөйлесу", "shout": "айқайлау", "jump": "секіру", "smile": "жымию", "think": "ойлау", "learn": "үйрену"}
            },
            "Level 7: Clothes & Values": {
                "Clothes": {"jeans": "джинсы", "polo shirt": "поло жейде", "suit": "костюм", "shorts": "шолақ шалбар", "shirt": "жейде", "vest": "кеудеше", "turtleneck": "водолазка", "dress": "көйлек", "jacket": "куртка", "shoes": "аяқ киім", "sneakers": "кроссовки", "boots": "бәтеңке", "sandals": "сандали", "hat": "бас киім", "gloves": "қолғап", "belt": "белдік", "tie": "галстук", "socks": "шұлық", "scarf": "сарқырама", "glasses": "көзілдірік", "watch": "сағат", "pajamas": "пижама"},
                "Clothes Actions": {"change": "ауыстыру", "try on": "киіп көру", "fold": "бүктеу", "hang up": "ілу", "put on": "кию", "take off": "шешу", "iron": "үтіктеу", "mend": "жөндеу", "dye": "бояу", "sew": "тігу", "stitch": "тоқу", "unbutton": "ағыту", "zip up": "замок тағу", "wash": "жуу", "dry": "кептіру"},
                "Values & Phrasal": {"patience": "шыдам", "understanding": "түсінік", "feedback": "кері байланыс", "effort": "күш", "advice": "кеңес", "support": "қолдау", "kindness": "мейірім", "honesty": "адалдық", "teamwork": "біздің жұмыс", "dedication": "шыншылдық", "expertise": "тәжірибе", "fresh": "балғын", "sour": "қышқыл", "tasty": "дәмді", "spicy": "ащы", "get in": "көлікке міну", "get off": "түсу", "get back": "оралу", "get on": "міну", "figure out": "шешу", "look for": "іздеу", "carry on": "жалғастыру", "stand up": "тұру", "sit down": "отыру", "wake up": "ояну"}
            }
        }
        
        for lvl_name, cats in all_words_data.items():
            lvl, _ = Level.objects.get_or_create(name=lvl_name)
            for cat_name, words in cats.items():
                cat, _ = Category.objects.get_or_create(level=lvl, name=cat_name)
                for eng, kaz in words.items():
                    Word.objects.get_or_create(category=cat, english=eng, kazakh=kaz)
        self.stdout.write(self.style.SUCCESS("Success! Data imported."))
