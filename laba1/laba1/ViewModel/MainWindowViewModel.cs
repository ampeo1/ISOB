using laba1.Model;
using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace laba1.ViewModel
{
    class MainWindowViewModel: INotifyPropertyChanged
    {
        private int key = -1;
        public string Key
        {
            get
            {
                return key.ToString();
            }
            set
            {
                try
                {
                    key = int.Parse(value);
                }
                catch (FormatException)
                {
                    key = -1;
                    MessageBox.Show("You need write number");
                }
            }
        }

        private string word = string.Empty;
        public string Word
        {
            get
            {
                return word;
            }
            set
            {
                word = value;
            }
        }

        private string inputText = string.Empty;
        public string InputText
        {
            get
            {
                return inputText;
            }
            set
            {
                inputText = value;
                OnPropertyChanged("InputText");
            }
        }

        private string outputText = string.Empty;
        public string OutputText
        {
            get
            {
                return outputText;
            }
            set
            {
                outputText = value;
                OnPropertyChanged("OutputText");
            }
        }

        private string fileName = string.Empty;
        public string FileName{ 
            get
            {
                return fileName;
            }
            set
            {
                fileName = value;
                OnPropertyChanged("FileName");
            }
        }

        private RelayCommand saveFile;
        public RelayCommand SaveFile
        {
            get
            {
                return saveFile ?? (saveFile = new RelayCommand(obj =>
                {
                    SaveFileDialog saveFileDialog = new SaveFileDialog();
                    saveFileDialog.Filter = "Txt file (*.txt)|*.txt";
                    if (saveFileDialog.ShowDialog() == true)
                    {
                        WorkFile.SaveFile(saveFileDialog.FileName, OutputText);
                    }
                }));
            }
        }

        private RelayCommand chooseFile;
        public RelayCommand ChooseFile
        {
            get
            {
                return chooseFile ?? (chooseFile = new RelayCommand(obj =>
                {
                    OpenFileDialog openFileDialog = new OpenFileDialog();
                    openFileDialog.Filter = "Txt file (*.txt)|*.txt";
                    inputText = string.Empty;
                    if (openFileDialog.ShowDialog() == true)
                    {
                        FileName = openFileDialog.FileName;
                        InputText = WorkFile.ReadFile(FileName);
                    }
                    else
                    {
                        MessageBox.Show("Что-то пошло не так");
                    }
                }));
            }
        }

        private RelayCommand causerEncryptCommand;
        public RelayCommand CauserEncryptCommand
        {
            get
            {
                return causerEncryptCommand ?? (causerEncryptCommand = new RelayCommand(obj =>
                {
                    if(key != -1 && !string.IsNullOrEmpty(inputText))
                    {
                        OutputText = Сiphers.CauserEncrypt(inputText, key);
                    }
                }));
            }
        }

        private RelayCommand causerDecryptCommand;
        public RelayCommand CauserDecryptCommand
        {
            get
            {
                return causerDecryptCommand ?? (causerDecryptCommand = new RelayCommand(obj =>
                {
                    if(key != -1 && !string.IsNullOrEmpty(inputText))
                    {
                        OutputText = Сiphers.CauserDecrypt(inputText, key);
                    }
                }));
            }
        }

        private RelayCommand vigenereEncryptCommand;
        public RelayCommand VigenereEncryptCommand
        {
            get
            {
                return vigenereEncryptCommand ?? (vigenereEncryptCommand = new RelayCommand(obj =>
                {
                    if(!string.IsNullOrEmpty(Word) && !string.IsNullOrEmpty(InputText))
                    {
                        OutputText = Сiphers.VigenereEncrypt(InputText, Word);
                    }
                }));
            }
        }

        private RelayCommand vigenereDecryptCommand;
        public RelayCommand VigenereDecryptCommand
        {
            get
            {
                return vigenereDecryptCommand ?? (vigenereDecryptCommand = new RelayCommand(obj =>
                {
                    if (!string.IsNullOrEmpty(Word) && !string.IsNullOrEmpty(InputText))
                    {
                        OutputText = Сiphers.VigenereDecrypt(InputText, Word);
                    }
                }));
            }
        }


        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyChanged([CallerMemberName] string prop = "")
        {
            if (PropertyChanged != null)
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
        } 

    }
}
