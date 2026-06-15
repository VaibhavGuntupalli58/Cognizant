#Use ref, out, and in Parameters
using System;

class Program
{
    static void RefMethod(ref int x)
    {
        x = x + 10;
    }

    static void OutMethod(out int y)
    {
        y = 100;
    }

    static void InMethod(in int z)
    {
        Console.WriteLine(z);
    }

    static void Main()
    {
        int a = 10;

        RefMethod(ref a);

        Console.WriteLine(a);

        int b;

        OutMethod(out b);

        Console.WriteLine(b);

        int c = 50;

        InMethod(in c);
    }
}