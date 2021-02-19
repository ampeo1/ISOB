using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace laba1.Model
{
    class WorkFile
    {
        static public string ReadFile(string path)
        {
            string data;
            using(FileStream file = File.OpenRead(path)){
                byte[] array = new byte[file.Length];
                file.Read(array, 0, array.Length);
                data = Encoding.UTF8.GetString(array);
            }
            return data;
        }

        static public void SaveFile(string path, string text)
        {
            using(FileStream file = File.OpenWrite(path))
            {
                byte[] array = Encoding.UTF8.GetBytes(text);
                file.Write(array, 0, array.Length);
            }
        }
    }
}
