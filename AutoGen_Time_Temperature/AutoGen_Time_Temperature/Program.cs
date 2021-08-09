using System;
using System.IO;

namespace AutoGen_Time_Temperature
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string path = System.Environment.CurrentDirectory;
                StreamWriter sw = new StreamWriter(path + "\\Time_Temperature.csv", true);

                int MAX = 1200;
                Random rand = new Random();
                double baseTemp = -5;

                string header = string.Format("Time    Temperature");
                Console.WriteLine(header);
                sw.WriteLine(header);

                double addDay = 0;
                while (addDay < MAX)
                {
                    DateTime dateTime = new DateTime(2016, 01, 01).AddDays(addDay);
                    string curr_data = string.Format("{0}    {1}", dateTime.ToString("yyyy-MM-dd"), Math.Round(baseTemp + rand.NextDouble() * 35, 1));
                    sw.WriteLine(curr_data);
                    Console.WriteLine(curr_data);
                    addDay++;
                }

                sw.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine(string.Format("Error occured {0}", ex));
            }
        }
    }
}
