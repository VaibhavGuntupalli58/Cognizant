#Demonstrate OOP Basics with Constructors
using System;

class Car
{
    public string Make;

    public string Model;

    public int Year;

    public Car()
    {
        Make = "Unknown";

        Model = "Unknown";

        Year = 0;
    }

    public Car(string make,
               string model,
               int year)
    {
        Make = make;

        Model = model;

        Year = year;
    }

    public void Display()
    {
        Console.WriteLine(
            $"{Make} {Model} {Year}"
        );
    }
}

class Program
{
    static void Main()
    {
        Car c1 = new Car();

        Car c2 = new Car(
            "Toyota",
            "Camry",
            2024
        );

        c1.Display();

        c2.Display();
    }
}