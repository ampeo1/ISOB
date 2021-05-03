import PySimpleGUI as sg #line:1
from db import *#line:2
from app import *#line:3
SIZE =(800 ,600 )#line:5
def start (O000OOO0OOOO00O0O =None ):#line:10
    O000O0O0000O00O00 =[[sg .Button ('Login'),sg .Button ('Register')]]#line:13
    OOOOOOO0OO00O00OO =sg .Window ('App',O000O0O0000O00O00 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE ,default_button_element_size =(5 ,4 ))#line:23
    OO00000O00OO0O00O =None #line:25
    while True :#line:27
        OO0OOO0O0O00000OO ,O0O00OOOOOO00O0OO =OOOOOOO0OO00O00OO .read ()#line:28
        if OO0OOO0O0O00000OO =='Login':#line:29
            OO00000O00OO0O00O =l1l1l1ll1l1l1lll #line:30
            break #line:31
        if OO0OOO0O0O00000OO =='Register':#line:32
            OO00000O00OO0O00O =register #line:33
            break #line:34
        if OO0OOO0O0O00000OO in (None ,'Exit','Cancel'):#line:35
            break #line:36
    OOOOOOO0OO00O00OO .close ()#line:37
    if OO00000O00OO0O00O :#line:39
        OO00000O00OO0O00O ()#line:40
def l1l1ll1lll1l1 (OOO0O0OO00OOOOOO0 =None ):#line:43
    O0OOO0000O00OO00O =[[sg .Button ('Login'),sg .Button ('Register')]]#line:46
    O0OO00OOOOO000O0O =sg .Window ('App',O0OOO0000O00OO00O ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE ,default_button_element_size =(5 ,4 ))#line:56
    O0O0O0OOO0OO00O00 =None #line:58
    while True :#line:60
        OOO0O00OOOOO0OO0O ,OOO0O0O0OOO000000 =O0OO00OOOOO000O0O .read ()#line:61
        if OOO0O00OOOOO0OO0O =='Login':#line:62
            O0O0O0OOO0OO00O00 =login #line:63
            break #line:64
        if OOO0O00OOOOO0OO0O =='Register':#line:65
            O0O0O0OOO0OO00O00 =register #line:66
            break #line:67
        if OOO0O00OOOOO0OO0O in (None ,'Exit','Cancel'):#line:68
            break #line:69
    O0OO00OOOOO000O0O .close ()#line:70
    if O0O0O0OOO0OO00O00 :#line:72
        O0O0O0OOO0OO00O00 ()#line:73
