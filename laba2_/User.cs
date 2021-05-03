using System.Security.Cryptography;
using System.Text;

namespace ISOB_2_Сlient
{
    class User
    {
        private string userName;
        private string password;  

        public string Name
        {
            get { return this.userName; }
        }

        public string PasswordHash
        {
            get { return GetPasswordHash(); }
        }

        public User(string userName, string password)
        {
            this.userName = userName;
            this.password = password;
        }

        public string GetPasswordHash()
        {
            var tmpSource = ASCIIEncoding.ASCII.GetBytes(this.password);
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