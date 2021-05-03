import PySimpleGUI as sg #line:1
from db import *#line:2
from app import *#line:3
SIZE =(800 ,600 )#line:5
def start (in_data =None ):#line:8
    OO0OOOOO00O0OO000 =[[sg .Button ('Login'),sg .Button ('Register')]]#line:11
    OO0O00O00OO000000 =sg .Window ('App',OO0OOOOO00O0OO000 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE ,default_button_element_size =(5 ,4 ))#line:21
    O000000O000O0OOOO =None #line:23
    while True :#line:25
        OOOO0O00OOO0OOO0O ,O000OOOO000OOOOOO =OO0O00O00OO000000 .read ()#line:26
        if OOOO0O00OOO0OOO0O =='Login':#line:27
            O000000O000O0OOOO =login #line:28
            break #line:29
        if OOOO0O00OOO0OOO0O =='Register':#line:30
            O000000O000O0OOOO =register #line:31
            break #line:32
        if OOOO0O00OOO0OOO0O in (None ,'Exit','Cancel'):#line:33
            break #line:34
    OO0O00O00OO000000 .close ()#line:35
    if O000000O000O0OOOO :#line:37
        O000000O000O0OOOO ()#line:38
def login (in_data =None ):#line:41
    OOO0000OOOO00OOO0 =[[sg .Text ('Login',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:47
    OOO0O0OOOO0OO00O0 =sg .Window ('App',OOO0000OOOO00OOO0 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:56
    OO0OO000OO00O000O =None #line:58
    O0O0O0OO0OOOO0O0O =None #line:59
    while True :#line:61
        OO0O0OOOO00O0O00O ,OOOO000OO0O000O00 =OOO0O0OOOO0OO00O0 .read ()#line:62
        if OO0O0OOOO00O0O00O =='Submit':#line:63
            OO0O0O0OO00O0OOO0 ,O0O0OO0OOO0OOO00O =get_user (OOOO000OO0O000O00 )#line:64
            if OO0O0O0OO00O0OOO0 :#line:65
                OO0OO000OO00O000O =application #line:66
                O0O0O0OO0OOOO0O0O =(OO0O0O0OO00O0OOO0 ,'')#line:67
                break #line:68
            else :#line:69
                OOO0O0OOOO0OO00O0 ['explanation'].update (O0O0OO0OOO0OOO00O )#line:70
        if OO0O0OOOO00O0O00O in (None ,'Exit','Cancel'):#line:71
            OO0OO000OO00O000O =start #line:72
            break #line:73
    OOO0O0OOOO0OO00O0 .close ()#line:74
    if OO0OO000OO00O000O :#line:76
        OO0OO000OO00O000O (O0O0O0OO0OOOO0O0O )#line:77
def register (in_data =None ):#line:80
    O0O0O0OOOO0OO000O =[[sg .Text ('Username',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password1',password_char ='*')],[sg .Text ('Repeat password',size =(15 ,1 )),sg .InputText (key ='password2',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:87
    OO0O00O00O00O00OO =sg .Window ('App',O0O0O0OOOO0OO000O ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:95
    O0OO0O0000000OO00 =None #line:97
    OOO0OOOOOO0OO0OO0 =None #line:98
    while True :#line:100
        O0O00OOOOOOO00OOO ,O0OO0O000000OO0O0 =OO0O00O00O00O00OO .read ()#line:101
        if O0O00OOOOOOO00OOO =='Submit':#line:102
            OOOOOOO000O0OOO00 ,OOOO00O0OOOO0O00O =create_user (O0OO0O000000OO0O0 )#line:103
            if OOOOOOO000O0OOO00 :#line:104
                O0OO0O0000000OO00 =application #line:105
                OOO0OOOOOO0OO0OO0 =(OOOOOOO000O0OOO00 ,'')#line:106
                break #line:107
            else :#line:108
                OO0O00O00O00O00OO ['explanation'].update (OOOO00O0OOOO0O00O )#line:109
        if O0O00OOOOOOO00OOO in (None ,'Exit','Cancel'):#line:110
            O0OO0O0000000OO00 =start #line:111
            break #line:112
    OO0O00O00O00O00OO .close ()#line:113
    if O0OO0O0000000OO00 :#line:115
        O0OO0O0000000OO00 (OOO0OOOOOO0OO0OO0 )#line:116
def prepare_user_layout (OOOOOO000OO00000O :UserModel ,O0O0000000OOOO00O :str ):#line:119
    OO0OO0O00000O00O0 =[[sg .Button ('Reload'),sg .Button ('Update my status'),sg .Button ('Logout',key ='Cancel')],[sg .Text (O0O0000000OOOO00O ,text_color ='red')],[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OOOOOO000OO00000O .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OOOOOO000OO00000O .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OOOOOO000OO00000O .status ,size =(15 ,1 ),key ='status',text_color ='Black'),],]#line:135
    O00O0000OOOOO000O =get_all_users (OOOOOO000OO00000O .role )#line:137
    for OOOO00O0OOOOO0OOO in O00O0000OOOOO000O :#line:138
        if OOOO00O0OOOOO0OOO .username !=OOOOOO000OO00000O .username :#line:139
            if check_role (OOOOOO000OO00000O .role ,Action .ModifyUsers ):#line:140
                OO0OO0O00000O00O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .InputText (OOOO00O0OOOOO0OOO .username ,size =(10 ,1 ),text_color ='Black',key =str (OOOO00O0OOOOO0OOO .id )+'-username'),sg .Text ('role: ',size =(5 ,1 )),sg .InputCombo (ROLES ,default_value =ROLES [OOOO00O0OOOOO0OOO .role ],text_color ='Black',key =str (OOOO00O0OOOOO0OOO .id )+'-role'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OOOO00O0OOOOO0OOO .status ,size =(15 ,1 ),text_color ='Black',key =str (OOOO00O0OOOOO0OOO .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (OOOO00O0OOOOO0OOO .id )+'-update')]]#line:149
            elif check_role (OOOOOO000OO00000O .role ,Action .ModifyStatuses ):#line:150
                OO0OO0O00000O00O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OOOO00O0OOOOO0OOO .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OOOO00O0OOOOO0OOO .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OOOO00O0OOOOO0OOO .status ,size =(15 ,1 ),text_color ='Black',key =str (OOOO00O0OOOOO0OOO .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (OOOO00O0OOOOO0OOO .id )+'-'+'update')]]#line:159
            else :#line:160
                OO0OO0O00000O00O0 +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OOOO00O0OOOOO0OOO .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OOOO00O0OOOOO0OOO .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .Text (OOOO00O0OOOOO0OOO .status ,size =(15 ,1 ),text_color ='Yellow')]]#line:168
    return OO0OO0O00000O00O0 #line:170
def application (in_data =None ):#line:173
    O00O000OO0O0O0O0O ,OO000OOOO0O00OOOO =in_data #line:174
    assert O00O000OO0O0O0O0O #line:175
    assert type (O00O000OO0O0O0O0O )==UserModel #line:176
    OOO00000OO0OO00O0 =prepare_user_layout (O00O000OO0O0O0O0O ,OO000OOOO0O00OOOO )#line:178
    OO0O000O000000OOO =sg .Window ('App',OOO00000OO0OO00O0 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:180
    OOOO000O000OOOO0O =None #line:182
    O0OOO00OOOOO00000 =None #line:183
    OO000OOOO0O00OOOO =''#line:184
    while True :#line:186
        O00O0OO0O0OOOOO0O ,OO0OOOO0OO0OOO0OO =OO0O000O000000OOO .read ()#line:187
        print (O00O0OO0O0OOOOO0O ,OO0OOOO0OO0OOO0OO )#line:188
        if O00O0OO0O0OOOOO0O and O00O0OO0O0OOOOO0O .endswith ('-update'):#line:190
            O000OO0O0O0000O0O =O00O0OO0O0OOOOO0O .split ('-')[0 ]#line:191
            O00O00O00OOOOOOOO =OO0OOOO0OO0OOO0OO .get (O000OO0O0O0000O0O +'-username')#line:192
            O0OOO0O0000O0000O =OO0OOOO0OO0OOO0OO .get (O000OO0O0O0000O0O +'-role')#line:193
            OOO00O000O000000O =OO0OOOO0OO0OOO0OO .get (O000OO0O0O0000O0O +'-status')#line:194
            if O00O00O00OOOOOOOO :#line:196
                O0O00O00O0OO0OO00 =update_user_username (int (O000OO0O0O0000O0O ),O00O00O00OOOOOOOO )#line:197
                if O0O00O00O0OO0OO00 :#line:198
                    _OO0OO0OOOOO00000O ,OO000OOOO0O00OOOO =O0O00O00O0OO0OO00 #line:199
            if O0OOO0O0000O0000O :#line:200
                O0O00O00O0OO0OO00 =update_user_role (int (O000OO0O0O0000O0O ),O0OOO0O0000O0000O )#line:201
                if O0O00O00O0OO0OO00 :#line:202
                    _OO0OO0OOOOO00000O ,OO000OOOO0O00OOOO =O0O00O00O0OO0OO00 #line:203
            if OOO00O000O000000O :#line:204
                O0O00O00O0OO0OO00 =update_user_status (int (O000OO0O0O0000O0O ),OOO00O000O000000O )#line:205
                if O0O00O00O0OO0OO00 :#line:206
                    _OO0OO0OOOOO00000O ,OO000OOOO0O00OOOO =O0O00O00O0OO0OO00 #line:207
            O00O0OO0O0OOOOO0O ='Reload'#line:208
        if O00O0OO0O0OOOOO0O =='Update my status':#line:210
            O0O00O00O0OO0OO00 =update_user_status (O00O000OO0O0O0O0O .username ,OO0OOOO0OO0OOO0OO ['status'])#line:211
            if O0O00O00O0OO0OO00 :#line:212
                _OO0OO0OOOOO00000O ,OO000OOOO0O00OOOO =O0O00O00O0OO0OO00 #line:213
            O00O0OO0O0OOOOO0O ='Reload'#line:214
        if O00O0OO0O0OOOOO0O =='Reload':#line:215
            OOOO000O000OOOO0O =application #line:216
            O0OOO00OOOOO00000 =get_user_by_username (O00O000OO0O0O0O0O .username )#line:217
            break #line:218
        if O00O0OO0O0OOOOO0O in (None ,'Exit','Cancel'):#line:219
            OOOO000O000OOOO0O =start #line:220
            break #line:221
    OO0O000O000000OOO .close ()#line:222
    if OOOO000O000OOOO0O :#line:224
        OOOO000O000OOOO0O ((O0OOO00OOOOO00000 ,OO000OOOO0O00OOOO ))#line:225
def check_installation ():#line:228
    try :#line:229
        with open ('appdata.txt')as OOOO00OO0O0OO0000 :#line:230
            O0OOO0O0O0O0OOOO0 =OOOO00OO0O0OO0000 .read ()#line:231
            if is_lisense_key (O0OOO0O0O0O0OOOO0 ):#line:232
                return True #line:233
    except Exception as OO00O00OO00OO0O00 :#line:234
        pass #line:235
    return False #line:236
def install ():#line:239
    O0OOOOO000O000O0O =input ('Enter your key\n')#line:240
    if is_lisense_key (O0OOOOO000O000O0O ):#line:241
        print ('Ok')#line:242
        with open ('appdata.txt','w')as O0O00O000O000O000 :#line:243
            O0O00O000O000O000 .write (O0OOOOO000O000O0O )#line:244
        start ()#line:245
    else :#line:246
        print ('Wrong key, bye bye')#line:247
if __name__ =='__main__':#line:250
    if check_installation ():#line:251
        start ()#line:252
    else :#line:253
        install ()#line:254