def login (O000000O0OOO000O0 =None ):#line:76
    O00OO0OOOOOO000OO =[[sg .Text ('Login',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:82
    O000O0000O00OOO0O =sg .Window ('App',O00OO0OOOOOO000OO ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:91
    O00O000OOO0OOOO00 =None #line:93
    O0O0O0OO0OO0OO0O0 =None #line:94
    while True :#line:96
        O0OOO000O00OO0O00 ,OOOOO000000OOO0OO =O000O0000O00OOO0O .read ()#line:97
        if O0OOO000O00OO0O00 =='Submit':#line:98
            O000000OO000O0OOO ,OOO0O000O00OO0O0O =get_user (OOOOO000000OOO0OO )#line:99
            if O000000OO000O0OOO :#line:100
                O00O000OOO0OOOO00 =application #line:101
                O0O0O0OO0OO0OO0O0 =(O000000OO000O0OOO ,'')#line:102
                break #line:103
            else :#line:104
                O000O0000O00OOO0O ['explanation'].update (OOO0O000O00OO0O0O )#line:105
        if O0OOO000O00OO0O00 in (None ,'Exit','Cancel'):#line:106
            O00O000OOO0OOOO00 =l1l1ll1lll1l1 #line:107
            break #line:108
    O000O0000O00OOO0O .close ()#line:109
    if O00O000OOO0OOOO00 :#line:111
        O00O000OOO0OOOO00 (O0O0O0OO0OO0OO0O0 )#line:112
def l1l1l1ll1l1l1lll (OO0OOO0000O0OOOOO =None ):#line:115
    OO0OO0OO0000O0000 =[[sg .Text ('Login',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:121
    O0OOO00OO0O00OO00 =sg .Window ('App',OO0OO0OO0000O0000 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:130
    O00OOO00OOO000OOO =None #line:132
    O0OO00O0O000O00O0 =None #line:133
    while True :#line:135
        O0O0OO0OO00O00O00 ,OO0OOOOOO00OOOOO0 =O0OOO00OO0O00OO00 .read ()#line:136
        if O0O0OO0OO00O00O00 =='Submit':#line:137
            O0OO00OO00000OOOO ,OOOO0O00OO0O00000 =get_user (OO0OOOOOO00OOOOO0 )#line:138
            if O0OO00OO00000OOOO :#line:139
                O00OOO00OOO000OOO =application #line:140
                O0OO00O0O000O00O0 =(O0OO00OO00000OOOO ,'')#line:141
                break #line:142
            else :#line:143
                O0OOO00OO0O00OO00 ['explanation'].update (OOOO0O00OO0O00000 )#line:144
        if O0O0OO0OO00O00O00 in (None ,'Exit','Cancel'):#line:145
            O00OOO00OOO000OOO =l1l1ll1lll1l1 #line:146
            break #line:147
    O0OOO00OO0O00OO00 .close ()#line:148
    if O00OOO00OOO000OOO :#line:150
        O00OOO00OOO000OOO (O0OO00O0O000O00O0 )#line:151
def register (OO0O0OO000OO0O0O0 =None ):#line:154
    O0O000000000OOO0O =[[sg .Text ('Username',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password1',password_char ='*')],[sg .Text ('Repeat password',size =(15 ,1 )),sg .InputText (key ='password2',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:161
    O00OOOOOO0O0O00O0 =sg .Window ('App',O0O000000000OOO0O ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:169
    O0O00O0O00OO000OO =None #line:171
    OOOOOO0OO00OOOO0O =None #line:172
    while True :#line:174
        O000O0OO0OOOOOO0O ,O0O000O000O00O0O0 =O00OOOOOO0O0O00O0 .read ()#line:175
        if O000O0OO0OOOOOO0O =='Submit':#line:176
            O0O00O00OO0OOOO0O ,O00O0OOOOO00O0O0O =create_user (O0O000O000O00O0O0 )#line:177
            if O0O00O00OO0OOOO0O :#line:178
                O0O00O0O00OO000OO =application #line:179
                OOOOOO0OO00OOOO0O =(O0O00O00OO0OOOO0O ,'')#line:180
                break #line:181
            else :#line:182
                O00OOOOOO0O0O00O0 ['explanation'].update (O00O0OOOOO00O0O0O )#line:183
        if O000O0OO0OOOOOO0O in (None ,'Exit','Cancel'):#line:184
            O0O00O0O00OO000OO =start #line:185
            break #line:186
    O00OOOOOO0O0O00O0 .close ()#line:187
    if O0O00O0O00OO000OO :#line:189
        O0O00O0O00OO000OO (OOOOOO0OO00OOOO0O )#line:190
def make_comment (OO000O0O00O000O0O ):#line:193
    if OO000O0O00O000O0O ==0 :#line:194
        return '1234'#line:195
    if OO000O0O00O000O0O ==2 :#line:196
        return '124'#line:197
    if OO000O0O00O000O0O ==4 :#line:198
        return '123'#line:199
    return ''#line:200
def application (O0O0OOOO00O000O00 =None ):#line:203
    OO00O00OO000O00OO ,O0O00O0OOO0O0OO00 =O0O0OOOO00O000O00 #line:204
    assert OO00O00OO000O00OO #line:205
    assert type (OO00O00OO000O00OO )==UserModel #line:206
    while True :#line:208
        O00O00O0000O000O0 =[[sg .Button ('Reload'),sg .Button ('Update my status'),sg .Button ('Logout',key ='Cancel')],[sg .Text (O0O00O0OOO0O0OO00 ,text_color ='red')],[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OO00O00OO000O00OO .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OO00O00OO000O00OO .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OO00O00OO000O00OO .status ,size =(15 ,1 ),key ='status',text_color ='Black'),],]#line:224
        O0O0000O0O00O0OO0 =get_all_users (OO00O00OO000O00OO .role )#line:226
        for OO0OOOOO0000O0O00 in O0O0000O0O00O0OO0 :#line:227
            if OO0OOOOO0000O0O00 .username !=OO00O00OO000O00OO .username :#line:228
                if check_role (OO00O00OO000O00OO .role ,Action .ModifyUsers ):#line:229
                    O00O00O0000O000O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .InputText (OO0OOOOO0000O0O00 .username ,size =(10 ,1 ),text_color ='Black',key =str (OO0OOOOO0000O0O00 .id )+'-username'),sg .Text ('role: ',size =(5 ,1 )),sg .InputCombo (ROLES ,default_value =ROLES [OO0OOOOO0000O0O00 .role ],text_color ='Black',key =str (OO0OOOOO0000O0O00 .id )+'-role'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OO0OOOOO0000O0O00 .status ,size =(15 ,1 ),text_color ='Black',key =str (OO0OOOOO0000O0O00 .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (OO0OOOOO0000O0O00 .id )+'-update')]]#line:238
                elif check_role (OO00O00OO000O00OO .role ,Action .ModifyStatuses ):#line:239
                    O00O00O0000O000O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OO0OOOOO0000O0O00 .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OO0OOOOO0000O0O00 .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OO0OOOOO0000O0O00 .status ,size =(15 ,1 ),text_color ='Black',key =str (OO0OOOOO0000O0O00 .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (OO0OOOOO0000O0O00 .id )+'-'+'update')]]#line:248
                else :#line:249
                    O00O00O0000O000O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OO0OOOOO0000O0O00 .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OO0OOOOO0000O0O00 .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .Text (OO0OOOOO0000O0O00 .status ,size =(15 ,1 ),text_color ='Yellow')]]#line:257
        break #line:258
    O000O0OOO0OOOO0OO =sg .Window ('App',O00O00O0000O000O0 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:261
    O0O0OOO0O000OO00O =None #line:263
    OO00OO0O00000OOOO =None #line:264
    O0O00O0OOO0O0OO00 =''#line:265
    for OO0OO00O0000O0O0O in range (100 ):#line:267
        O0O00O0OOO0O0OO00 +=make_comment (OO0OO00O0000O0O0O )#line:268
        if O0O00O0OOO0O0OO00 =='isob':#line:269
            O0O00O0OOO0O0OO00 ='claviatura'#line:270
        if O0O00O0OOO0O0OO00 =='claviatura':#line:271
            O0O00O0OOO0O0OO00 ='isob'#line:272
        if O0O00O0OOO0O0OO00 =='arbuz':#line:273
            O0O00O0OOO0O0OO00 ='dynya'#line:274
    if len (O0O00O0OOO0O0OO00 )>10 :#line:276
        O0O00O0OOO0O0OO00 =''#line:277
    while True :#line:279
        O0O0OOO0OOOO00OO0 ,OOO0OO000O000OO0O =O000O0OOO0OOOO0OO .read ()#line:280
        print (O0O0OOO0OOOO00OO0 ,OOO0OO000O000OO0O )#line:281
        if O0O0OOO0OOOO00OO0 and O0O0OOO0OOOO00OO0 .endswith ('-update'):#line:283
            O0OO0O0OO00O0OOOO =O0O0OOO0OOOO00OO0 .split ('-')[0 ]#line:284
            O0OOO00OO0OOOOOOO =OOO0OO000O000OO0O .get (O0OO0O0OO00O0OOOO +'-username')#line:285
            O0OOOOOO0OOO0O00O =OOO0OO000O000OO0O .get (O0OO0O0OO00O0OOOO +'-role')#line:286
            O0OO00O0O00OO00O0 =OOO0OO000O000OO0O .get (O0OO0O0OO00O0OOOO +'-status')#line:287
            if O0OOO00OO0OOOOOOO :#line:289
                O00O000OO000O00O0 =update_user_username (int (O0OO0O0OO00O0OOOO ),O0OOO00OO0OOOOOOO )#line:290
                if O00O000OO000O00O0 :#line:291
                    _O0OO0OOOO00OO0000 ,O0O00O0OOO0O0OO00 =O00O000OO000O00O0 #line:292
            if O0OOOOOO0OOO0O00O :#line:293
                O00O000OO000O00O0 =update_user_role (int (O0OO0O0OO00O0OOOO ),O0OOOOOO0OOO0O00O )#line:294
                if O00O000OO000O00O0 :#line:295
                    _O0OO0OOOO00OO0000 ,O0O00O0OOO0O0OO00 =O00O000OO000O00O0 #line:296
            if O0OO00O0O00OO00O0 :#line:297
                O00O000OO000O00O0 =update_user_status (int (O0OO0O0OO00O0OOOO ),O0OO00O0O00OO00O0 )#line:298
                if O00O000OO000O00O0 :#line:299
                    _O0OO0OOOO00OO0000 ,O0O00O0OOO0O0OO00 =O00O000OO000O00O0 #line:300
            O0O0OOO0OOOO00OO0 ='Reload'#line:301
        if O0O0OOO0OOOO00OO0 =='Update my status':#line:303
            O00O000OO000O00O0 =update_user_status (OO00O00OO000O00OO .username ,OOO0OO000O000OO0O ['status'])#line:304
            if O00O000OO000O00O0 :#line:305
                _O0OO0OOOO00OO0000 ,O0O00O0OOO0O0OO00 =O00O000OO000O00O0 #line:306
            O0O0OOO0OOOO00OO0 ='Reload'#line:307
        if O0O0OOO0OOOO00OO0 =='Reload':#line:308
            O0O0OOO0O000OO00O =application #line:309
            OO00OO0O00000OOOO =get_user_by_username (OO00O00OO000O00OO .username )#line:310
            break #line:311
        if O0O0OOO0OOOO00OO0 in (None ,'Exit','Cancel'):#line:312
            O0O0OOO0O000OO00O =start #line:313
            break #line:314
        if O0O0OOO0OOOO00OO0 =='event1':#line:316
            O0O0OOO0O000OO00O =start #line:317
            break #line:318
        if O0O0OOO0OOOO00OO0 =='event2':#line:319
            O0O0OOO0O000OO00O =start #line:320
            break #line:321
        if O0O0OOO0OOOO00OO0 =='event3':#line:322
            O0O0OOO0O000OO00O =l1l1ll1lll1l1 #line:323
            break #line:324
        if O0O0OOO0OOOO00OO0 =='event4':#line:325
            O0O0OOO0O000OO00O =start #line:326
            break #line:327
        if O0O0OOO0OOOO00OO0 =='event5':#line:328
            O0O0OOO0O000OO00O =l1l1ll1lll1l1 #line:329
            break #line:330
        if O0O0OOO0OOOO00OO0 =='event6':#line:331
            O0O0OOO0O000OO00O =start #line:332
            break #line:333rf
        if O0O0OOO0OOOO00OO0 =='event7':#line:334
            O0O0OOO0O000OO00O =l1l1ll1lll1l1 #line:335
            break #line:336
        if O0O0OOO0OOOO00OO0 =='event8':#line:337
            O0O0OOO0O000OO00O =start #line:338
            break #line:339
    O000O0OOO0OOOO0OO .close ()#line:341
    if O0O0OOO0O000OO00O :#line:343
        O0O0OOO0O000OO00O ((OO00OO0O00000OOOO ,O0O00O0OOO0O0OO00 ))#line:344
def check_installation ():#line:347
    try :#line:348
        with open ('appdata.txt')as O00O0O00O00OOO0O0 :#line:349
            OOOO0OOOOO0OOO000 =O00O0O00O00OOO0O0 .read ()#line:350
            if is_lisense_key (OOOO0OOOOO0OOO000 ):#line:351
                return True #line:352
    except Exception as OO0O00000OOO0OO0O :#line:353
        pass #line:354
    return False #line:355
def install ():#line:358
    key =input ('Enter your key\n')#line:359
    if is_lisense_key (key ):#line:360
        print ('Ok')#line:361
        with open ('appdata.txt','w')as O00OOOO0O0OO000O0 :#line:362
            O00OOOO0O0OO000O0 .write (key )#line:363
        start ()#line:364
    else :#line:365
        print ('Wrong key, bye bye')#line:366
if __name__ =='__main__':#line:369
    if check_installation ():#line:370
        l1l1ll1lll1l1 ()#line:371
    else :#line:372
        install ()#line:373
