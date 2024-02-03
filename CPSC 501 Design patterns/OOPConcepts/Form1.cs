namespace OOPConcepts
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnExchange_Click(object sender, EventArgs e)
        {
            int x = 5;
            int y = 7;
            Exchange<int>(ref x, ref y);
            MessageBox.Show("x = " + x.ToString() + "  y = " + y.ToString());

            double p = 7.8;
            double q = 6.9;
            Exchange<double>(ref p, ref q);
            MessageBox.Show("p = " + p.ToString() + "  q = " + q.ToString());
        }

        private void btnGenClass_Click(object sender, EventArgs e)
        {
            MyGen<int, double> g1 = new MyGen<int, double>();
            g1.A = 5;
            g1.B = 8.9;
            MessageBox.Show(g1.ToString());
        }

        private void btnTestList_Click(object sender, EventArgs e)
        {
            List<Student> ST = new List<Student>();
            //alternative to using aconstructor, eliminate the need to have a constructor
            Student s1 = new Student { Id = 1234, Name = "Mahmood", Test1 = 89, Test2 = 5 };
            ST.Add(s1);
            Student s2 = new Student { Id = 14, Name = "Ausif", Test1 = 89, Test2 = 5 };
            ST.Add(s2);
            MessageBox.Show(ST.Count.ToString());

            for (int i = 0; i < ST.Count; i++)
            {
                MessageBox.Show(ST[i].Id.ToString());
            }

            //for each loop, used in data structures
            foreach (var st in ST)
            {
                MessageBox.Show(st.Id.ToString() + "  " + st.Name);
            }

            //using a constructor
            //Student s1 = new Student(1234, "Mahmood", 89,5);
            //s1.Id = 1234;
            //s1.Name = "Mahmood";
            //s1.Test1 = 89;
            //s1.Test2 = 5;
        }

        private void btnExtMethod_Click(object sender, EventArgs e)
        {
            Employee e1 = new Employee { HoursWorked = 60, Id = 1234, Name = "Kaliso", PayRate = 10 };
            double pay = e1.ComputePay();
            MessageBox.Show(pay.ToString());

            double overtimePay = e1.ComputeOverTimePay(2);
            MessageBox.Show(overtimePay.ToString());

        }

        //public void Exchange(ref int a,ref int b)
        //{
        //    int temp = a;
        //    a = b;
        //    b = temp;
        //}

        //public void Exchange(ref double a, ref double b)
        //{
        //    double temp = a;
        //    a = b;
        //    b = temp;
        //}
        ////this creates a problem
        //public void Exchange(ref string a, string  b)
        //{
        //    string temp = a;
        //    a = b;
        //    b = temp;
        //}

        //making a generic function
        public void Exchange<T>(ref T a, ref T b)
        {
            T temp = a;
            a = b;
            b = temp;
        }
    }
}