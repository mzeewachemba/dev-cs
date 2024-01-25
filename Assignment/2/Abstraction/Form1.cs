namespace Abstraction
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnTestAreaVolume_Click(object sender, EventArgs e)
        {
            IAreaVolume iav = new AreaVolume();
            double radius = 5.2;
            double res = iav.ComputeSphereVolume(radius);
            MessageBox.Show("Volume of sphere with radius " + radius + " = " + res);
        }

        private void btnTestIclonable_Click(object sender, EventArgs e)
        {
            Student s1 = new Student("Bill", "Baker", 1234, 87, 91);
            Student s2 = (Student)s1.Clone(); //get a copy of s1 and put it in s2, 
            s1.TestScores[0] = 80; //trying to change one of the values in s1
            MessageBox.Show(s2.ToString()); //s2 value should remain the same
            MessageBox.Show(s1.ToString()); //evaluating s1 value
        }

        private void btnTestICloneableAddr_Click(object sender, EventArgs e)
        {
            Student s1 = new Student("Bill", "Baker", 1234, 87, 91);
            s1.Addr.Street = "50 Main Street";
            s1.Addr.City = "Bridgeport";
            Student s2 = (Student)s1.Clone();
            s1.TestScores[0] = 80;
            s1.Addr.Street = "20 New Street";
            MessageBox.Show(s2.ToString()); // display second student with value of first student changed
            MessageBox.Show(s1.ToString()); // display  student 
        }

        private void btnTestIComparable_Click(object sender, EventArgs e)
        {
            List<Student> STList = new List<Student>();
            //adding students to a list
            Student s1 = new Student("Bill", "Xavier", 1234, 87, 91);
            STList.Add(s1);
            Student s2 = new Student("Mark", "Mathews", 1235, 81, 88);
            STList.Add(s2);
            Student s3 = new Student("Sally", "Simpson", 1230, 80, 95);
            STList.Add(s3);
            STList.Sort(); // initiate Icomparable to sort
            string out1 = "";
            //iterating through the student list
            foreach (Student st in STList)
                out1 += st.ToString() + "\n";
            MessageBox.Show(out1);
        }
    }
}