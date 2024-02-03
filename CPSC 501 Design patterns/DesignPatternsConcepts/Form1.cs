namespace DesignPatternsConcepts
{
    public partial class Form1 : Form
    {
        Address addr = new Address();
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTest_Click(object sender, EventArgs e)
        {
            Student s1 = new Student(addr);
            s1.Addr.City = "bridgeport";
            MessageBox.Show("The address is " + s1.Addr.City);
        }

        private void btnTestFactory_Click(object sender, EventArgs e)
        {
            //caller will not give us compute fast
            IComputeArea icomp = ComputeFactory.CreateObject(ComputeCriteria.ACCURATE);
            double res = icomp.ComputeCircleArea(5);
            MessageBox.Show(res.ToString());
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Student s1 = new Student(null);
            s1.Test1 = 85;
            MessageBox.Show(s1.Test1.ToString());
            Student s2 = (Student)s1.Clone();
            s1.Test1 = 91;
            MessageBox.Show(s2.Test1.ToString());
        }

        private void btnTestAdaptor_Click(object sender, EventArgs e)
        {
            //caller calls the existing code via the new interface
            IComputeNew icomp = new ComputeNew();
            double[] data = { 5, 8, 9.2 };
            double res = icomp.ComputeAvg(data);
            MessageBox.Show("Result =  " + res.ToString());
        }
    }
}