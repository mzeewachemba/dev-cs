namespace StrategyPattern
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnStrategySort_Click(object sender, EventArgs e)
        {
            List<Student> STList = new List<Student>();
            Student s1 = new Student
            {
                FirstName = "Bill",
                LastName = "Baker",
                Id = 12345,
                Test1Score = 85,
                Test2Score = 91
            };
            STList.Add(s1);
            Student s2 = new Student
            {
                FirstName = "Sally",
                LastName = "Mathews",
                Id = 12348,
                Test1Score = 87,
                Test2Score = 93
            };
            STList.Add(s2);
            Student s3 = new Student
            {
                FirstName = "Adam",
                LastName = "Fredericks",
                Id = 12341,
                Test1Score = 82,
                Test2Score = 83
            };
            STList.Add(s3);
            //shellsort , pass shell sort object
            SortContext cxt = new SortContext(new ShellSortStrategy());
            cxt.DoSort(STList);
            string out1 = "";
            foreach (Student st in STList)
                out1 += st.ToString() + "\n";
            MessageBox.Show(out1);
            // switch to Quicksort , pass quicksort object
            SortContext cxt2 = new SortContext(new QuickSortStrategy());
            cxt.DoSort(STList);
            string out2 = "";
            foreach (Student st in STList)
                out2 += st.ToString() + "\n";
            MessageBox.Show(out2);
        }

        private void btnStrategySortUniversity_Click(object sender, EventArgs e)
        {
            // Sorting university students

            // Initialize ShellSort strategy
            IStrategySort<Student> ist = new ShellSortStrategy();
            University u1 = new University(ist);

            // Add students to the university
            Student s1 = new Student
            {
                FirstName = "Bill",
                LastName = "Baker",
                Id = 12345,
                Test1Score = 85,
                Test2Score = 91
            };
            u1.AddStudent(s1);

            Student s2 = new Student
            {
                FirstName = "Sally",
                LastName = "Mathews",
                Id = 12348,
                Test1Score = 87,
                Test2Score = 93
            };
            u1.AddStudent(s2);

            Student s3 = new Student
            {
                FirstName = "Adam",
                LastName = "Fredericks",
                Id = 12341,
                Test1Score = 82,
                Test2Score = 83
            };
            u1.AddStudent(s3);

            // Sort students using Shell sort
            u1.SortStudent();
            DisplayStudents(u1.STList, "Sorted using Shell Sort");

            // Change sorting strategy to QuickSort
            u1.SortStrategy = new QuickSortStrategy();
            u1.SortStudent();
            DisplayStudents(u1.STList, "Sorted using QuickSort");

            // Function to display students
            void DisplayStudents(List<Student> students, string message)
            {
                string output = "";
                foreach (Student st in students)
                {
                    output += st.ToString() + "\n";
                }
                MessageBox.Show($"{message}\n{output}");
            }
        }
    }
}
