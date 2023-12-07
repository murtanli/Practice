



public class Sortir
{
    public List<int> list = new List<int>();
    
    public Sortir(List<int> lis)
    {
        list = lis;
    }

    public void pyzir()
    {
        int n = list.Count;
        int max;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - 1; j++)
            {
                if (list[j] > list[j + 1])
                {
                    max = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = max;
                }
            }
        }
        Console.WriteLine("Sortir Pyzir");
        foreach (int k in list)
        {
            Console.WriteLine(k);
        }
    }

    public void rekursia(int n)
    {
        if (n == 1)
        {
            Console.WriteLine("Sortir Rekursia");
            foreach (int i in list)
            {
                Console.WriteLine(i);
            }
            return;
        }

        for(int i = 0;i < n - 1;i++)
        {
            if (list[i] > list[i + 1])
            {
                int min = list[i];
                list[i] = list[i + 1];
                list[i + 1] = min;
            }
        }
        rekursia(n - 1);
    }
    public void sheiker()
    {
        for (int i = 0; i < list.Count; i++)
        {
            bool izm = false;
            for (int j = i; j < list.Count - i - 1; j++)
            {
               if (list[j] > list[j + 1])
                {
                    int max = list[j];
                    list[j] = list[j + 1];
                    list[j + 1] = max;
                    izm = true;
                }
            }

            for (int j = list.Count - 2 - i; j > 1; j--)
            {
                if (list[j - 1] > list[j])
                {
                    int max = list[j - 1];
                    list[j - 1] = list[j];
                    list[j] = max;
                    izm = true;
                }
            }

            if ( !izm )
            {
                break;
            }
        }
        Console.WriteLine("Sortir Shiker");
        foreach (int i in list)
        {
            Console.WriteLine(i);
        }
    }

    public void rashestka()
    {
        int n = list.Count;
        double del = 1.3;
        bool sw;
        int gap = n;

        do
        {
            gap = (int)(gap / del);
            if (gap < 1) gap = 1;
            sw = false;

            for (int i = 0; i < n - gap; i++)
            {
                int j = i + gap;

                if (list[i] > list[j])
                {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        } while (gap > 1 || sw);

        Console.WriteLine("Raschestka");
        foreach ( int i in list )
        {
            Console.WriteLine(i);
        }
        
    }
}

class Proga
{
    static void Main()
    {
        List <int> list = new List<int>();
        list = [12, 22, 90, 23, 1, 4, 2, 76, 123, 112, 232, 1222, 231, 999, 1, -2];
        Sortir classobjec = new Sortir(list);
        classobjec.pyzir();
        classobjec.rekursia(list.Count);
        classobjec.sheiker();
        classobjec.rashestka();
    }
}