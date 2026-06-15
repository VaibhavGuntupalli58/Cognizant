#Demonstrate Type Inference with var and new()
using System;

class Employee
{
    public string Name { get; set; }
}

class Program
{
    static void Main()
    {
        var number = 100;

        var text = "Hello";

        Employee emp = new()
        {
            Name = "Bujji"
        };

        Console.WriteLine(number.GetType());

        Console.WriteLine(text.GetType());

        Console.WriteLine(emp.Name);
    }
}