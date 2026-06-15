#Explore Value vs Reference Types
using System;

class Student
{
    public string Name;
}

class Program
{
    static void ChangeValue(int x)
    {
        x = 100;
    }

    static void ChangeReference(Student s)
    {
        s.Name = "Bujji";
    }

    static void Main()
    {
        int number = 10;

        Student student = new Student();

        student.Name = "John";

        Console.WriteLine("Before Value: " + number);

        ChangeValue(number);

        Console.WriteLine("After Value: " + number);

        Console.WriteLine("Before Reference: " + student.Name);

        ChangeReference(student);

        Console.WriteLine("After Reference: " + student.Name);
    }
}
