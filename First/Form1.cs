namespace First
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCompute_Click(object sender, EventArgs e)
        {
            ComputeAreaVolume r1 = new ComputeAreaVolume();
            r1.Width = 20;
            r1.Height = 10;
            double area = r1.ComputeArea();

            MessageBox.Show("Area = " + area.ToString());
        }
    }
}