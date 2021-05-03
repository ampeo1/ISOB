import PySimpleGUI as sg #line:1
from db import *#line:2
from app import *#line:3
SIZE =(800 ,600 )#line:5
def start (O00OOOOO00O000000 =None ):#line:8
    O0000O0OOOOOOO0OO =[[sg .Button ('Login'),sg .Button ('Register')]]#line:11
    O0O00O0000O00000O =sg .Window ('App',O0000O0OOOOOOO0OO ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE ,default_button_element_size =(5 ,4 ))#line:21
    O0O0O0OO0000O00O0 =None #line:23
    while True :#line:25
        O0O00O000OO0OO0OO ,O0OO0OOOO00O0O0OO =O0O00O0000O00000O .read ()#line:26
        if O0O00O000OO0OO0OO =='Login':#line:27
            O0O0O0OO0000O00O0 =login #line:28
            break #line:29
        if O0O00O000OO0OO0OO =='Register':#line:30
            O0O0O0OO0000O00O0 =register #line:31
            break #line:32
        if O0O00O000OO0OO0OO in (None ,'Exit','Cancel'):#line:33
            break #line:34
    O0O00O0000O00000O .close ()#line:35
    if O0O0O0OO0000O00O0 :#line:37
        O0O0O0OO0000O00O0 ()#line:38
