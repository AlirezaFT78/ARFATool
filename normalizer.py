class Normalizer:
    """این کلاس شامل توابعی برای نرمال‌سازی متن است.
    
    Args:
        eng_num: اعداد فارسی را به انگلیسی تبدیل می کند
        rem_punc: همه علائم نگارشی به جز نقطه را پاک می کند
        rem_vow: اعراب و تنوین را پاک می کند
        standard: تمام کاراکترهایی که از حروف، عدد و علائم نگارشی فارسی یا انگلیسی نیستند را پاک می کند
        
        """
    
    def __init__(
        self: "Normalizer",
        eng_num: bool = False,
        rem_punc: bool = False,
        rem_vow: bool = True,
        standard: bool = False,
        ) -> None:
        
        self.rem_punc = rem_punc
        self.rem_vow = rem_vow
        self.eng_num = eng_num
        self.standard = standard
        
        self.norm_dict = {"ء": "ئ"} 
        self.norm_dict.update(dict.fromkeys(['ﺁ','آ'],'آ'))
        self.norm_dict.update(dict.fromkeys(['ﺄ','ﺃ','ﺂ','ﺈ','ﺇ','ﺎ','ٲ','ٱ','إ','ﺍ','أ'],'ا'))
        self.norm_dict.update(dict.fromkeys(['ﺒ','ﺑ'],'ب'))
        self.norm_dict.update(dict.fromkeys(['ﺏ','ﺐ'],'ب\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﭙ','ﭘ'],'پ'))
        self.norm_dict.update(dict.fromkeys(['ﭖ','ﭗ'],'پ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ٹ','ٺ','ﭞ','ٿ','ﭡ','ﺘ','ﺗ'],'ت'))
        self.norm_dict.update(dict.fromkeys(['ﺕ','ﺖ'],'ت\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺜ','ﺛ'],'ث'))
        self.norm_dict.update(dict.fromkeys(['ﺙ','ﺚ'],'ث\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺠ','ﺟ'],'ج'))
        self.norm_dict.update(dict.fromkeys(['ﺝ','ﺞ'],'ج\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﭽ','ﭼ'],'چ'))
        self.norm_dict.update(dict.fromkeys(['ﭺ','ﭻ'],'چ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ځ','ﺤ','ﺣ'],'ح'))
        self.norm_dict.update(dict.fromkeys(['ﺡ','ﺢ'],'ح\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺨ','ﺧ'],'خ'))
        self.norm_dict.update(dict.fromkeys(['ﺥ','ﺦ'],'خ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ڏ','ډ','ﺪ','ﺩ'],'د'))
        self.norm_dict.update(dict.fromkeys(['ﺬ','ﺫ'],'ذ'))
        self.norm_dict.update(dict.fromkeys(['ڙ','ڗ','ڒ','ڑ','ڕ','ﺮ','ﺭ'],'ر'))
        self.norm_dict.update(dict.fromkeys(['ﺰ','ﺯ'],'ز'))
        self.norm_dict.update(dict.fromkeys(['ﮋ','ﮊ'],'ژ'))
        self.norm_dict.update(dict.fromkeys(['ﺴ','ﺳ'],'س'))
        self.norm_dict.update(dict.fromkeys(['ﺱ','ﺲ'],'س\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺸ','ﺷ'],'ش'))
        self.norm_dict.update(dict.fromkeys(['ﺵ','ﺶ'],'ش\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺼ','ﺻ'],'ص'))
        self.norm_dict.update(dict.fromkeys(['ﺹ','ﺺ'],'ص\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻀ','ﺿ'],'ض'))
        self.norm_dict.update(dict.fromkeys(['ﺽ','ﺾ'],'ض\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻄ','ﻃ'],'ط'))
        self.norm_dict.update(dict.fromkeys(['ﻁ','ﻂ'],'ط\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻈ','ﻇ'],'ظ'))
        self.norm_dict.update(dict.fromkeys(['ﻅ','ﻆ'],'ظ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻌ','ﻋ'],'ع'))
        self.norm_dict.update(dict.fromkeys(['ﻉ','ﻊ'],'ع\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻐ','ﻏ'],'غ'))
        self.norm_dict.update(dict.fromkeys(['ﻍ','ﻎ'],'غ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻔ','ﻓ'],'ف'))
        self.norm_dict.update(dict.fromkeys(['ﻑ','ﻒ'],'ف\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻘ','ﻗ'],'ق'))
        self.norm_dict.update(dict.fromkeys(['ﻕ','ﻖ'],'ق\u200c'))
        self.norm_dict.update(dict.fromkeys(['ڪ','ڭ','ګ','ك','ﮑ','ﻜ','ﮐ','ﻛ'],'ک'))
        self.norm_dict.update(dict.fromkeys(['ﻙ','ﮎ','ﻚ','ﮏ'],'ک\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﮕ','ﮔ'],'گ'))
        self.norm_dict.update(dict.fromkeys(['ﮒ','ﮓ'],'گ\u200c'))
        self.norm_dict.update(dict.fromkeys(['ڵ','ﻠ','ﻟ'],'ل'))
        self.norm_dict.update(dict.fromkeys(['ﻝ','ﻞ'],'ل\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﻤ','ﻣ'],'م'))
        self.norm_dict.update(dict.fromkeys(['ﻡ','ﻢ'],'م\u200c'))
        self.norm_dict.update(dict.fromkeys(['ڼ','ﻨ','ﻧ'],'ن'))
        self.norm_dict.update(dict.fromkeys(['ﻥ','ﻦ'],'ن\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺆ','ﺅ','ﯙ','ۈ','ۅ','ۉ','ۉ','ﻭ','ﻮ','ؤ'],'و'))
        self.norm_dict.update(dict.fromkeys(['ﻬ','ﻫ','ھ'],'ه'))
        self.norm_dict.update(dict.fromkeys(['ﮤ','ة','ۀ','ە','ﻩ','ﮥ','ﻪ','ﺔ'],'ه\u200c'))
        self.norm_dict.update(dict.fromkeys(['ې','ێ','ى','ي','ﻴ','ﯿ','ﻳ','ﯾ'],'ی'))
        self.norm_dict.update(dict.fromkeys(['ﻯ','ۍ','ﯼ','ﻰ','ﻱ','ﻲ','ﯽ','ے'],'ی\u200c'))
        self.norm_dict.update(dict.fromkeys(['ﺌ','ﺋ'],'ئ'))
        self.norm_dict.update(dict.fromkeys(['ﺉ','ﺊ'],'ئ\u200c'))
        self.norm_dict.update({'٠':'۰', '١':'۱', '٢':'۲', '٣':'۳', '٤':'۴', '٥':'۵', '٦':'۶', '٧':'۷', '٨':'۸', '٩':'۹'})
        self.norm_dict.update({'.':' . ', '،':' ، ','؛':' ؛ ','»':' » ','«':' « ','…':' ... ','؟':' ؟ ' ,'“':' “ ','”':' ” ','!':' ! ',
                               '"':' " ',"'":" ' ", ':':' : ',';':' ; ','?':' ? ', '[': ' [ ',']':' ] ','\\':' \\ ','/':' / ','|':' | ',
                               '{':' { ','}':' } ',',':' , ','-':' - ','_':' _ '})
        
        self.norm_dict.update({'ﷲ':'الله', 'ؐ':'(ص)', 'ؑ':'(ع)', 'ؒ':'(ره)', 'ؓ':'(رض)'})
        self.norm_dict.update(dict.fromkeys(['ﻼ','ﻹ','ﻸ','ﻺ','ﻻ','ﻷ','ﻵ','ﻶ'],'لا'))
        
        self.punc_dict = {'.':'.'}
        punc_ls = ['!','?',';',':',"'",'"',',','،','؛','»','«','…','؟','“','”','\\','/','|',']','[','{','}','_','-']
        self.punc_dict.update({i:'' for i in punc_ls})  
        
        self.vow_dict = ['ﱠ', ' َ', ' ِ',' ُ',' ً','ً','ٌ','ٍ','َ','ُ','ِ','ّ','ْ','ٓ','ٔ','ٕ','ٖ','ٗ','٘','ٙ','ٚ','ٛ']
        self.vow_dict.extend(['ٝ','ٞ','ٟ','ﹰ','ﹱ','ﹲ','ﹴ','ﹶ','ﹸ','ﹹ','ﹳ','ﹷ','ﹺ','ﹻ','ﹼ','ﹾ','ﹽ','ﹿ','ٜ']) 
        
        self.num_dict = {'۰':'0', '۱':'1', '۲':'2', '۳':'3', '۴':'4', '۵':'5', '۶':'6', '۷':'7', '۸':'8', '۹':'9'}
        
        self.standard_dict = set(chr(i) for i in range(32,127)) 
        self.standard_dict = self.standard_dict.union(set(i for i in list(self.norm_dict.values()) if len(i)==1))
        self.standard_dict = self.standard_dict.union(set(self.punc_dict.keys()))
        self.standard_dict = self.standard_dict.union(set(['\u200c']))
        
        
        
    def remove_punctuation(self, txt):
        """
        به کمک دیکشنری "اعلائم نگارشی"، به جز نقطه بقیه اعلائم نگارشی را پاک می کند
        """
        mytable = str.maketrans(self.punc_dict)
        txt = txt.translate(mytable)
        return txt

    def remove_vowels(self, txt):
        """
        به کمک دیکشنری "اعراب"، انواع اعراب، ساکن و تنوین را پاک می کند
        """
        for i in self.vow_dict:
            txt = txt.replace(i,'')
        return txt
    
    def persian_num_to_english(self, txt):
        """
        به کمک دیکشنری "اعداد"، اعداد فارسی را به انگلیسی تبدیل می کند
        """
        mytable = str.maketrans(self.num_dict)
        txt = txt.translate(mytable)
        return txt
    
    def standard_chars(self, txt):
        """
        به کمک دیکشنری "استاندارد"، تمام کاراکتر های غیر فارسی یا انگلیسی را حذف می کند
        """
        for i in txt:
            if i not in self.standard_dict:
                txt = txt.replace(i,'')
        return txt
        
    def normalize(self, txt):
        """
        در این تابع حروف و اعداد فارسی به فرم استاندارد تبدیل می شوند و قبل از اعلائم نگارشی نیز یک فاصله
        قرار می گیرد تا برای توکنایزیشن قابل جدا سازی باشد. همچنین به جای برخی کلمات که کاراکتر مخصوص 
        دارند مانند الله یا لا خود کلمه قرار می گیرد. در یونکد فرم های غیراستاندارد فارسی (عربی) هر حرف 3
        یا 4 شکل دارد ابتدا، وسط، آخر و تنها که در تبدیل دو شکل آخر به استناندارد گاهی احتیاج به افزودن
        نیم فاصله نیز دارد اینکار به کمک نرم دیکت انجام می شود و چنانچه نیم فاصله اضافه شده
        ضروری نباشد حذف می شود 
        """
        mytable = str.maketrans(self.norm_dict)
        new_txt = txt.translate(mytable)
        new_txt = new_txt.replace('\u200c ', ' ')
        
        if self.rem_punc:
            new_txt = self.remove_punctuation(new_txt) 
            
        if self.rem_vow:
            new_txt = self.remove_vowels(new_txt)
            
        if self.eng_num:
            new_txt = self.persian_num_to_english(new_txt)
        
        if self.standard:
            new_txt = self.standard_chars(new_txt)
            
        new_txt = ' '.join(new_txt.split())  
        return  new_txt
    
