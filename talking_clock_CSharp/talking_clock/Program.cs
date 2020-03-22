using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Media;
using System.IO;
using System.Reflection;
using System.Resources;
using System.Diagnostics;


namespace talking_clock
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Title = "Talking kurdish Clock";
            string stunde = DateTime.Now.ToString("hh");
            string minute = DateTime.Now.ToString("mm");
            int iMinute = Convert.ToInt16(minute);
            bool zero = true;

            Play("seht.wav");
            Play(stunde + ".wav");
                                    
            
            switch(iMinute)
            {
                case 20:
                    Play(minute + ".wav");
                    break;

                case 21:
                    Play("20.wav");
                    Play("01.wav");
                    break;

                case 22:
                    Play("20.wav");
                    Play("02.wav");
                    break;

                case 23:
                    Play("20.wav");
                    Play("03.wav");
                    break;

                case 24:
                    Play("20.wav");
                    Play("04.wav");
                    break;

                case 25:
                    Play("20.wav");
                    Play("05.wav");
                    break;

                case 26:
                    Play("20.wav");
                    Play("06.wav");
                    break;

                case 27:
                    Play("20.wav");
                    Play("07.wav");
                    break;

                case 28:
                    Play("20.wav");
                    Play("08.wav");
                    break;

                case 29:
                    Play("20.wav");
                    Play("09.wav");
                    break;

                case 30:
                    Play(minute + ".wav");
                                        break;

                case 31:
                    Play("30.wav");
                    Play("01.wav");
                    break;

                case 32:
                    Play("30.wav");
                    Play("02.wav");
                    break;

                case 33:
                    Play("30.wav");
                    Play("03.wav");
                    break;

                case 34:
                    Play("30.wav");
                    Play("04.wav");
                    break;

                case 35:
                    Play("30.wav");
                    Play("05.wav");
                    break;

                case 36:
                    Play("30.wav");
                    Play("06.wav");
                    break;

                case 37:
                    Play("30.wav");
                    Play("07.wav");
                    break;

                case 38:
                    Play("30.wav");
                    Play("08.wav");
                    break;

                case 39:
                    Play("30.wav");
                    Play("09.wav");
                    break;

                case 40:
                    Play(minute + ".wav");
                                        break;

                case 41:
                    Play("40.wav");
                    Play("01.wav");
                    break;

                case 42:
                    Play("40.wav");
                    Play("02.wav");
                    break;

                
                case 43:
                    Play("40.wav");
                    Play("03.wav");
                    break;

                case 44:
                    Play("40.wav");
                    Play("04.wav");
                    break;

                case 45:
                    Play("40.wav");
                    Play("05.wav");
                    break;

                case 46:
                    Play("40.wav");
                    Play("06.wav");
                    break;

                case 47:
                    Play("40.wav");
                    Play("07.wav");
                    break;

                case 48:
                    Play("40.wav");
                    Play("08.wav");
                    break;

                case 49:
                    Play("40.wav");
                    Play("09.wav");
                    break;

                case 50:
                    Play(minute + ".wav");
                                        break;

                case 51:
                    Play("50.wav");
                    Play("01.wav");
                    break;

                case 52:
                    Play("50.wav");
                    Play("02.wav");
                    break;

                case 53:
                    Play("50.wav");
                    Play("03.wav");
                    break;

                case 54:
                    Play("50.wav");
                    Play("04.wav");
                    break;

                case 55:
                    Play("50.wav");
                    Play("05.wav");
                    break;

                case 56:
                    Play("50.wav");
                    Play("06.wav");
                    break;

                case 57:
                    Play("50.wav");
                    Play("07.wav");
                    break;

                case 58:
                    Play("50.wav");
                    Play("08.wav");
                    break;

                case 59:
                    Play("50.wav");
                    Play("09.wav");
                    break;

                default:
                    if(iMinute == 0)
                    {
                        zero = false;
                    } else {
                    Play(minute + ".wav");
                    }
                    break;
            }

            if(zero)    
            Play("deqe.wav");
            

            //Console.ReadLine();
        }

        static void Play(String fn)
        {
            try {
                                    SoundPlayer sp;
            int Rate = 4000;
            byte[] B = File.ReadAllBytes("wave/" + fn);
            int SampleRate = BitConverter.ToInt32(B, 24) + Rate;
            Array.Copy(BitConverter.GetBytes(SampleRate), 0, B, 24, 4);

            using (sp = new SoundPlayer(new MemoryStream(B)))
            {
                //sp.Load();
                sp.LoadAsync();
                //sp.Play();
                sp.PlaySync();
        }
                //            System.Threading.Thread.Sleep(500);
                //Console.WriteLine(fn);
            }
            catch(Exception ex)
            {
                //Console.WriteLine(ex.Message.ToString());
                Console.WriteLine(fn);
            }
        }

    }//end class
}//end namespace