def login (OO0O0000O00O0OOOO =None ):#line:41
    O0OOOOOOOOO0O00OO =[[sg .Text ('Login',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:47
    O0OO0000O0OO00000 =sg .Window ('App',O0OOOOOOOOO0O00OO ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:56
    O000O0O0000OO0000 =None #line:58
    O00000000O000OOO0 =None #line:59
    while True :#line:61
        OOO00O00O0OOO000O ,OO0O000O0O0OO0OO0 =O0OO0000O0OO00000 .read ()#line:62
        if OOO00O00O0OOO000O =='Submit':#line:63
            OO0O0O0OO0O0OO0O0 ,OO0O0O000OOOOO000 =get_user (OO0O000O0O0OO0OO0 )#line:64
            if OO0O0O0OO0O0OO0O0 :#line:65
                O000O0O0000OO0000 =application #line:66
                O00000000O000OOO0 =(OO0O0O0OO0O0OO0O0 ,'')#line:67
                break #line:68
            else :#line:69
                O0OO0000O0OO00000 ['explanation'].update (OO0O0O000OOOOO000 )#line:70
        if OOO00O00O0OOO000O in (None ,'Exit','Cancel'):#line:71
            O000O0O0000OO0000 =start #line:72
            break #line:73
    O0OO0000O0OO00000 .close ()#line:74
    if O000O0O0000OO0000 :#line:76
        O000O0O0000OO0000 (O00000000O000OOO0 )#line:77
def register (OO0OO0O000000OOO0 =None ):#line:80
    O0000OOOOOOO0O00O =[[sg .Text ('Username',size =(15 ,1 )),sg .InputText (key ='login')],[sg .Text ('Password',size =(15 ,1 )),sg .InputText (key ='password1',password_char ='*')],[sg .Text ('Repeat password',size =(15 ,1 )),sg .InputText (key ='password2',password_char ='*')],[sg .Submit (),sg .Cancel ()],[sg .Text ('',text_color ='red',key ='explanation',size =(40 ,1 ))]]#line:87
    O0OOO0O00OOOOOOOO =sg .Window ('App',O0000OOOOOOO0O00O ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:95
    OOOOOOO0000OO0000 =None #line:97
    O0OO0O000OO000000 =None #line:98
    while True :#line:100
        OO0OOOO00O00000OO ,O000O0OOOOOO00000 =O0OOO0O00OOOOOOOO .read ()#line:101
        if OO0OOOO00O00000OO =='Submit':#line:102
            OOO00O0O0O0000OOO ,O000O0O0O0O0O0000 =create_user (O000O0OOOOOO00000 )#line:103
            if OOO00O0O0O0000OOO :#line:104
                OOOOOOO0000OO0000 =application #line:105
                O0OO0O000OO000000 =(OOO00O0O0O0000OOO ,'')#line:106
                break #line:107
            else :#line:108
                O0OOO0O00OOOOOOOO ['explanation'].update (O000O0O0O0O0O0000 )#line:109
        if OO0OOOO00O00000OO in (None ,'Exit','Cancel'):#line:110
            OOOOOOO0000OO0000 =start #line:111
            break #line:112
    O0OOO0O00OOOOOOOO .close ()#line:113
    if OOOOOOO0000OO0000 :#line:115
        OOOOOOO0000OO0000 (O0OO0O000OO000000 )#line:116
def prepare_user_layout (OOO00O0000O0O0OOO :UserModel ,O00O0OO0O00OO0000 :str ):#line:119
    OO000O0OOO0O0OO0O =[[sg .Button ('Reload'),sg .Button ('Update my status'),sg .Button ('Logout',key ='Cancel')],[sg .Text (O00O0OO0O00OO0000 ,text_color ='red')],[sg .Text ('username: ',size =(10 ,1 )),sg .Text (OOO00O0000O0O0OOO .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [OOO00O0000O0O0OOO .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (OOO00O0000O0O0OOO .status ,size =(15 ,1 ),key ='status',text_color ='Black'),],]#line:135
    OO0000OO0O00OOOOO =get_all_users (OOO00O0000O0O0OOO .role )#line:137
    for O0OOO0OO0OOOO000O in OO0000OO0O00OOOOO :#line:138
        if O0OOO0OO0OOOO000O .username !=OOO00O0000O0O0OOO .username :#line:139
            if check_role (OOO00O0000O0O0OOO .role ,Action .ModifyUsers ):#line:140
                OO000O0OOO0O0OO0O +=[[sg .Text ('username: ',size =(10 ,1 )),sg .InputText (O0OOO0OO0OOOO000O .username ,size =(10 ,1 ),text_color ='Black',key =str (O0OOO0OO0OOOO000O .id )+'-username'),sg .Text ('role: ',size =(5 ,1 )),sg .InputCombo (ROLES ,default_value =ROLES [O0OOO0OO0OOOO000O .role ],text_color ='Black',key =str (O0OOO0OO0OOOO000O .id )+'-role'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (O0OOO0OO0OOOO000O .status ,size =(15 ,1 ),text_color ='Black',key =str (O0OOO0OO0OOOO000O .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (O0OOO0OO0OOOO000O .id )+'-update')]]#line:149
            elif check_role (OOO00O0000O0O0OOO .role ,Action .ModifyStatuses ):#line:150
                OO000O0OOO0O0OO0O +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (O0OOO0OO0OOOO000O .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [O0OOO0OO0OOOO000O .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .InputText (O0OOO0OO0OOOO000O .status ,size =(15 ,1 ),text_color ='Black',key =str (O0OOO0OO0OOOO000O .id )+'-status'),sg .Button ('U',button_color =('black','green'),key =str (O0OOO0OO0OOOO000O .id )+'-'+'update')]]#line:159
            else :#line:160
                OO000O0OOO0O0OO0O +=[[sg .Text ('username: ',size =(10 ,1 )),sg .Text (O0OOO0OO0OOOO000O .username ,size =(10 ,1 ),text_color ='Yellow'),sg .Text ('role: ',size =(5 ,1 )),sg .Text (ROLES [O0OOO0OO0OOOO000O .role ],size =(10 ,1 ),text_color ='Yellow'),sg .Text ('status: ',size =(5 ,1 )),sg .Text (O0OOO0OO0OOOO000O .status ,size =(15 ,1 ),text_color ='Yellow')]]#line:168
    return OO000O0OOO0O0OO0O #line:170
def application (O0000O0OO0O0O00OO =None ):#line:173
    OO0OOOOOO0OOOO0OO ,OOO000OOOO0O0OO00 =O0000O0OO0O0O00OO #line:174
    assert OO0OOOOOO0OOOO0OO #line:175
    assert type (OO0OOOOOO0OOOO0OO )==UserModel #line:176
    OO0O0O0OOO0O00000 =prepare_user_layout (OO0OOOOOO0OOOO0OO ,OOO000OOOO0O0OO00 )#line:178
    OOOOO0OOOO0O0O000 =sg .Window ('App',OO0O0O0OOO0O00000 ,default_element_size =(90 ,10 ),auto_size_text =True ,font =('Helvetica',20 ),size =SIZE )#line:180
    OO000O0000000OOOO =None #line:182
    O0OO0OOO0OOO0000O =None #line:183
    OOO000OOOO0O0OO00 =''#line:184
    while True :#line:186
        OO0O0000O000OO0O0 ,O0O0O00OOOOO0O0O0 =OOOOO0OOOO0O0O000 .read ()#line:187
        print (OO0O0000O000OO0O0 ,O0O0O00OOOOO0O0O0 )#line:188
        if OO0O0000O000OO0O0 and OO0O0000O000OO0O0 .endswith ('-update'):#line:190
            OO0000OO0O0O00000 =OO0O0000O000OO0O0 .split ('-')[0 ]#line:191
            OO0OOO0O0OO000O0O =O0O0O00OOOOO0O0O0 .get (OO0000OO0O0O00000 +'-username')#line:192
            O00000000O0O00O00 =O0O0O00OOOOO0O0O0 .get (OO0000OO0O0O00000 +'-role')#line:193
            O00OOOOOO000OO0OO =O0O0O00OOOOO0O0O0 .get (OO0000OO0O0O00000 +'-status')#line:194
            if OO0OOO0O0OO000O0O :#line:196
                OOOO00OOOO00O0O0O =update_user_username (int (OO0000OO0O0O00000 ),OO0OOO0O0OO000O0O )#line:197
                if OOOO00OOOO00O0O0O :#line:198
                    _OOOOO00OO000O0OOO ,OOO000OOOO0O0OO00 =OOOO00OOOO00O0O0O #line:199
            if O00000000O0O00O00 :#line:200
                OOOO00OOOO00O0O0O =update_user_role (int (OO0000OO0O0O00000 ),O00000000O0O00O00 )#line:201
                if OOOO00OOOO00O0O0O :#line:202
                    _OOOOO00OO000O0OOO ,OOO000OOOO0O0OO00 =OOOO00OOOO00O0O0O #line:203
            if O00OOOOOO000OO0OO :#line:204
                OOOO00OOOO00O0O0O =update_user_status (int (OO0000OO0O0O00000 ),O00OOOOOO000OO0OO )#line:205
                if OOOO00OOOO00O0O0O :#line:206
                    _OOOOO00OO000O0OOO ,OOO000OOOO0O0OO00 =OOOO00OOOO00O0O0O #line:207
            OO0O0000O000OO0O0 ='Reload'#line:208
        if OO0O0000O000OO0O0 =='Update my status':#line:210
            OOOO00OOOO00O0O0O =update_user_status (OO0OOOOOO0OOOO0OO .username ,O0O0O00OOOOO0O0O0 ['status'])#line:211
            if OOOO00OOOO00O0O0O :#line:212
                _OOOOO00OO000O0OOO ,OOO000OOOO0O0OO00 =OOOO00OOOO00O0O0O #line:213
            OO0O0000O000OO0O0 ='Reload'#line:214
        if OO0O0000O000OO0O0 =='Reload':#line:215
            OO000O0000000OOOO =application #line:216
            O0OO0OOO0OOO0000O =get_user_by_username (OO0OOOOOO0OOOO0OO .username )#line:217
            break #line:218
        if OO0O0000O000OO0O0 in (None ,'Exit','Cancel'):#line:219
            OO000O0000000OOOO =start #line:220
            break #line:221
    OOOOO0OOOO0O0O000 .close ()#line:222
    if OO000O0000000OOOO :#line:224
        OO000O0000000OOOO ((O0OO0OOO0OOO0000O ,OOO000OOOO0O0OO00 ))#line:225
def check_installation ():#line:228
    try :#line:229
        with open ('appdata.txt')as O00O0OO00000O00OO :#line:230
            OOO0OOO000O0OOOO0 =O00O0OO00000O00OO .read ()#line:231
            if is_lisense_key (OOO0OOO000O0OOOO0 ):#line:232
                return True #line:233
    except Exception as O00000O00OOOO0OO0 :#line:234
        pass #line:235
    return False #line:236
def install ():#line:239
    key =input ('Enter your key\n')#line:240
    if is_lisense_key (key ):#line:241
        print ('Ok')#line:242
        with open ('appdata.txt','w')as O000O0O0O0000O00O :#line:243
            O000O0O0O0000O00O .write (key )#line:244
        start ()#line:245
    else :#line:246
        print ('Wrong key, bye bye')#line:247
if __name__ =='__main__':#line:250
    if check_installation ():#line:251
        start ()#line:252
    else :#line:253
        install ()#line:254
