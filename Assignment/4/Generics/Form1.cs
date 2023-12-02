namespace Generics
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnExchange_Click(object sender, EventArgs e)
        {
            //integers
            int x = 5;
            int y = 7;
            GenUtil.Exchange(ref x, ref y);
            MessageBox.Show("x = " + x.ToString() + " y = " + y.ToString());

            //doubles
            double p = 5.8;
            double q = 7.3;
            GenUtil.Exchange(ref p, ref q);
            MessageBox.Show("p = " + p.ToString() + " q = " + q.ToString());

            //string
            string l = "Bill";
            string m = "Baker";
            GenUtil.Exchange(ref l, ref m);
            MessageBox.Show("l = " + l.ToString() + " m = " + m.ToString());
        }

        private void btnGenericClass_Click(object sender, EventArgs e)
        {
            //creating an object of generic class <> has to indicate two datatypes
            MyGen<int, float> mg = new MyGen<int, float>();
            mg.A = 5;
            mg.B = 3.75f;
            MessageBox.Show(mg.ToString());
        }

        private void btnInitArray_Click(object sender, EventArgs e)
        {
            //creating an array of reference first then assign memory by creating objects with new keyword
            //can be COMMON, use generic to solve this
            //Student[] STArr = new Student[5];
            //for (int i = 0; i < STArr.Length; i++)
            //    STArr[i] = new Student();

            Student[] STArr = GenArr<Student>.InitArray<Student>(4);
            MessageBox.Show(STArr.Length.ToString());
        }

        private void btnFindMaxScoreStudent_Click(object sender, EventArgs e)
        {
            //finding maximum score of a student
            Student[] STArr = GenArr<Student>.InitArray<Student>(3);

            STArr[0].Id = 12345;
            STArr[0].FirstName = "Bill";
            STArr[0].Test1Score = 83;

            STArr[1].Id = 12348;
            STArr[1].FirstName = "Sally";
            STArr[1].Test1Score = 91;

            STArr[2].Id = 12346;
            STArr[2].FirstName = "Mark";
            STArr[2].Test1Score = 85;

            Student maxScoreStudent = GenArr<Student>.FindMax<Student>(STArr);
            MessageBox.Show(maxScoreStudent.ToString());
        }
    }
}