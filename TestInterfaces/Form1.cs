using System.Security.Cryptography.X509Certificates;

namespace TestInterfaces
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ICompute icom = new MyCompute();

            double res = icom.ComputeSphereVolume(5.2);

            MessageBox.Show(res.ToString());

            //calling computepay
            //using a is operator

            if (icom is IComputePay)
            {
                //typecast MyCompute into IComputePay
                IComputePay icp = (IComputePay)icom;
                double pay = icp.ComputePay(20, 15);
                MessageBox.Show("Pay = " + pay.ToString());
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Student s1 = new Student();
            s1.Test1 = 85;
            s1.Test2 = 91;
            s1.Id = 1000;

            List<Student> STList = new List<Student>();

            STList.Add(s1);

            Student s2 = new Student();
            s2.Test1 = 93;
            s2.Test2 = 90;
            s2.Id = 1001;

            STList.Add(s2);

            Student s3 = new Student();
            s3.Test1 = 93;
            s3.Test2 = 90;
            s3.Id = 1001;

            STList.Add(s3);

            STList.Sort();

            int a = 5;

            string out1 = " ";

            for (int i = 0; i < STList.Count; i++)
            {
                out1 = out1 + STList[i].ToString();
            }

            MessageBox.Show(out1);
        }
    }
}