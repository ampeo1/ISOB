using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba1.Model
{
    class Сiphers
    {
        private const int PowerAlhabet = 'z' - 'a' + 1;
        public static string CauserEncrypt(string inputText, int key)
        {
            StringBuilder stringBuilder = new StringBuilder();
            inputText = inputText.ToLower();
            for (int i = 0; i < inputText.Length; i++)
            {
                if (CheckSymbol(inputText[i]))
                {
                    stringBuilder.Append((char)((inputText[i] - 'a' + key) % PowerAlhabet + 'a'));
                }
                else
                {
                    stringBuilder.Append(inputText[i]);
                }
            }

            return stringBuilder.ToString();
        }

        public static string CauserDecrypt(string inputText, int key)
        {
            StringBuilder stringBuilder = new StringBuilder();
            for (int i = 0; i < inputText.Length; i++)
            {
                if (CheckSymbol(inputText[i]))
                {
                    stringBuilder.Append((char)((inputText[i] - 'a' - key + PowerAlhabet) % PowerAlhabet + 'a'));
                }
                else
                {
                    stringBuilder.Append(inputText[i]);
                }

            }

            return stringBuilder.ToString();
        }

        public static string VigenereEncrypt(string inputText, string word)
        {
            StringBuilder stringBuilder = new StringBuilder();
            word = word.ToLower();
            inputText = inputText.ToLower();
            for (int i = 0, j = 0; i < inputText.Length; i++, j++)
            {
                if (j == word.Length)
                {
                    j = 0;
                }
                 
                if (CheckSymbol(inputText[i]))
                {
                    stringBuilder.Append((char)((inputText[i] + word[j] - 2 * 'a') % PowerAlhabet + 'a'));
                }
                else
                {
                    stringBuilder.Append(inputText[i]);
                }
            }

            return stringBuilder.ToString();
        }

        public static string VigenereDecrypt(string inputText, string word)
        {
            StringBuilder stringBuilder = new StringBuilder();
            word = word.ToLower();
            inputText = inputText.ToLower();
            for(int i = 0, j = 0; i < inputText.Length; i++, j++)
            {
                if (j == word.Length)
                {
                    j = 0;
                }

                if (CheckSymbol(inputText[i]))
                {
                    stringBuilder.Append((char)((inputText[i] - word[j] + PowerAlhabet) % PowerAlhabet + 'a'));
                }
                else
                {
                    stringBuilder.Append(inputText[i]);
                }
            }

            return stringBuilder.ToString();
        }

        private static bool CheckSymbol(char symbol)
        {
            switch (symbol)
            {
                case ' ':
                case ',':
                case '.':
                case ':':
                case '-':
                case '\r':
                case '\n':
                    return false;
                default:
                    return true;
            }
        }
    }
}
