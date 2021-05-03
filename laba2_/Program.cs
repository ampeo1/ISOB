using System;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Collections.Generic;

namespace ISOB_2_Сlient
{
    class Program
    {
        static void Main(string[] args)
        {
            string domenName = "domenName";
            Console.WriteLine("Введите имя:");
            string userName = Console.ReadLine();
            Console.WriteLine("Введите пароль:");
            string password = Console.ReadLine();
            User clientUser = new User(userName, password);
            /*
             * 2)
             * Затем компьютер пользователя обращается к службе KDC и передает ей 
             * имя пользователя, имя домена, а также текущее время на рабочей станции 
             * пользователя, при этом имя пользователя передается в открытом виде, 
             * текущее время на рабочей станции пользователя передается в 
             * зашифрованном виде и является аутентификатором. 
             * Ключ шифрования формируется из пароля пользователя в 
             * результате хеширования.
             */

            var value = new StringBuilder();
            value.Append(userName + "/");
            value.Append(domenName + "/");
            var userTime = DateTime.Now;
            value.Append(new DES().Encrypt(userTime.ToString(), clientUser.PasswordHash));
            string message = value.ToString();

            Console.WriteLine($"Зашифрованное сообщение: { message }");

            /*
             * 3)
             * Служба KDC ищет пользователя в AD, 
             * выявляет мастер ключ пользователя, 
             * который основан на пароле пользователя и расшифровывает аутентификатор, 
             * т. е. получает время отправки запроса. Разница во времени отправки запроса и
             * текущего времени на контроллере домена не должно превышать определенного значения, 
             * установленного политикой протокола Kerberos
             */

            var userList = new Dictionary<string, string>();
            userList.Add("ampeo", "12345");

            DateTime timeStamp;
            User KDKuser ;

            if (userList.ContainsKey(message.Split('/')[0]))
            {
                KDKuser = new User(message.Split('/')[0], userList[message.Split('/')[0]]);
                timeStamp = DateTime.Parse(new DES().Decipher(message.Split('/')[2], KDKuser.PasswordHash));
                if (timeStamp.AddMinutes(2) > DateTime.Now)
                {
                    Console.WriteLine("timeStamp: " + timeStamp);
                    Console.WriteLine("Время не превышает 2 минут");
                }
                else
                {
                    Console.WriteLine("Время превышает 2 минут");
                    Console.ReadLine();
                    return;
                }
            }
            else
            {
                Console.WriteLine("Пользователь не найден");
                Console.ReadLine();
                return;
            }


            /*
            * 4)
            * Затем KDC создает два объекта:
            * a. ключ сессии, посредством которого будет обеспечиваться зашифрование данных при обмене между клиентом и службой KDC,
            * b. билет на получение билета "Ticket-Granting Ticket" (TGT). 
            * TGT включает: вторую копию ключа сессии, имя пользователя, 
            * время окончания жизни билета. Билет на получение билета шифруется с использованием собственного мастер ключа службы KDC,
            * который известен только KDC, т. е. TGT может быть расшифрован только самой службой KDC.
            */

            string KDCsessionKey = GetHash(new Random().Next(1000000, 9999999).ToString());
            string KDCMasterKey = GetHash("masterKey");
            var TGT = new StringBuilder();
            TGT.Append(KDCsessionKey + "/");
            TGT.Append(KDKuser.Name + "/");
            TGT.Append(DateTime.Now.AddMinutes(30).ToString());
            string encryptTGT = new DES().Encrypt(TGT.ToString(), KDCMasterKey);
            Console.WriteLine("TGT: " + TGT);
            Console.WriteLine("stringTGT: " + encryptTGT);

            /*
            * 5)
            * Служба KDC зашифровывает аутентификатор пользователя (time stamp)
            * и ключ сессии с помощью ключа клиента.
            * После этого эти данные отправляются клиенту. 
            */

            var toUser = new StringBuilder();
            toUser.Append(timeStamp + "/");
            toUser.Append(KDCsessionKey);
            string encryptToUser = new DES().Encrypt(toUser.ToString(), KDKuser.PasswordHash);
            Console.WriteLine("toUser: " + toUser);
            Console.WriteLine("encryptToUser: ");
            Console.WriteLine(encryptToUser);
            /*
            * 6)
            * Компьютер клиента получает информацию от службы KDC,
            * проверяет аутентификатор,
            * расшифровывает ключ сессии. 
            */

            string decryptToUser = new DES().Decipher(encryptToUser, clientUser.PasswordHash);
            timeStamp = DateTime.Parse(decryptToUser.Split('/')[0]);
            string userSessionKey;
            if (timeStamp.ToString().Equals(userTime.ToString()))
            {
                userSessionKey = decryptToUser.Split('/')[1];
                Console.WriteLine("timeStamp совпадает");
            }
            else
            {
                Console.WriteLine("timeStamp не совпадает");
                Console.ReadLine();
                return;
            }
            /*
             * 7)
             * Теперь клиент обладает ключом сессии и TGT,
             * что предоставляет возможность безопасного 
             * взаимодействия со службой KDC. Клиент аутентифицирован
             * в домене и получает возможность осуществлять доступ к ресурсам домена,
             * используя протокол Kerberos.
             */

            /*
             * 1)
             * Клиент обращается к службе KDC. 
             * Клиент представляет KDC свой TGT и маркер времени,
             * которые зашифрованы с помощью ключа сессии, 
             * известного службе KDC.
             */

            var toKDC = new StringBuilder();
            toKDC.Append(encryptTGT + "/");
            userTime = DateTime.Now;
            toKDC.Append(new DES().Encrypt(userTime.ToString(), userSessionKey));     
            Console.WriteLine("toKDC: " + toKDC);

            /*
             * 2)
             * KDC расшифровывает TGT, используя свой собственный ключ.
             * Маркер времени расшифровывается с помощью сессионного ключа.
             * Теперь KDC может подтвердить, 
             * что запрос пришел от «правильного» пользователя, 
             * т. к. этот пользователь может использовать этот сессионный ключ.
             */

            encryptTGT = new DES().Decipher(toKDC.ToString().Split('/')[0], KDCMasterKey);
            timeStamp = DateTime.Parse(new DES().Decipher(toKDC.ToString().Split('/')[1], KDCsessionKey));
            if (timeStamp.AddMinutes(5) > DateTime.Now)
            {
                Console.WriteLine("timeStamp совпадает");
                Console.WriteLine("encryptTGT: " + encryptTGT);
                Console.WriteLine("timeStamp: " + timeStamp);
            }
            else
            {
                Console.WriteLine("timeStamp не совпадает");
                Console.ReadLine();
                return;
            }

            /*
             * 3)
             * KDC создает пару билетов, один для клиента, один для сервера, 
             * к ресурсам которого клиент должен будет получать доступ.
             * Каждый билет содержит имя пользователя, запрашивающего доступ, 
             * получателя запроса, маркер времени, показывающий, 
             * когда был создан билет, а также срок жизни билета. 
             * Оба билета будут также содержать новый ключ, K_cs который, 
             * таким образом известен и клиенту и серверу. 
             * Этот ключ будет обеспечивать возможность безопасного взаимодействия между ними.
             * KDC шифрует билет сервера, используя мастер – ключ сервера, 
             * затем вкладывает билет сервера внутрь билета клиента, 
             * который также содержит ключ K_cs.
             */

            var ticketToClient = new StringBuilder();
            ticketToClient.Append(KDKuser.Name + "/");
            ticketToClient.Append("requested access" + "/");
            ticketToClient.Append("ServerName" + "/");
            ticketToClient.Append(DateTime.Now + "/");
            ticketToClient.Append(DateTime.Now.AddMinutes(30) + "/");
            string keyK_cs = GetHash("keyK_cs" + "/");
            ticketToClient.Append(keyK_cs);
            string serverMasterKey =  GetHash("serverMasterKey");
            var ticketToServer = new DES().Encrypt(ticketToClient.ToString(), serverMasterKey);
            ticketToClient.Append("/" + ticketToServer);
            Console.WriteLine("ticketToServer: " + ticketToServer);
            Console.WriteLine("ticketToClient: " + ticketToClient);

            /*
             * 4)
             * Вся эта структура зашифровывается с помощью сессионного ключа,
             * который стал доступен пользователю при аутентификации.
             * После чего эта информация отправляется клиенту.
             */

            var encryptTicketToClient = new DES().Encrypt(ticketToClient.ToString(), KDCsessionKey);
            Console.WriteLine("encryptTicketToClient: " + encryptTicketToClient);


            /*
             * 5)
             * Получив билет, клиент расшифровывает его с помощью сессионного ключа,
             * т. е. K_cs становится доступным клиенту, K_cs доступен также и серверу.
             * Клиент не может прочитать билет сервера, т. к. он зашифрован на ключе сервера.
             */

            var decryptTicketToClient = new DES().Decipher(encryptTicketToClient, userSessionKey);
            Console.WriteLine("decryptTicketToClient: " + decryptTicketToClient);
            var userK_cs = decryptTicketToClient.Split('/')[5];
            Console.WriteLine("userK_cs: " + userK_cs);

            /*
             * 6)
             * Клиент зашифровывает маркер времени с помощью ключа,
             * K_cs затем отправляет маркер времени и билет сервера
             * самому серверу, к ресурсам которого пытается получить
             * доступ клиент.
             */

            var toServer = new StringBuilder();
            toServer.Append(new DES().Encrypt(DateTime.Now.ToString(), userK_cs));
            toServer.Append("/" + decryptTicketToClient.Split('/')[6]);

            Console.WriteLine("toServer: " + toServer);

            /*
             * 7)
             *  Получив эту информацию, на первом этапе сервер расшифровывает
             *  свой билет, используя свой долговременный ключ. 
             *  Это предоставляет возможность получить доступ к K_cs ,
             *  с помощью которого будет на втором этапе расшифрован маркер времени,
             *  полученный от клиента.
             */

            var decryptTicketToServer = new DES().Decipher(toServer.ToString().Split("/")[1], serverMasterKey);
            Console.WriteLine("decryptTicketToServer: " + decryptTicketToServer);
            var serverK_cs = decryptTicketToServer.Split("/")[5];
            Console.WriteLine("serverK_cs: " + serverK_cs);
            if (DateTime.Parse(new DES().Decipher(toServer.ToString().Split("/")[0], serverK_cs)).AddMinutes(5) > DateTime.Now)
            {
                Console.WriteLine("timeStamp совпадает");
            }
            else
            {
                Console.WriteLine("timeStamp не совпадает");
                Console.ReadLine();
                return;
            }
        }

        private static string GetHash(string str)
        {
            var tmpSource = ASCIIEncoding.ASCII.GetBytes(str);
            var tmpHash = new MD5CryptoServiceProvider().ComputeHash(tmpSource);
            StringBuilder value = new StringBuilder(tmpHash.Length);
            for (int i = 0; i < tmpHash.Length; i++)
            {
                value.Append(tmpHash[i].ToString("X2"));
            }
            return value.ToString();
        }
    }
}