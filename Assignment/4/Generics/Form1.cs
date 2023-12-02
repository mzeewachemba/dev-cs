using static Generics.MyEnums;

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

        private void btnComparerGeneric_Click(object sender, EventArgs e)
        {
            List<Student> STList = new List<Student>();
            // List is the generic equivalent of ArrayList class.

            Student s1 = new Student
            {
                FirstName = "Bill",
                LastName = "Baker",
                Test1Score = 85,
                Test2Score = 91,
                Id = 12345
            };
            STList.Add(s1);

            Student s2 = new Student
            {
                FirstName = "Sally",
                LastName = "Simpson",
                Test1Score = 89,
                Test2Score = 93,
                Id = 12348
            };
            STList.Add(s2);

            Student s3 = new Student
            {
                FirstName = "Mark",
                LastName = "Williams",
                Test1Score = 81,
                Test2Score = 87,
                Id = 12347
            };
            STList.Add(s3);

            Student s4 = new Student
            {
                FirstName = "James",
                LastName = "Jacobs",
                Test1Score = 80,
                Test2Score = 77,
                Id = 12346
            };
            STList.Add(s4);

            StudentComparer sc = new StudentComparer();
            sc.SortField = SORTFIELD.TEST2SCORE;
            sc.SortDir = SORTDIR.DESC;

            STList.Sort(sc); // will use IComparer to sort

            string out1 = "";
            foreach (Student st in STList)
            {
                out1 += st.ToString() + "\n";
            }

            MessageBox.Show(out1);

        }

        private void btnDictionary_Click(object sender, EventArgs e)
        {
            // Dictionary is the generic equivalent of Hashtable
            Dictionary<int, Student> DTable = new Dictionary<int, Student>();

            Student s1 = new Student
            {
                FirstName = "Bill",
                LastName = "Baker",
                Id = 12337,
                Test1Score = 87,
                Test2Score = 91
            };
            DTable.Add(s1.Id, s1);

            Student s2 = new Student
            {
                FirstName = "Sally",
                LastName = "Simpson",
                Id = 12365,
                Test1Score = 89,
                Test2Score = 93
            };
            DTable.Add(s2.Id, s2);

            // lookup a student
            int id = 12365;
            try
            {
                Student st = DTable[id];
                MessageBox.Show(st.ToString());
            }
            catch (KeyNotFoundException)
            {
                MessageBox.Show("Student does not exist");
            }

        }
    }
}