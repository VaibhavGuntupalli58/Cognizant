#Perform Conditional Logic for Grade Calculation
using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter Score: ");

        int score = Convert.ToInt32(Console.ReadLine());

        if (score >= 90)
        {
            Console.WriteLine("Grade A");
        }

        else if (score >= 75)
        {
            Console.WriteLine("Grade B");
        }

        else if (score >= 50)
        {
            Console.WriteLine("Grade C");
        }

        else
        {
            Console.WriteLine("Fail");
        }

        string result = score switch
        {
            >= 90 => "Excellent",
            >= 75 => "Good",
            >= 50 => "Average",
            _ => "Poor"
        };

        Console.WriteLine(result);
    }
}

