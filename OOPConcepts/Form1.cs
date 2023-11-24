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
            MyGen<int,double> g1 = new MyGen<int,double>();
            g1.A = 5;
            g1.B = 8.9;
            MessageBox.Show(g1.ToString());
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