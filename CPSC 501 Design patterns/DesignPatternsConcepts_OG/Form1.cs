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
    }
}